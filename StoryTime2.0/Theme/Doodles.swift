import SwiftUI

// MARK: - Doodle Icon System
//
// Hand-authored SVG-style paths that intentionally wobble — irregular
// control points, deliberately non-uniform geometry. Drawn as loose
// line art with Theme.Stroke.line in Theme.Palette.ink. No fills, no
// gradients.
//
// All doodles render inside a 24x24 conceptual viewBox and scale to
// whatever frame they sit in.

enum DoodleName: String, CaseIterable {
    case tv
    case books
    case gear
    case play
    case pause
    case arrowRight
    case chevronLeft
    case chevronRight
    case bookmark
    case bookmarkFill
    case heart
    case heartFill
    case plus
    case xmark
    case search
    case sparkle
    case clock
    case checkmark
    case sortArrows
    case filter
    case popcorn
    case clapperboard
    case speaker
    case speakerPlaying
    case share
    case star
    case starFill
    case undo
    case flame
    case branch
    case stack
    case bell
    case person
    case shield
    case scroll
    case chevronRightSmall
    case link
}

struct DoodleIcon: View {
    let name: DoodleName
    var size: CGFloat = 24
    var color: Color = Theme.Palette.ink
    var stroke: CGFloat = Theme.Stroke.line
    var filled: Bool = false

    init(_ name: DoodleName,
         size: CGFloat = 24,
         color: Color = Theme.Palette.ink,
         stroke: CGFloat = Theme.Stroke.line,
         filled: Bool = false) {
        self.name = name
        self.size = size
        self.color = color
        self.stroke = stroke
        self.filled = filled
    }

    var body: some View {
        Canvas { context, canvasSize in
            let scale = min(canvasSize.width, canvasSize.height) / 24.0
            var transform = CGAffineTransform(scaleX: scale, y: scale)
            for stroke in DoodlePaths.paths(for: name) {
                let cg = stroke.path.cgPath
                guard let scaledCG = cg.copy(using: &transform) else { continue }
                let scaled = Path(scaledCG)
                context.stroke(
                    scaled,
                    with: .color(color),
                    style: StrokeStyle(
                        lineWidth: stroke.widthMultiplier * self.stroke,
                        lineCap: .round,
                        lineJoin: .round
                    )
                )
                if filled, stroke.closesShape {
                    context.fill(scaled, with: .color(color.opacity(0.15)))
                }
            }
        }
        .frame(width: size, height: size)
        .accessibilityHidden(true)
    }
}

// MARK: - Paths

private struct DoodleStroke {
    let path: UIBezierPath
    var widthMultiplier: CGFloat = 1.0
    var closesShape: Bool = false
}

private enum DoodlePaths {

    static func paths(for name: DoodleName) -> [DoodleStroke] {
        switch name {
        case .tv:            return tv()
        case .books:         return books()
        case .gear:          return gear()
        case .play:          return play()
        case .pause:         return pause()
        case .arrowRight:    return arrow(left: false)
        case .chevronLeft:   return chevron(left: true)
        case .chevronRight:  return chevron(left: false)
        case .bookmark:      return bookmark(filled: false)
        case .bookmarkFill:  return bookmark(filled: true)
        case .heart:         return heart(filled: false)
        case .heartFill:     return heart(filled: true)
        case .plus:          return plus()
        case .xmark:         return xmark()
        case .search:        return search()
        case .sparkle:       return sparkle()
        case .clock:         return clock()
        case .checkmark:     return checkmark()
        case .sortArrows:    return sortArrows()
        case .filter:        return filter()
        case .popcorn:       return popcorn()
        case .clapperboard:  return clapperboard()
        case .speaker:       return speaker(playing: false)
        case .speakerPlaying:return speaker(playing: true)
        case .share:         return share()
        case .star:          return star(filled: false)
        case .starFill:      return star(filled: true)
        case .undo:          return undo()
        case .flame:         return flame()
        case .branch:        return branch()
        case .stack:         return stack()
        case .bell:          return bell()
        case .person:        return person()
        case .shield:        return shield()
        case .scroll:        return scroll()
        case .chevronRightSmall: return chevron(left: false)
        case .link:          return link()
        }
    }

    // Helpers ---------------------------------------------------------

    private static func wobble(_ value: CGFloat, _ jitter: CGFloat = 0.4) -> CGFloat {
        // Pseudo-random hand-drawn imperfection, seeded by value so
        // doodles are stable per-icon but feel non-machine-perfect.
        let seed = sin(value * 12.9898) * 43758.5453
        return value + CGFloat(seed.truncatingRemainder(dividingBy: 1)) * jitter - jitter / 2
    }

    private static func bezier(_ build: (UIBezierPath) -> Void) -> UIBezierPath {
        let p = UIBezierPath()
        build(p)
        return p
    }

