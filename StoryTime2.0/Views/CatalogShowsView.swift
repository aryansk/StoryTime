import SwiftUI

// MARK: - Shows tab
//
// The curated catalog. "New This Week" rail at the top, then genre
// filters, then the rest of the grid. Every card is a flat sketchbook
// page, every icon is a hand-drawn doodle.

struct CatalogShowsView: View {
    @ObservedObject var catalog: CatalogService
    @ObservedObject var settings: SettingsModel
    @EnvironmentObject var progressStore: ReadingProgressStore
    @EnvironmentObject var favoritesStore: FavoritesStore
    @EnvironmentObject var personalStore: PersonalStoriesStore

    @State private var genre: StoryGenre = .all
    @State private var ratingFilter: RatingFilter = .all
    @State private var searchText: String = ""
    @State private var activeCollection: StoryCollection? = nil
    @State private var showCreator: Bool = false

    /// Merged catalog: personal stories first (most recently added on top),
    /// then bundled/remote.
    private var allStories: [CatalogStory] {
        let bundled = catalog.stories
        let bundledIds = Set(bundled.map(\.id))
        let personal = personalStore.stories.filter { !bundledIds.contains($0.id) }
        return personal + bundled
    }

    private var filtered: [CatalogStory] {
        var list = allStories
        if genre != .all { list = list.filter { $0.genre == genre } }
        list = list.filter { ratingFilter.matches($0) }
        if let collection = activeCollection {
            list = list.filter { collection.matches($0) }
        }
        if !searchText.isEmpty {
            list = list.filter {
                $0.title.localizedCaseInsensitiveContains(searchText) ||
                $0.sourceTitle.localizedCaseInsensitiveContains(searchText) ||
                $0.synopsis.localizedCaseInsensitiveContains(searchText)
            }
        }
        return list
    }

