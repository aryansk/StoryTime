import SwiftUI

// MARK: - Onboarding
//
// A first-run flow modeled on the strongest consumer onboarding out there
// (Duolingo, Headspace, Blinkist):
//   1. Hook    — one emotional promise, honest social proof, instant skip.
//   2. Taste   — pick the genres you love; the answer visibly shapes step 5.
//   3. Goal    — single-tap question that auto-advances (no dead
//   4. Pace      "Continue" taps), with copy that says *why* we ask.
//   5. Name    — optional, never blocks progress.
//   6. Payoff  — three personalized picks pulled live from the catalog;
//                one tap drops you straight into a story, so time-to-first-
//                story stays under a minute.
//
// Every step can go back: answers are editable, not a one-way chute.

struct OnboardingView: View {
    @ObservedObject var userModel: UserModel
    @ObservedObject var catalog: CatalogService
    /// Called exactly once when the flow finishes. Non-nil when the user
    /// tapped one of their personalized picks and should land in that story.
    var onFinish: (CatalogStory?) -> Void

    @State private var step = 0
    @State private var goingBack = false
    /// Guards the auto-advance on single-select steps so a fast double tap
    /// can't skip two screens.
    @State private var advancing = false

    @State private var name = ""
    @State private var selectedGenres: Set<String> = []
    @State private var selectedGoal = ""
    @State private var selectedPace = ""

    private static let quizStepCount = 4   // taste, goal, pace, name

    private static let goalOptions: [QuizOption] = [
        QuizOption(title: "Unwind",
                   subtitle: "Cozy comedies, low-stakes drama.",
                   doodle: .popcorn),
        QuizOption(title: "Get Hooked",
                   subtitle: "Thrillers with teeth. One more scene.",
                   doodle: .flame),
        QuizOption(title: "Roleplay",
                   subtitle: "Be the hero — fantasy, action, sci-fi.",
                   doodle: .sparkle),
        QuizOption(title: "Bedtime",
                   subtitle: "Short, calm stories that end well.",
                   doodle: .clock)
    ]

    private static let paceOptions: [QuizOption] = [
        QuizOption(title: "Casual",
                   subtitle: "A quick story now and then.",
                   doodle: .play),
        QuizOption(title: "Devoted",
                   subtitle: "A story most nights.",
                   doodle: .books),
        QuizOption(title: "Obsessed",
                   subtitle: "Every ending. Every saga. All of it.",
                   doodle: .stack)
    ]

    private static let tasteGenres: [(genre: StoryGenre, doodle: DoodleName)] = [
        (.drama, .tv), (.comedy, .popcorn), (.thriller, .clapperboard),
        (.sciFi, .sparkle), (.horror, .flame), (.fantasy, .scroll),
        (.action, .play)
    ]

    var body: some View {
        ZStack {
            PageBackground()

            VStack(spacing: 0) {
                if (1...Self.quizStepCount).contains(step) {
                    header
                        .padding(.horizontal, 20)
                        .padding(.top, 16)
                }

                Spacer(minLength: 12)

                Group {
                    switch step {
                    case 0:
                        WelcomeStep(storyCount: catalog.stories.count,
                                    onContinue: advance,
                                    onSkip: { complete() })
                    case 1:
                        TasteStep(genres: Self.tasteGenres,
                                  selection: $selectedGenres,
                                  onContinue: advance)
                    case 2:
                        OptionListStep(title: "What brings you here?",
                                       subtitle: "This tunes tonight's pick — you can change it anytime.",
                                       options: Self.goalOptions,
                                       selection: $selectedGoal,
                                       onSelect: autoAdvance)
                    case 3:
                        OptionListStep(title: "How deep do you go?",
                                       subtitle: "So we know whether to hand you one-shots or whole sagas.",
                                       options: Self.paceOptions,
                                       selection: $selectedPace,
                                       onSelect: autoAdvance)
                    case 4:
                        NameStep(name: $name, onContinue: advance)
                    case 5:
                        PayoffStep(name: displayName,
                                   picks: personalizedPicks,
                                   onStart: { complete(startWith: $0) },
                                   onBrowse: { complete() })
                    default:
                        EmptyView()
                    }
                }
                .transition(.asymmetric(
                    insertion: .move(edge: goingBack ? .leading : .trailing).combined(with: .opacity),
                    removal:   .move(edge: goingBack ? .trailing : .leading).combined(with: .opacity)
                ))

                Spacer(minLength: 12)
            }
        }
    }