    // Shapes ----------------------------------------------------------

    private static func tv() -> [DoodleStroke] {
        let body = bezier { p in
            p.move(to: CGPoint(x: 3.2, y: 8.4))
            p.addCurve(to: CGPoint(x: 20.6, y: 8.1),
                       controlPoint1: CGPoint(x: 9, y: 7.8),
                       controlPoint2: CGPoint(x: 15, y: 8.6))
            p.addCurve(to: CGPoint(x: 20.9, y: 18.5),
                       controlPoint1: CGPoint(x: 21, y: 11.5),
                       controlPoint2: CGPoint(x: 20.7, y: 15.2))
            p.addCurve(to: CGPoint(x: 3, y: 18.4),
                       controlPoint1: CGPoint(x: 14, y: 19),
                       controlPoint2: CGPoint(x: 8, y: 18.9))
            p.addCurve(to: CGPoint(x: 3.2, y: 8.4),
                       controlPoint1: CGPoint(x: 2.7, y: 14.8),
                       controlPoint2: CGPoint(x: 2.9, y: 11.5))
            p.close()
        }
        let antL = bezier { p in
            p.move(to: CGPoint(x: 7.5, y: 4.2))
            p.addCurve(to: CGPoint(x: 10.5, y: 7.9),
                       controlPoint1: CGPoint(x: 8.5, y: 5.5),
                       controlPoint2: CGPoint(x: 9.6, y: 6.7))
        }
        let antR = bezier { p in
            p.move(to: CGPoint(x: 16.4, y: 4.0))
            p.addCurve(to: CGPoint(x: 13.5, y: 7.8),
                       controlPoint1: CGPoint(x: 15.2, y: 5.4),
                       controlPoint2: CGPoint(x: 14.3, y: 6.6))
        }
        let knob = bezier { p in
            p.addArc(withCenter: CGPoint(x: 17.5, y: 14),
                     radius: 0.6, startAngle: 0, endAngle: .pi * 2, clockwise: true)
        }
        return [
            DoodleStroke(path: body, closesShape: true),
            DoodleStroke(path: antL),
            DoodleStroke(path: antR),
            DoodleStroke(path: knob, widthMultiplier: 0.9)
        ]
    }

    private static func books() -> [DoodleStroke] {
        let b1 = bezier { p in
            p.move(to: CGPoint(x: 4.1, y: 5.2))
            p.addLine(to: CGPoint(x: 4.4, y: 19.7))
            p.addLine(to: CGPoint(x: 8.5, y: 19.5))
            p.addLine(to: CGPoint(x: 8.2, y: 5.0))
            p.close()
        }
        let b2 = bezier { p in
            p.move(to: CGPoint(x: 9.2, y: 6.1))
            p.addLine(to: CGPoint(x: 9.6, y: 19.6))
            p.addLine(to: CGPoint(x: 13.7, y: 19.4))
            p.addLine(to: CGPoint(x: 13.3, y: 5.9))
            p.close()
        }
        let b3 = bezier { p in
            p.move(to: CGPoint(x: 15.4, y: 8.2))
            p.addCurve(to: CGPoint(x: 21.0, y: 6.7),
                       controlPoint1: CGPoint(x: 17, y: 7.6),
                       controlPoint2: CGPoint(x: 19, y: 7.0))
            p.addLine(to: CGPoint(x: 22.3, y: 18.2))
            p.addCurve(to: CGPoint(x: 16.6, y: 19.7),
                       controlPoint1: CGPoint(x: 20.5, y: 18.7),
                       controlPoint2: CGPoint(x: 18.5, y: 19.3))
            p.close()
        }
        let line1 = bezier { p in
            p.move(to: CGPoint(x: 5, y: 9))
            p.addLine(to: CGPoint(x: 7.5, y: 8.9))
        }
        let line2 = bezier { p in
            p.move(to: CGPoint(x: 10.2, y: 10))
            p.addLine(to: CGPoint(x: 12.7, y: 9.9))
        }
        return [
            DoodleStroke(path: b1, closesShape: true),
            DoodleStroke(path: b2, closesShape: true),
            DoodleStroke(path: b3, closesShape: true),
            DoodleStroke(path: line1, widthMultiplier: 0.7),
            DoodleStroke(path: line2, widthMultiplier: 0.7)
        ]
    }

