import UIKit

/// Small, semantic feedback vocabulary for the interactive-reading loop.
/// Keeping the mapping in one place prevents every screen from inventing its
/// own intensity and makes the experience easy to mute.
enum NarrativeFeedbackEvent {
    case selection
    case pageTurn
    case bookmark
    case ending
}

@MainActor
enum NarrativeFeedback {
    static func play(_ event: NarrativeFeedbackEvent, enabled: Bool = true) {
        guard enabled else { return }

        switch event {
        case .selection:
            UISelectionFeedbackGenerator().selectionChanged()
        case .pageTurn:
            UIImpactFeedbackGenerator(style: .light).impactOccurred()
        case .bookmark:
            UIImpactFeedbackGenerator(style: .medium).impactOccurred()
        case .ending:
            let generator = UINotificationFeedbackGenerator()
            generator.notificationOccurred(.success)
        }
    }
}
