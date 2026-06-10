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
            Theme.Palette.paperYellow
            VStack(alignment: .leading, spacing: 14) {
                HStack {
                    Text("STORYTIME")
                        .font(Theme.Fonts.label())
                        .tracking(2)
                        .foregroundColor(Theme.Palette.inkSoft)
                    Spacer()
                    DoodleIcon(.starFill, size: 18, filled: true)
                }

                Text("What you did in")
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
                        .fill(Theme.Palette.butterDeep)
                    WobblyRect(jitter: 0.6, corner: 10, seed: 13)
                        .stroke(Theme.Palette.ink, lineWidth: Theme.Stroke.bold)
                    HStack(spacing: 14) {
                        DoodleIcon(genreDoodle(for: story.genre), size: 48)
                            .jitter(amplitude: 0.3)
                        VStack(alignment: .leading, spacing: 4) {
                            Text("Your ending")
                                .font(Theme.Fonts.label())
                                .tracking(1)
                                .foregroundColor(Theme.Palette.inkSoft)
                            Text(endingTitle)
                                .font(Theme.Fonts.cardTitle())
                                .foregroundColor(Theme.Palette.ink)
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
                Text("storytime — what would you have done?")
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

    /// Render the card to a UIImage at retina scale.
    @MainActor
    static func render(story: CatalogStory, endingTitle: String, pathLabel: String) -> UIImage? {
        let view = ShareEndingCard(story: story, endingTitle: endingTitle, pathLabel: pathLabel)
        let renderer = ImageRenderer(content: view)
        renderer.scale = UIScreen.main.scale
        return renderer.uiImage
    }
}
