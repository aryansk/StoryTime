import SwiftUI

class SettingsModel: ObservableObject {
    @AppStorage("textSize") var textSize: Double = 16
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
    @AppStorage("reminderEnabled") var reminderEnabled: Bool = false
    @AppStorage("reminderHour") var reminderHour: Int = 19
    @AppStorage("reminderMinute") var reminderMinute: Int = 0

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
            return Color(hex: "FFFBE6") // Light Yellow
        case 1:
            return Color(hex: "F5F5F5") // Light Grey
        case 2:
            return Color(hex: customThemeColor)
        default:
            return Color(hex: "FFFBE6")
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