    private static func gear() -> [DoodleStroke] {
        let outer = UIBezierPath()
        let teeth = 8
        let center = CGPoint(x: 12, y: 12)
        let rOut: CGFloat = 9.5
        let rIn: CGFloat  = 7.2
        for i in 0..<(teeth * 2) {
            let angle = (CGFloat(i) / CGFloat(teeth * 2)) * .pi * 2
            let r = i.isMultiple(of: 2) ? rOut : rIn
            let jitter = wobble(angle, 0.25)
            let pt = CGPoint(x: center.x + cos(angle + jitter * 0.05) * r,
                             y: center.y + sin(angle + jitter * 0.05) * r)
            if i == 0 { outer.move(to: pt) } else { outer.addLine(to: pt) }
        }
        outer.close()
        let core = bezier { p in
            p.addArc(withCenter: center, radius: 3.0,
                     startAngle: 0, endAngle: .pi * 2, clockwise: true)
        }
        return [
            DoodleStroke(path: outer, closesShape: true),
            DoodleStroke(path: core)
        ]
    }

    private static func play() -> [DoodleStroke] {
        let tri = bezier { p in
            p.move(to: CGPoint(x: 7.5, y: 4.8))
            p.addLine(to: CGPoint(x: 19.2, y: 12.1))
            p.addLine(to: CGPoint(x: 7.3, y: 19.4))
            p.close()
        }
        return [DoodleStroke(path: tri, widthMultiplier: 1.1, closesShape: true)]
    }

    private static func pause() -> [DoodleStroke] {
        let l = bezier { p in
            p.move(to: CGPoint(x: 8.0, y: 5.0))
            p.addLine(to: CGPoint(x: 8.4, y: 19.0))
        }
        let r = bezier { p in
            p.move(to: CGPoint(x: 15.8, y: 5.0))
            p.addLine(to: CGPoint(x: 16.0, y: 19.2))
        }
        return [
            DoodleStroke(path: l, widthMultiplier: 1.5),
            DoodleStroke(path: r, widthMultiplier: 1.5)
        ]
    }

    private static func arrow(left: Bool) -> [DoodleStroke] {
        let dir: CGFloat = left ? -1 : 1
        let shaft = bezier { p in
            p.move(to: CGPoint(x: 12 - 7 * dir, y: 12.2))
            p.addCurve(to: CGPoint(x: 12 + 7 * dir, y: 11.9),
                       controlPoint1: CGPoint(x: 8 - dir, y: 12.7),
                       controlPoint2: CGPoint(x: 8 + 3 * dir, y: 11.5))
        }
        let head1 = bezier { p in
            p.move(to: CGPoint(x: 12 + 7 * dir, y: 11.9))
            p.addLine(to: CGPoint(x: 12 + 3.5 * dir, y: 7.6))
        }
        let head2 = bezier { p in
            p.move(to: CGPoint(x: 12 + 7 * dir, y: 11.9))
            p.addLine(to: CGPoint(x: 12 + 3.7 * dir, y: 16.4))
        }
        return [
            DoodleStroke(path: shaft, widthMultiplier: 1.1),
            DoodleStroke(path: head1),
            DoodleStroke(path: head2)
        ]
    }

    private static func chevron(left: Bool) -> [DoodleStroke] {
        let dir: CGFloat = left ? -1 : 1
        let p = bezier { p in
            p.move(to: CGPoint(x: 12 - 3 * dir, y: 5.5))
            p.addLine(to: CGPoint(x: 12 + 3.5 * dir, y: 12.1))
            p.addLine(to: CGPoint(x: 12 - 3 * dir, y: 18.7))
        }
        return [DoodleStroke(path: p, widthMultiplier: 1.2)]
    }

    private static func bookmark(filled: Bool) -> [DoodleStroke] {
        let p = bezier { p in
            p.move(to: CGPoint(x: 6.5, y: 3.8))
            p.addLine(to: CGPoint(x: 6.8, y: 20.5))
            p.addLine(to: CGPoint(x: 12.0, y: 16.0))
            p.addLine(to: CGPoint(x: 17.3, y: 20.6))
            p.addLine(to: CGPoint(x: 17.0, y: 3.7))
            p.close()
        }
        return [DoodleStroke(path: p, widthMultiplier: 1.1, closesShape: filled)]
    }

    private static func heart(filled: Bool) -> [DoodleStroke] {
        let p = bezier { p in
            p.move(to: CGPoint(x: 12, y: 20))
            p.addCurve(to: CGPoint(x: 3.5, y: 9.5),
                       controlPoint1: CGPoint(x: 6, y: 17),
                       controlPoint2: CGPoint(x: 3, y: 13))
            p.addCurve(to: CGPoint(x: 12, y: 7.2),
                       controlPoint1: CGPoint(x: 4, y: 5.5),
                       controlPoint2: CGPoint(x: 9, y: 5))
            p.addCurve(to: CGPoint(x: 20.5, y: 9.5),
                       controlPoint1: CGPoint(x: 15, y: 5),
                       controlPoint2: CGPoint(x: 20, y: 5.5))
            p.addCurve(to: CGPoint(x: 12, y: 20),
                       controlPoint1: CGPoint(x: 21, y: 13),
                       controlPoint2: CGPoint(x: 18, y: 17))
            p.close()
        }
        return [DoodleStroke(path: p, widthMultiplier: 1.1, closesShape: filled)]
    }

