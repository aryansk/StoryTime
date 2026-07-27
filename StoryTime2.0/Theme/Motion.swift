import SwiftUI

// MARK: - Motion
//
// One place for every reusable animation in the app, so timing stays
// coherent across surfaces instead of each view inventing its own
// `.easeOut(duration: 0.2)`.
//
// Three rules the whole app follows:
//
//   1. Motion is *physical*, not decorative. Springs everywhere; linear
//      easing only for things that genuinely have no mass (crossfades).
//   2. Motion is interruptible. SwiftUI springs already retarget mid-flight,
//      so we never gate an animation behind an `asyncAfter` delay that would
//      make a fast tap feel stuck.
//   3. Motion is optional. Every modifier here reads
//      `accessibilityReduceMotion` and degrades to an instant state change
//      (or a plain crossfade) rather than simply animating faster.

extension Theme {

    struct Motion {
        // MARK: Core springs
        //
        // These map onto the iOS 26 system feel: `snappy` for direct
        // manipulation, `smooth` for state changes the user didn't touch,
        // `bouncy` for moments that should read as delight.

        /// Immediate feedback — press states, selection, chips.
        static let quick   = Animation.snappy(duration: 0.24, extraBounce: 0.02)
        /// The default for layout and content changes.
        static let settle  = Animation.smooth(duration: 0.38)
        /// Scene / page changes in the reader.
        static let page    = Animation.smooth(duration: 0.42)
        /// Celebration: endings, achievements unlocking, goal completion.
        static let bouncy  = Animation.bouncy(duration: 0.5, extraBounce: 0.24)
        /// Near-instant, for things that must not lag the finger.
        static let snappy  = Animation.snappy(duration: 0.16, extraBounce: 0)
        /// Slow, ambient — progress bars filling, counters counting.
        static let drift   = Animation.smooth(duration: 0.7)

        /// A `settle` spring delayed by the row's position in a list, so a
        /// section reads as one gesture instead of ten simultaneous pops.
        /// The delay is capped so a long list never makes the reader wait.
        static func stagger(_ index: Int,
                            base: Animation = Theme.Motion.settle,
                            step: Double = 0.045,
                            cap: Int = 8) -> Animation {
            base.delay(Double(min(max(index, 0), cap)) * step)
        }
    }
}

// MARK: - Reduce Motion

/// Returns `animation` normally, or `nil` when the reader has asked for
/// reduced motion — `withAnimation(nil)` applies the change instantly, which
/// is what Reduce Motion actually means (not "the same animation, faster").
func stMotion(_ animation: Animation?, reduced: Bool) -> Animation? {
    reduced ? nil : animation
}

// MARK: - Appear transition
//
// A first-appearance fade-and-rise. Used for cards, choice rows, and
// section content so surfaces assemble rather than blink into place.
//
// Deliberately fires once per view identity: LazyVStack rows would
// otherwise re-run the animation every time they're recycled back into
// view, which turns a calm entrance into scroll-triggered strobing.

struct AppearModifier: ViewModifier {
    var index: Int = 0
    var rise: CGFloat = 14
    var scale: CGFloat = 1
    var animation: Animation = Theme.Motion.settle
    /// Set false to render immediately. Callers in `LazyVStack`s pass
    /// `index < someThreshold` so only the first screenful animates —
    /// rows created later are scroll-recycled, and fading each one in as it
    /// crosses the edge reads as flicker, not as an entrance.
    var enabled: Bool = true

    @Environment(\.accessibilityReduceMotion) private var reduceMotion
    @State private var shown = false

    private var active: Bool { enabled && !reduceMotion }

    func body(content: Content) -> some View {
        content
            .opacity(shown ? 1 : 0)
            .offset(y: shown ? 0 : rise)
            .scaleEffect(shown ? 1 : scale, anchor: .center)
            .onAppear {
                guard !shown else { return }
                guard active else { shown = true; return }
                withAnimation(Theme.Motion.stagger(index, base: animation)) {
                    shown = true
                }
            }
    }
}

// MARK: - Pressable
//
// A button style with weight: the label sinks slightly and dims under the
// finger, then springs back. Replaces the flat `.plain` style on every
// tappable card so taps feel acknowledged before the navigation lands.
//
// The actual effect lives in a nested `View` rather than directly in
// `makeBody`. A `ButtonStyle` is not itself part of the view hierarchy, so
// `@Environment` declared on the style struct is never populated — reading
// Reduce Motion has to happen inside a real view.

struct PressableStyle: ButtonStyle {
    var scale: CGFloat = 0.97
    var dim: Double = 0.9
    /// Sketch surfaces also nudge down-right, echoing `SketchPressStyle`.
    var nudge: CGFloat = 0

