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
    @EnvironmentObject var endingsTracker: EndingsTracker
    @EnvironmentObject var personalStore: PersonalStoriesStore
    @Environment(\.dismiss) private var dismiss

    @State private var showDeleteConfirm = false
    @State private var showRestartConfirm = false

    @State private var goReading = false

    private var savedProgress: ReadingProgress? {
        progressStore.progress(for: story.storageKey)
    }
    private var isFavorite: Bool {
        favoritesStore.isFavorite(story.storageKey)
    }
    /// Personal (user-authored or AI-generated) stories carry the `user-`
    /// id prefix and live in `PersonalStoriesStore` — they can be deleted
    /// from this screen.
    private var isPersonalStory: Bool {
        story.id.hasPrefix("user-")
    }

    private var invitation: String {
        story.title == story.sourceTitle
            ? "Your choices decide how this version unfolds."
            : "What would you have done in \(story.sourceTitle)?"
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
                        if isPersonalStory {
                            DoodleButton(doodle: .xmark, label: "Delete") {
                                showDeleteConfirm = true
                            }
                        }
                        DoodleButton(doodle: isFavorite ? .heartFill : .heart,
                                     label: isFavorite ? "Remove from Library" : "Save to Library") {
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
                        Text(invitation)
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
                                .lineSpacing(6)
                        }
                    }
                    .padding(.horizontal, 24)

                    // Metadata
                    HStack(spacing: 10) {
                        SketchBadge(text: story.genre.rawValue)
                        SketchBadge(text: story.kind.displayName)
                        SketchBadge(text: "\(story.estimatedMinutes) min")
                        SketchBadge(text: "\(story.endingCount) endings")
                    }
                    .padding(.horizontal, 24)

                    if let stars = story.stars {
                        HStack(spacing: 10) {
                            StarRating(rating: stars, loved: story.isLoved, size: 18)
                            Text(story.isLoved ? "A favorite" : "Rated")
                                .font(Theme.Fonts.bodyItalic(13))
                                .foregroundColor(Theme.Palette.inkSoft)
                        }
                        .padding(.horizontal, 24)
                    }

                    EndingsGridView(
                        story: story,
                        discovered: endingsTracker.reached(for: story.storageKey)
                    )
                    .padding(.horizontal, 24)

                    // CTAs
                    VStack(spacing: 14) {
                        if let progress = savedProgress {
                            VStack(alignment: .leading, spacing: 8) {
                                HStack(spacing: 8) {
                                    DoodleIcon(.bookmarkFill, size: 16, filled: true)
                                    Text("Continue from \(progress.sceneTitle ?? "your saved place")")
                                        .font(Theme.Fonts.bodyItalic(13))
                                        .foregroundColor(Theme.Palette.inkSoft)
                                    Spacer()
                                    Text("\(Int(progress.completionFraction * 100))%")
                                        .font(Theme.Fonts.headingMedium(12))
                                        .foregroundColor(Theme.Palette.inkSoft)
                                }
                                GeometryReader { geometry in
                                    ZStack(alignment: .leading) {
                                        Capsule().fill(Theme.Palette.inkHair)
                                        Capsule().fill(Theme.Palette.ink)
                                            .frame(width: geometry.size.width * progress.completionFraction)
                                    }
                                }
                                .frame(height: 7)
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
                                showRestartConfirm = true
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
        .confirmationDialog(
            "Delete this story?",
            isPresented: $showDeleteConfirm,
            titleVisibility: .visible
        ) {
            Button("Delete", role: .destructive) {
                let key = story.storageKey
                personalStore.remove(id: story.id)
                progressStore.clear(storyKey: key)
                if favoritesStore.isFavorite(key) {
                    favoritesStore.toggle(key)
                }
                dismiss()
            }
            Button("Cancel", role: .cancel) { }
        } message: {
            Text("This will remove “\(story.title)” from your stories. Your progress for it is also cleared.")
        }
        .confirmationDialog(
            "Start from the beginning?",
            isPresented: $showRestartConfirm,
            titleVisibility: .visible
        ) {
            Button("Start Over", role: .destructive) {
                progressStore.clear(storyKey: story.storageKey)
                goReading = true
            }
            Button("Keep My Place", role: .cancel) { }
        } message: {
            Text("Your current place in “\(story.title)” will be replaced.")
        }
    }
}
