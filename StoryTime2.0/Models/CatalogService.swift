import Foundation

// MARK: - CatalogService
//
// Loads the curated catalog of stories. Strategy:
//   1. On launch, load bundled seed catalog so the app is usable offline.
//   2. If a remote base URL is configured (Info.plist "CatalogBaseURL"),
//      fetch the index in the background and merge new stories on top.
//   3. Cache the remote payload in Application Support so repeat launches
//      survive offline.
//
// All errors are swallowed gracefully — we degrade to whatever we have.

@MainActor
final class CatalogService: ObservableObject {

    @Published private(set) var stories: [CatalogStory] = []
    @Published private(set) var isRefreshing: Bool = false
    @Published private(set) var lastError: String?
    @Published private(set) var lastUpdated: Date?

    private let session: URLSession
    private let baseURL: URL?

    init(session: URLSession = .shared) {
        self.session = session
        // Priority: UserDefaults override > Info.plist > nil (offline-only)
        if let raw = UserDefaults.standard.string(forKey: "CatalogBaseURL"),
           let url = URL(string: raw), !raw.isEmpty {
            self.baseURL = url
        } else if let raw = Bundle.main.object(forInfoDictionaryKey: "CatalogBaseURL") as? String,
                  let url = URL(string: raw), !raw.isEmpty {
            self.baseURL = url
        } else {
            self.baseURL = nil
        }
        loadBundled()
        loadCached()
    }

    /// Override the catalog base URL at runtime (e.g. from a developer
    /// menu) and persist the choice across launches.
    func setRemoteBaseURL(_ urlString: String) {
        UserDefaults.standard.set(urlString, forKey: "CatalogBaseURL")
    }

    func story(id: String) -> CatalogStory? {
        stories.first { $0.id == id }
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
            var fetched: [CatalogStory] = []
            for entry in index.stories {
                if let story = try await fetchStory(entry: entry, base: baseURL) {
                    fetched.append(story)
                }
            }
            if !fetched.isEmpty {
                self.stories = mergeStories(local: self.stories, remote: fetched)
                self.lastUpdated = index.updatedAt
                cacheCurrent()
            }
            self.lastError = nil
        } catch {
            self.lastError = error.localizedDescription
        }
    }

    private func fetchStory(entry: CatalogIndexEntry, base: URL) async throws -> CatalogStory? {
        guard let path = entry.storyURL else { return nil }
        let url = URL(string: path, relativeTo: base) ?? base.appendingPathComponent(path)
        let (data, _) = try await session.data(from: url)
        return try CatalogJSON.decoder.decode(CatalogStory.self, from: data)
    }

    private func mergeStories(local: [CatalogStory], remote: [CatalogStory]) -> [CatalogStory] {
        var byId: [String: CatalogStory] = [:]
        for s in local { byId[s.id] = s }
        for s in remote { byId[s.id] = s }   // remote wins
        return byId.values.sorted { $0.addedAt > $1.addedAt }
    }

    // MARK: Bundled seed

    private func loadBundled() {
        // Try with subdirectory (folder reference) first, then flat
        let indexURL = bundleURL(for: "index", subdir: "Catalog")
        guard let url = indexURL else { return }
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
            self.stories = loaded.sorted { $0.addedAt > $1.addedAt }
            self.lastUpdated = index.updatedAt
        } catch {
            self.lastError = "bundle load: \(error.localizedDescription)"
        }
    }

    private func bundleURL(for resource: String, subdir: String) -> URL? {
        if let url = Bundle.main.url(forResource: resource, withExtension: "json", subdirectory: subdir) {
            return url
        }
        return Bundle.main.url(forResource: resource, withExtension: "json")
    }

    // MARK: Disk cache

    private var cacheURL: URL? {
        guard let dir = try? FileManager.default.url(for: .applicationSupportDirectory,
                                                      in: .userDomainMask,
                                                      appropriateFor: nil,
                                                      create: true) else { return nil }
        return dir.appendingPathComponent("catalog.cache.json")
    }

    private func cacheCurrent() {
        guard let url = cacheURL else { return }
        if let data = try? CatalogJSON.encoder.encode(stories) {
            try? data.write(to: url, options: .atomic)
        }
    }

    private func loadCached() {
        guard let url = cacheURL,
              FileManager.default.fileExists(atPath: url.path),
              let data = try? Data(contentsOf: url),
              let cached = try? CatalogJSON.decoder.decode([CatalogStory].self, from: data) else {
            return
        }
        if !cached.isEmpty {
            self.stories = mergeStories(local: self.stories, remote: cached)
        }
    }
}
