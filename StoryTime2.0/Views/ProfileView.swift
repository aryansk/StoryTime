import SwiftUI

// MARK: - Profile tab
//
// User identity + stats + legal pages. Stats live here rather than in
// Settings because they belong to the storyteller, not to app configuration.

struct ProfileView: View {
    @ObservedObject var userModel: UserModel
    @ObservedObject var settings: SettingsModel
    @EnvironmentObject var statsStore: StatsStore
    @EnvironmentObject var progressStore: ReadingProgressStore
    @EnvironmentObject var favoritesStore: FavoritesStore
    @EnvironmentObject var choiceDNA: ChoiceDNAStore
    @EnvironmentObject var endingsTracker: EndingsTracker

    @State private var editingName: Bool = false
    @State private var nameDraft: String = ""

    var appVersion: String {
        let v = Bundle.main.infoDictionary?["CFBundleShortVersionString"] as? String ?? "1.0"
        let b = Bundle.main.infoDictionary?["CFBundleVersion"] as? String ?? "1"
        return "v\(v) (\(b))"
    }

    var body: some View {
        NavigationStack {
            ZStack {
                PageBackground()

                ScrollView(showsIndicators: false) {
                    VStack(alignment: .leading, spacing: 26) {
                        // Title
                        VStack(alignment: .leading, spacing: 6) {
                            Text("Your")
                                .font(Theme.Fonts.body(20))
                                .foregroundColor(Theme.Palette.inkSoft)
                            HStack(alignment: .bottom, spacing: 8) {
                                Text("Profile")
                                    .font(Theme.Fonts.display())
                                    .foregroundColor(Theme.Palette.ink)
                                DoodleIcon(.person, size: 36)
                                    .jitter(amplitude: 0.4)
                                Spacer()
                            }
                        }
                        .padding(.horizontal, 24)
                        .padding(.top, 16)

                        identityCard
                            .padding(.horizontal, 24)

                        tasteBlock
                            .padding(.horizontal, 24)

                        readingGoalBlock
                            .padding(.horizontal, 24)

                        statsBlock
                            .padding(.horizontal, 24)

                        achievementsBlock

                        dnaBlock
                            .padding(.horizontal, 24)

                        legalBlock
                            .padding(.horizontal, 24)

                        aboutBlock
                            .padding(.horizontal, 24)

                        Spacer(minLength: 40)
                    }
                }
            }
            .navigationBarHidden(true)
        }
    }

    // MARK: Identity

    private var identityCard: some View {
        SketchCard(fill: Theme.Palette.mist, seed: 21.0) {
            HStack(alignment: .center, spacing: 16) {
                ZStack {
                    WobblyRect(jitter: 0.5, corner: 36, seed: 77)
                        .fill(Theme.Palette.butter)
                        .frame(width: 72, height: 72)
                    WobblyRect(jitter: 0.5, corner: 36, seed: 77)
                        .stroke(Theme.Palette.ink, lineWidth: Theme.Stroke.bold)
                        .frame(width: 72, height: 72)
                    DoodleIcon(.person, size: 42)
                        .jitter(amplitude: 0.3)
                }

                VStack(alignment: .leading, spacing: 6) {
                    if editingName {
                        SketchTextField(placeholder: "Your name", text: $nameDraft)
                        HStack(spacing: 8) {
                            SketchButton(title: "Save", style: .primary, fullWidth: false) {
                                let trimmed = nameDraft.trimmingCharacters(in: .whitespaces)
                                if !trimmed.isEmpty { userModel.username = trimmed }
                                editingName = false
                            }
                            SketchButton(title: "Cancel", style: .ghost, fullWidth: false) {
                                editingName = false
                            }
                        }
                    } else {
                        Text(userModel.username.isEmpty ? "Storyteller" : userModel.username)
                            .font(Theme.Fonts.cardTitle())
                            .foregroundColor(Theme.Palette.ink)
                        Text(userModel.greeting)
                            .font(Theme.Fonts.bodyItalic(13))
                            .foregroundColor(Theme.Palette.inkSoft)
                        Button {
                            nameDraft = userModel.username
                            editingName = true
                        } label: {
                            HStack(spacing: 4) {
                                Text("Edit name")
                                    .font(Theme.Fonts.headingMedium(12))
                                DoodleIcon(.chevronRightSmall, size: 12, color: Theme.Palette.ink)
                            }
                            .foregroundColor(Theme.Palette.ink)
                            .padding(.top, 2)
                        }
                        .buttonStyle(.plain)
                    }
                }
                Spacer()
            }
        }
    }

