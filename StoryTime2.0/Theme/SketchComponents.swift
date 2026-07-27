import SwiftUI

// MARK: - Sketch components
//
// Flat, hand-drawn primitives. No shadows. No gradients. Borders are
// intentionally slightly wobbly to feel like index cards / sketchbook
// pages.

// MARK: Wobbly rectangle (the basis for cards, buttons, pills)

struct WobblyRect: Shape {
    /// 0…1, how much the border deviates from a perfect rect.
    var jitter: CGFloat = 0.6
    /// Corner softness in points.
    var corner: CGFloat = 6
    /// Stable per-instance seed (so the same view always wobbles the same way).
    var seed: CGFloat = 0

    func path(in rect: CGRect) -> Path {
        var p = Path()
        let r = corner
        let j = jitter
        func w(_ base: CGFloat, _ i: Int) -> CGFloat {
            let s = sin((base + seed + CGFloat(i) * 13.7) * 12.9898) * 43758.5453
            return CGFloat(s.truncatingRemainder(dividingBy: 1)) * j - j / 2
        }
        let tl = CGPoint(x: rect.minX + r,        y: rect.minY)
        let tr = CGPoint(x: rect.maxX - r,        y: rect.minY)
        let trC = CGPoint(x: rect.maxX,           y: rect.minY + r)
        let brC = CGPoint(x: rect.maxX,           y: rect.maxY - r)
        let br = CGPoint(x: rect.maxX - r,        y: rect.maxY)
        let bl = CGPoint(x: rect.minX + r,        y: rect.maxY)
        let blC = CGPoint(x: rect.minX,           y: rect.maxY - r)
        let tlC = CGPoint(x: rect.minX,           y: rect.minY + r)

        p.move(to: tl.offset(dx: w(rect.minX, 0), dy: w(rect.minY, 1)))
        // Top
        let topMid = CGPoint(x: rect.midX, y: rect.minY + w(rect.midX, 2))
        p.addQuadCurve(to: tr.offset(dx: w(rect.maxX, 3), dy: w(rect.minY, 4)), control: topMid)
        // TR corner
        p.addQuadCurve(to: trC.offset(dx: w(rect.maxX, 5), dy: w(rect.minY + r, 6)),
                       control: CGPoint(x: rect.maxX, y: rect.minY))
        // Right
        let rightMid = CGPoint(x: rect.maxX + w(rect.midY, 7), y: rect.midY)
        p.addQuadCurve(to: brC.offset(dx: w(rect.maxX, 8), dy: w(rect.maxY - r, 9)), control: rightMid)
        // BR corner
        p.addQuadCurve(to: br.offset(dx: w(rect.maxX - r, 10), dy: w(rect.maxY, 11)),
                       control: CGPoint(x: rect.maxX, y: rect.maxY))
        // Bottom
        let botMid = CGPoint(x: rect.midX, y: rect.maxY + w(rect.midX, 12))
        p.addQuadCurve(to: bl.offset(dx: w(rect.minX + r, 13), dy: w(rect.maxY, 14)), control: botMid)
        // BL corner
        p.addQuadCurve(to: blC.offset(dx: w(rect.minX, 15), dy: w(rect.maxY - r, 16)),
                       control: CGPoint(x: rect.minX, y: rect.maxY))
        // Left
        let leftMid = CGPoint(x: rect.minX + w(rect.midY, 17), y: rect.midY)
        p.addQuadCurve(to: tlC.offset(dx: w(rect.minX, 18), dy: w(rect.minY + r, 19)), control: leftMid)
        // TL corner
        p.addQuadCurve(to: tl.offset(dx: w(rect.minX + r, 20), dy: w(rect.minY, 21)),
                       control: CGPoint(x: rect.minX, y: rect.minY))
        p.closeSubpath()
        return p
    }
}

private extension CGPoint {
    func offset(dx: CGFloat, dy: CGFloat) -> CGPoint {
        CGPoint(x: x + dx, y: y + dy)
    }
}

// MARK: SketchCard

struct SketchCard<Content: View>: View {
    let content: Content
    var fill: Color = Theme.Palette.mist
    var border: Color = Theme.Palette.ink
    var stroke: CGFloat = Theme.Stroke.line
    var corner: CGFloat = 8
    var padding: CGFloat = 18
    private let seed: CGFloat

