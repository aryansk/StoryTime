import Foundation

struct ReadingProgress: Codable, Identifiable, Hashable {
    var storyKey: String
    var title: String
    var storyDescription: String
    var nodeId: String
    var sceneTitle: String?
    var lastUpdated: Date

    var id: String { storyKey }
}

final class ReadingProgressStore: ObservableObject {
    @Published private(set) var entries: [String: ReadingProgress] = [:]

    private let defaultsKey = "readingProgress.v2"

    init() {
        load()
    }

    var inProgress: [ReadingProgress] {
        entries.values.sorted { $0.lastUpdated > $1.lastUpdated }
    }

    func progress(for storyKey: String) -> ReadingProgress? {
        entries[storyKey]
    }

    func save(storyKey: String,
              title: String,
              description: String,
              nodeId: String,
              sceneTitle: String? = nil) {
        entries[storyKey] = ReadingProgress(
            storyKey: storyKey,
            title: title,
            storyDescription: description,
            nodeId: nodeId,
            sceneTitle: sceneTitle,
            lastUpdated: Date()
        )
        persist()
    }

    func clear(storyKey: String) {
        entries.removeValue(forKey: storyKey)
        persist()
    }

    private func persist() {
        if let data = try? JSONEncoder().encode(entries) {
            UserDefaults.standard.set(data, forKey: defaultsKey)
        }
    }

    private func load() {
        guard let data = UserDefaults.standard.data(forKey: defaultsKey),
              let decoded = try? JSONDecoder().decode([String: ReadingProgress].self, from: data) else {
            return
        }
        entries = decoded
    }
}
