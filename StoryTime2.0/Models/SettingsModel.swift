import SwiftUI

class SettingsModel: ObservableObject {
    @AppStorage("textSize") var textSize: Double = 16
    @AppStorage("isDarkMode") var isDarkMode: Bool = false {
        didSet {
            applyTheme()
        }
    }
    @AppStorage("selectedFontName") var selectedFontName: String = "New York"
    @AppStorage("selectedTheme") var selectedTheme: Int = 0 // 0: Light Yellow, 1: Light Grey, 2: Custom
    @AppStorage("customThemeColor") var customThemeColor: String = "FFFFFF" // Stored as hex
    
    let minTextSize: Double = 12
    let maxTextSize: Double = 24
    
    let availableFonts = [
        "New York",
        "Georgia",
        "Palatino",
        "Times New Roman",
        "Baskerville"
    ]
    
    @Published var isTransitioning: Bool = false
    private var themeTransitionTimer: Timer?
    
    @Published private var currentThemeColor: Color
    
    var themeColor: Color {
        currentThemeColor
    }
    
    init() {
        // Initialize with default theme color
        self.currentThemeColor = Color(hex: "FFFBE6") // Light Yellow
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
    
    func transitionToTheme(_ newTheme: Int) {
        isTransitioning = true
        
        withAnimation(.spring(response: 0.6, dampingFraction: 0.8)) {
            selectedTheme = newTheme
            updateThemeColor()
        }
        
        // Reset transition flag after animation completes
        themeTransitionTimer?.invalidate()
        themeTransitionTimer = Timer.scheduledTimer(withTimeInterval: 0.6, repeats: false) { [weak self] _ in
            self?.isTransitioning = false
        }
    }
    
    private func updateThemeColor() {
        switch selectedTheme {
        case 0:
            currentThemeColor = Color(hex: "FFFBE6") // Light Yellow
        case 1:
            currentThemeColor = Color(hex: "F5F5F5") // Light Grey
        case 2:
            currentThemeColor = Color(hex: customThemeColor)
        default:
            currentThemeColor = Color(hex: "FFFBE6")
        }
    }
}

extension Color {
    init(hex: String) {
        let hex = hex.trimmingCharacters(in: CharacterSet.alphanumerics.inverted)
        var int: UInt64 = 0
        Scanner(string: hex).scanHexInt64(&int)
        let a, r, g, b: UInt64
        switch hex.count {
        case 3: // RGB (12-bit)
            (a, r, g, b) = (255, (int >> 8) * 17, (int >> 4 & 0xF) * 17, (int & 0xF) * 17)
        case 6: // RGB (24-bit)
            (a, r, g, b) = (255, int >> 16, int >> 8 & 0xFF, int & 0xFF)
        case 8: // ARGB (32-bit)
            (a, r, g, b) = (int >> 24, int >> 16 & 0xFF, int >> 8 & 0xFF, int & 0xFF)
        default:
            (a, r, g, b) = (255, 0, 0, 0)
        }
        self.init(
            .sRGB,
            red: Double(r) / 255,
            green: Double(g) / 255,
            blue:  Double(b) / 255,
            opacity: Double(a) / 255
        )
    }
    
    func toHex() -> String {
        let uic = UIColor(self)
        guard let components = uic.cgColor.components, components.count >= 3 else {
            return "FFFFFF"
        }
        let r = Float(components[0])
        let g = Float(components[1])
        let b = Float(components[2])
        return String(format: "%02lX%02lX%02lX",
                     lroundf(r * 255),
                     lroundf(g * 255),
                     lroundf(b * 255))
    }
} 