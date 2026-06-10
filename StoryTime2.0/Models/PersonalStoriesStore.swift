import Foundation

// MARK: - Personal stories store
//
// User-authored or AI-generated CatalogStory values, persisted to a JSON
// file under Application Support. These are surfaced in the catalog UI
// alongside the bundled/remote stories.
//
// We deliberately reuse the existing CatalogStory schema so personal
// stories play through the same reader, share the same endings tracker,
// share the same Choice DNA scoring, and so on. The only field of note
// is that all personal-story ids carry the "user-" prefix, which lets
// callers filter for them when needed.

@MainActor
final class PersonalStoriesStore: ObservableObject {
    @Published private(set) var stories: [CatalogStory] = []

    private let filename = "personal-stories.json"
    private var fileURL: URL? {
        guard let dir = try? FileManager.default.url(for: .applicationSupportDirectory,
                                                      in: .userDomainMask,
                                                      appropriateFor: nil,
                                                      create: true) else { return nil }
        return dir.appendingPathComponent(filename)
    }

    init() {
        load()
    }

    func add(_ story: CatalogStory) {
        // De-dup by id.
        stories.removeAll { $0.id == story.id }
        stories.insert(story, at: 0)
        persist()
    }

    func remove(id: String) {
        stories.removeAll { $0.id == id }
        persist()
    }

    func story(id: String) -> CatalogStory? {
        stories.first { $0.id == id }
    }

    // MARK: Persistence

    private func persist() {
        guard let url = fileURL else { return }
        if let data = try? CatalogJSON.encoder.encode(stories) {
            try? data.write(to: url, options: .atomic)
        }
    }

    private func load() {
        guard let url = fileURL,
              FileManager.default.fileExists(atPath: url.path),
              let data = try? Data(contentsOf: url),
              let decoded = try? CatalogJSON.decoder.decode([CatalogStory].self, from: data) else {
            return
        }
        stories = decoded
    }

    // MARK: Helpers

    /// Generate a fresh, namespaced story id from a human title.
    static func makeId(from title: String) -> String {
        let slug = title.lowercased()
            .components(separatedBy: CharacterSet.alphanumerics.inverted)
            .filter { !$0.isEmpty }
            .joined(separator: "-")
        let stub = slug.isEmpty ? "story" : String(slug.prefix(40))
        let suffix = String(Int.random(in: 1000...9999))
        return "user-\(stub)-\(suffix)"
    }
}
