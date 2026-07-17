import Foundation

// MARK: - Catalog data model
//
// Stories are delivered as JSON, either bundled (for offline / first
// launch) or fetched from a remote index. Each story is a graph of
// nodes; the user navigates by picking choices.

enum StoryKind: String, Codable, CaseIterable {
    case movie
    case show
    case book

    var displayName: String {
        switch self {
        case .movie: return "Movie"
        case .show:  return "Show"
        case .book:  return "Book"
        }
    }
}

enum StoryGenre: String, Codable, CaseIterable, Identifiable, Hashable {
    case all       = "All"
    case drama     = "Drama"
    case comedy    = "Comedy"
    case thriller  = "Thriller"
    case sciFi     = "Sci-Fi"
    case horror    = "Horror"
    case fantasy   = "Fantasy"
    case action    = "Action"

    var id: String { rawValue }
}

struct CatalogStory: Codable, Identifiable, Hashable {
    let id: String
    let title: String
    let sourceTitle: String        // e.g. "Dune: Part Two"
    let kind: StoryKind
    let synopsis: String
    let releaseYear: Int?
    let addedAt: Date
    let genre: StoryGenre
    let tags: [String]
    /// Curator's star rating, 1...5. Optional so older payloads still decode.
    let rating: Int?
    /// Curator's "loved" glow (the 🌟 in the source list).
    let loved: Bool?
    /// Optional "next story in saga" link, e.g. Dune I → Dune II.
    let nextStoryId: String?
    let startNodeId: String
    let nodes: [StoryNode]

    /// Stable key used for progress + favorites persistence.
    var storageKey: String { id }

    /// Clamped star rating, or nil when unrated.
    var stars: Int? {
        guard let rating else { return nil }
        return min(5, max(0, rating))
    }
    var isLoved: Bool { loved ?? false }

    func node(id: String) -> StoryNode? {
        nodes.first { $0.id == id }
    }

    static func == (lhs: CatalogStory, rhs: CatalogStory) -> Bool { lhs.id == rhs.id }
    func hash(into hasher: inout Hasher) { hasher.combine(id) }

    var isNewThisWeek: Bool {
        addedAt.timeIntervalSinceNow > -60 * 60 * 24 * 7
    }

    /// Reader-facing length estimate. Interactive scenes are intentionally
    /// short, but choices and consequence beats add thinking time that a
    /// plain word-count estimate misses.
    ///
    /// Memoized: the raw computation word-counts every node, and the
    /// recommendation scorers call this for the whole catalog on every
    /// Discover render — uncached, that's megabytes of string splitting per
    /// keystroke in the search field. `addedAt` doubles as the per-story
    /// revision, so a remote update naturally misses the stale entry.
    var estimatedMinutes: Int {
        let key = "\(id)|\(addedAt.timeIntervalSinceReferenceDate)"
        if let cached = Self.minutesCache.value(for: key) { return cached }
        let words = nodes.reduce(0) { total, node in
            total + node.text.wordCount
                + node.choices.reduce(0) { $0 + $1.text.wordCount + $1.consequence.wordCount }
        }
        let readingMinutes = Double(words) / 190.0
        let decisionMinutes = Double(decisionCount) * 0.22
        let minutes = max(2, Int(ceil(readingMinutes + decisionMinutes)))
        Self.minutesCache.store(minutes, for: key)
        return minutes
    }

    /// Lock-protected so nonisolated decode paths and the main actor can
    /// both read safely.
    private static let minutesCache = MinutesCache()

    private final class MinutesCache: @unchecked Sendable {
        private var values: [String: Int] = [:]
        private let lock = NSLock()

        func value(for key: String) -> Int? {
            lock.lock(); defer { lock.unlock() }
            return values[key]
        }

        func store(_ minutes: Int, for key: String) {
            lock.lock(); defer { lock.unlock() }
            values[key] = minutes
        }
    }

    var decisionCount: Int { nodes.filter { !$0.isEnding }.count }
    var endingCount: Int { nodes.filter(\.isEnding).count }

    /// A normalized progress estimate based on graph depth instead of raw
    /// node count. Branching stories may contain many scenes a single play-
    /// through never visits, so `current index / nodes.count` understates
    /// progress badly.
    func progressFraction(at nodeId: String) -> Double {
        let byId = Dictionary(nodes.map { ($0.id, $0) }, uniquingKeysWith: { first, _ in first })
        guard byId[startNodeId] != nil else { return 0 }

        var depth: [String: Int] = [startNodeId: 0]
        var queue: [String] = [startNodeId]
        var cursor = 0
        while cursor < queue.count {
            let id = queue[cursor]
            cursor += 1
            guard let node = byId[id], let currentDepth = depth[id] else { continue }
            for choice in node.choices {
                guard let next = choice.nextNodeId, byId[next] != nil else { continue }
                let candidate = currentDepth + 1
                if depth[next] == nil || candidate < depth[next]! {
                    depth[next] = candidate
                    queue.append(next)
                }
            }
        }

        guard let current = depth[nodeId] else { return 0 }
        let endingDepths = nodes.filter(\.isEnding).compactMap { depth[$0.id] }
        let journeyDepth = max(1, endingDepths.max() ?? depth.values.max() ?? 1)
        return min(1, max(0.04, Double(current + 1) / Double(journeyDepth + 1)))
    }
}

struct StoryNode: Codable, Hashable {
    let id: String
    let text: String
    /// Optional scene title shown above the text.
    let sceneTitle: String?
    let choices: [StoryChoice]
    let isEnding: Bool
    let endingTitle: String?
}

struct StoryChoice: Codable, Hashable {
    let text: String
    let consequence: String
    let nextNodeId: String?
}

// MARK: - JSON index manifest (for remote loading)

struct CatalogIndex: Codable {
    let version: Int
    let updatedAt: Date
    let stories: [CatalogIndexEntry]
}

struct CatalogIndexEntry: Codable, Identifiable {
    let id: String
    let title: String
    let sourceTitle: String
    let kind: StoryKind
    let synopsis: String
    let releaseYear: Int?
    let addedAt: Date
    let genre: StoryGenre
    let tags: [String]
    let rating: Int?
    let loved: Bool?
    let nextStoryId: String?
    /// URL to the per-story JSON (relative or absolute).
    let storyURL: String?
}

// MARK: - Shared JSON helpers

enum CatalogJSON {
    static var decoder: JSONDecoder {
        let d = JSONDecoder()
        d.dateDecodingStrategy = .iso8601
        return d
    }
    static var encoder: JSONEncoder {
        let e = JSONEncoder()
        e.dateEncodingStrategy = .iso8601
        e.outputFormatting = [.prettyPrinted, .sortedKeys]
        return e
    }
}

private extension String {
    var wordCount: Int {
        split { !$0.isLetter && !$0.isNumber && $0 != "'" && $0 != "’" }.count
    }
}