    private static func plus() -> [DoodleStroke] {
        let h = bezier { p in
            p.move(to: CGPoint(x: 4.5, y: 12.0))
            p.addCurve(to: CGPoint(x: 19.7, y: 12.2),
                       controlPoint1: CGPoint(x: 10, y: 11.7),
                       controlPoint2: CGPoint(x: 15, y: 12.4))
        }
        let v = bezier { p in
            p.move(to: CGPoint(x: 12.0, y: 4.5))
            p.addCurve(to: CGPoint(x: 12.2, y: 19.6),
                       controlPoint1: CGPoint(x: 11.7, y: 10),
                       controlPoint2: CGPoint(x: 12.4, y: 15))
        }
        return [
            DoodleStroke(path: h, widthMultiplier: 1.2),
            DoodleStroke(path: v, widthMultiplier: 1.2)
        ]
    }

    private static func xmark() -> [DoodleStroke] {
        let a = bezier { p in
            p.move(to: CGPoint(x: 5.5, y: 5.7))
            p.addLine(to: CGPoint(x: 18.6, y: 18.5))
        }
        let b = bezier { p in
            p.move(to: CGPoint(x: 18.5, y: 5.8))
            p.addLine(to: CGPoint(x: 5.4, y: 18.4))
        }
        return [
            DoodleStroke(path: a, widthMultiplier: 1.1),
            DoodleStroke(path: b, widthMultiplier: 1.1)
        ]
    }

    private static func search() -> [DoodleStroke] {
        let circle = bezier { p in
            p.addArc(withCenter: CGPoint(x: 10.4, y: 10.4),
                     radius: 5.6, startAngle: 0, endAngle: .pi * 2, clockwise: true)
        }
        let handle = bezier { p in
            p.move(to: CGPoint(x: 14.5, y: 14.5))
            p.addLine(to: CGPoint(x: 20.0, y: 20.2))
        }
        return [
            DoodleStroke(path: circle),
            DoodleStroke(path: handle, widthMultiplier: 1.1)
        ]
    }

    private static func sparkle() -> [DoodleStroke] {
        let v = bezier { p in
            p.move(to: CGPoint(x: 12, y: 3.5))
            p.addCurve(to: CGPoint(x: 12, y: 11),
                       controlPoint1: CGPoint(x: 11.5, y: 6),
                       controlPoint2: CGPoint(x: 12.5, y: 9))
            p.addCurve(to: CGPoint(x: 4.5, y: 12),
                       controlPoint1: CGPoint(x: 9, y: 11.5),
                       controlPoint2: CGPoint(x: 6, y: 11.7))
            p.addCurve(to: CGPoint(x: 12, y: 13),
                       controlPoint1: CGPoint(x: 6, y: 12.3),
                       controlPoint2: CGPoint(x: 9, y: 12.7))
            p.addCurve(to: CGPoint(x: 12, y: 20.5),
                       controlPoint1: CGPoint(x: 12.5, y: 15),
                       controlPoint2: CGPoint(x: 11.5, y: 18))
            p.addCurve(to: CGPoint(x: 13, y: 13),
                       controlPoint1: CGPoint(x: 13, y: 18),
                       controlPoint2: CGPoint(x: 12.5, y: 15))
            p.addCurve(to: CGPoint(x: 20, y: 12),
                       controlPoint1: CGPoint(x: 15, y: 12.7),
                       controlPoint2: CGPoint(x: 18, y: 12.3))
            p.addCurve(to: CGPoint(x: 12, y: 11),
                       controlPoint1: CGPoint(x: 18, y: 11.7),
                       controlPoint2: CGPoint(x: 15, y: 11.3))
        }
        let small = bezier { p in
            p.move(to: CGPoint(x: 19, y: 5))
            p.addLine(to: CGPoint(x: 19.4, y: 7.4))
            p.addLine(to: CGPoint(x: 21.6, y: 6.2))
            p.addLine(to: CGPoint(x: 19.6, y: 5.6))
            p.close()
        }
        return [DoodleStroke(path: v), DoodleStroke(path: small, widthMultiplier: 0.8)]
    }

    private static func clock() -> [DoodleStroke] {
        let circle = bezier { p in
            p.addArc(withCenter: CGPoint(x: 12, y: 12.2),
                     radius: 8.5, startAngle: 0, endAngle: .pi * 2, clockwise: true)
        }
        let hands = bezier { p in
            p.move(to: CGPoint(x: 12, y: 12))
            p.addLine(to: CGPoint(x: 12, y: 6.6))
            p.move(to: CGPoint(x: 12, y: 12))
            p.addLine(to: CGPoint(x: 16, y: 13.4))
        }
        return [DoodleStroke(path: circle), DoodleStroke(path: hands)]
    }

