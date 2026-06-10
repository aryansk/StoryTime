import Foundation

// MARK: - Endings tracker
//
// Per-story record of which ending node ids the reader has reached. Used
// to surface "3 of 7 endings discovered" on the start screen, and to mark
// individual endings as revealed/undiscovered in the endings grid.

final class EndingsTracker: ObservableObject {
    @Published private(set) var discovered: [String: Set<String>] = [:]

    private let defaultsKey = "endingsTracker.v1"

    init() {
        load()
    }

    /// Returns the set of ending node ids the reader has reached for this story.
    func reached(for storyKey: String) -> Set<String> {
        discovered[storyKey] ?? []
    }

    /// Convenience: count of discovered endings for the given story.
    func count(for storyKey: String) -> Int {
        reached(for: storyKey).count
    }

    /// Record that a given ending node has been reached. Idempotent.
    func record(storyKey: String, endingNodeId: String) {
        var set = discovered[storyKey] ?? []
        let inserted = set.insert(endingNodeId).inserted
        if inserted {
            discovered[storyKey] = set
            persist()
        }
    }

    /// Reset all tracked endings (for the "clear progress" flow).
    func reset() {
        discovered = [:]
        persist()
    }

    // MARK: Persistence

    private func persist() {
        // Set is not Codable directly; convert to arrays.
        let plain = discovered.mapValues { Array($0) }
        if let data = try? JSONEncoder().encode(plain) {
            UserDefaults.standard.set(data, forKey: defaultsKey)
        }
    }

    private func load() {
        guard let data = UserDefaults.standard.data(forKey: defaultsKey),
              let decoded = try? JSONDecoder().decode([String: [String]].self, from: data) else {
            return
        }
        discovered = decoded.mapValues { Set($0) }
    }
}