    var body: some View {
        NavigationStack {
            ZStack {
                PageBackground()

                ScrollView(showsIndicators: false) {
                    VStack(alignment: .leading, spacing: 28) {
                        // Title block
                        VStack(alignment: .leading, spacing: 6) {
                            Text("Tonight's")
                                .font(Theme.Fonts.body(20))
                                .foregroundColor(Theme.Palette.inkSoft)
                            HStack(alignment: .bottom, spacing: 8) {
                                Text("Adventures")
                                    .font(Theme.Fonts.display())
                                    .foregroundColor(Theme.Palette.ink)
                                DoodleIcon(.sparkle, size: 36)
                                    .jitter(amplitude: 0.5)
                                Spacer()
                                Button {
                                    showCreator = true
                                } label: {
                                    DoodleIcon(.plus, size: 28)
                                        .jitter(amplitude: 0.3)
                                        .padding(8)
                                        .background(
                                            WobblyRect(jitter: 0.4, corner: 8, seed: 41)
                                                .stroke(Theme.Palette.ink, lineWidth: Theme.Stroke.line)
                                        )
                                }
                                .buttonStyle(.plain)
                                .accessibilityLabel("Create a story")
                            }
                            Text("Step inside the stories you've been watching. Pick a path. See what breaks.")
                                .font(Theme.Fonts.body(15))
                                .foregroundColor(Theme.Palette.inkSoft)
                                .padding(.top, 4)
                        }
                        .padding(.horizontal, 24)
                        .padding(.top, 16)

                        // Search
                        SketchTextField(placeholder: "Search the catalog…",
                                        text: $searchText,
                                        doodle: .search)
                            .padding(.horizontal, 24)

                        // New this week rail
                        if !catalog.newThisWeek.isEmpty && searchText.isEmpty {
                            VStack(alignment: .leading, spacing: 14) {
                                HStack(spacing: 8) {
                                    SketchSectionHeader("New This Week")
                                    Spacer()
                                }
                                ScrollView(.horizontal, showsIndicators: false) {
                                    HStack(spacing: 16) {
                                        ForEach(catalog.newThisWeek) { story in
                                            NavigationLink(value: story) {
                                                NewPosterCard(story: story)
                                            }
                                            .buttonStyle(.plain)
                                        }
                                    }
                                    .padding(.horizontal, 24)
                                    .padding(.vertical, 4)
                                }
                            }
                        }

                        // Collections (mood / curated)
                        VStack(alignment: .leading, spacing: 12) {
                            SketchSectionHeader("Collections")
                            ScrollView(.horizontal, showsIndicators: false) {
                                HStack(spacing: 10) {
                                    SketchPill(title: "All",
                                               selected: activeCollection == nil) {
                                        withAnimation(.easeOut(duration: 0.15)) {
                                            activeCollection = nil
                                        }
                                    }
                                    ForEach(StoryCollections.all) { c in
                                        SketchPill(title: c.title,
                                                   selected: activeCollection?.id == c.id) {
                                            withAnimation(.easeOut(duration: 0.15)) {
                                                activeCollection = (activeCollection?.id == c.id) ? nil : c
                                            }
                                        }
                                    }
                                }
                                .padding(.horizontal, 24)
                            }
                            if let c = activeCollection {
                                Text(c.subtitle)
                                    .font(Theme.Fonts.bodyItalic(13))
                                    .foregroundColor(Theme.Palette.inkSoft)
                                    .padding(.horizontal, 24)
                            }
                        }

                        // Genre pills
                        VStack(alignment: .leading, spacing: 12) {
                            SketchSectionHeader("Browse")
                            ScrollView(.horizontal, showsIndicators: false) {
                                HStack(spacing: 10) {
                                    ForEach(StoryGenre.allCases) { g in
                                        SketchPill(title: g.rawValue,
                                                   selected: genre == g) {
                                            withAnimation(.easeOut(duration: 0.15)) {
                                                genre = g
                                            }
                                        }
                                    }
                                }
                                .padding(.horizontal, 24)
                            }

                            // Rating filter: complements the genre pills so the
                            // catalog can be narrowed by curator's star rating
                            // and the "loved" glow.
                            ScrollView(.horizontal, showsIndicators: false) {
                                HStack(spacing: 10) {
                                    ForEach(RatingFilter.allCases) { r in
                                        SketchPill(title: r.label,
                                                   selected: ratingFilter == r) {
                                            withAnimation(.easeOut(duration: 0.15)) {
                                                ratingFilter = r
                                            }
                                        }
                                    }
                                }
                                .padding(.horizontal, 24)
                            }
                        }

                        // Grid
                        VStack(alignment: .leading, spacing: 16) {
                            SketchSectionHeader(genre == .all ? "All Stories"
                                                              : "\(genre.rawValue) Stories")
                            if filtered.isEmpty {
                                EmptyCatalogState()
                                    .padding(.horizontal, 24)
                            } else {
                                LazyVStack(spacing: 16) {
                                    ForEach(filtered) { story in
                                        NavigationLink(value: story) {
                                            CatalogRowCard(story: story,
                                                            isFavorite: favoritesStore.isFavorite(story.storageKey))
                                        }
                                        .buttonStyle(.plain)
                                        .contextMenu {
                                            Button {
                                                favoritesStore.toggle(story.storageKey)
                                            } label: {
                                                Label(
                                                    favoritesStore.isFavorite(story.storageKey)
                                                        ? "Remove from Library"
                                                        : "Save to Library",
                                                    systemImage: favoritesStore.isFavorite(story.storageKey)
                                                        ? "heart.slash"
                                                        : "heart"
                                                )
                                            }
                                        }
                                    }
                                }
                                .padding(.horizontal, 24)
                            }
                        }

                        Spacer(minLength: 40)
                    }
                    .padding(.bottom, 12)
                }
                .refreshable {
                    await catalog.refresh()
                }
            }
            .navigationBarHidden(true)
            .navigationDestination(for: CatalogStory.self) { story in
                StoryStartView(story: story, settings: settings)
            }
            .sheet(isPresented: $showCreator) {
                CreateStoryView(settings: settings)
                    .environmentObject(personalStore)
            }
        }
    }
}

// MARK: - Rating filter

/// Filter pill row that complements the genre pills: narrows the
/// catalog by curator's star rating, with a dedicated "Loved" bucket
/// for the 🌟-flagged entries.
enum RatingFilter: String, CaseIterable, Identifiable, Hashable {
    case all
    case loved
    case fiveStar
    case fourPlus
    case threePlus

    var id: String { rawValue }

    var label: String {
        switch self {
        case .all:        return "Any Rating"
        case .loved:      return "Loved"
        case .fiveStar:   return "5★"
        case .fourPlus:   return "4★+"
        case .threePlus:  return "3★+"
        }
    }

