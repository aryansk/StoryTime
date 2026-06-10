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
