import SwiftUI

// MARK: - Theme
//
// Visual identity: quirky, handcrafted, editorial.
// Buttery yellow / pastel blue backgrounds, ink-navy linework
// (never pure black), chunky rounded sans for headings,
// vintage serif for body. No drop shadows. No gradients on UI.
// Hand-drawn doodles in place of SF Symbols (see DoodleIcon.swift).

struct Theme {

    // MARK: Palette
    //
    // Every palette entry is a *dynamic* color: it resolves to a light or
    // dark variant based on the active interface style. Because the whole UI
    // reads these tokens, flipping `preferredColorScheme` (driven by the
    // user's Dark Mode toggle) re-themes the entire app for free.
    //
    // The ink↔butter pair is intentionally inverted in dark mode: ink (text
    // and linework) becomes a warm cream, and butter (the color drawn *behind*
    // ink, e.g. primary-button text and selected medallions) becomes the dark
    // page tone — so every existing contrast pairing keeps working.

    struct Palette {
        /// Behind-ink accent: pale butter in light, deep ink-navy in dark.
        static let butter   = dyn(light: UIColor(r: 0.996, g: 0.973, b: 0.851),
                                  dark:  UIColor(r: 0.121, g: 0.141, b: 0.200))
        /// Secondary card surfaces.
        static let mist     = dyn(light: UIColor(r: 0.847, g: 0.871, b: 0.910),
                                  dark:  UIColor(r: 0.169, g: 0.200, b: 0.275))
        /// All text and linework.
        static let ink      = dyn(light: UIColor(r: 0.102, g: 0.153, b: 0.267),
                                  dark:  UIColor(r: 0.925, g: 0.906, b: 0.839))
        /// Muted ink for secondary copy. Kept high enough to clear WCAG-ish
        /// contrast on butter/dark paper — faint grey-on-cream is the #1
        /// readability killer, so secondary text stays firmly legible.
        static let inkSoft  = dyn(light: UIColor(r: 0.102, g: 0.153, b: 0.267, a: 0.68),
                                  dark:  UIColor(r: 0.925, g: 0.906, b: 0.839, a: 0.74))
        /// Faint ink tint for hairlines and disabled states.
        static let inkHair  = dyn(light: UIColor(r: 0.102, g: 0.153, b: 0.267, a: 0.22),
                                  dark:  UIColor(r: 0.925, g: 0.906, b: 0.839, a: 0.26))
        /// Slightly deeper butter for pressed/selected fills.
        static let butterDeep = dyn(light: UIColor(r: 0.984, g: 0.945, b: 0.776),
                                    dark:  UIColor(r: 0.180, g: 0.212, b: 0.314))

        // MARK: Page paper presets (used by PageBackground)

        /// Default light "paper" tint (Light Yellow theme).
        static let paperYellow = Color(red: 0.996, green: 0.973, blue: 0.851) // #FEF8D9
        /// Light Grey theme paper.
        static let paperGrey   = Color(red: 0.961, green: 0.961, blue: 0.961) // #F5F5F5
        /// Dark-mode page paper (independent of the light tint choice).
        static let paperDark   = Color(red: 0.086, green: 0.102, blue: 0.149) // #161A26
    }

    /// Build a Color that resolves differently in light vs. dark interface styles.
    fileprivate static func dyn(light: UIColor, dark: UIColor) -> Color {
        Color(uiColor: UIColor { $0.userInterfaceStyle == .dark ? dark : light })
    }

    // MARK: Typography
    //
    // We bundle Space Grotesk (heading) + Source Serif 4 (body) in Resources/Fonts/.
    // Until the files are registered, we fall back to system rounded / serif so
    // the app still renders.

    struct Fonts {
        static let headingFamily = "SpaceGrotesk-Bold"
        static let headingMediumFamily = "SpaceGrotesk-Medium"
        static let bodyFamily    = "SourceSerif4-Regular"
        static let bodyItalicFamily = "SourceSerif4-Italic"

