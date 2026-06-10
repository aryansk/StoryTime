import Foundation
import UserNotifications

enum NotificationAuthState {
    case unknown, authorized, denied
}

final class NotificationService: ObservableObject {
    @Published private(set) var authState: NotificationAuthState = .unknown

    private let reminderIdentifier = "storytime.dailyReminder"
    private let dailyStoryIdentifier = "storytime.dailyStory"
    private let center = UNUserNotificationCenter.current()

    init() {
        refreshAuthState()
    }

    func refreshAuthState() {
        center.getNotificationSettings { [weak self] settings in
            DispatchQueue.main.async {
                switch settings.authorizationStatus {
                case .authorized, .provisional, .ephemeral:
                    self?.authState = .authorized
                case .denied:
                    self?.authState = .denied
                default:
                    self?.authState = .unknown
                }
            }
        }
    }

    func requestAuthorization() async -> Bool {
        do {
            let granted = try await center.requestAuthorization(options: [.alert, .sound, .badge])
            await MainActor.run {
                self.authState = granted ? .authorized : .denied
            }
            return granted
        } catch {
            await MainActor.run { self.authState = .denied }
            return false
        }
    }

    // MARK: Plain daily reminder (legacy)

    func scheduleDailyReminder(hour: Int, minute: Int) {
        cancelReminder()

        let content = UNMutableNotificationContent()
        content.title = "Time to read"
        content.body = "Your story is waiting — keep your streak going."
        content.sound = .default

        var components = DateComponents()
        components.hour = hour
        components.minute = minute

        let trigger = UNCalendarNotificationTrigger(dateMatching: components, repeats: true)
        let request = UNNotificationRequest(identifier: reminderIdentifier, content: content, trigger: trigger)

        center.add(request) { _ in }
    }

    func cancelReminder() {
        center.removePendingNotificationRequests(withIdentifiers: [reminderIdentifier])
    }

    // MARK: Daily story (content-rich)
    //
    // Picks a story the reader hasn't started yet (or hasn't finished) and
    // schedules a single, daily-repeating notification with its title and
    // synopsis. Caller re-runs this whenever the catalog/progress changes
    // and the reminder is enabled.

    func scheduleDailyStory(hour: Int,
                            minute: Int,
                            from catalog: [CatalogStory],
                            startedKeys: Set<String>) {
        center.removePendingNotificationRequests(withIdentifiers: [dailyStoryIdentifier])

        // Prefer a story the reader hasn't started; fall back to any.
        let unstarted = catalog.filter { !startedKeys.contains($0.storageKey) }
        let pool = unstarted.isEmpty ? catalog : unstarted
        guard let pick = pool.randomElement() else { return }

        let content = UNMutableNotificationContent()
        content.title = "Tonight's story: \(pick.title)"
        content.body = pick.synopsis
        content.sound = .default
        content.userInfo = ["storyId": pick.id]

        var components = DateComponents()
        components.hour = hour
        components.minute = minute

        let trigger = UNCalendarNotificationTrigger(dateMatching: components, repeats: true)
        let request = UNNotificationRequest(identifier: dailyStoryIdentifier, content: content, trigger: trigger)
        center.add(request) { _ in }
    }

    func cancelDailyStory() {
        center.removePendingNotificationRequests(withIdentifiers: [dailyStoryIdentifier])
    }
}
