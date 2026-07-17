import Foundation

struct ReadingProgress: Codable, Identifiable, Hashable {
    var storyKey: String
    var title: String
    var storyDescription: String
    var nodeId: String
    var sceneTitle: String?
    var lastUpdated: Date
    /// Optional for backward-compatible decoding of existing v2 saves.
    var fraction: Double?

    var id: String { storyKey }
    var completionFraction: Double { min(1, max(0, fraction ?? 0.05)) }
}

final class ReadingProgressStore: ObservableObject {
    @Published private(set) var entries: [String: ReadingProgress] = [:]

    private let defaultsKey = "readingProgress.v2"
    /// Coalesces frequent saves (one per scene visit) into a single debounced
    /// disk write, encoded off the main thread. The in-memory `entries` still
    /// updates synchronously so the UI stays live.
    private var pendingWrite: DispatchWorkItem?

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
              sceneTitle: String? = nil,
              fraction: Double? = nil) {
        entries[storyKey] = ReadingProgress(
            storyKey: storyKey,
            title: title,
            storyDescription: description,
            nodeId: nodeId,
            sceneTitle: sceneTitle,
            lastUpdated: Date(),
            fraction: fraction
        )
        persistDebounced()
    }

    func clear(storyKey: String) {
        entries.removeValue(forKey: storyKey)
        persistNow()
    }

    /// Schedule a coalesced write ~0.6s out, replacing any pending one.
    private func persistDebounced() {
        pendingWrite?.cancel()
        let snapshot = entries
        let key = defaultsKey
        let work = DispatchWorkItem {
            if let data = try? JSONEncoder().encode(snapshot) {
                UserDefaults.standard.set(data, forKey: key)
            }
        }
        pendingWrite = work
        DispatchQueue.global(qos: .utility).asyncAfter(deadline: .now() + 0.6, execute: work)
    }

    /// Flush immediately (used for clears, which shouldn't be lost).
    private func persistNow() {
        pendingWrite?.cancel()
        pendingWrite = nil
        let snapshot = entries
        let key = defaultsKey
        DispatchQueue.global(qos: .utility).async {
            if let data = try? JSONEncoder().encode(snapshot) {
                UserDefaults.standard.set(data, forKey: key)
            }
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