        static func heading(_ size: CGFloat) -> Font {
            if UIFont(name: headingFamily, size: size) != nil {
                return .custom(headingFamily, size: size)
            }
            return .system(size: size, weight: .black, design: .rounded)
        }

        static func headingMedium(_ size: CGFloat) -> Font {
            if UIFont(name: headingMediumFamily, size: size) != nil {
                return .custom(headingMediumFamily, size: size)
            }
            return .system(size: size, weight: .semibold, design: .rounded)
        }

        static func body(_ size: CGFloat) -> Font {
            if UIFont(name: bodyFamily, size: size) != nil {
                return .custom(bodyFamily, size: size)
            }
            return .system(size: size, weight: .regular, design: .serif)
        }

        static func bodyItalic(_ size: CGFloat) -> Font {
            if UIFont(name: bodyItalicFamily, size: size) != nil {
                return .custom(bodyItalicFamily, size: size)
            }
            return .system(size: size, weight: .regular, design: .serif).italic()
        }

        // Semantic presets
        static func display() -> Font   { heading(42) }
        static func title() -> Font     { heading(30) }
        static func sectionHeader() -> Font { heading(20) }
        static func cardTitle() -> Font { heading(18) }
        static func label() -> Font     { headingMedium(13) }
        static func bodyText() -> Font  { body(17) }
        static func small() -> Font     { body(14) }
        static func meta() -> Font      { headingMedium(11) }
    }

    // MARK: Stroke widths

    struct Stroke {
        static let hair: CGFloat   = 1.0
        static let line: CGFloat   = 1.5
        static let bold: CGFloat   = 2.0
        static let chunky: CGFloat = 2.5
    }
}

// MARK: - UIColor shorthand (used by the dynamic palette)

extension UIColor {
    convenience init(r: CGFloat, g: CGFloat, b: CGFloat, a: CGFloat = 1) {
        self.init(red: r, green: g, blue: b, alpha: a)
    }
}

// MARK: - Color hex helper (kept from previous Settings code)

extension Color {
    init(hex: String) {
        let trimmed = hex.trimmingCharacters(in: CharacterSet.alphanumerics.inverted)
        var int: UInt64 = 0
        Scanner(string: trimmed).scanHexInt64(&int)
        let a, r, g, b: UInt64
        switch trimmed.count {
        case 3:
            (a, r, g, b) = (255, (int >> 8) * 17, (int >> 4 & 0xF) * 17, (int & 0xF) * 17)
        case 6:
            (a, r, g, b) = (255, int >> 16, int >> 8 & 0xFF, int & 0xFF)
        case 8:
            (a, r, g, b) = (int >> 24, int >> 16 & 0xFF, int >> 8 & 0xFF, int & 0xFF)
        default:
            (a, r, g, b) = (255, 0, 0, 0)
        }
        self.init(.sRGB,
                  red:   Double(r) / 255,
                  green: Double(g) / 255,
                  blue:  Double(b) / 255,
                  opacity: Double(a) / 255)
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

// MARK: - Page background

struct PageBackground: View {
    @Environment(\.colorScheme) private var scheme
    // Read the user's paper-tint choice directly so every PageBackground in
    // the app reacts to Settings changes without threading `settings` through.
    @AppStorage("selectedTheme") private var selectedTheme: Int = 0
    @AppStorage("customThemeColor") private var customThemeColor: String = "FFFFFF"

    /// Optional explicit override (rarely needed).
    var color: Color? = nil

    private var lightPaper: Color {
        switch selectedTheme {
        case 1:  return Theme.Palette.paperGrey
        case 2:  return Color(hex: customThemeColor)
        default: return Theme.Palette.paperYellow
        }
    }

    var body: some View {
        let resolved = color ?? (scheme == .dark ? Theme.Palette.paperDark : lightPaper)
        resolved.ignoresSafeArea()
    }
}
