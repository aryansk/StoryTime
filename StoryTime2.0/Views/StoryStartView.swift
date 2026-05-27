import SwiftUI

// MARK: - Story start screen
//
// The "cover page" for a catalog story. Synopsis, metadata, and the
// big button that drops you into the branching scene reader.

struct StoryStartView: View {
    let story: CatalogStory
    @ObservedObject var settings: SettingsModel
    @EnvironmentObject var progressStore: ReadingProgressStore
    @EnvironmentObject var favoritesStore: FavoritesStore
    @Environment(\.dismiss) private var dismiss

    @State private var goReading = false

    private var savedProgress: ReadingProgress? {
        progressStore.progress(for: story.storageKey)
    }
    private var isFavorite: Bool {
        favoritesStore.isFavorite(story.storageKey)
    }

    var body: some View {
        ZStack {
            PageBackground()

            ScrollView(showsIndicators: false) {
                VStack(alignment: .leading, spacing: 24) {
                    // Top bar
                    HStack {
                        DoodleButton(doodle: .chevronLeft, label: "Back") { dismiss() }
                        Spacer()
                        DoodleButton(doodle: isFavorite ? .heartFill : .heart,
                                     label: isFavorite ? "Unfavorite" : "Favorite") {
                            favoritesStore.toggle(story.storageKey)
                        }
                    }
                    .padding(.horizontal, 16)
                    .padding(.top, 8)

                    // Cover doodle
                    ZStack {
                        WobblyRect(jitter: 0.5, corner: 10, seed: 4.0)
                            .fill(Theme.Palette.mist)
                        WobblyRect(jitter: 0.5, corner: 10, seed: 4.0)
                            .stroke(Theme.Palette.ink, lineWidth: Theme.Stroke.bold)
                        VStack(spacing: 12) {
                            DoodleIcon(doodleFor(story), size: 96)
                                .jitter(amplitude: 0.4)
                            if let year = story.releaseYear {
                                Text("\(story.sourceTitle) • \(String(year))")
                                    .font(Theme.Fonts.bodyItalic(13))
                                    .foregroundColor(Theme.Palette.inkSoft)
                            }
                        }
                    }
                    .frame(height: 220)
                    .padding(.horizontal, 24)

                    // Title block
                    VStack(alignment: .leading, spacing: 8) {
                        if story.isNewThisWeek {
                            SketchBadge(text: "NEW THIS WEEK")
                        }
                        Text(story.title)
                            .font(Theme.Fonts.title())
                            .foregroundColor(Theme.Palette.ink)
                        Text("A choose-your-own-adventure after \(story.sourceTitle)")
                            .font(Theme.Fonts.bodyItalic(15))
                            .foregroundColor(Theme.Palette.inkSoft)
                    }
                    .padding(.horizontal, 24)

                    // Synopsis card
                    SketchCard(fill: Theme.Palette.butterDeep, seed: 7.7) {
                        VStack(alignment: .leading, spacing: 8) {
                            Text("Synopsis")
                                .font(Theme.Fonts.label())
                                .tracking(1)
                                .foregroundColor(Theme.Palette.inkSoft)
                            Text(story.synopsis)
                                .font(Theme.Fonts.body(16))
                                .foregroundColor(Theme.Palette.ink)
                                .lineSpacing(5)
                        }
                    }
                    .padding(.horizontal, 24)

                    // Metadata
                    HStack(spacing: 10) {
                        SketchBadge(text: story.genre.rawValue)
                        SketchBadge(text: story.kind == .show ? "Show" : "Movie")
                        SketchBadge(text: "\(story.nodes.count) scenes")
                    }
                    .padding(.horizontal, 24)

                    // CTAs
                    VStack(spacing: 14) {
                        if let progress = savedProgress {
                            HStack(spacing: 8) {
                                DoodleIcon(.bookmarkFill, size: 16, filled: true)
                                Text("Last scene: \(progress.sceneTitle ?? "in progress")")
                                    .font(Theme.Fonts.bodyItalic(13))
                                    .foregroundColor(Theme.Palette.inkSoft)
                                Spacer()
                            }
                        }
                        SketchButton(
                            title: savedProgress == nil ? "Begin the Story" : "Continue Reading",
                            trailingDoodle: .arrowRight,
                            style: .primary
                        ) {
                            goReading = true
                        }
                        if savedProgress != nil {
                            SketchButton(
                                title: "Start Over",
                                doodle: .undo,
                                style: .ghost
                            ) {
                                progressStore.clear(storyKey: story.storageKey)
                            }
                        }
                    }
                    .padding(.horizontal, 24)
                    .padding(.top, 4)

                    Spacer(minLength: 40)
                }
            }
        }
        .navigationBarBackButtonHidden(true)
        .navigationDestination(isPresented: $goReading) {
            StoryReaderView(story: story, settings: settings)
        }
    }
}
