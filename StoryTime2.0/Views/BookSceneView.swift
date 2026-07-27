import SwiftUI
import WebKit

enum BookSceneMode: String, Codable {
    case onboarding
    case hero
    case detail
    case ending
}

enum BookSceneEvent {
    case opened
    case closed
    case pageTurned
}

/// A single reusable Three.js book scene. The catalog keeps its lightweight
/// native cards; opening any card presents this shared scene so the WebGL
/// renderer is not duplicated hundreds of times in a scrolling list.
struct BookSceneView: UIViewRepresentable {
    let story: CatalogStory
    var mode: BookSceneMode = .detail
    var endingTitle: String? = nil
    var onEvent: ((BookSceneEvent) -> Void)? = nil

    func makeCoordinator() -> Coordinator { Coordinator() }

    func makeUIView(context: Context) -> WKWebView {
        let content = WKUserContentController()
        content.add(context.coordinator, name: "booksceneReady")
        content.add(context.coordinator, name: "booksceneEvent")

        let configuration = WKWebViewConfiguration()
        configuration.userContentController = content
        configuration.allowsInlineMediaPlayback = true

        let webView = WKWebView(frame: .zero, configuration: configuration)
        webView.isOpaque = false
        webView.backgroundColor = .clear
        webView.scrollView.isScrollEnabled = false
        context.coordinator.webView = webView
        context.coordinator.payload = payload(for: story)
        context.coordinator.onEvent = onEvent

        // Xcode's synchronized resource group flattens the Web folder in the
        // final bundle, while the HTML and Three.js asset remain siblings.
        if let url = Bundle.main.url(forResource: "bookscene",
                                     withExtension: "html") {
            webView.loadFileURL(url, allowingReadAccessTo: url.deletingLastPathComponent())
        }
        return webView
    }

    func updateUIView(_ webView: WKWebView, context: Context) {
        context.coordinator.payload = payload(for: story)
        context.coordinator.onEvent = onEvent
        context.coordinator.pushPayload()
    }

    private func payload(for story: CatalogStory) -> String {
        let minutes = story.estimatedMinutes
        let endings = story.endingCount
        let books = [
            SceneBook(title: story.sourceTitle == story.title ? "A different path" : story.sourceTitle,
                      genre: story.genre.rawValue,
                      minutes: minutes,
                      endings: endings,
                      endingTitle: nil),
            SceneBook(title: story.title,
                      genre: story.genre.rawValue,
                      minutes: minutes,
                      endings: endings,
                      endingTitle: endingTitle),
            SceneBook(title: "The next chapter",
                      genre: story.genre.rawValue,
                      minutes: minutes,
                      endings: endings,
                      endingTitle: nil),
        ]
        let encoder = JSONEncoder()
        guard let data = try? encoder.encode(ScenePayload(books: books,
                                                          mode: mode,
                                                          endingTitle: endingTitle)),
              let json = String(data: data, encoding: .utf8) else { return "{\"books\":[]}" }
        return json
    }

    private struct ScenePayload: Encodable {
        let books: [SceneBook]
        let mode: BookSceneMode
        let endingTitle: String?
    }

    private struct SceneBook: Encodable {
        let title: String
        let genre: String
        let minutes: Int
        let endings: Int
        let endingTitle: String?
    }

    final class Coordinator: NSObject, WKScriptMessageHandler {
        weak var webView: WKWebView?
        var payload = "{\"books\":[]}"
        var ready = false
        var lastPushedPayload: String?
        var onEvent: ((BookSceneEvent) -> Void)?

        func userContentController(_ userContentController: WKUserContentController,
                                   didReceive message: WKScriptMessage) {
            if message.name == "booksceneReady" {
                ready = true
                pushPayload()
                return
            }
            guard message.name == "booksceneEvent",
                  let body = message.body as? [String: Any],
                  let type = body["type"] as? String else { return }
            switch type {
            case "opened": onEvent?(.opened)
            case "closed": onEvent?(.closed)
            case "pageTurned": onEvent?(.pageTurned)
            default: break
            }
        }

        func pushPayload() {
            guard ready, let webView else { return }
            guard lastPushedPayload != payload else { return }
            lastPushedPayload = payload
            webView.evaluateJavaScript("window.setBookData(\(payload));", completionHandler: nil)
        }
    }
}

/// Lightweight native book-shaped artwork used by catalog cards. The actual
/// WebGL page-turn scene is intentionally shared on the detail screen.
struct BookCoverThumbnail: View {
    let story: CatalogStory
    var compact = false

    private var coverColor: Color {
        switch story.genre {
        case .horror: return Color(red: 0.35, green: 0.15, blue: 0.25)
        case .thriller: return Color(red: 0.65, green: 0.24, blue: 0.22)
        case .comedy: return Color(red: 0.86, green: 0.55, blue: 0.22)
        case .drama: return Color(red: 0.26, green: 0.40, blue: 0.60)
        case .fantasy: return Color(red: 0.40, green: 0.32, blue: 0.58)
        case .action: return Color(red: 0.62, green: 0.32, blue: 0.24)
        case .sciFi: return Color(red: 0.18, green: 0.52, blue: 0.56)
        case .all: return Theme.Palette.ink
        }
    }

    var body: some View {
        ZStack(alignment: .leading) {
            RoundedRectangle(cornerRadius: compact ? 5 : 8)
                .fill(Theme.Palette.paperYellow)
                .offset(x: 5)
            HStack(spacing: 0) {
                Rectangle()
                    .fill(coverColor.opacity(0.78))
                    .frame(width: compact ? 7 : 10)
                VStack(alignment: .leading, spacing: compact ? 5 : 9) {
                    Text("STORYTIME")
                        .font(Theme.Fonts.meta())
                        .tracking(1.2)
                        .foregroundColor(Theme.Palette.butter)
                    Spacer(minLength: 0)
                    Text(story.title)
                        .font(Theme.Fonts.heading(compact ? 12 : 17))
                        .foregroundColor(Theme.Palette.butter)
                        .lineLimit(compact ? 3 : 4)
                    Spacer(minLength: 0)
                    Text(story.genre.rawValue.uppercased())
                        .font(Theme.Fonts.meta())
                        .tracking(0.8)
                        .foregroundColor(Theme.Palette.butter.opacity(0.82))
                }
                .padding(compact ? 9 : 14)
                Spacer(minLength: 0)
            }
            .background(coverColor)
            .clipShape(RoundedRectangle(cornerRadius: compact ? 5 : 8))
            .overlay(
                RoundedRectangle(cornerRadius: compact ? 5 : 8)
                    .stroke(Theme.Palette.ink, lineWidth: Theme.Stroke.line)
            )
        }
        .rotation3DEffect(.degrees(-7), axis: (x: 0, y: 1, z: 0), perspective: 0.7)
        .accessibilityLabel("Book cover for \(story.title)")
    }
}