    private static func checkmark() -> [DoodleStroke] {
        let p = bezier { p in
            p.move(to: CGPoint(x: 4.5, y: 12.5))
            p.addCurve(to: CGPoint(x: 10, y: 17.5),
                       controlPoint1: CGPoint(x: 6.8, y: 14),
                       controlPoint2: CGPoint(x: 8.5, y: 16))
            p.addCurve(to: CGPoint(x: 19.5, y: 6.5),
                       controlPoint1: CGPoint(x: 13.5, y: 13.5),
                       controlPoint2: CGPoint(x: 16.5, y: 9.5))
        }
        return [DoodleStroke(path: p, widthMultiplier: 1.3)]
    }

    private static func sortArrows() -> [DoodleStroke] {
        let up = bezier { p in
            p.move(to: CGPoint(x: 8, y: 4.5))
            p.addLine(to: CGPoint(x: 8.1, y: 14.5))
            p.move(to: CGPoint(x: 5.2, y: 7.5))
            p.addLine(to: CGPoint(x: 8, y: 4.5))
            p.addLine(to: CGPoint(x: 10.9, y: 7.4))
        }
        let dn = bezier { p in
            p.move(to: CGPoint(x: 16, y: 19.5))
            p.addLine(to: CGPoint(x: 15.9, y: 9.5))
            p.move(to: CGPoint(x: 13.1, y: 16.4))
            p.addLine(to: CGPoint(x: 16, y: 19.5))
            p.addLine(to: CGPoint(x: 18.9, y: 16.5))
        }
        return [DoodleStroke(path: up), DoodleStroke(path: dn)]
    }

    private static func filter() -> [DoodleStroke] {
        let p = bezier { p in
            p.move(to: CGPoint(x: 3.5, y: 5.5))
            p.addLine(to: CGPoint(x: 20.5, y: 5.6))
            p.addLine(to: CGPoint(x: 14, y: 12.5))
            p.addLine(to: CGPoint(x: 14.1, y: 19.5))
            p.addLine(to: CGPoint(x: 10, y: 17.5))
            p.addLine(to: CGPoint(x: 10, y: 12.4))
            p.close()
        }
        return [DoodleStroke(path: p, closesShape: true)]
    }

    private static func popcorn() -> [DoodleStroke] {
        let box = bezier { p in
            p.move(to: CGPoint(x: 5.5, y: 8.5))
            p.addLine(to: CGPoint(x: 18.5, y: 8.5))
            p.addLine(to: CGPoint(x: 17, y: 21))
            p.addLine(to: CGPoint(x: 7, y: 21))
            p.close()
        }
        let stripes = bezier { p in
            p.move(to: CGPoint(x: 10, y: 9))
            p.addLine(to: CGPoint(x: 9, y: 20.5))
            p.move(to: CGPoint(x: 14.2, y: 9))
            p.addLine(to: CGPoint(x: 15, y: 20.5))
        }
        let kernels = UIBezierPath()
        for (cx, cy, r) in [
            (8.5, 6.5, 1.6),
            (11.5, 4.8, 1.9),
            (15.0, 6.0, 1.7),
            (17.5, 7.5, 1.3),
            (6.5, 7.7, 1.2)
        ] as [(CGFloat, CGFloat, CGFloat)] {
            kernels.move(to: CGPoint(x: cx + r, y: cy))
            kernels.addArc(withCenter: CGPoint(x: cx, y: cy),
                           radius: r, startAngle: 0, endAngle: .pi * 2, clockwise: true)
        }
        return [
            DoodleStroke(path: box),
            DoodleStroke(path: stripes, widthMultiplier: 0.7),
            DoodleStroke(path: kernels)
        ]
    }

    private static func clapperboard() -> [DoodleStroke] {
        let base = bezier { p in
            p.move(to: CGPoint(x: 3.5, y: 9))
            p.addLine(to: CGPoint(x: 20.5, y: 9))
            p.addLine(to: CGPoint(x: 20.5, y: 20))
            p.addLine(to: CGPoint(x: 3.5, y: 20))
            p.close()
        }
        let arm = bezier { p in
            p.move(to: CGPoint(x: 3.5, y: 9))
            p.addLine(to: CGPoint(x: 5.5, y: 4))
            p.addLine(to: CGPoint(x: 9.5, y: 6))
            p.addLine(to: CGPoint(x: 7.5, y: 9))
            p.move(to: CGPoint(x: 9.5, y: 6))
            p.addLine(to: CGPoint(x: 13.5, y: 5))
            p.addLine(to: CGPoint(x: 11.5, y: 8.5))
            p.move(to: CGPoint(x: 13.5, y: 5))
            p.addLine(to: CGPoint(x: 17.5, y: 4.5))
            p.addLine(to: CGPoint(x: 15.5, y: 8.5))
        }
        return [DoodleStroke(path: base), DoodleStroke(path: arm)]
    }

