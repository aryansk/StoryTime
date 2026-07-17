import Foundation

// MARK: - CatalogService
//
// Loads the curated catalog of stories. Strategy:
//   1. On launch, load the bundled seed catalog *off the main thread* so
//      the app is usable offline without blocking the first frame.
//   2. If a remote base URL is configured (Info.plist "CatalogBaseURL"),
//      fetch the index in the background and merge new stories on top —
//      the per-story fetches run concurrently (bounded).
//   3. Cache the remote payload in Application Support so repeat launches
//      survive offline.
//
// All errors are swallowed gracefully — we degrade to whatever we have.

@MainActor
final class CatalogService: ObservableObject {

    @Published private(set) var stories: [CatalogStory] = [] {
        didSet { rebuildIndex() }
    }
    @Published private(set) var isRefreshing: Bool = false
    @Published private(set) var lastError: String?
    @Published private(set) var lastUpdated: Date?

    /// O(1) id → story map, kept in sync with `stories`. Lookups used to be
    /// a linear scan over ~175 entries on every call (reader saga links,
    /// deep links, Library row resolution).
    private var storiesById: [String: CatalogStory] = [:]

    private func rebuildIndex() {
        storiesById = Dictionary(stories.map { ($0.id, $0) },
                                 uniquingKeysWith: { _, new in new })
    }

    private let session: URLSession
    private let baseURL: URL?

    /// How many per-story fetches to keep in flight during a refresh.
    private static let maxConcurrentFetches = 8

    init(session: URLSession = .shared) {
        self.session = session
        self.baseURL = Self.resolveBaseURL()
        // Load bundled + cached catalog off the main thread, then publish.
        // The heavy file IO and Codable decoding used to run synchronously
        // in `init` on the main actor, stalling launch for 175 files.
        Task { [weak self] in
            let bundled = await Self.loadBundledCatalog()
            let cached = await Self.loadCachedCatalog()
            self?.applyInitialLoad(bundled: bundled.stories,
                                   bundledUpdatedAt: bundled.updatedAt,
                                   cached: cached)
        }
    }

    private static func resolveBaseURL() -> URL? {
        // Priority: UserDefaults override > Info.plist > nil (offline-only)
        if let raw = UserDefaults.standard.string(forKey: "CatalogBaseURL"),
           let url = URL(string: raw), !raw.isEmpty {
            return url
        }
        if let raw = Bundle.main.object(forInfoDictionaryKey: "CatalogBaseURL") as? String,
           let url = URL(string: raw), !raw.isEmpty {
            return url
        }
        return nil
    }

    private func applyInitialLoad(bundled: [CatalogStory],
                                  bundledUpdatedAt: Date?,
                                  cached: [CatalogStory]) {
        var merged = bundled
        if !cached.isEmpty {
            merged = Self.mergeStories(local: merged, remote: cached)
        }
        self.stories = merged
        self.lastUpdated = bundledUpdatedAt
    }

    /// Override the catalog base URL at runtime (e.g. from a developer
    /// menu) and persist the choice across launches.
    func setRemoteBaseURL(_ urlString: String) {
        UserDefaults.standard.set(urlString, forKey: "CatalogBaseURL")
    }

    func story(id: String) -> CatalogStory? {
        storiesById[id]
    }

    func stories(matching genre: StoryGenre) -> [CatalogStory] {
        guard genre != .all else { return stories }
        return stories.filter { $0.genre == genre }
    }

    var newThisWeek: [CatalogStory] {
        stories.filter { $0.isNewThisWeek }
               .sorted { $0.addedAt > $1.addedAt }
    }

    // MARK: Refresh

    func refresh() async {
        guard let baseURL else { return }
        isRefreshing = true
        defer { isRefreshing = false }
        do {
            let indexURL = baseURL.appendingPathComponent("index.json")
            let (data, _) = try await session.data(from: indexURL)
            let index = try CatalogJSON.decoder.decode(CatalogIndex.self, from: data)

            // Nothing new since our last successful sync (or the bundled seed
            // already matches the remote) — skip the whole per-story fetch.
            // This turns the common launch from ~175 requests into just 1.
            if let lastUpdated, index.updatedAt <= lastUpdated {
                self.lastError = nil
                return
            }

            // Fetch only entries we don't already hold at the same revision.
            // Everything unchanged is reused from memory rather than
            // re-downloaded. `addedAt` doubles as the per-story revision.
            let existing = self.storiesById
            let stale = index.stories.filter { entry in
                guard let current = existing[entry.id] else { return true }
                return current.addedAt != entry.addedAt
            }

            let fetched = try await fetchStories(entries: stale, base: baseURL)
            if !fetched.isEmpty {
                self.stories = Self.mergeStories(local: self.stories, remote: fetched)
            }
            // Advance the watermark even when the delta was empty, so we
            // don't keep re-evaluating the same index on every launch.
            self.lastUpdated = index.updatedAt
            await cacheCurrent()
            self.lastError = nil
        } catch {
            self.lastError = error.localizedDescription
        }
    }

