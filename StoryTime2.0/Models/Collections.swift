import Foundation

// MARK: - Curated collections
//
// Mood-based and curator-curated groupings shown above the genre pills
// in the catalog. Each collection has either an explicit list of story
// ids or a filter predicate against the catalog.

struct StoryCollection: Identifiable, Hashable {
    let id: String
    let title: String
    let subtitle: String
    /// "doodle name" used by the chip — falls back to .sparkle.
    let doodle: String

    /// Selection rule. Either explicit ids or a predicate on CatalogStory.
    enum Rule {
        case explicit(Set<String>)
        case predicate((CatalogStory) -> Bool)
    }
    let rule: Rule

    func matches(_ story: CatalogStory) -> Bool {
        switch rule {
        case .explicit(let ids):
            return ids.contains(story.id)
        case .predicate(let p):
            return p(story)
        }
    }

    // Hashable on id — predicates aren't hashable so we don't try.
    static func == (lhs: StoryCollection, rhs: StoryCollection) -> Bool { lhs.id == rhs.id }
    func hash(into hasher: inout Hasher) { hasher.combine(id) }
}

enum StoryCollections {
    /// Master list, displayed left-to-right in the catalog "Collections" row.
    static let all: [StoryCollection] = [
        StoryCollection(
            id: "night-shelf",
            title: "The Night Shelf",
            subtitle: "First-party after-midnight originals",
            doodle: "sparkle",
            rule: .predicate { $0.tags.contains("night-shelf") }
        ),
        StoryCollection(
            id: "quick",
            title: "Quick Reads",
            subtitle: "Five-minute stories",
            doodle: "clock",
            rule: .predicate { $0.tags.contains("mini") }
        ),
        StoryCollection(
            id: "loved",
            title: "Loved",
            subtitle: "Curator favorites",
            doodle: "starFill",
            rule: .predicate { $0.isLoved }
        ),
        StoryCollection(
            id: "books",
            title: "Books",
            subtitle: "Step inside a classic novel",
            doodle: "tv",
            rule: .predicate { $0.kind == .book }
        ),
        StoryCollection(
            id: "classics",
            title: "Classics",
            subtitle: "25 famous movies & 25 famous books",
            doodle: "sparkle",
            rule: .predicate { $0.id.hasPrefix("fm-") || $0.id.hasPrefix("fb-") }
        ),
        StoryCollection(
            id: "cozy",
            title: "Cozy",
            subtitle: "Warm, gentle, low-stakes",
            doodle: "popcorn",
            rule: .predicate { story in
                let cozyIds: Set<String> = [
                    "abbott-supply-day", "superstore-closing-shift",
                    "young-sheldon-science-fair", "the-intern-day-one",
                    "fm-forrest-gump", "fm-lion-king", "fm-wizard-of-oz",
                    "fb-pride-prejudice", "fb-hobbit", "more-the-merrier-thanksgiving",
                ]
                return cozyIds.contains(story.id) || story.genre == .comedy
            }
        ),
        StoryCollection(
            id: "tense",
            title: "Tense",
            subtitle: "Hold-your-breath stories",
            doodle: "clapperboard",
            rule: .predicate { $0.genre == .thriller || $0.genre == .horror }
        ),
        StoryCollection(
            id: "tearjerkers",
            title: "Tear-jerkers",
            subtitle: "Bring tissues",
            doodle: "heart",
            rule: .predicate { story in
                let weepy: Set<String> = [
                    "the-lost-bus-evacuation", "shrinking-the-honest-week",
                    "wuthering-heights-the-moor", "pursuit-happiness-the-internship",
                    "fm-forrest-gump", "fm-titanic", "fm-schindlers-list",
                    "fm-saving-private-ryan", "fm-et", "fm-lion-king",
                    "fb-beloved", "fb-tale-two-cities",
                ]
                return weepy.contains(story.id)
            }
        ),
        StoryCollection(
            id: "epic",
            title: "Epic",
            subtitle: "Big worlds, big stakes",
            doodle: "flame",
            rule: .predicate { story in
                story.genre == .fantasy || story.genre == .sciFi || story.genre == .action
            }
        ),
        StoryCollection(
            id: "clever",
            title: "Clever",
            subtitle: "Twists, deductions, schemes",
            doodle: "branch",
            rule: .predicate { story in
                let clever: Set<String> = [
                    "fb-sherlock-holmes", "fb-and-then-none",
                    "wayward-tall-pines", "bodkin-the-podcast",
                    "him-and-hers-the-recording", "cabin-10-the-luxury-cruise",
                    "the-boys-the-leak", "loot-the-giveaway",
                    "fm-pulp-fiction", "fm-the-matrix", "fm-inception",
                ]
                return clever.contains(story.id)
            }
        ),
        StoryCollection(
            id: "adapted",
            title: "Book → Screen",
            subtitle: "Stories that lived twice",
            doodle: "bookmark",
            rule: .explicit([
                // Things that exist on screen and on the page in the curated set.
                "wuthering-heights-the-moor",  // book + WH source
                "fb-hobbit", "fb-lotr",
                "fm-lotr-fotr",
                "fb-pride-prejudice",
                "fb-1984", "fb-frankenstein", "fb-dracula",
                "fb-jane-eyre", "fb-mockingbird",
                "fb-harry-potter-1", "fb-don-quixote",
                "fb-and-then-none",
            ])
        ),
    ]

    static func stories(in collection: StoryCollection, from catalog: [CatalogStory]) -> [CatalogStory] {
        catalog.filter { collection.matches($0) }
    }
}