    func matches(_ story: CatalogStory) -> Bool {
        switch self {
        case .all:        return true
        case .loved:      return story.isLoved
        case .fiveStar:   return (story.stars ?? 0) >= 5
        case .fourPlus:   return (story.stars ?? 0) >= 4
        case .threePlus:  return (story.stars ?? 0) >= 3
        }
    }
}

// MARK: - Cards

struct NewPosterCard: View {
    let story: CatalogStory
    var body: some View {
        SketchCard(fill: Theme.Palette.mist, padding: 0, seed: CGFloat(story.id.hashValue % 100)) {
            VStack(alignment: .leading, spacing: 0) {
                ZStack {
                    Theme.Palette.butter
                    DoodleIcon(doodleFor(story), size: 70)
                        .jitter(amplitude: 0.3)
                }
                .frame(width: 200, height: 140)
                .overlay(
                    SketchBadge(text: "NEW")
                        .padding(10),
                    alignment: .topLeading
                )

                VStack(alignment: .leading, spacing: 6) {
                    Text(story.title)
                        .font(Theme.Fonts.cardTitle())
                        .foregroundColor(Theme.Palette.ink)
                        .lineLimit(1)
                    Text(story.kind.displayName)
                        .font(Theme.Fonts.bodyItalic(13))
                        .foregroundColor(Theme.Palette.inkSoft)
                        .lineLimit(1)
                    if let stars = story.stars {
                        StarRating(rating: stars, loved: story.isLoved, size: 13)
                            .padding(.top, 2)
                    }
                }
                .padding(.horizontal, 14)
                .padding(.vertical, 12)
            }
        }
        .frame(width: 220)
    }
}

struct CatalogRowCard: View {
    let story: CatalogStory
    let isFavorite: Bool

    var body: some View {
        SketchCard(fill: Theme.Palette.mist, seed: CGFloat(story.id.hashValue % 100)) {
            HStack(alignment: .top, spacing: 14) {
                ZStack {
                    Theme.Palette.butter
                    DoodleIcon(doodleFor(story), size: 54)
                }
                .frame(width: 80, height: 100)
                .overlay(
                    WobblyRect(jitter: 0.3, corner: 4,
                               seed: CGFloat(story.id.hashValue % 50))
                        .stroke(Theme.Palette.ink, lineWidth: Theme.Stroke.line)
                )

                VStack(alignment: .leading, spacing: 8) {
                    HStack(alignment: .firstTextBaseline, spacing: 8) {
                        Text(story.title)
                            .font(Theme.Fonts.cardTitle())
                            .foregroundColor(Theme.Palette.ink)
                            .lineLimit(1)
                        if story.isNewThisWeek {
                            SketchBadge(text: "NEW")
                        }
                    }
                    Text("After \(story.sourceTitle)")
                        .font(Theme.Fonts.bodyItalic(13))
                        .foregroundColor(Theme.Palette.inkSoft)
                    Text(story.synopsis)
                        .font(Theme.Fonts.body(15))
                        .foregroundColor(Theme.Palette.ink)
                        .lineLimit(3)
                        .lineSpacing(4)

                    HStack(spacing: 8) {
                        SketchBadge(text: story.genre.rawValue)
                        if let stars = story.stars {
                            StarRating(rating: stars, loved: story.isLoved)
                        }
                        if isFavorite {
                            DoodleIcon(.heartFill, size: 16, filled: true)
                        }
                        Spacer()
                        DoodleIcon(.arrowRight, size: 18)
                    }
                    .padding(.top, 2)
                }
            }
        }
    }
}

// MARK: - Empty state

struct EmptyCatalogState: View {
    var body: some View {
        VStack(spacing: 14) {
            DoodleIcon(.popcorn, size: 88)
                .jitter(amplitude: 0.4)
            Text("Nothing here yet")
                .font(Theme.Fonts.cardTitle())
                .foregroundColor(Theme.Palette.ink)
            Text("Try another genre, or pull down to refresh.")
                .font(Theme.Fonts.body(14))
                .foregroundColor(Theme.Palette.inkSoft)
                .multilineTextAlignment(.center)
        }
        .frame(maxWidth: .infinity)
        .padding(.vertical, 40)
    }
}

// MARK: - Helpers

func doodleFor(_ story: CatalogStory) -> DoodleName {
    switch story.genre {
    case .sciFi, .fantasy: return .sparkle
    case .thriller, .horror: return .clapperboard
    case .comedy: return .popcorn
    case .action: return .flame
    case .drama, .all: return .tv
    }
}