    init(fill: Color = Theme.Palette.mist,
         border: Color = Theme.Palette.ink,
         stroke: CGFloat = Theme.Stroke.line,
         corner: CGFloat = 8,
         padding: CGFloat = 18,
         seed: CGFloat? = nil,
         @ViewBuilder content: () -> Content) {
        self.fill = fill
        self.border = border
        self.stroke = stroke
        self.corner = corner
        self.padding = padding
        // A *stable* default seed. Previously this was `CGFloat.random`, so
        // any card left unseeded re-rolled its wobble on every body
        // re-evaluation, making borders visibly shimmer when unrelated
        // state changed (and defeating shape caching). Callers that want
        // distinct wobble still pass their own content-derived seed.
        self.seed = seed ?? 7
        self.content = content()
    }

    var body: some View {
        let shape = WobblyRect(jitter: 0.6, corner: corner, seed: seed)
        content
            .padding(padding)
            .background(shape.fill(fill))
            .overlay(shape.stroke(border, lineWidth: stroke))
    }
}

// MARK: SketchButton

struct SketchButton: View {
    let title: String
    var doodle: DoodleName? = nil
    var trailingDoodle: DoodleName? = nil
    var style: Style = .primary
    var fullWidth: Bool = true
    let action: () -> Void

    enum Style { case primary, secondary, ghost }

    @State private var pressed = false

    var body: some View {
        Button(action: {
            UIImpactFeedbackGenerator(style: .light).impactOccurred()
            action()
        }) {
            HStack(spacing: 10) {
                if let d = doodle {
                    DoodleIcon(d, size: 18, color: foreground)
                }
                Text(title)
                    .font(Theme.Fonts.headingMedium(15))
                    .foregroundColor(foreground)
                if let d = trailingDoodle {
                    DoodleIcon(d, size: 16, color: foreground)
                }
            }
            .padding(.horizontal, 22)
            .padding(.vertical, 14)
            .frame(minHeight: 48)
            .frame(maxWidth: fullWidth ? .infinity : nil)
            .background(
                WobblyRect(jitter: 0.5, corner: 6, seed: 1.5)
                    .fill(background)
            )
            .overlay(
                WobblyRect(jitter: 0.5, corner: 6, seed: 1.5)
                    .stroke(borderColor, lineWidth: Theme.Stroke.bold)
            )
        }
        .buttonStyle(SketchPressStyle())
    }

    private var background: Color {
        switch style {
        case .primary:   return Theme.Palette.ink
        case .secondary: return Theme.Palette.mist
        case .ghost:     return .clear
        }
    }
    private var foreground: Color {
        switch style {
        case .primary: return Theme.Palette.butter
        case .secondary, .ghost: return Theme.Palette.ink
        }
    }
    private var borderColor: Color { Theme.Palette.ink }
}

/// The sketch vocabulary's press state: the element nudges down-right as if
/// pressed into the paper, and sinks very slightly. Kept as its own style
/// (rather than folding into `PressableStyle`) because the directional nudge
/// is what makes a hand-drawn button feel stamped rather than tapped.
struct SketchPressStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        Effect(configuration: configuration)
    }

    // See PressableStyle: @Environment only resolves inside a real View,
    // not on the ButtonStyle struct itself — and the nested type can't be
    // called `Body`, which is `ButtonStyle`'s own associated type.
    private struct Effect: View {
        let configuration: ButtonStyleConfiguration
        @Environment(\.accessibilityReduceMotion) private var reduceMotion

        var body: some View {
            let pressed = configuration.isPressed
            return configuration.label
                .offset(x: pressed ? 1.5 : 0, y: pressed ? 1.5 : 0)
                .scaleEffect(reduceMotion ? 1 : (pressed ? 0.98 : 1))
                .animation(reduceMotion ? nil : Theme.Motion.snappy, value: pressed)
        }
    }
}

// MARK: SketchPill (filter chip)

struct SketchPill: View {
    let title: String
    var doodle: DoodleName? = nil
    var selected: Bool = false
    let action: () -> Void

    @Environment(\.accessibilityReduceMotion) private var reduceMotion

    var body: some View {
        Button(action: {
            UISelectionFeedbackGenerator().selectionChanged()
            action()
        }) {
            HStack(spacing: 6) {
                if let d = doodle {
                    DoodleIcon(d, size: 14, color: Theme.Palette.ink)
                }
                Text(title)
                    .font(Theme.Fonts.headingMedium(13))
                    .foregroundColor(Theme.Palette.ink)
            }
            .padding(.horizontal, 14)
            .padding(.vertical, 10)
            .frame(minHeight: 44)
            .background(
                WobblyRect(jitter: 0.4, corner: 14, seed: CGFloat(title.stableSeed(100)))
                    .fill(selected ? Theme.Palette.butterDeep : Color.clear)
            )
            .overlay(
                WobblyRect(jitter: 0.4, corner: 14, seed: CGFloat(title.stableSeed(100)))
                    .stroke(Theme.Palette.ink, lineWidth: selected ? Theme.Stroke.bold : Theme.Stroke.line)
            )
            .scaleEffect(selected && !reduceMotion ? 1.04 : 1)
            .animation(reduceMotion ? nil : Theme.Motion.bouncy, value: selected)
        }
        .stPressable(scale: 0.94)
        .accessibilityLabel(title)
        .accessibilityAddTraits(selected ? [.isButton, .isSelected] : .isButton)
    }
}

