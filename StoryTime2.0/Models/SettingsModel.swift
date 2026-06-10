import SwiftUI

class SettingsModel: ObservableObject {
    @AppStorage("textSize") var textSize: Double = 17
    @AppStorage("typingSpeed") var typingSpeed: Double = 0.05
    @AppStorage("isDarkMode") var isDarkMode: Bool = false {
        didSet {
            applyTheme()
        }
    }
    @AppStorage("selectedFontName") var selectedFontName: String = "New York"
    @AppStorage("selectedTheme") var selectedTheme: Int = 0 // 0: Light Yellow, 1: Light Grey, 2: Custom
    @AppStorage("customThemeColor") var customThemeColor: String = "FFFFFF" // Stored as hex
    @AppStorage("narrationRate") var narrationRate: Double = 0.5 // 0.0 (slowest) … 1.0 (fastest), mapped to AVSpeechUtterance rates
    @AppStorage("typewriterEnabled") var typewriterEnabled: Bool = false
    @AppStorage("reminderEnabled") var reminderEnabled: Bool = false
    @AppStorage("reminderHour") var reminderHour: Int = 19
    @AppStorage("reminderMinute") var reminderMinute: Int = 0
    /// When on, the daily reminder picks a real catalog title and uses it
    /// as the notification body, like a curator nudging tonight's read.
    @AppStorage("dailyStoryEnabled") var dailyStoryEnabled: Bool = false
    /// Loop genre ambience audio under the reader. The toggle is harmless
    /// if no bundled audio assets are present.
    @AppStorage("ambienceEnabled") var ambienceEnabled: Bool = false
    /// Pass-and-play companion mode: two players alternate decisions on
    /// the same device. Toggle in Settings; reader shows whose turn it is.
    @AppStorage("companionEnabled") var companionEnabled: Bool = false
    @AppStorage("companionPlayerA") var companionPlayerA: String = "Player 1"
    @AppStorage("companionPlayerB") var companionPlayerB: String = "Player 2"
    /// One-shot migration flag so the old UserDefaults-backed key is moved
    /// into the Keychain at first launch after this change.
    @AppStorage("anthropicAPIKey_migratedToKeychain_v1") private var apiKeyMigrated: Bool = false
    /// Legacy UserDefaults slot for the key. We only read this once, to
    /// migrate it into the Keychain on first launch, then clear it.
    @AppStorage("anthropicAPIKey") private var legacyAnthropicAPIKey: String = ""

    /// Anthropic API key for the AI generator. Stored in the Keychain,
    /// never sent anywhere except api.anthropic.com.
    var anthropicAPIKey: String {
        get {
            migrateLegacyKeyIfNeeded()
            return SecretStore.get(SecretKey.anthropicAPIKey) ?? ""
        }
        set {
            SecretStore.set(newValue, for: SecretKey.anthropicAPIKey)
            objectWillChange.send()
        }
    }

    private func migrateLegacyKeyIfNeeded() {
        guard !apiKeyMigrated else { return }
        defer { apiKeyMigrated = true }
        let legacy = legacyAnthropicAPIKey
        if !legacy.isEmpty {
            SecretStore.set(legacy, for: SecretKey.anthropicAPIKey)
            legacyAnthropicAPIKey = ""
        }
    }

    /// Today's AI generation count (per-calendar-day spend cap).
    @AppStorage("aiGenerationsToday") private(set) var aiGenerationsToday: Int = 0
    @AppStorage("aiGenerationsResetAt") private var aiGenerationsResetAt: Double = 0
    /// Soft cap on AI generations per day. Keeps a stolen key from racking
    /// up real money. Tunable in code; not user-facing.
    let aiDailyCap: Int = 20

    /// Atomically record a generation, returning false if the daily cap is
    /// already hit.
    func recordAIGeneration() -> Bool {
        rolloverAICountIfNeeded()
        guard aiGenerationsToday < aiDailyCap else { return false }
        aiGenerationsToday += 1
        return true
    }

    /// How many generations the user can still do today.
    var aiGenerationsRemaining: Int {
        rolloverAICountIfNeeded()
        return max(0, aiDailyCap - aiGenerationsToday)
    }

    private func rolloverAICountIfNeeded() {
        let today = Calendar.current.startOfDay(for: Date()).timeIntervalSince1970
        if aiGenerationsResetAt != today {
            aiGenerationsResetAt = today
            aiGenerationsToday = 0
        }
    }

    let minTextSize: Double = 12
    let maxTextSize: Double = 24
    let minTypingSpeed: Double = 0.01
    let maxTypingSpeed: Double = 0.1
    
    let availableFonts = [
        "New York",
        "Georgia",
        "Palatino",
        "Times New Roman",
        "Baskerville"
    ]
    
    var themeColor: Color {
        switch selectedTheme {
        case 0:
            return Color(hex: "FAF7E8") // Light Yellow
        case 1:
            return Color(hex: "F5F5F5") // Light Grey
        case 2:
            return Color(hex: customThemeColor)
        default:
            return Color(hex: "FAF7E8")
        }
    }

    /// Maps the user's chosen reading font to a SwiftUI `Font`. Unknown names
    /// fall back to the bundled body serif so the reader always renders.
    func readerFont(_ size: CGFloat) -> Font {
        switch selectedFontName {
        case "New York":        return .system(size: size, design: .serif)
        case "Georgia":         return .custom("Georgia", size: size)
        case "Palatino":        return .custom("Palatino", size: size)
        case "Times New Roman": return .custom("TimesNewRomanPSMT", size: size)
        case "Baskerville":     return .custom("Baskerville", size: size)
        default:                return Theme.Fonts.body(size)
        }
    }

    init() {
        applyTheme()
    }
    
    private func applyTheme() {
        // Set the system-wide appearance
        if let windowScene = UIApplication.shared.connectedScenes.first as? UIWindowScene {
            windowScene.windows.forEach { window in
                window.overrideUserInterfaceStyle = isDarkMode ? .dark : .light
            }
        }
    }
}

// Color hex helpers now live in Theme.swift.