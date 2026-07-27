import SwiftUI

// MARK: - Library tab
//
// Continue Reading + Favorites. No authoring. No "+" button.

struct LibraryView: View {
    @ObservedObject var catalog: CatalogService
    @ObservedObject var settings: SettingsModel
    @EnvironmentObject var progressStore: ReadingProgressStore
    @EnvironmentObject var favoritesStore: FavoritesStore
    @EnvironmentObject var personalStore: PersonalStoriesStore
    @EnvironmentObject var statsStore: StatsStore
    @EnvironmentObject var endingsTracker: EndingsTracker

    @Environment(\.accessibilityReduceMotion) private var reduceMotion

    @State private var favoritesGenre: StoryGenre = .all
    /// Library rows now participate in the same cover-to-story zoom that
    /// Discover uses, so opening a book from either shelf feels identical.
    @Namespace private var storyTransition

    /// Catalog stories + personal stories (personal first), de-duped by id.
    private var allStories: [CatalogStory] {
        let bundled = catalog.stories
        let bundledIds = Set(bundled.map(\.id))
        let personal = personalStore.stories.filter { !bundledIds.contains($0.id) }
        return personal + bundled
    }

    /// Everything the body needs, derived in one pass. Previously each of
    /// these was a computed property that rebuilt `allStories` (and a Set)
    /// from scratch on every access, and `inProgress` did a linear scan per
    /// progress entry — O(stories × progress). Here we build one id→story
    /// index and reuse it.

    /// One in-progress shelf entry. A named type rather than a tuple so it
    /// can be `Identifiable` — `ForEach` and `.indexed` both need an id, and
    /// Swift has no key paths into tuple components.
    private struct ResumeEntry: Identifiable {
        let story: CatalogStory
        let progress: ReadingProgress
        var id: CatalogStory.ID { story.id }
    }

    private struct Derived {
        var inProgress: [ResumeEntry]
        var finished: [CatalogStory]
        var allFavorites: [CatalogStory]
        var shownFavorites: [CatalogStory]
        var favoriteGenres: [StoryGenre]
    }

    private func derive() -> Derived {
        let all = allStories
        let index = Dictionary(all.map { ($0.id, $0) }, uniquingKeysWith: { a, _ in a })

        let inProgress: [ResumeEntry] = progressStore.inProgress.compactMap {
            guard let story = index[$0.storyKey] else { return nil }
            return ResumeEntry(story: story, progress: $0)
        }

        // Reaching an ending clears progress and records completion, so a
        // finished story never also sits in Continue Reading — but guard the
        // overlap anyway in case a resume was rebuilt. Sorted A–Z for a
        // stable shelf (completions carry no timestamp).
        let inProgressKeys = Set(inProgress.map { $0.story.storageKey })
        let finished = all
            .filter { statsStore.completedStories.contains($0.storageKey)
                      && !inProgressKeys.contains($0.storageKey) }
            .sorted { $0.title.localizedCaseInsensitiveCompare($1.title) == .orderedAscending }

        let favorites = all.filter { favoritesStore.isFavorite($0.storageKey) }

        var seen: Set<StoryGenre> = []
        var genres: [StoryGenre] = [.all]
        for s in favorites where !seen.contains(s.genre) {
            seen.insert(s.genre)
            genres.append(s.genre)
        }

        let shown = favoritesGenre == .all
            ? favorites
            : favorites.filter { $0.genre == favoritesGenre }

        return Derived(inProgress: inProgress,
                       finished: finished,
                       allFavorites: favorites,
                       shownFavorites: shown,
                       favoriteGenres: genres)
    }