    // MARK: Header (back + progress)

    private var header: some View {
        VStack(spacing: 8) {
            HStack(spacing: 12) {
                DoodleButton(doodle: .chevronLeft, size: 18, label: "Back") {
                    back()
                }
                HStack(spacing: 6) {
                    ForEach(0..<Self.quizStepCount, id: \.self) { idx in
                        WobblyRect(jitter: 0.4, corner: 3, seed: CGFloat(idx))
                            .fill(idx < step ? Theme.Palette.ink : Theme.Palette.inkHair)
                            .frame(height: 5)
                            .animation(.easeOut(duration: 0.25), value: step)
                    }
                }
                // Balances the back button so the bar stays centered.
                Color.clear.frame(width: 44, height: 44)
            }
            Text("Step \(min(Self.quizStepCount, step)) of \(Self.quizStepCount)")
                .font(Theme.Fonts.meta())
                .foregroundColor(Theme.Palette.inkSoft)
        }
    }

    // MARK: Navigation

    private func advance() {
        goingBack = false
        advancing = false
        withAnimation(.easeOut(duration: 0.25)) { step += 1 }
    }

    private func back() {
        guard step > 0 else { return }
        goingBack = true
        advancing = false
        withAnimation(.easeOut(duration: 0.25)) { step -= 1 }
    }

    /// Single-select steps advance on their own after a beat, so picking an
    /// answer never needs a second "Continue" tap (the Duolingo trick).
    private func autoAdvance() {
        guard !advancing else { return }
        advancing = true
        DispatchQueue.main.asyncAfter(deadline: .now() + 0.35) {
            if advancing { advance() }
        }
    }

    // MARK: Completion

    private var displayName: String {
        name.trimmingCharacters(in: .whitespacesAndNewlines)
    }

    private func complete(startWith story: CatalogStory? = nil) {
        userModel.username = displayName.isEmpty ? "Storyteller" : displayName
        userModel.favoriteGenres = Self.tasteGenres
            .map(\.genre.rawValue)
            .filter { selectedGenres.contains($0) }
        userModel.goal = selectedGoal
        userModel.experienceLevel = selectedPace
        userModel.onboardingCompleted = true
        onFinish(story)
    }

    // MARK: Personalized picks (the payoff)

    /// Top three stories for *this* user's answers. Favors their genres,
    /// their goal, and short + highly-rated stories that make a friendly
    /// first play.
    private var personalizedPicks: [CatalogStory] {
        catalog.stories
            .map { (story: $0, score: firstStoryScore($0)) }
            .sorted { $0.score > $1.score }
            .prefix(3)
            .map(\.story)
    }

    private func firstStoryScore(_ story: CatalogStory) -> Int {
        var score = (story.stars ?? 3) * 4 + (story.isLoved ? 8 : 0)
        if selectedGenres.contains(story.genre.rawValue) { score += 16 }

        switch selectedGoal {
        case "Unwind":
            if [.comedy, .drama].contains(story.genre) { score += 10 }
        case "Get Hooked":
            if [.thriller, .horror].contains(story.genre) { score += 10 }
        case "Roleplay":
            if [.fantasy, .action, .sciFi].contains(story.genre) { score += 10 }
        case "Bedtime":
            if story.tags.contains("mini") { score += 12 }
        default:
            break
        }

        switch selectedPace {
        case "Casual":
            if story.estimatedMinutes <= 8 { score += 6 }
        case "Obsessed":
            if story.nextStoryId != nil || story.endingCount >= 4 { score += 6 }
        default:
            break
        }

        // A short, self-contained story is the friendliest first play.
        if story.estimatedMinutes <= 10 { score += 5 }
        return score
    }
}