// MARK: SketchBadge (tiny metadata pill, no interactivity)

struct SketchBadge: View {
    let text: String
    var body: some View {
        Text(text.uppercased())
            .font(Theme.Fonts.meta())
            .tracking(0.8)
            .foregroundColor(Theme.Palette.ink)
            .padding(.horizontal, 8)
            .padding(.vertical, 4)
            .overlay(
                WobblyRect(jitter: 0.3, corner: 4, seed: CGFloat(text.stableSeed(100)))
                    .stroke(Theme.Palette.ink, lineWidth: Theme.Stroke.hair)
            )
    }
}

// MARK: StarRating — hand-drawn stars + optional "loved" glow

struct StarRating: View {
    let rating: Int          // 0...5 filled stars
    var loved: Bool = false
    var size: CGFloat = 14

    var body: some View {
        HStack(spacing: 3) {
            ForEach(0..<5, id: \.self) { i in
                DoodleIcon(i < rating ? .starFill : .star,
                           size: size,
                           filled: i < rating)
                    .scaleEffect(i < rating ? 1 : 0.92)
                    .animation(Theme.Motion.bouncy.delay(Double(i) * 0.04),
                               value: rating)
            }
            if loved {
                DoodleIcon(.sparkle, size: size + 2)
                    .jitter(amplitude: 0.4)
                    .transition(.scale(scale: 0.3).combined(with: .opacity))
            }
        }
        .accessibilityElement(children: .ignore)
        .accessibilityLabel(loved
            ? "Rated \(rating) out of 5 stars, loved"
            : "Rated \(rating) out of 5 stars")
    }
}

// MARK: SectionHeader (chunky sans)

struct SketchSectionHeader: View {
    let title: String
    var trailing: AnyView? = nil
    var horizontalInset: CGFloat = 24

    init(_ title: String, trailing: AnyView? = nil, horizontalInset: CGFloat = 24) {
        self.title = title
        self.trailing = trailing
        self.horizontalInset = horizontalInset
    }

    var body: some View {
        HStack(alignment: .firstTextBaseline) {
            Text(title)
                .font(Theme.Fonts.sectionHeader())
                .foregroundColor(Theme.Palette.ink)
            Spacer()
            if let trailing { trailing }
        }
        .padding(.horizontal, horizontalInset)
    }
}

// MARK: Jitter modifier — stop-motion micro-animation
//
// Driven by TimelineView rather than a raw Timer: the previous version
// scheduled a repeating Timer in `onAppear` that was never stored and
// never invalidated, so every jittered view leaked a timer that kept
// firing (and redrawing) forever — one more per re-appearance. TimelineView
// ties the cadence to the view's lifetime and pauses automatically when the
// view is offscreen. Also honors Reduce Motion.

struct JitterModifier: ViewModifier {
    var active: Bool = true
    var amplitude: CGFloat = 0.6
    @Environment(\.accessibilityReduceMotion) private var reduceMotion
    // Set on hidden tabs so their (opacity-0 but still live) jitter animations
    // stop redrawing behind the visible tab. See ContentView.tabContent.
    @Environment(\.stJitterPaused) private var paused

    func body(content: Content) -> some View {
        if active && !reduceMotion && !paused {
            TimelineView(.animation(minimumInterval: 0.12, paused: false)) { context in
                let frame = context.date.timeIntervalSinceReferenceDate / 0.12
                content
                    .offset(x: sin(CGFloat(frame) * 1.3) * amplitude,
                            y: cos(CGFloat(frame) * 1.7) * amplitude)
            }
        } else {
            content
        }
    }
}

// MARK: Jitter-pause environment
//
// A cheap way to freeze every stop-motion animation inside a subtree without
// threading state through each view. Hidden tabs set this true.

private struct JitterPausedKey: EnvironmentKey {
    static let defaultValue = false
}

extension EnvironmentValues {
    var stJitterPaused: Bool {
        get { self[JitterPausedKey.self] }
        set { self[JitterPausedKey.self] = newValue }
    }
}