    // MARK: Taste (onboarding answers, editable in place)
    //
    // The genres and mood picked during onboarding shape "Tonight's Pick".
    // Surfacing them here keeps that quiz from being a one-way chute — the
    // user can retune recommendations anytime without redoing onboarding.

    private var tasteBlock: some View {
        VStack(alignment: .leading, spacing: 14) {
            SketchSectionHeader("Your Taste", horizontalInset: 0)
            SketchCard(seed: 27.0) {
                VStack(alignment: .leading, spacing: 14) {
                    VStack(alignment: .leading, spacing: 8) {
                        Text("GENRES YOU LOVE")
                            .font(Theme.Fonts.meta())
                            .tracking(1)
                            .foregroundColor(Theme.Palette.inkSoft)
                        LazyVGrid(columns: [GridItem(.adaptive(minimum: 96), spacing: 8)],
                                  alignment: .leading, spacing: 8) {
                            ForEach(StoryGenre.allCases.filter { $0 != .all }) { genre in
                                SketchPill(title: genre.rawValue,
                                           selected: userModel.favoriteGenres.contains(genre.rawValue)) {
                                    toggleFavoriteGenre(genre.rawValue)
                                }
                            }
                        }
                    }

                    SketchDivider()

                    VStack(alignment: .leading, spacing: 8) {
                        Text("READING MOOD")
                            .font(Theme.Fonts.meta())
                            .tracking(1)
                            .foregroundColor(Theme.Palette.inkSoft)
                        LazyVGrid(columns: [GridItem(.adaptive(minimum: 108), spacing: 8)],
                                  alignment: .leading, spacing: 8) {
                            ForEach(["Unwind", "Get Hooked", "Roleplay", "Bedtime"], id: \.self) { goal in
                                SketchPill(title: goal,
                                           selected: userModel.goal == goal) {
                                    userModel.goal = (userModel.goal == goal) ? "" : goal
                                }
                            }
                        }
                    }

                    Text("Tonight's Pick on the Discover tab is tuned by these.")
                        .font(Theme.Fonts.bodyItalic(12))
                        .foregroundColor(Theme.Palette.inkSoft)
                }
            }
        }
    }

    private func toggleFavoriteGenre(_ genre: String) {
        if let idx = userModel.favoriteGenres.firstIndex(of: genre) {
            userModel.favoriteGenres.remove(at: idx)
        } else {
            userModel.favoriteGenres.append(genre)
        }
    }

    // MARK: Stats