// MARK: - Quiz option model

private struct QuizOption: Identifiable {
    let title: String
    let subtitle: String
    let doodle: DoodleName
    var id: String { title }
}

// MARK: - Steps

private struct WelcomeStep: View {
    let storyCount: Int
    let onContinue: () -> Void
    let onSkip: () -> Void

    var body: some View {
        VStack(spacing: 32) {
            VStack(spacing: 18) {
                DoodleIcon(.clapperboard, size: 96)
                    .jitter(amplitude: 0.4)
                Text("StoryTime")
                    .font(Theme.Fonts.display())
                    .foregroundColor(Theme.Palette.ink)
            }

            VStack(spacing: 12) {
                Text("What would you have done in your favorite movie?")
                    .font(Theme.Fonts.title())
                    .foregroundColor(Theme.Palette.ink)
                    .multilineTextAlignment(.center)
                    .padding(.horizontal, 24)
                Text("\(max(storyCount, 100))+ hand-authored stories from the movies, shows, and books everyone has opinions about. Every choice is yours.")
                    .font(Theme.Fonts.body(15))
                    .foregroundColor(Theme.Palette.inkSoft)
                    .multilineTextAlignment(.center)
                    .padding(.horizontal, 32)
                    .lineSpacing(4)
            }

            VStack(spacing: 12) {
                SketchButton(title: "Begin", trailingDoodle: .arrowRight, action: onContinue)
                Text("4 quick questions · about 30 seconds")
                    .font(Theme.Fonts.meta())
                    .foregroundColor(Theme.Palette.inkSoft)
                Button(action: onSkip) {
                    Text("Skip — take me straight in")
                        .font(Theme.Fonts.headingMedium(13))
                        .foregroundColor(Theme.Palette.inkSoft)
                        .frame(minHeight: 44)
                }
            }
            .padding(.horizontal, 40)
        }
    }
}

private struct TasteStep: View {
    let genres: [(genre: StoryGenre, doodle: DoodleName)]
    @Binding var selection: Set<String>
    let onContinue: () -> Void

    private let columns = [GridItem(.flexible(), spacing: 12),
                           GridItem(.flexible(), spacing: 12)]

    var body: some View {
        VStack(spacing: 26) {
            VStack(spacing: 8) {
                Text("What do you love?")
                    .font(Theme.Fonts.title())
                    .foregroundColor(Theme.Palette.ink)
                    .multilineTextAlignment(.center)
                Text("Pick as many as you like. Your shelf is built from these.")
                    .font(Theme.Fonts.body(14))
                    .foregroundColor(Theme.Palette.inkSoft)
                    .multilineTextAlignment(.center)
                    .padding(.horizontal, 32)
            }

            LazyVGrid(columns: columns, spacing: 12) {
                ForEach(genres, id: \.genre) { item in
                    GenreChip(title: item.genre.rawValue,
                              doodle: item.doodle,
                              selected: selection.contains(item.genre.rawValue)) {
                        UISelectionFeedbackGenerator().selectionChanged()
                        if selection.contains(item.genre.rawValue) {
                            selection.remove(item.genre.rawValue)
                        } else {
                            selection.insert(item.genre.rawValue)
                        }
                    }
                }
            }
            .padding(.horizontal, 32)

            SketchButton(title: selection.isEmpty ? "Pick at least one" : "Build my shelf",
                         trailingDoodle: .arrowRight,
                         action: onContinue)
                .padding(.horizontal, 40)
                .opacity(selection.isEmpty ? 0.5 : 1)
                .disabled(selection.isEmpty)
        }
    }
}

private struct GenreChip: View {
    let title: String
    let doodle: DoodleName
    let selected: Bool
    let action: () -> Void

