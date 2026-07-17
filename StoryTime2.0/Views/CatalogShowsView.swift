import SwiftUI

// MARK: - Discover tab
//
// The curated catalog. "New This Week" rail at the top, then genre
// filters, then the rest of the grid. Every card is a flat sketchbook
// page, every icon is a hand-drawn doodle.

struct CatalogShowsView: View {
    @ObservedObject var catalog: CatalogService
    @ObservedObject var settings: SettingsModel
    @ObservedObject var userModel: UserModel
    @EnvironmentObject var progressStore: ReadingProgressStore
    @EnvironmentObject var favoritesStore: FavoritesStore
    @EnvironmentObject var personalStore: PersonalStoriesStore
    @EnvironmentObject var statsStore: StatsStore

    @State private var genre: StoryGenre = .all
    @State private var ratingFilter: RatingFilter = .all
    @State private var sort: StorySort = .featured
    @State private var searchText: String = ""
    @State private var activeCollection: StoryCollection? = nil
    @State private var showCreator: Bool = false
    /// Programmatic navigation stack. NavigationLink(value:) rows append to
    /// this, and "Surprise Me" pushes a random story onto it directly.
    @State private var path: [CatalogStory] = []

    /// Merged catalog: personal stories first (most recently added on top),
    /// then bundled/remote.
    private var allStories: [CatalogStory] {
        let bundled = catalog.stories
        let bundledIds = Set(bundled.map(\.id))
        let personal = personalStore.stories.filter { !bundledIds.contains($0.id) }
        return personal + bundled
    }

    /// Empty-state copy that reflects *why* nothing matched, instead of
    /// always blaming the genre.
    private var emptyStateMessage: String {
        if !searchText.isEmpty {
            return "No stories match “\(searchText).” Try a different search."
        }
        if activeCollection != nil {
            return "This collection is empty right now. Try another, or clear it."
        }
        if ratingFilter != .all {
            return "No stories at this rating. Try “Any Rating.”"
        }
        if genre != .all {
            return "No \(genre.rawValue) stories yet. Try another genre."
        }
        return "Try another genre, or pull down to refresh."
    }

    /// Whether any narrowing filter is currently applied (drives the
    /// one-tap "Clear filters" recovery in the empty state).
    private var filtersActive: Bool {
        genre != .all || ratingFilter != .all || activeCollection != nil || !searchText.isEmpty
    }

    private func filtered(from allStories: [CatalogStory]) -> [CatalogStory] {
        var list = allStories
        if genre != .all { list = list.filter { $0.genre == genre } }
        list = list.filter { ratingFilter.matches($0) }
        if let collection = activeCollection {
            list = list.filter { collection.matches($0) }
        }
        let query = searchText.trimmingCharacters(in: .whitespacesAndNewlines)
        if !query.isEmpty {
            list = list.filter {
                $0.title.localizedCaseInsensitiveContains(query) ||
                $0.sourceTitle.localizedCaseInsensitiveContains(query) ||
                $0.synopsis.localizedCaseInsensitiveContains(query) ||
                $0.genre.rawValue.localizedCaseInsensitiveContains(query) ||
                $0.kind.displayName.localizedCaseInsensitiveContains(query) ||
                $0.tags.contains { $0.localizedCaseInsensitiveContains(query) }
            }
        }
        return list
    }

    /// A deterministic daily recommendation tuned by onboarding intent and
    /// reading history. It changes each calendar day but remains stable across
    /// launches, which makes it feel curated instead of random.
    /// Scores each story exactly once — `max(by:)` on the raw list evaluated
    /// the (string-hashing) scorer twice per comparison.
    private func tonightPick(from allStories: [CatalogStory]) -> CatalogStory? {
        let day = Calendar.current.ordinality(of: .day, in: .era, for: Date()) ?? 0
        return allStories
            .map { (story: $0, score: recommendationScore($0, day: day)) }
            .max { $0.score < $1.score }?
            .story
    }