    private var readingGoalBlock: some View {
        let read = statsStore.todaySceneCount()
        let goal = max(1, settings.dailySceneGoal)
        let fraction = min(1, Double(read) / Double(goal))
        return VStack(alignment: .leading, spacing: 14) {
            SketchSectionHeader("Today's Reading", horizontalInset: 0)
            SketchCard(fill: Theme.Palette.butterDeep, seed: 29) {
                VStack(alignment: .leading, spacing: 12) {
                    HStack(spacing: 12) {
                        DoodleIcon(fraction >= 1 ? .starFill : .flame,
                                   size: 28,
                                   filled: fraction >= 1)
                        VStack(alignment: .leading, spacing: 3) {
                            Text(fraction >= 1 ? "Goal complete" : "Keep the story moving")
                                .font(Theme.Fonts.cardTitle())
                                .foregroundColor(Theme.Palette.ink)
                            Text(fraction >= 1
                                 ? "You made time for a story today."
                                 : "\(read) of \(goal) scenes read")
                                .font(Theme.Fonts.bodyItalic(13))
                                .foregroundColor(Theme.Palette.inkSoft)
                        }
                        Spacer()
                        Text("\(Int(fraction * 100))%")
                            .font(Theme.Fonts.heading(22))
                            .foregroundColor(Theme.Palette.ink)
                    }
                    GeometryReader { geometry in
                        ZStack(alignment: .leading) {
                            Capsule().fill(Theme.Palette.inkHair)
                            Capsule().fill(Theme.Palette.ink)
                                .frame(width: geometry.size.width * fraction)
                        }
                    }
                    .frame(height: 8)
                }
            }
        }
    }

    private var statsBlock: some View {
        VStack(alignment: .leading, spacing: 14) {
            SketchSectionHeader("Your Stats", horizontalInset: 0)
            HStack(spacing: 12) {
                ProfileStatTile(doodle: .flame,
                                value: "\(statsStore.currentStreak)",
                                label: "Day streak")
                ProfileStatTile(doodle: .books,
                                value: "\(statsStore.completedStories.count)",
                                label: "Completed")
            }
            HStack(spacing: 12) {
                ProfileStatTile(doodle: .stack,
                                value: "\(statsStore.scenesRead)",
                                label: "Scenes read")
                ProfileStatTile(doodle: .branch,
                                value: "\(statsStore.choicesMade)",
                                label: "Choices made")
            }
            HStack(spacing: 12) {
                ProfileStatTile(doodle: .clock,
                                value: "\(statsStore.readingMinutes)",
                                label: "Minutes read")
                ProfileStatTile(doodle: .heartFill,
                                value: "\(favoritesStore.favoriteTitles.count)",
                                label: "Saved")
            }
        }
    }

    // MARK: Achievements

    private struct Achievement: Identifiable {
        let id: String
        let title: String
        let subtitle: String
        let doodle: DoodleName
        let unlocked: Bool
    }

    private struct AchievementCard: View {
        let achievement: Achievement

        var body: some View {
            SketchCard(fill: achievement.unlocked ? Theme.Palette.butterDeep : Theme.Palette.mist,
                       padding: 14,
                       seed: CGFloat(achievement.id.stableSeed(100))) {
                VStack(alignment: .leading, spacing: 8) {
                    HStack {
                        DoodleIcon(achievement.doodle,
                                   size: 25,
                                   filled: achievement.unlocked)
                        Spacer()
                        if achievement.unlocked {
                            DoodleIcon(.checkmark, size: 15)
                        } else {
                            SketchBadge(text: "Locked")
                        }
                    }
                    Text(achievement.title)
                        .font(Theme.Fonts.cardTitle())
                        .foregroundColor(Theme.Palette.ink)
                    Text(achievement.subtitle)
                        .font(Theme.Fonts.bodyItalic(12))
                        .foregroundColor(Theme.Palette.inkSoft)
                        .lineLimit(2)
                }
                .frame(width: 145, alignment: .leading)
                .opacity(achievement.unlocked ? 1 : 0.62)
            }
            .accessibilityElement(children: .combine)
            .accessibilityLabel("\(achievement.title), \(achievement.unlocked ? "unlocked" : "locked"). \(achievement.subtitle)")
        }
    }