    var body: some View {
        Button(action: action) {
            HStack(spacing: 8) {
                DoodleIcon(doodle, size: 18)
                Text(title)
                    .font(Theme.Fonts.headingMedium(14))
                    .foregroundColor(Theme.Palette.ink)
                Spacer(minLength: 0)
                if selected {
                    DoodleIcon(.checkmark, size: 14)
                }
            }
            .padding(.horizontal, 14)
            .padding(.vertical, 13)
            .frame(minHeight: 48)
            .background(
                WobblyRect(jitter: 0.4, corner: 8, seed: CGFloat(title.stableSeed(100)))
                    .fill(selected ? Theme.Palette.butterDeep : Color.clear)
            )
            .overlay(
                WobblyRect(jitter: 0.4, corner: 8, seed: CGFloat(title.stableSeed(100)))
                    .stroke(Theme.Palette.ink,
                            lineWidth: selected ? Theme.Stroke.bold : Theme.Stroke.line)
            )
        }
        .buttonStyle(.plain)
        .accessibilityLabel(title)
        .accessibilityAddTraits(selected ? [.isButton, .isSelected] : .isButton)
    }
}

private struct OptionListStep: View {
    let title: String
    let subtitle: String
    let options: [QuizOption]
    @Binding var selection: String
    /// Fires after a fresh choice so the parent can auto-advance.
    let onSelect: () -> Void

    var body: some View {
        VStack(spacing: 26) {
            VStack(spacing: 8) {
                Text(title)
                    .font(Theme.Fonts.title())
                    .foregroundColor(Theme.Palette.ink)
                    .multilineTextAlignment(.center)
                Text(subtitle)
                    .font(Theme.Fonts.body(14))
                    .foregroundColor(Theme.Palette.inkSoft)
                    .multilineTextAlignment(.center)
                    .padding(.horizontal, 32)
            }
            VStack(spacing: 10) {
                ForEach(options) { opt in
                    Button {
                        UISelectionFeedbackGenerator().selectionChanged()
                        selection = opt.title
                        onSelect()
                    } label: {
                        HStack(spacing: 14) {
                            DoodleIcon(opt.doodle, size: 26)
                            VStack(alignment: .leading, spacing: 3) {
                                Text(opt.title)
                                    .font(Theme.Fonts.headingMedium(15))
                                    .foregroundColor(Theme.Palette.ink)
                                Text(opt.subtitle)
                                    .font(Theme.Fonts.bodyItalic(13))
                                    .foregroundColor(Theme.Palette.inkSoft)
                            }
                            Spacer()
                            if selection == opt.title {
                                DoodleIcon(.checkmark, size: 18)
                            }
                        }
                        .padding(.horizontal, 18)
                        .padding(.vertical, 13)
                        .background(
                            WobblyRect(jitter: 0.4, corner: 6, seed: CGFloat(opt.title.stableSeed(100)))
                                .fill(selection == opt.title ? Theme.Palette.butterDeep : Color.clear)
                        )
                        .overlay(
                            WobblyRect(jitter: 0.4, corner: 6, seed: CGFloat(opt.title.stableSeed(100)))
                                .stroke(Theme.Palette.ink,
                                        lineWidth: selection == opt.title ? Theme.Stroke.bold : Theme.Stroke.line)
                        )
                    }
                    .buttonStyle(.plain)
                    .accessibilityLabel("\(opt.title). \(opt.subtitle)")
                    .accessibilityAddTraits(selection == opt.title ? [.isButton, .isSelected] : .isButton)
                }
            }
            .padding(.horizontal, 40)
        }
    }
}

private struct NameStep: View {
    @Binding var name: String
    let onContinue: () -> Void

