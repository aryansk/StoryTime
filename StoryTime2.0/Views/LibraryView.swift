import SwiftUI

// MARK: - Library tab
//
// Continue Reading + Favorites. No authoring. No "+" button.

struct LibraryView: View {
    @ObservedObject var catalog: CatalogService
    @ObservedObject var settings: SettingsModel
    @EnvironmentObject var progressStore: ReadingProgressStore
    @EnvironmentObject var favoritesStore: FavoritesStore

    @State private var favoritesGenre: StoryGenre = .all

    private var allFavorites: [CatalogStory] {
        catalog.stories.filter { favoritesStore.isFavorite($0.storageKey) }
    }
    private var favoriteStories: [CatalogStory] {
        guard favoritesGenre != .all else { return allFavorites }
        return allFavorites.filter { $0.genre == favoritesGenre }
    }
    private var favoriteGenres: [StoryGenre] {
        var seen: Set<StoryGenre> = []
        var ordered: [StoryGenre] = [.all]
        for s in allFavorites where !seen.contains(s.genre) {
            seen.insert(s.genre)
            ordered.append(s.genre)
        }
        return ordered
    }

    private var inProgressStories: [(CatalogStory, ReadingProgress)] {
        progressStore.inProgress.compactMap { progress in
            guard let story = catalog.story(id: progress.storyKey) else { return nil }
            return (story, progress)
        }
    }

    var body: some View {
        NavigationStack {
            ZStack {
                PageBackground()

                ScrollView(showsIndicators: false) {
                    VStack(alignment: .leading, spacing: 28) {
                        VStack(alignment: .leading, spacing: 6) {
                            Text("Your")
                                .font(Theme.Fonts.body(20))
                                .foregroundColor(Theme.Palette.inkSoft)
                            HStack(alignment: .bottom, spacing: 8) {
                                Text("Library")
                                    .font(Theme.Fonts.display())
                                    .foregroundColor(Theme.Palette.ink)
                                DoodleIcon(.books, size: 36)
                                    .jitter(amplitude: 0.4)
                                Spacer()
                            }
                        }
                        .padding(.horizontal, 24)
                        .padding(.top, 16)

                        if inProgressStories.isEmpty && favoriteStories.isEmpty {
                            EmptyLibraryState()
                                .padding(.horizontal, 24)
                                .padding(.top, 40)
                        }

                        if !inProgressStories.isEmpty {
                            VStack(alignment: .leading, spacing: 14) {
                                SketchSectionHeader("Continue Reading")
                                LazyVStack(spacing: 14) {
                                    ForEach(inProgressStories, id: \.0.id) { story, progress in
                                        NavigationLink(value: story) {
                                            ContinueReadingRow(story: story, progress: progress)
                                        }
                                        .buttonStyle(.plain)
                                    }
                                }
                                .padding(.horizontal, 24)
                            }
                        }

                        if !allFavorites.isEmpty {
                            VStack(alignment: .leading, spacing: 14) {
                                SketchSectionHeader("Favorites")
                                if favoriteGenres.count > 2 {
                                    ScrollView(.horizontal, showsIndicators: false) {
                                        HStack(spacing: 10) {
                                            ForEach(favoriteGenres) { g in
                                                SketchPill(title: g.rawValue,
                                                           selected: favoritesGenre == g) {
                                                    withAnimation(.easeOut(duration: 0.15)) {
                                                        favoritesGenre = g
                                                    }
                                                }
                                            }
                                        }
                                        .padding(.horizontal, 24)
                                    }
                                }
                                LazyVStack(spacing: 14) {
                                    ForEach(favoriteStories) { story in
                                        NavigationLink(value: story) {
                                            CatalogRowCard(story: story, isFavorite: true)
                                        }
                                        .buttonStyle(.plain)
                                        .contextMenu {
                                            Button(role: .destructive) {
                                                favoritesStore.toggle(story.storageKey)
                                            } label: {
                                                Label("Remove", systemImage: "heart.slash")
                                            }
                                        }
                                    }
                                }
                                .padding(.horizontal, 24)
                            }
                        }

                        Spacer(minLength: 40)
                    }
                }
            }
            .navigationBarHidden(true)
            .navigationDestination(for: CatalogStory.self) { story in
                StoryStartView(story: story, settings: settings)
            }
        }
    }
}

struct ContinueReadingRow: View {
    let story: CatalogStory
    let progress: ReadingProgress

    var body: some View {
        SketchCard(fill: Theme.Palette.butterDeep,
                    seed: CGFloat(story.id.hashValue % 100)) {
            HStack(alignment: .top, spacing: 14) {
                DoodleIcon(.bookmarkFill, size: 28, filled: true)
                VStack(alignment: .leading, spacing: 6) {
                    SketchBadge(text: "In Progress")
                    Text(story.title)
                        .font(Theme.Fonts.cardTitle())
                        .foregroundColor(Theme.Palette.ink)
                    Text(progress.sceneTitle ?? "Resume your story")
                        .font(Theme.Fonts.bodyItalic(13))
                        .foregroundColor(Theme.Palette.inkSoft)
                        .lineLimit(2)
                    HStack(spacing: 6) {
                        Text("Continue")
                            .font(Theme.Fonts.headingMedium(13))
                        DoodleIcon(.arrowRight, size: 14)
                    }
                    .foregroundColor(Theme.Palette.ink)
                    .padding(.top, 4)
                }
                Spacer()
            }
        }
    }
}

struct EmptyLibraryState: View {
    var body: some View {
        VStack(spacing: 16) {
            DoodleIcon(.bookmark, size: 90)
                .jitter(amplitude: 0.4)
            Text("Your library is empty")
                .font(Theme.Fonts.cardTitle())
                .foregroundColor(Theme.Palette.ink)
            Text("Tap the heart on any story to save it here, or start one to keep your place.")
                .font(Theme.Fonts.body(14))
                .foregroundColor(Theme.Palette.inkSoft)
                .multilineTextAlignment(.center)
                .padding(.horizontal, 12)
        }
        .frame(maxWidth: .infinity)
    }
}