    private static func speaker(playing: Bool) -> [DoodleStroke] {
        let body = bezier { p in
            p.move(to: CGPoint(x: 3.5, y: 9.5))
            p.addLine(to: CGPoint(x: 7.5, y: 9.5))
            p.addLine(to: CGPoint(x: 12.5, y: 5))
            p.addLine(to: CGPoint(x: 12.5, y: 19))
            p.addLine(to: CGPoint(x: 7.5, y: 14.5))
            p.addLine(to: CGPoint(x: 3.5, y: 14.5))
            p.close()
        }
        var strokes: [DoodleStroke] = [DoodleStroke(path: body, closesShape: true)]
        if playing {
            let wave1 = bezier { p in
                p.move(to: CGPoint(x: 15, y: 10))
                p.addCurve(to: CGPoint(x: 15.5, y: 14),
                           controlPoint1: CGPoint(x: 16, y: 11.2),
                           controlPoint2: CGPoint(x: 16, y: 12.8))
            }
            let wave2 = bezier { p in
                p.move(to: CGPoint(x: 18, y: 7.5))
                p.addCurve(to: CGPoint(x: 18.5, y: 16.5),
                           controlPoint1: CGPoint(x: 21, y: 10),
                           controlPoint2: CGPoint(x: 21, y: 14))
            }
            strokes.append(DoodleStroke(path: wave1))
            strokes.append(DoodleStroke(path: wave2))
        }
        return strokes
    }

    private static func share() -> [DoodleStroke] {
        let box = bezier { p in
            p.move(to: CGPoint(x: 5, y: 11))
            p.addLine(to: CGPoint(x: 5, y: 20))
            p.addLine(to: CGPoint(x: 19, y: 20))
            p.addLine(to: CGPoint(x: 19, y: 11))
        }
        let arrow = bezier { p in
            p.move(to: CGPoint(x: 12, y: 4))
            p.addLine(to: CGPoint(x: 12, y: 15))
            p.move(to: CGPoint(x: 8.5, y: 7.5))
            p.addLine(to: CGPoint(x: 12, y: 4))
            p.addLine(to: CGPoint(x: 15.5, y: 7.5))
        }
        return [DoodleStroke(path: box), DoodleStroke(path: arrow)]
    }

    private static func star(filled: Bool) -> [DoodleStroke] {
        let p = UIBezierPath()
        let center = CGPoint(x: 12, y: 12.3)
        let r1: CGFloat = 8.5
        let r2: CGFloat = 3.6
        for i in 0..<10 {
            let angle = -CGFloat.pi / 2 + (CGFloat(i) / 10) * .pi * 2
            let r = i.isMultiple(of: 2) ? r1 : r2
            let pt = CGPoint(x: center.x + cos(angle) * r,
                             y: center.y + sin(angle) * r)
            if i == 0 { p.move(to: pt) } else { p.addLine(to: pt) }
        }
        p.close()
        return [DoodleStroke(path: p, closesShape: filled)]
    }

    private static func undo() -> [DoodleStroke] {
        let arc = bezier { p in
            p.addArc(withCenter: CGPoint(x: 12, y: 13),
                     radius: 7, startAngle: .pi, endAngle: -.pi / 4, clockwise: false)
        }
        let head = bezier { p in
            p.move(to: CGPoint(x: 5, y: 13))
            p.addLine(to: CGPoint(x: 5, y: 8))
            p.move(to: CGPoint(x: 5, y: 13))
            p.addLine(to: CGPoint(x: 10, y: 13))
        }
        return [DoodleStroke(path: arc), DoodleStroke(path: head)]
    }

    private static func flame() -> [DoodleStroke] {
        let p = bezier { p in
            p.move(to: CGPoint(x: 12, y: 3.5))
            p.addCurve(to: CGPoint(x: 6.5, y: 12.5),
                       controlPoint1: CGPoint(x: 10, y: 7),
                       controlPoint2: CGPoint(x: 6, y: 9))
            p.addCurve(to: CGPoint(x: 12, y: 20.5),
                       controlPoint1: CGPoint(x: 7, y: 17),
                       controlPoint2: CGPoint(x: 9, y: 20))
            p.addCurve(to: CGPoint(x: 17.5, y: 13),
                       controlPoint1: CGPoint(x: 15, y: 20),
                       controlPoint2: CGPoint(x: 17, y: 17))
            p.addCurve(to: CGPoint(x: 13, y: 8),
                       controlPoint1: CGPoint(x: 18, y: 10),
                       controlPoint2: CGPoint(x: 15, y: 10))
            p.addCurve(to: CGPoint(x: 12, y: 3.5),
                       controlPoint1: CGPoint(x: 12, y: 6),
                       controlPoint2: CGPoint(x: 13, y: 5))
            p.close()
        }
        return [DoodleStroke(path: p, closesShape: true)]
    }

