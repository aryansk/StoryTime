import Foundation

private struct StatsSnapshot: Codable {
    var scenesRead: Int = 0
    var choicesMade: Int = 0
    var storiesStarted: Set<String> = []
    var lastReadDate: Date? = nil
    var currentStreak: Int = 0
    // Optional additions keep snapshots written by earlier versions decodable.
    var completedStories: Set<String>?
    var readingSeconds: TimeInterval?
    var dailyScenesDate: Date?
    var dailyScenesRead: Int?
}

final class StatsStore: ObservableObject {
    @Published private(set) var scenesRead: Int = 0
    @Published private(set) var choicesMade: Int = 0
    @Published private(set) var storiesStarted: Set<String> = []
    @Published private(set) var lastReadDate: Date? = nil
    @Published private(set) var currentStreak: Int = 0
    @Published private(set) var completedStories: Set<String> = []
    @Published private(set) var readingSeconds: TimeInterval = 0
    @Published private(set) var dailyScenesDate: Date? = nil
    @Published private(set) var dailyScenesRead: Int = 0

    private let defaultsKey = "readingStats.v1"
    private lazy var writer = DefaultsWriter<StatsSnapshot>(key: defaultsKey)
    private var activeSessionStartedAt: Date?

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
        rolloverDailyScenesIfNeeded()
        dailyScenesRead += 1
        bumpStreak()
        persist()
    }

    func recordChoice() {
        choicesMade += 1
        persist()
    }

    func recordStoryCompleted(_ storyKey: String) {
        if completedStories.insert(storyKey).inserted {
            persist()
        }
    }

    func beginReadingSession() {
        guard activeSessionStartedAt == nil else { return }
        activeSessionStartedAt = Date()
    }

    func endReadingSession() {
        guard let started = activeSessionStartedAt else { return }
        activeSessionStartedAt = nil
        readingSeconds += max(0, Date().timeIntervalSince(started))
        persist()
    }

    var readingMinutes: Int {
        let active = activeSessionStartedAt.map { max(0, Date().timeIntervalSince($0)) } ?? 0
        return Int(((readingSeconds + active) / 60).rounded())
    }

    func todaySceneCount() -> Int {
        rolloverDailyScenesIfNeeded()
        return dailyScenesRead
    }

    func reset() {
        scenesRead = 0
        choicesMade = 0
        storiesStarted = []
        lastReadDate = nil
        currentStreak = 0
        completedStories = []
        readingSeconds = 0
        dailyScenesDate = nil
        dailyScenesRead = 0
        activeSessionStartedAt = nil
        persist(immediate: true)
    }

    private func rolloverDailyScenesIfNeeded() {
        let today = Calendar.current.startOfDay(for: Date())
        guard let stored = dailyScenesDate,
              Calendar.current.isDate(stored, inSameDayAs: today) else {
            dailyScenesDate = today
            dailyScenesRead = 0
            return
        }
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

    private func persist(immediate: Bool = false) {
        let snapshot = StatsSnapshot(
            scenesRead: scenesRead,
            choicesMade: choicesMade,
            storiesStarted: storiesStarted,
            lastReadDate: lastReadDate,
            currentStreak: currentStreak,
            completedStories: completedStories,
            readingSeconds: readingSeconds,
            dailyScenesDate: dailyScenesDate,
            dailyScenesRead: dailyScenesRead
        )
        if immediate { writer.flushNow(snapshot) } else { writer.schedule(snapshot) }
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
        completedStories = snapshot.completedStories ?? []
        readingSeconds = snapshot.readingSeconds ?? 0
        dailyScenesDate = snapshot.dailyScenesDate
        dailyScenesRead = snapshot.dailyScenesRead ?? 0
        rolloverDailyScenesIfNeeded()
    }
}