extension View {
    func jitter(_ active: Bool = true, amplitude: CGFloat = 0.6) -> some View {
        modifier(JitterModifier(active: active, amplitude: amplitude))
    }
}

// MARK: Sketch text field

struct SketchTextField: View {
    let placeholder: String
    @Binding var text: String
    var doodle: DoodleName? = nil

    var body: some View {
        HStack(spacing: 10) {
            if let d = doodle {
                DoodleIcon(d, size: 18, color: Theme.Palette.inkSoft)
            }
            TextField(placeholder, text: $text)
                .font(Theme.Fonts.body(16))
                .foregroundColor(Theme.Palette.ink)
                .tint(Theme.Palette.ink)
            if !text.isEmpty {
                Button {
                    text = ""
                } label: {
                    DoodleIcon(.xmark, size: 15, color: Theme.Palette.inkSoft)
                        .padding(4)
                        .contentShape(Rectangle())
                }
                .stPressable(scale: 0.85)
                .accessibilityLabel("Clear text")
                .transition(.scale(scale: 0.4).combined(with: .opacity))
            }
        }
        .animation(Theme.Motion.quick, value: text.isEmpty)
        .padding(.horizontal, 14)
        .padding(.vertical, 14)
        .background(
            WobblyRect(jitter: 0.4, corner: 6, seed: 2.0)
                .fill(Color.white.opacity(0.0))
        )
        .overlay(
            WobblyRect(jitter: 0.4, corner: 6, seed: 2.0)
                .stroke(Theme.Palette.ink, lineWidth: Theme.Stroke.line)
        )
    }
}

/// Key/password field that keeps the sketch vocabulary without exposing
/// sensitive text on screen or in screenshots.
struct SketchSecureField: View {
    let placeholder: String
    @Binding var text: String
    @State private var revealsText = false

    var body: some View {
        HStack(spacing: 10) {
            DoodleIcon(.shield, size: 18, color: Theme.Palette.inkSoft)
            Group {
                if revealsText {
                    TextField(placeholder, text: $text)
                } else {
                    SecureField(placeholder, text: $text)
                }
            }
            .font(Theme.Fonts.body(16))
            .foregroundColor(Theme.Palette.ink)
            .tint(Theme.Palette.ink)

            Button {
                revealsText.toggle()
            } label: {
                DoodleIcon(.focus,
                           size: 15,
                           color: Theme.Palette.inkSoft)
                    .frame(width: 32, height: 32)
                    .contentShape(Rectangle())
            }
            .buttonStyle(.plain)
            .accessibilityLabel(revealsText ? "Hide key" : "Reveal key")
        }
        .padding(.horizontal, 14)
        .padding(.vertical, 10)
        .frame(minHeight: 48)
        .overlay(
            WobblyRect(jitter: 0.4, corner: 6, seed: 2.4)
                .stroke(Theme.Palette.ink, lineWidth: Theme.Stroke.line)
        )
    }
}

// MARK: Divider doodle (squiggly)

struct SketchDivider: View {
    var body: some View {
        Canvas { context, size in
            var path = Path()
            let mid = size.height / 2
            path.move(to: CGPoint(x: 0, y: mid))
            let segments = max(4, Int(size.width / 30))
            for i in 1...segments {
                let x = size.width * CGFloat(i) / CGFloat(segments)
                let dy = CGFloat(i % 2 == 0 ? -1.5 : 1.5)
                path.addQuadCurve(
                    to: CGPoint(x: x, y: mid),
                    control: CGPoint(x: x - size.width / CGFloat(segments) / 2,
                                     y: mid + dy)
                )
            }
            context.stroke(path, with: .color(Theme.Palette.ink),
                           style: StrokeStyle(lineWidth: Theme.Stroke.line,
                                              lineCap: .round))
        }
        .frame(height: 6)
    }
}

// MARK: Doodle button (icon-only)

struct DoodleButton: View {
    let doodle: DoodleName
    var size: CGFloat = 22
    var label: String? = nil
    let action: () -> Void

    var body: some View {
        Button(action: {
            UIImpactFeedbackGenerator(style: .light).impactOccurred()
            action()
        }) {
            DoodleIcon(doodle, size: size, color: Theme.Palette.ink)
                .frame(width: 44, height: 44)
                .contentShape(Rectangle())
        }
        .stPressable(scale: 0.86)
        // Fall back to a humanized version of the doodle name so an
        // icon-only button is never unlabeled to VoiceOver.
        .accessibilityLabel(label ?? doodle.rawValue)
    }
}