    private static func branch() -> [DoodleStroke] {
        let trunk = bezier { p in
            p.move(to: CGPoint(x: 6, y: 3.5))
            p.addLine(to: CGPoint(x: 6, y: 20.5))
        }
        let b1 = bezier { p in
            p.move(to: CGPoint(x: 6, y: 9))
            p.addCurve(to: CGPoint(x: 18, y: 6),
                       controlPoint1: CGPoint(x: 11, y: 9),
                       controlPoint2: CGPoint(x: 14, y: 7))
        }
        let b2 = bezier { p in
            p.move(to: CGPoint(x: 6, y: 14))
            p.addCurve(to: CGPoint(x: 18, y: 17),
                       controlPoint1: CGPoint(x: 11, y: 14),
                       controlPoint2: CGPoint(x: 14, y: 16))
        }
        let n1 = bezier { p in
            p.addArc(withCenter: CGPoint(x: 18, y: 6), radius: 1.5,
                     startAngle: 0, endAngle: .pi * 2, clockwise: true)
        }
        let n2 = bezier { p in
            p.addArc(withCenter: CGPoint(x: 18, y: 17), radius: 1.5,
                     startAngle: 0, endAngle: .pi * 2, clockwise: true)
        }
        let n3 = bezier { p in
            p.addArc(withCenter: CGPoint(x: 6, y: 4), radius: 1.5,
                     startAngle: 0, endAngle: .pi * 2, clockwise: true)
        }
        return [
            DoodleStroke(path: trunk),
            DoodleStroke(path: b1),
            DoodleStroke(path: b2),
            DoodleStroke(path: n1),
            DoodleStroke(path: n2),
            DoodleStroke(path: n3)
        ]
    }

    private static func stack() -> [DoodleStroke] {
        let l1 = bezier { p in
            p.move(to: CGPoint(x: 4, y: 7))
            p.addLine(to: CGPoint(x: 12, y: 4))
            p.addLine(to: CGPoint(x: 20, y: 7))
            p.addLine(to: CGPoint(x: 12, y: 10))
            p.close()
        }
        let l2 = bezier { p in
            p.move(to: CGPoint(x: 4, y: 12))
            p.addLine(to: CGPoint(x: 12, y: 15))
            p.addLine(to: CGPoint(x: 20, y: 12))
        }
        let l3 = bezier { p in
            p.move(to: CGPoint(x: 4, y: 17))
            p.addLine(to: CGPoint(x: 12, y: 20))
            p.addLine(to: CGPoint(x: 20, y: 17))
        }
        return [DoodleStroke(path: l1), DoodleStroke(path: l2), DoodleStroke(path: l3)]
    }

    private static func person() -> [DoodleStroke] {
        let head = bezier { p in
            p.addArc(withCenter: CGPoint(x: 12, y: 8),
                     radius: 3.8, startAngle: 0, endAngle: .pi * 2, clockwise: true)
        }
        let shoulders = bezier { p in
            p.move(to: CGPoint(x: 4.5, y: 20.5))
            p.addCurve(to: CGPoint(x: 19.5, y: 20.5),
                       controlPoint1: CGPoint(x: 5, y: 14.5),
                       controlPoint2: CGPoint(x: 19, y: 14.5))
        }
        return [DoodleStroke(path: head), DoodleStroke(path: shoulders)]
    }

    private static func shield() -> [DoodleStroke] {
        let body = bezier { p in
            p.move(to: CGPoint(x: 12, y: 3.5))
            p.addCurve(to: CGPoint(x: 4.5, y: 6.5),
                       controlPoint1: CGPoint(x: 9, y: 5),
                       controlPoint2: CGPoint(x: 6, y: 6))
            p.addCurve(to: CGPoint(x: 12, y: 20.5),
                       controlPoint1: CGPoint(x: 4.5, y: 14),
                       controlPoint2: CGPoint(x: 8, y: 19))
            p.addCurve(to: CGPoint(x: 19.5, y: 6.5),
                       controlPoint1: CGPoint(x: 16, y: 19),
                       controlPoint2: CGPoint(x: 19.5, y: 14))
            p.addCurve(to: CGPoint(x: 12, y: 3.5),
                       controlPoint1: CGPoint(x: 18, y: 6),
                       controlPoint2: CGPoint(x: 15, y: 5))
            p.close()
        }
        let check = bezier { p in
            p.move(to: CGPoint(x: 8.5, y: 12))
            p.addLine(to: CGPoint(x: 11, y: 14.5))
            p.addLine(to: CGPoint(x: 15.5, y: 9.5))
        }
        return [DoodleStroke(path: body, closesShape: true), DoodleStroke(path: check)]
    }