    private func recommendationScore(_ story: CatalogStory, day: Int) -> Int {
        var score = (story.stars ?? 3) * 4 + (story.isLoved ? 6 : 0)
        if !statsStore.storiesStarted.contains(story.storageKey) { score += 5 }
        if !statsStore.completedStories.contains(story.storageKey) { score += 4 }
        if userModel.favoriteGenres.contains(story.genre.rawValue) { score += 10 }

        switch userModel.goal {
        case "Unwind":
            if [.comedy, .drama].contains(story.genre) { score += 12 }
        case "Get Hooked":
            if [.thriller, .horror].contains(story.genre) { score += 12 }
        case "Roleplay":
            if [.fantasy, .action, .sciFi].contains(story.genre) { score += 12 }
        case "Bedtime":
            if story.tags.contains("mini") { score += 16 }
            if [.drama, .comedy].contains(story.genre) { score += 5 }
        default:
            break
        }

        switch userModel.experienceLevel {
        case "Casual":
            if story.estimatedMinutes <= 8 { score += 8 }
        case "Obsessed":
            if story.nextStoryId != nil || story.endingCount >= 4 { score += 8 }
        default:
            if (9...18).contains(story.estimatedMinutes) { score += 4 }
        }

        score += "\(story.id)-\(day)".stableSeed(9)
        return score
    }

    // MARK: Surprise Me + Sort controls

    /// Picks a random story, preferring ones the reader hasn't opened yet, so
    /// "Surprise Me" leans toward genuine discovery rather than re-surfacing a
    /// story that's already been started or finished.
    private func surprisePick(from all: [CatalogStory]) -> CatalogStory? {
        guard !all.isEmpty else { return nil }
        let unread = all.filter {
            !statsStore.storiesStarted.contains($0.storageKey)
                && !statsStore.completedStories.contains($0.storageKey)
        }
        return (unread.isEmpty ? all : unread).randomElement()
    }

    private func surpriseButton(from all: [CatalogStory]) -> some View {
        Button {
            guard let story = surprisePick(from: all) else { return }
            UIImpactFeedbackGenerator(style: .medium).impactOccurred()
            withAnimation(.easeOut(duration: 0.2)) { path.append(story) }
        } label: {
            HStack(spacing: 5) {
                DoodleIcon(.sparkle, size: 14).jitter(amplitude: 0.4)
                Text("Surprise me")
                    .font(Theme.Fonts.headingMedium(12))
                    .foregroundColor(Theme.Palette.ink)
            }
            .padding(.horizontal, 12)
            .padding(.vertical, 7)
            .overlay(
                WobblyRect(jitter: 0.4, corner: 12, seed: 57)
                    .stroke(Theme.Palette.ink, lineWidth: Theme.Stroke.line)
            )
        }
        .buttonStyle(.plain)
        .accessibilityLabel("Surprise me with a random story")
    }

    private var sortMenu: some View {
        Menu {
            ForEach(StorySort.allCases) { option in
                Button {
                    withAnimation(.easeOut(duration: 0.15)) { sort = option }
                } label: {
                    if sort == option {
                        Label(option.label, systemImage: "checkmark")
                    } else {
                        Text(option.label)
                    }
                }
            }
        } label: {
            HStack(spacing: 5) {
                DoodleIcon(.sortArrows, size: 15)
                Text(sort.label)
                    .font(Theme.Fonts.headingMedium(12))
                    .foregroundColor(Theme.Palette.ink)
            }
            .padding(.horizontal, 12)
            .padding(.vertical, 7)
            .overlay(
                WobblyRect(jitter: 0.4, corner: 12, seed: 63)
                    .stroke(Theme.Palette.ink, lineWidth: Theme.Stroke.line)
            )
        }
        .accessibilityLabel("Sort stories, currently \(sort.label)")
    }

