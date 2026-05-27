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

    struct Palette {
        /// Pale warm buttery cream — primary page background.
        static let butter   = Color(red: 0.965, green: 0.937, blue: 0.831) // #F6EFD4
        /// Soft, slightly grayish muted pastel blue — secondary surfaces.
        static let mist     = Color(red: 0.847, green: 0.871, blue: 0.910) // #D8DEE8
        /// Very dark blue / off-black. Used for all text and linework.
        static let ink      = Color(red: 0.102, green: 0.153, blue: 0.267) // #1A2744
        /// Muted ink for secondary copy.
        static let inkSoft  = Color(red: 0.102, green: 0.153, blue: 0.267).opacity(0.55)
        /// Faint ink tint for hairlines and disabled states.
        static let inkHair  = Color(red: 0.102, green: 0.153, blue: 0.267).opacity(0.18)
        /// Slightly deeper butter for pressed/selected fills on yellow.
        static let butterDeep = Color(red: 0.929, green: 0.875, blue: 0.741) // #EDDFBD
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
    var color: Color = Theme.Palette.butter
    var body: some View {
        color.ignoresSafeArea()
    }
}
