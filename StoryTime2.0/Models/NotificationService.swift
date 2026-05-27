import Foundation
import UserNotifications

enum NotificationAuthState {
    case unknown, authorized, denied
}

final class NotificationService: ObservableObject {
    @Published private(set) var authState: NotificationAuthState = .unknown

    private let reminderIdentifier = "storytime.dailyReminder"
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
}