    var body: some View {
        VStack(spacing: 28) {
            VStack(spacing: 10) {
                Text("What should we call you?")
                    .font(Theme.Fonts.title())
                    .foregroundColor(Theme.Palette.ink)
                    .multilineTextAlignment(.center)
                Text("So the stories can address the storyteller by name.")
                    .font(Theme.Fonts.body(14))
                    .foregroundColor(Theme.Palette.inkSoft)
            }
            SketchTextField(placeholder: "Your name", text: $name)
                .padding(.horizontal, 40)
                .submitLabel(.done)
                .onSubmit(onContinue)
            VStack(spacing: 12) {
                SketchButton(title: "Continue", trailingDoodle: .arrowRight, action: onContinue)
                Button(action: onContinue) {
                    Text("Maybe later")
                        .font(Theme.Fonts.headingMedium(13))
                        .foregroundColor(Theme.Palette.inkSoft)
                        .frame(minHeight: 44)
                }
            }
            .padding(.horizontal, 40)
        }
    }
}

private struct PayoffStep: View {
    let name: String
    let picks: [CatalogStory]
    let onStart: (CatalogStory) -> Void
    let onBrowse: () -> Void

    var body: some View {
        ScrollView(showsIndicators: false) {
            VStack(spacing: 24) {
                VStack(spacing: 12) {
                    DoodleIcon(.sparkle, size: 72)
                        .jitter(amplitude: 0.5)
                    Text(name.isEmpty ? "Your shelf is ready." : "Your shelf is ready, \(name).")
                        .font(Theme.Fonts.title())
                        .foregroundColor(Theme.Palette.ink)
                        .multilineTextAlignment(.center)
                        .padding(.horizontal, 24)
                    Text(picks.isEmpty
                         ? "The catalog is warming up — head in and look around."
                         : "Three picks tuned to your answers. Tap one to start reading right now.")
                        .font(Theme.Fonts.body(14))
                        .foregroundColor(Theme.Palette.inkSoft)
                        .multilineTextAlignment(.center)
                        .padding(.horizontal, 32)
                }

                if !picks.isEmpty {
                    VStack(spacing: 12) {
                        ForEach(picks) { story in
                            Button {
                                onStart(story)
                            } label: {
                                PickCard(story: story)
                            }
                            .buttonStyle(SketchPressStyle())
                        }
                    }
                    .padding(.horizontal, 32)
                }

                SketchButton(title: picks.isEmpty ? "Enter the catalog" : "Browse everything instead",
                             trailingDoodle: .arrowRight,
                             style: picks.isEmpty ? .primary : .ghost,
                             action: onBrowse)
                    .padding(.horizontal, 40)
            }
            .padding(.vertical, 8)
        }
    }
}

private struct PickCard: View {
    let story: CatalogStory

    var body: some View {
        HStack(spacing: 14) {
            ZStack {
                WobblyRect(jitter: 0.4, corner: 8,
                           seed: CGFloat(story.id.stableSeed(50)))
                    .fill(Theme.Palette.butter)
                DoodleIcon(doodleFor(story), size: 36)
            }
            .frame(width: 62, height: 72)

            VStack(alignment: .leading, spacing: 5) {
                Text(story.title)
                    .font(Theme.Fonts.cardTitle())
                    .foregroundColor(Theme.Palette.ink)
                    .lineLimit(2)
                    .multilineTextAlignment(.leading)
                Text("\(story.genre.rawValue) · \(story.estimatedMinutes) min · \(story.endingCount) endings")
                    .font(Theme.Fonts.bodyItalic(13))
                    .foregroundColor(Theme.Palette.inkSoft)
                if let stars = story.stars {
                    StarRating(rating: stars, loved: story.isLoved, size: 12)
                }
            }
            Spacer(minLength: 0)
            DoodleIcon(.arrowRight, size: 18)
        }
        .padding(14)
        .background(
            WobblyRect(jitter: 0.5, corner: 8, seed: CGFloat(story.id.stableSeed(100)))
                .fill(Theme.Palette.mist)
        )
        .overlay(
            WobblyRect(jitter: 0.5, corner: 8, seed: CGFloat(story.id.stableSeed(100)))
                .stroke(Theme.Palette.ink, lineWidth: Theme.Stroke.line)
        )
        .accessibilityElement(children: .combine)
        .accessibilityLabel("\(story.title), \(story.genre.rawValue), about \(story.estimatedMinutes) minutes")
        .accessibilityHint("Starts this story")
    }
}