    private var achievements: [Achievement] {
        let endingsFound = endingsTracker.discovered.values.reduce(0) { $0 + $1.count }
        return [
            Achievement(id: "first-step", title: "First Step", subtitle: "Start a story",
                        doodle: .books, unlocked: !statsStore.storiesStarted.isEmpty),
            Achievement(id: "the-end", title: "The End", subtitle: "Finish a story",
                        doodle: .starFill, unlocked: !statsStore.completedStories.isEmpty),
            Achievement(id: "branching", title: "Pathfinder", subtitle: "Make 25 choices",
                        doodle: .branch, unlocked: statsStore.choicesMade >= 25),
            Achievement(id: "collector", title: "Collector", subtitle: "Find 5 endings",
                        doodle: .stack, unlocked: endingsFound >= 5),
            Achievement(id: "streak", title: "In Rhythm", subtitle: "Read 3 days running",
                        doodle: .flame, unlocked: statsStore.currentStreak >= 3),
            Achievement(id: "shelf", title: "Full Shelf", subtitle: "Save 5 stories",
                        doodle: .heartFill, unlocked: favoritesStore.favoriteTitles.count >= 5),
        ]
    }

    private var achievementsBlock: some View {
        VStack(alignment: .leading, spacing: 14) {
            SketchSectionHeader("Achievements")
            ScrollView(.horizontal, showsIndicators: false) {
                HStack(spacing: 12) {
                    ForEach(achievements) { achievement in
                        AchievementCard(achievement: achievement)
                    }
                }
                .padding(.horizontal, 24)
                .padding(.vertical, 2)
            }
        }
    }

    // MARK: Choice DNA

    private var dnaBlock: some View {
        VStack(alignment: .leading, spacing: 14) {
            SketchSectionHeader("Your Choice DNA", horizontalInset: 0)
            SketchCard(seed: 31.0) {
                if choiceDNA.ranked.isEmpty {
                    VStack(alignment: .leading, spacing: 8) {
                        HStack(spacing: 8) {
                            DoodleIcon(.branch, size: 18)
                            Text("Make a few choices first")
                                .font(Theme.Fonts.cardTitle())
                                .foregroundColor(Theme.Palette.ink)
                        }
                        Text("As you play, your choices add up to a quiet personality reading.")
                            .font(Theme.Fonts.bodyItalic(14))
                            .foregroundColor(Theme.Palette.inkSoft)
                            .lineSpacing(3)
                    }
                } else {
                    VStack(alignment: .leading, spacing: 12) {
                        HStack(spacing: 8) {
                            DoodleIcon(.branch, size: 18)
                            Text(dnaHeadline)
                                .font(Theme.Fonts.cardTitle())
                                .foregroundColor(Theme.Palette.ink)
                            Spacer()
                        }
                        ForEach(choiceDNA.ranked.prefix(5), id: \.trait) { row in
                            dnaRow(trait: row.trait,
                                   percent: choiceDNA.percent(for: row.trait))
                        }
                        Text("Based on \(choiceDNA.totalChoices) tracked choices.")
                            .font(Theme.Fonts.bodyItalic(12))
                            .foregroundColor(Theme.Palette.inkSoft)
                            .padding(.top, 2)
                    }
                }
            }
        }
    }

    private var dnaHeadline: String {
        guard let top = choiceDNA.ranked.first else { return "Mostly Quiet" }
        return "Mostly \(top.trait.rawValue)"
    }

    private func dnaRow(trait: ChoiceTrait, percent: Int) -> some View {
        VStack(alignment: .leading, spacing: 4) {
            HStack {
                Text(trait.rawValue)
                    .font(Theme.Fonts.label())
                    .tracking(0.8)
                    .foregroundColor(Theme.Palette.ink)
                Spacer()
                Text("\(percent)%")
                    .font(Theme.Fonts.headingMedium(13))
                    .foregroundColor(Theme.Palette.inkSoft)
            }
            ZStack(alignment: .leading) {
                WobblyRect(jitter: 0.3, corner: 4,
                            seed: CGFloat(trait.rawValue.stableSeed(30)))
                    .fill(Theme.Palette.mist)
                    .frame(height: 10)
                WobblyRect(jitter: 0.3, corner: 4,
                            seed: CGFloat(trait.rawValue.stableSeed(30)))
                    .fill(Theme.Palette.ink)
                    .frame(width: max(6, CGFloat(percent) * 2.4), height: 10)
            }
            Text(trait.blurb)
                .font(Theme.Fonts.bodyItalic(12))
                .foregroundColor(Theme.Palette.inkSoft)
        }
    }

