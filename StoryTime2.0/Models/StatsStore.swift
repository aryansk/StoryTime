import Foundation

private struct StatsSnapshot: Codable {
    var scenesRead: Int = 0
    var choicesMade: Int = 0
    var storiesStarted: Set<String> = []
    var lastReadDate: Date? = nil
    var currentStreak: Int = 0
}

final class StatsStore: ObservableObject {
    @Published private(set) var scenesRead: Int = 0
    @Published private(set) var choicesMade: Int = 0
    @Published private(set) var storiesStarted: Set<String> = []
    @Published private(set) var lastReadDate: Date? = nil
    @Published private(set) var currentStreak: Int = 0

    private let defaultsKey = "readingStats.v1"

    init() {
        load()
    }

    func recordStoryStarted(_ title: String) {
        if !storiesStarted.contains(title) {
            storiesStarted.insert(title)
        }
        bumpStreak()
        persist()
    }

    func recordSceneVisit() {
        scenesRead += 1
        bumpStreak()
        persist()
    }

    func recordChoice() {
        choicesMade += 1
        persist()
    }

    func reset() {
        scenesRead = 0
        choicesMade = 0
        storiesStarted = []
        lastReadDate = nil
        currentStreak = 0
        persist()
    }

    private func bumpStreak() {
        let today = Calendar.current.startOfDay(for: Date())
        guard let last = lastReadDate else {
            currentStreak = 1
            lastReadDate = today
            return
        }
        let lastDay = Calendar.current.startOfDay(for: last)
        let dayDiff = Calendar.current.dateComponents([.day], from: lastDay, to: today).day ?? 0
        switch dayDiff {
        case 0: break // same day, streak unchanged
        case 1: currentStreak += 1
        default: currentStreak = 1
        }
        lastReadDate = today
    }

    private func persist() {
        let snapshot = StatsSnapshot(
            scenesRead: scenesRead,
            choicesMade: choicesMade,
            storiesStarted: storiesStarted,
            lastReadDate: lastReadDate,
            currentStreak: currentStreak
        )
        if let data = try? JSONEncoder().encode(snapshot) {
            UserDefaults.standard.set(data, forKey: defaultsKey)
        }
    }

    private func load() {
        guard let data = UserDefaults.standard.data(forKey: defaultsKey),
              let snapshot = try? JSONDecoder().decode(StatsSnapshot.self, from: data) else {
            return
        }
        scenesRead = snapshot.scenesRead
        choicesMade = snapshot.choicesMade
        storiesStarted = snapshot.storiesStarted
        lastReadDate = snapshot.lastReadDate
        currentStreak = snapshot.currentStreak
    }
}