    func makeBody(configuration: Configuration) -> some View {
        // Not named `Body`: `ButtonStyle` already has an associated type by
        // that name, and a nested type would shadow it and fail to match
        // `makeBody`'s opaque return type.
        Effect(configuration: configuration, scale: scale, dim: dim, nudge: nudge)
    }

    private struct Effect: View {
        let configuration: ButtonStyleConfiguration
        let scale: CGFloat
        let dim: Double
        let nudge: CGFloat

        @Environment(\.accessibilityReduceMotion) private var reduceMotion

        var body: some View {
            let pressed = configuration.isPressed
            return configuration.label
                .scaleEffect(reduceMotion ? 1 : (pressed ? scale : 1))
                .offset(x: pressed ? nudge : 0, y: pressed ? nudge : 0)
                .opacity(pressed ? dim : 1)
                .animation(reduceMotion ? nil : Theme.Motion.snappy, value: pressed)
        }
    }
}

// MARK: - Indexed collections
//
// `ForEach(Array(items.enumerated()), id: \.element.id)` does not compile:
// Swift has no key paths into tuple components. Wrapping each element in a
// real struct gives the row both its position (for stagger delays) and the
// model's own identity (so filtering and reordering diff correctly, which
// `id: \.self` on indices would break).

struct Indexed<Value: Identifiable>: Identifiable {
    let index: Int
    let value: Value
    var id: Value.ID { value.id }
}

extension Collection where Element: Identifiable {
    var indexed: [Indexed<Element>] {
        enumerated().map { Indexed(index: $0.offset, value: $0.element) }
    }
}

// MARK: - Count-up number
//
// Stat tiles and percentages roll to their new value instead of swapping.
// Uses SwiftUI's numeric content transition where the value is small enough
// to read digit-by-digit, and an interpolated count-up where it isn't.

struct CountUpText: View {
    let value: Int
    var font: Font
    var color: Color

    @Environment(\.accessibilityReduceMotion) private var reduceMotion
    @State private var displayed: Int = 0

    var body: some View {
        Text("\(displayed)")
            .font(font)
            .foregroundColor(color)
            .contentTransition(.numericText(value: Double(displayed)))
            .monospacedDigit()
            .onAppear { apply(value, animated: !reduceMotion) }
            .onChange(of: value) { _, new in apply(new, animated: !reduceMotion) }
            .accessibilityLabel("\(value)")
    }

    private func apply(_ new: Int, animated: Bool) {
        guard animated else { displayed = new; return }
        withAnimation(Theme.Motion.drift) { displayed = new }
    }
}

// MARK: - Progress bar
//
// Every progress capsule in the app (daily goal, continue-reading, Choice
// DNA) went through the same hand-rolled GeometryReader + ZStack. Pulling
// it here means they all fill with the same spring, animate when the value
// changes, and stay legible under Reduce Motion.

struct AnimatedProgressBar: View {
    /// 0…1
    let fraction: Double
    var height: CGFloat = 7
    var track: Color = Theme.Palette.inkHair
    var fill: Color = Theme.Palette.ink

    @Environment(\.accessibilityReduceMotion) private var reduceMotion

    var body: some View {
        GeometryReader { geo in
            ZStack(alignment: .leading) {
                Capsule().fill(track)
                Capsule()
                    .fill(fill)
                    .frame(width: max(0, geo.size.width * min(max(fraction, 0), 1)))
            }
        }
        .frame(height: height)
        .animation(reduceMotion ? nil : Theme.Motion.drift, value: fraction)
    }
}

// MARK: - View sugar

extension View {
    /// Fade-and-rise on first appearance. Pass the row's index in its
    /// section to stagger a group.
    func stAppear(_ index: Int = 0,
                  rise: CGFloat = 14,
                  scale: CGFloat = 1,
                  animation: Animation = Theme.Motion.settle,
                  enabled: Bool = true) -> some View {
        modifier(AppearModifier(index: index,
                                rise: rise,
                                scale: scale,
                                animation: animation,
                                enabled: enabled))
    }

    /// Press feedback for tappable cards and rows.
    func stPressable(scale: CGFloat = 0.97, nudge: CGFloat = 0) -> some View {
        buttonStyle(PressableStyle(scale: scale, nudge: nudge))
    }

    /// Applies `animation` unless the reader has Reduce Motion on.
    @ViewBuilder
    func stAnimation<V: Equatable>(_ animation: Animation?,
                                   value: V,
                                   reduceMotion: Bool) -> some View {
        self.animation(reduceMotion ? nil : animation, value: value)
    }
}