    private static func scroll() -> [DoodleStroke] {
        let body = bezier { p in
            p.move(to: CGPoint(x: 5, y: 4))
            p.addLine(to: CGPoint(x: 18, y: 4))
            p.addCurve(to: CGPoint(x: 20, y: 6.5),
                       controlPoint1: CGPoint(x: 19, y: 4.5),
                       controlPoint2: CGPoint(x: 20, y: 5.5))
            p.addCurve(to: CGPoint(x: 18, y: 9),
                       controlPoint1: CGPoint(x: 20, y: 7.5),
                       controlPoint2: CGPoint(x: 19, y: 8.5))
            p.addLine(to: CGPoint(x: 18, y: 18))
            p.addCurve(to: CGPoint(x: 15, y: 20.5),
                       controlPoint1: CGPoint(x: 18, y: 19.5),
                       controlPoint2: CGPoint(x: 16.5, y: 20.5))
            p.addLine(to: CGPoint(x: 6, y: 20.5))
            p.addCurve(to: CGPoint(x: 4, y: 18),
                       controlPoint1: CGPoint(x: 4.5, y: 20),
                       controlPoint2: CGPoint(x: 4, y: 19.5))
            p.addLine(to: CGPoint(x: 4, y: 6.5))
            p.addCurve(to: CGPoint(x: 5, y: 4),
                       controlPoint1: CGPoint(x: 4, y: 5),
                       controlPoint2: CGPoint(x: 4.5, y: 4.2))
        }
        let lines = bezier { p in
            p.move(to: CGPoint(x: 7, y: 11));  p.addLine(to: CGPoint(x: 15, y: 11))
            p.move(to: CGPoint(x: 7, y: 14));  p.addLine(to: CGPoint(x: 15, y: 14))
            p.move(to: CGPoint(x: 7, y: 17));  p.addLine(to: CGPoint(x: 12, y: 17))
        }
        return [DoodleStroke(path: body), DoodleStroke(path: lines, widthMultiplier: 0.7)]
    }

    private static func link() -> [DoodleStroke] {
        let a = bezier { p in
            p.move(to: CGPoint(x: 9, y: 14))
            p.addCurve(to: CGPoint(x: 6, y: 10),
                       controlPoint1: CGPoint(x: 7, y: 13),
                       controlPoint2: CGPoint(x: 6, y: 11.5))
            p.addCurve(to: CGPoint(x: 10, y: 7),
                       controlPoint1: CGPoint(x: 6, y: 8.5),
                       controlPoint2: CGPoint(x: 7.5, y: 7))
            p.addLine(to: CGPoint(x: 13, y: 7))
        }
        let b = bezier { p in
            p.move(to: CGPoint(x: 15, y: 10))
            p.addCurve(to: CGPoint(x: 18, y: 14),
                       controlPoint1: CGPoint(x: 17, y: 11),
                       controlPoint2: CGPoint(x: 18, y: 12.5))
            p.addCurve(to: CGPoint(x: 14, y: 17),
                       controlPoint1: CGPoint(x: 18, y: 15.5),
                       controlPoint2: CGPoint(x: 16.5, y: 17))
            p.addLine(to: CGPoint(x: 11, y: 17))
        }
        let mid = bezier { p in
            p.move(to: CGPoint(x: 9, y: 12))
            p.addLine(to: CGPoint(x: 15, y: 12))
        }
        return [DoodleStroke(path: a), DoodleStroke(path: b), DoodleStroke(path: mid)]
    }

    private static func bell() -> [DoodleStroke] {
        let body = bezier { p in
            p.move(to: CGPoint(x: 6, y: 17))
            p.addCurve(to: CGPoint(x: 12, y: 4.5),
                       controlPoint1: CGPoint(x: 6, y: 11),
                       controlPoint2: CGPoint(x: 7.5, y: 4.5))
            p.addCurve(to: CGPoint(x: 18, y: 17),
                       controlPoint1: CGPoint(x: 16.5, y: 4.5),
                       controlPoint2: CGPoint(x: 18, y: 11))
            p.addLine(to: CGPoint(x: 6, y: 17))
            p.close()
        }
        let clapper = bezier { p in
            p.move(to: CGPoint(x: 10, y: 19.5))
            p.addCurve(to: CGPoint(x: 14, y: 19.5),
                       controlPoint1: CGPoint(x: 11, y: 21),
                       controlPoint2: CGPoint(x: 13, y: 21))
        }
        return [DoodleStroke(path: body, closesShape: true), DoodleStroke(path: clapper)]
    }
}