    var body: some View {
        // Compute the derived lists once per render. `allStories` merges
        // personal + bundled behind a Set, `filtered` runs up to four
        // sequential passes, and the pick scorer touches every story — so
        // bind each exactly once instead of re-deriving per read.
        let all = allStories
        let results = sort.apply(filtered(from: all))
        let fresh = all.filter(\.isNewThisWeek).sorted { $0.addedAt > $1.addedAt }
        let pick = tonightPick(from: all)
        return NavigationStack(path: $path) {
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

                        if let pick, searchText.isEmpty {
                            VStack(alignment: .leading, spacing: 14) {
                                SketchSectionHeader("Tonight's Pick",
                                                    trailing: AnyView(surpriseButton(from: all)))
                                NavigationLink(value: pick) {
                                    TonightPickCard(
                                        story: pick,
                                        goal: userModel.goal,
                                        scenesToday: statsStore.todaySceneCount(),
                                        dailyGoal: settings.dailySceneGoal
                                    )
                                }
                                .buttonStyle(.plain)
                                .padding(.horizontal, 24)
                            }
                        }

                        // New this week rail
                        if !fresh.isEmpty && searchText.isEmpty {
                            VStack(alignment: .leading, spacing: 14) {
                                HStack(spacing: 8) {
                                    SketchSectionHeader("New This Week")
                                    Spacer()
                                }
                                ScrollView(.horizontal, showsIndicators: false) {
                                    HStack(spacing: 16) {
                                        ForEach(fresh) { story in
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
                            SketchSectionHeader(results.count == all.count
                                                ? "All Stories · \(results.count)"
                                                : "\(results.count) Matches",
                                                trailing: AnyView(sortMenu))
                            if results.isEmpty {
                                EmptyCatalogState(
                                    message: emptyStateMessage,
                                    onClearFilters: filtersActive ? {
                                        withAnimation(.easeOut(duration: 0.15)) {
                                            genre = .all
                                            ratingFilter = .all
                                            activeCollection = nil
                                            searchText = ""
                                        }
                                    } : nil
                                )
                                .padding(.horizontal, 24)
                            } else {
                                LazyVStack(spacing: 16) {
                                    ForEach(results) { story in
                                        NavigationLink(value: story) {
                                            CatalogRowCard(story: story,
                                                            isFavorite: favoritesStore.isFavorite(story.storageKey))
                                        }
                                        .buttonStyle(.plain)
                                        .contextMenu {
                                            Button {
                                                favoritesStore.toggle(story.storageKey)
                                            } label: {
                                                Label {
                                                    Text(favoritesStore.isFavorite(story.storageKey)
                                                        ? "Remove from Library"
                                                        : "Save to Library")
                                                } icon: {
                                                    DoodleIcon(favoritesStore.isFavorite(story.storageKey)
                                                               ? .heartSlash
                                                               : .heart,
                                                               size: 16)
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
                    .padding(.bottom, 12)
                }
                .scrollDismissesKeyboard(.interactively)
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

// MARK: - Sort order
//
// Reorders the (already filtered) grid. "Featured" preserves the curated
// default order — personal stories first, then the catalog by recency — so
// switching sorts is always reversible back to what the reader saw first.
enum StorySort: String, CaseIterable, Identifiable, Hashable {
    case featured
    case newest
    case topRated
    case shortest
    case aToZ

    var id: String { rawValue }

    var label: String {
        switch self {
        case .featured: return "Featured"
        case .newest:   return "Newest"
        case .topRated: return "Top Rated"
        case .shortest: return "Shortest"
        case .aToZ:     return "A–Z"
        }
    }

    func apply(_ list: [CatalogStory]) -> [CatalogStory] {
        switch self {
        case .featured:
            return list
        case .newest:
            return list.sorted { $0.addedAt > $1.addedAt }
        case .topRated:
            return list.sorted { a, b in
                if a.isLoved != b.isLoved { return a.isLoved && !b.isLoved }
                let ra = a.stars ?? 0, rb = b.stars ?? 0
                if ra != rb { return ra > rb }
                return a.title.localizedCaseInsensitiveCompare(b.title) == .orderedAscending
            }
        case .shortest:
            return list.sorted { a, b in
                if a.estimatedMinutes != b.estimatedMinutes {
                    return a.estimatedMinutes < b.estimatedMinutes
                }
                return a.title.localizedCaseInsensitiveCompare(b.title) == .orderedAscending
            }
        case .aToZ:
            return list.sorted {
                $0.title.localizedCaseInsensitiveCompare($1.title) == .orderedAscending
            }
        }
    }
}

// MARK: - Cards

struct TonightPickCard: View {
    let story: CatalogStory
    let goal: String
    let scenesToday: Int
    let dailyGoal: Int

    private var goalProgress: Double {
        guard dailyGoal > 0 else { return 1 }
        return min(1, Double(scenesToday) / Double(dailyGoal))
    }

    var body: some View {
        SketchCard(fill: Theme.Palette.butterDeep,
                   padding: 0,
                   seed: CGFloat(story.id.stableSeed(100))) {
            VStack(alignment: .leading, spacing: 0) {
                HStack(alignment: .center, spacing: 16) {
                    ZStack {
                        WobblyRect(jitter: 0.4, corner: 8, seed: 62)
                            .fill(Theme.Palette.mist)
                        DoodleIcon(doodleFor(story), size: 64)
                            .jitter(amplitude: 0.3)
                    }
                    .frame(width: 104, height: 116)

                    VStack(alignment: .leading, spacing: 7) {
                        Text(goal.isEmpty ? "CURATED FOR TONIGHT" : "FOR \(goal.uppercased())")
                            .font(Theme.Fonts.meta())
                            .tracking(1)
                            .foregroundColor(Theme.Palette.inkSoft)
                        Text(story.title)
                            .font(Theme.Fonts.cardTitle())
                            .foregroundColor(Theme.Palette.ink)
                            .lineLimit(2)
                        Text("\(story.estimatedMinutes) min · \(story.endingCount) endings")
                            .font(Theme.Fonts.bodyItalic(13))
                            .foregroundColor(Theme.Palette.inkSoft)
                        HStack(spacing: 6) {
                            Text("Open tonight's story")
                                .font(Theme.Fonts.headingMedium(13))
                            DoodleIcon(.arrowRight, size: 14)
                        }
                        .foregroundColor(Theme.Palette.ink)
                    }
                    Spacer(minLength: 0)
                }
                .padding(16)

                SketchDivider()
                    .padding(.horizontal, 16)

                VStack(alignment: .leading, spacing: 7) {
                    HStack {
                        Text("Daily reading goal")
                            .font(Theme.Fonts.headingMedium(12))
                        Spacer()
                        Text("\(min(scenesToday, dailyGoal)) / \(dailyGoal) scenes")
                            .font(Theme.Fonts.bodyItalic(12))
                    }
                    .foregroundColor(Theme.Palette.inkSoft)
                    GeometryReader { geometry in
                        ZStack(alignment: .leading) {
                            Capsule().fill(Theme.Palette.inkHair)
                            Capsule().fill(Theme.Palette.ink)
                                .frame(width: geometry.size.width * goalProgress)
                        }
                    }
                    .frame(height: 7)
                }
                .padding(.horizontal, 16)
                .padding(.vertical, 12)
            }
        }
        .accessibilityElement(children: .combine)
        .accessibilityLabel("Tonight's pick, \(story.title), about \(story.estimatedMinutes) minutes. Daily goal \(scenesToday) of \(dailyGoal) scenes.")
        .accessibilityHint("Opens the story")
    }
}

struct NewPosterCard: View {
    let story: CatalogStory
    var body: some View {
        SketchCard(fill: Theme.Palette.mist, padding: 0, seed: CGFloat(story.id.stableSeed(100))) {
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

    private var sourceLine: String {
        if story.title == story.sourceTitle {
            let year = story.releaseYear.map(String.init) ?? "Interactive story"
            return "\(story.kind.displayName) · \(year) · \(story.estimatedMinutes) min"
        }
        return "Inspired by \(story.sourceTitle) · \(story.estimatedMinutes) min"
    }

    var body: some View {
        SketchCard(fill: Theme.Palette.mist, seed: CGFloat(story.id.stableSeed(100))) {
            HStack(alignment: .top, spacing: 14) {
                ZStack {
                    Theme.Palette.butter
                    DoodleIcon(doodleFor(story), size: 54)
                }
                .frame(width: 80, height: 100)
                .overlay(
                    WobblyRect(jitter: 0.3, corner: 4,
                               seed: CGFloat(story.id.stableSeed(50)))
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
                    Text(sourceLine)
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
    var message: String = "Try another genre, or pull down to refresh."
    /// When the empty result is caused by active filters, callers pass a
    /// reset action so the user can recover in one tap.
    var onClearFilters: (() -> Void)? = nil

    var body: some View {
        VStack(spacing: 14) {
            DoodleIcon(.popcorn, size: 88)
                .jitter(amplitude: 0.4)
            Text("Nothing here yet")
                .font(Theme.Fonts.cardTitle())
                .foregroundColor(Theme.Palette.ink)
            Text(message)
                .font(Theme.Fonts.body(14))
                .foregroundColor(Theme.Palette.inkSoft)
                .multilineTextAlignment(.center)
            if let onClearFilters {
                SketchButton(title: "Clear filters",
                             doodle: .undo,
                             style: .secondary,
                             fullWidth: false) {
                    onClearFilters()
                }
                .padding(.top, 4)
            }
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