    // MARK: Legal

    private var legalBlock: some View {
        VStack(alignment: .leading, spacing: 14) {
            SketchSectionHeader("Legal", horizontalInset: 0)
            SketchCard(padding: 4, seed: 22.0) {
                VStack(spacing: 0) {
                    NavigationLink(destination: PrivacyPolicyView()) {
                        ProfileRow(doodle: .shield, title: "Privacy Policy",
                                   subtitle: "What we collect, what we don't")
                    }
                    SketchDivider()
                        .padding(.horizontal, 14)
                    NavigationLink(destination: TermsOfServiceView()) {
                        ProfileRow(doodle: .scroll, title: "Terms of Service",
                                   subtitle: "The deal between you and us")
                    }
                    SketchDivider()
                        .padding(.horizontal, 14)
                    NavigationLink(destination: AcknowledgementsView()) {
                        ProfileRow(doodle: .sparkle, title: "Acknowledgements",
                                   subtitle: "Fonts, tools, thanks")
                    }
                }
            }
        }
    }

    // MARK: About

    private var aboutBlock: some View {
        VStack(alignment: .leading, spacing: 14) {
            SketchSectionHeader("About", horizontalInset: 0)
            SketchCard(seed: 23.0) {
                VStack(alignment: .leading, spacing: 6) {
                    HStack(spacing: 8) {
                        DoodleIcon(.sparkle, size: 18)
                        Text("StoryTime")
                            .font(Theme.Fonts.cardTitle())
                            .foregroundColor(Theme.Palette.ink)
                        Spacer()
                        Text(appVersion)
                            .font(Theme.Fonts.bodyItalic(12))
                            .foregroundColor(Theme.Palette.inkSoft)
                    }
                    Text("Choose-your-own-adventure stories after the latest movies and shows. Hand-authored, refreshed weekly.")
                        .font(Theme.Fonts.bodyItalic(13))
                        .foregroundColor(Theme.Palette.inkSoft)
                        .lineSpacing(3)
                }
            }
        }
    }
}

// MARK: - Stat tile

private struct ProfileStatTile: View {
    let doodle: DoodleName
    let value: String
    let label: String

    var body: some View {
        SketchCard(fill: Theme.Palette.mist, padding: 14, seed: CGFloat(label.stableSeed(100))) {
            VStack(alignment: .leading, spacing: 8) {
                DoodleIcon(doodle, size: 22)
                Text(value)
                    .font(Theme.Fonts.heading(24))
                    .foregroundColor(Theme.Palette.ink)
                Text(label)
                    .font(Theme.Fonts.body(12))
                    .foregroundColor(Theme.Palette.inkSoft)
            }
            .frame(maxWidth: .infinity, alignment: .leading)
        }
    }
}

// MARK: - Row used by Legal block

private struct ProfileRow: View {
    let doodle: DoodleName
    let title: String
    let subtitle: String

    var body: some View {
        HStack(spacing: 14) {
            DoodleIcon(doodle, size: 22)
                .frame(width: 28)
            VStack(alignment: .leading, spacing: 2) {
                Text(title)
                    .font(Theme.Fonts.headingMedium(15))
                    .foregroundColor(Theme.Palette.ink)
                Text(subtitle)
                    .font(Theme.Fonts.bodyItalic(12))
                    .foregroundColor(Theme.Palette.inkSoft)
            }
            Spacer()
            DoodleIcon(.chevronRightSmall, size: 14, color: Theme.Palette.inkSoft)
        }
        .padding(.horizontal, 14)
        .padding(.vertical, 14)
        .contentShape(Rectangle())
    }
}