    var body: some View {
        let derived = derive()
        return NavigationStack {
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

                        if derived.inProgress.isEmpty && derived.finished.isEmpty && derived.allFavorites.isEmpty {
                            EmptyLibraryState()
                                .padding(.horizontal, 24)
                                .padding(.top, 40)
                                .stAppear(0, rise: 20)
                        }

                        if !derived.inProgress.isEmpty {
                            VStack(alignment: .leading, spacing: 14) {
                                SketchSectionHeader("Continue Reading")
                                LazyVStack(spacing: 14) {
                                    ForEach(derived.inProgress.indexed) { item in
                                        let story = item.value.story
                                        NavigationLink(value: story) {
                                            ContinueReadingRow(story: story,
                                                               progress: item.value.progress)
                                                .matchedTransitionSource(id: story.id, in: storyTransition)
                                        }
                                        .stPressable()
                                        .stAppear(item.index, rise: 16, enabled: item.index < 10)
                                    }
                                }
                                .padding(.horizontal, 24)
                            }
                        }

                        if !derived.finished.isEmpty {
                            VStack(alignment: .leading, spacing: 14) {
                                SketchSectionHeader("Finished · \(derived.finished.count)")
                                LazyVStack(spacing: 14) {
                                    ForEach(derived.finished.indexed) { item in
                                        let story = item.value
                                        NavigationLink(value: story) {
                                            FinishedRow(
                                                story: story,
                                                endingsFound: endingsTracker.count(for: story.storageKey)
                                            )
                                            .matchedTransitionSource(id: story.id, in: storyTransition)
                                        }
                                        .stPressable()
                                        .stAppear(item.index, rise: 16, enabled: item.index < 10)
                                    }
                                }
                                .padding(.horizontal, 24)
                            }
                        }

                        if !derived.allFavorites.isEmpty {
                            VStack(alignment: .leading, spacing: 14) {
                                SketchSectionHeader("Favorites")
                                if derived.favoriteGenres.count > 2 {
                                    ScrollView(.horizontal, showsIndicators: false) {
                                        HStack(spacing: 10) {
                                            ForEach(derived.favoriteGenres) { g in
                                                SketchPill(title: g.rawValue,
                                                           selected: favoritesGenre == g) {
                                                    withAnimation(stMotion(Theme.Motion.settle,
                                                                            reduced: reduceMotion)) {
                                                        favoritesGenre = g
                                                    }
                                                }
                                            }
                                        }
                                        .padding(.horizontal, 24)
                                    }
                                }
                                LazyVStack(spacing: 14) {
                                    ForEach(derived.shownFavorites.indexed) { item in
                                        let story = item.value
                                        NavigationLink(value: story) {
                                            CatalogRowCard(story: story, isFavorite: true)
                                                .matchedTransitionSource(id: story.id, in: storyTransition)
                                        }
                                        .stPressable()
                                        .stAppear(item.index, rise: 16, enabled: item.index < 10)
                                        .contextMenu {
                                            Button(role: .destructive) {
                                                favoritesStore.toggle(story.storageKey)
                                            } label: {
                                                Label {
                                                    Text("Remove")
                                                } icon: {
                                                    DoodleIcon(.heartSlash, size: 16)
                                                }
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
                StoryStartView(story: story,
                               settings: settings,
                               transitionNamespace: storyTransition)
            }
        }
    }
}

struct ContinueReadingRow: View {
    let story: CatalogStory
    let progress: ReadingProgress

    var body: some View {
        SketchCard(fill: Theme.Palette.butterDeep,
                    seed: CGFloat(story.id.stableSeed(100))) {
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
                    AnimatedProgressBar(fraction: progress.completionFraction, height: 6)
                        .accessibilityLabel("\(Int(progress.completionFraction * 100)) percent complete")
                    HStack(spacing: 6) {
                        Text("Continue")
                            .font(Theme.Fonts.headingMedium(13))
                        DoodleIcon(.arrowRight, size: 14)
                        Spacer()
                        Text(progress.lastUpdated, style: .relative)
                            .font(Theme.Fonts.bodyItalic(11))
                            .foregroundColor(Theme.Palette.inkSoft)
                    }
                    .foregroundColor(Theme.Palette.ink)
                    .padding(.top, 4)
                }
                Spacer()
            }
        }
    }
}

// MARK: - Finished shelf row
//
// Celebrates a completed story and nudges replay: branching stories usually
// have several endings, and this is the one place that surfaces "you've seen
// 2 of 5 — go find the rest."

struct FinishedRow: View {
    let story: CatalogStory
    let endingsFound: Int

    private var totalEndings: Int { story.endingCount }
    private var allFound: Bool { totalEndings > 0 && endingsFound >= totalEndings }

    var body: some View {
        SketchCard(fill: Theme.Palette.mist,
                   seed: CGFloat(story.id.stableSeed(100))) {
            HStack(alignment: .top, spacing: 14) {
                ZStack {
                    WobblyRect(jitter: 0.5, corner: 14, seed: CGFloat(story.id.stableSeed(70)))
                        .fill(allFound ? Theme.Palette.butterDeep : Theme.Palette.butter)
                        .frame(width: 44, height: 44)
                    WobblyRect(jitter: 0.5, corner: 14, seed: CGFloat(story.id.stableSeed(70)))
                        .stroke(Theme.Palette.ink, lineWidth: Theme.Stroke.bold)
                        .frame(width: 44, height: 44)
                    DoodleIcon(allFound ? .starFill : .checkmark, size: 22, filled: allFound)
                }

                VStack(alignment: .leading, spacing: 6) {
                    SketchBadge(text: allFound ? "All endings found" : "Finished")
                    Text(story.title)
                        .font(Theme.Fonts.cardTitle())
                        .foregroundColor(Theme.Palette.ink)
                        .lineLimit(1)
                    if totalEndings > 1 {
                        Text("\(endingsFound) of \(totalEndings) endings discovered")
                            .font(Theme.Fonts.bodyItalic(13))
                            .foregroundColor(Theme.Palette.inkSoft)
                    }
                    HStack(spacing: 6) {
                        DoodleIcon(.undo, size: 14)
                        Text(allFound ? "Read it again" : "Replay for another ending")
                            .font(Theme.Fonts.headingMedium(13))
                        Spacer()
                        DoodleIcon(.arrowRight, size: 14)
                    }
                    .foregroundColor(Theme.Palette.ink)
                    .padding(.top, 4)
                }
                Spacer(minLength: 0)
            }
        }
        .accessibilityElement(children: .combine)
        .accessibilityLabel(
            "\(story.title), finished. \(endingsFound) of \(totalEndings) endings discovered."
        )
        .accessibilityHint("Opens the story to replay")
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