    /// Fetch every story referenced by the index, keeping at most
    /// `maxConcurrentFetches` requests in flight at once. This replaces the
    /// old strictly-sequential loop (one round-trip per story).
    private func fetchStories(entries: [CatalogIndexEntry], base: URL) async throws -> [CatalogStory] {
        let session = self.session
        return try await withThrowingTaskGroup(of: CatalogStory?.self) { group in
            var results: [CatalogStory] = []
            results.reserveCapacity(entries.count)
            var next = 0
            let seed = min(Self.maxConcurrentFetches, entries.count)
            while next < seed {
                let entry = entries[next]
                group.addTask { try await Self.fetchStory(entry: entry, base: base, session: session) }
                next += 1
            }
            while let story = try await group.next() {
                if let story { results.append(story) }
                if next < entries.count {
                    let entry = entries[next]
                    group.addTask { try await Self.fetchStory(entry: entry, base: base, session: session) }
                    next += 1
                }
            }
            return results
        }
    }

    private nonisolated static func fetchStory(entry: CatalogIndexEntry,
                                               base: URL,
                                               session: URLSession) async throws -> CatalogStory? {
        guard let path = entry.storyURL else { return nil }
        let url = URL(string: path, relativeTo: base) ?? base.appendingPathComponent(path)
        let (data, _) = try await session.data(from: url)
        return try CatalogJSON.decoder.decode(CatalogStory.self, from: data)
    }

    private nonisolated static func mergeStories(local: [CatalogStory], remote: [CatalogStory]) -> [CatalogStory] {
        var byId: [String: CatalogStory] = [:]
        for s in local { byId[s.id] = s }
        for s in remote { byId[s.id] = s }   // remote wins
        return byId.values.sorted { $0.addedAt > $1.addedAt }
    }

    // MARK: Bundled seed (runs off the main actor)

    private nonisolated static func loadBundledCatalog() async -> (stories: [CatalogStory], updatedAt: Date?) {
        // Try with subdirectory (folder reference) first, then flat
        guard let url = bundleURL(for: "index", subdir: "Catalog") else { return ([], nil) }
        do {
            let data = try Data(contentsOf: url)
            let index = try CatalogJSON.decoder.decode(CatalogIndex.self, from: data)
            var loaded: [CatalogStory] = []
            for entry in index.stories {
                guard let storyURL = entry.storyURL else { continue }
                let resourceName = (storyURL as NSString).deletingPathExtension
                if let storyFile = bundleURL(for: resourceName, subdir: "Catalog"),
                   let data = try? Data(contentsOf: storyFile),
                   let story = try? CatalogJSON.decoder.decode(CatalogStory.self, from: data) {
                    loaded.append(story)
                }
            }
            return (loaded.sorted { $0.addedAt > $1.addedAt }, index.updatedAt)
        } catch {
            return ([], nil)
        }
    }

    private nonisolated static func bundleURL(for resource: String, subdir: String) -> URL? {
        if let url = Bundle.main.url(forResource: resource, withExtension: "json", subdirectory: subdir) {
            return url
        }
        return Bundle.main.url(forResource: resource, withExtension: "json")
    }

    // MARK: Disk cache (runs off the main actor)

    private nonisolated static func cacheURL() -> URL? {
        guard let dir = try? FileManager.default.url(for: .applicationSupportDirectory,
                                                      in: .userDomainMask,
                                                      appropriateFor: nil,
                                                      create: true) else { return nil }
        return dir.appendingPathComponent("catalog.cache.json")
    }

    private func cacheCurrent() async {
        let snapshot = stories
        await Self.writeCache(snapshot)
    }

    private nonisolated static func writeCache(_ stories: [CatalogStory]) async {
        guard let url = cacheURL() else { return }
        if let data = try? CatalogJSON.encoder.encode(stories) {
            try? data.write(to: url, options: .atomic)
        }
    }

    private nonisolated static func loadCachedCatalog() async -> [CatalogStory] {
        guard let url = cacheURL(),
              FileManager.default.fileExists(atPath: url.path),
              let data = try? Data(contentsOf: url),
              let cached = try? CatalogJSON.decoder.decode([CatalogStory].self, from: data) else {
            return []
        }
        return cached
    }
}
