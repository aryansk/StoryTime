import SwiftUI
import UIKit

// MARK: - Shareable ending card
//
// Renders a small square sketch poster of the ending the reader just
// reached: source title, ending title, "what would you have done in X?"
// tagline, and a doodle. Used by StoryReaderView to produce a UIImage
// suitable for the system share sheet.

struct ShareEndingCard: View {
    let story: CatalogStory
    let endingTitle: String
    let pathLabel: String          // e.g. "Path of 22"

    var body: some View {
        ZStack {
            Theme.Palette.paperSpeckle
            VStack(alignment: .leading, spacing: 14) {
                HStack {
                    Text("STORYTIME")
                        .font(Theme.Fonts.label())
                        .tracking(2)
                        .foregroundColor(Theme.Palette.inkSoft)
                    Spacer()
                    HStack(spacing: 6) {
                        DoodleIcon(.bookmarkFill, size: 16, filled: true)
                        Text("ENDING FOUND")
                            .font(Theme.Fonts.meta())
                            .tracking(1)
                    }
                    .foregroundColor(Theme.Palette.storyCoral)
                }

                Text("WHAT YOU DID IN")
                    .font(Theme.Fonts.bodyItalic(15))
                    .foregroundColor(Theme.Palette.inkSoft)
                Text(story.sourceTitle)
                    .font(Theme.Fonts.title())
                    .foregroundColor(Theme.Palette.ink)
                    .lineLimit(3)
                    .minimumScaleFactor(0.5)

                Spacer(minLength: 6)

                ZStack {
                    WobblyRect(jitter: 0.6, corner: 10, seed: 13)
                        .fill(coverColor)
                    WobblyRect(jitter: 0.6, corner: 10, seed: 13)
                        .stroke(Theme.Palette.ink, lineWidth: Theme.Stroke.line)
                    HStack(spacing: 14) {
                        ZStack {
                            RoundedRectangle(cornerRadius: 5)
                                .fill(Theme.Palette.butter.opacity(0.92))
                            DoodleIcon(genreDoodle(for: story.genre), size: 42,
                                       color: Theme.Palette.ink)
                        }
                        .frame(width: 62, height: 82)
                        VStack(alignment: .leading, spacing: 4) {
                            Text("YOUR ENDING")
                                .font(Theme.Fonts.label())
                                .tracking(1)
                                .foregroundColor(Theme.Palette.butter.opacity(0.80))
                            Text(endingTitle)
                                .font(Theme.Fonts.cardTitle())
                                .foregroundColor(Theme.Palette.butter)
                                .lineLimit(3)
                                .minimumScaleFactor(0.6)
                        }
                        Spacer(minLength: 0)
                    }
                    .padding(.horizontal, 16)
                    .padding(.vertical, 16)
                }
                .frame(maxWidth: .infinity, minHeight: 130)

                HStack(spacing: 8) {
                    SketchBadge(text: story.kind.displayName)
                    SketchBadge(text: story.genre.rawValue)
                    Spacer()
                    Text(pathLabel)
                        .font(Theme.Fonts.bodyItalic(13))
                        .foregroundColor(Theme.Palette.inkSoft)
                }

                Spacer(minLength: 4)
                Text("What would you have done?")
                    .font(Theme.Fonts.bodyItalic(12))
                    .foregroundColor(Theme.Palette.inkSoft)
            }
            .padding(22)
        }
        .frame(width: 540, height: 540)
        .clipped()
    }

    private func genreDoodle(for genre: StoryGenre) -> DoodleName {
        switch genre {
        case .sciFi, .fantasy: return .sparkle
        case .thriller, .horror: return .clapperboard
        case .comedy: return .popcorn
        case .action: return .flame
        case .drama, .all: return .tv
        }
    }

    private var coverColor: Color {
        switch story.genre {
        case .horror: return Color(red: 0.38, green: 0.16, blue: 0.28)
        case .thriller: return Color(red: 0.72, green: 0.24, blue: 0.25)
        case .comedy: return Color(red: 0.88, green: 0.49, blue: 0.18)
        case .drama: return Color(red: 0.25, green: 0.37, blue: 0.62)
        case .fantasy: return Color(red: 0.42, green: 0.31, blue: 0.62)
        case .action: return Color(red: 0.72, green: 0.31, blue: 0.23)
        case .sciFi: return Color(red: 0.16, green: 0.50, blue: 0.60)
        case .all: return Theme.Palette.ink
        }
    }

    /// Render the card to a UIImage at retina scale.
    @MainActor
    static func render(story: CatalogStory, endingTitle: String, pathLabel: String) -> UIImage? {
        let view = ShareEndingCard(story: story, endingTitle: endingTitle, pathLabel: pathLabel)
        let renderer = ImageRenderer(content: view)
        renderer.scale = UIScreen.main.scale
        return renderer.uiImage
    }
}
