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

    @Environment(\.accessibilityReduceMotion) private var reduceMotion

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

    private static let tasteGenres: [TasteGenre] = {
        // Annotated separately: implicit member expressions inside an array
        // literal can't be inferred through the `.enumerated().map` chain.
        let raw: [(StoryGenre, DoodleName)] = [
            (.drama, .tv), (.comedy, .popcorn), (.thriller, .clapperboard),
            (.sciFi, .sparkle), (.horror, .flame), (.fantasy, .scroll),
            (.action, .play)
        ]
        return raw.enumerated().map {
            TasteGenre(order: $0.offset, genre: $0.element.0, doodle: $0.element.1)
        }
    }()

    var body: some View {
        ZStack {
            PageBackground()

            VStack(spacing: 0) {
                topBar
                    .padding(.horizontal, 20)
                    .padding(.top, 8)

                ScrollView(showsIndicators: false) {
                    VStack(spacing: 18) {
                        livingBookPreview

                        Group {
                            switch step {
                            case 0:
                                WelcomeStep(storyCount: catalog.stories.count,
                                            onContinue: advance)
                            case 1:
                                TasteStep(genres: Self.tasteGenres,
                                          selection: $selectedGenres,
                                          onContinue: advance)
                            case 2:
                                OptionListStep(title: "What kind of night is it?",
                                               subtitle: "Your answer changes the book waiting on your shelf.",
                                               options: Self.goalOptions,
                                               selection: $selectedGoal,
                                               onSelect: autoAdvance)
                            case 3:
                                OptionListStep(title: "How much story do you want?",
                                               subtitle: "We’ll tune the shelf for a quick scene or a whole saga.",
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
                        .transition(stepTransition)
                        .padding(.bottom, 24)
                    }
                    .padding(.top, 2)
                }
            }
        }
    }

    // MARK: Pool-like shell: one living object, one quiet progress cue

    private var topBar: some View {
        HStack(spacing: 12) {
            if step > 0 && step < 5 {
                Button(action: back) {
                    DoodleIcon(.chevronLeft, size: 17)
                        .frame(width: 44, height: 44)
                }
                .buttonStyle(.plain)
                .accessibilityLabel("Back")
            } else {
                Color.clear.frame(width: 44, height: 44)
            }

            Spacer(minLength: 0)

            if (1...Self.quizStepCount).contains(step) {
                HStack(spacing: 6) {
                    ForEach(0..<Self.quizStepCount, id: \.self) { index in
                        Capsule()
                            .fill(index < step ? Theme.Palette.storyBlue : Theme.Palette.inkHair)
                            .frame(width: index == step - 1 ? 22 : 7, height: 5)
                            .animation(reduceMotion ? nil : Theme.Motion.bouncy, value: step)
                    }
                }
                .accessibilityElement()
                .accessibilityLabel("Step \(step) of \(Self.quizStepCount)")
            } else {
                Text(step == 5 ? "YOUR SHELF" : "STORYTIME")
                    .font(Theme.Fonts.meta())
                    .tracking(1.4)
                    .foregroundColor(Theme.Palette.inkSoft)
            }

            Spacer(minLength: 0)

            if step < 5 {
                Button("Skip", action: { complete() })
                    .font(Theme.Fonts.headingMedium(13))
                    .foregroundColor(Theme.Palette.inkSoft)
                    .frame(minWidth: 44, minHeight: 44)
            } else {
                Color.clear.frame(width: 44, height: 44)
            }
        }
    }

    private var livingBookPreview: some View {
        VStack(spacing: 5) {
            if let story = onboardingPreviewStory {
                BookSceneView(story: story,
                              mode: .onboarding,
                              onEvent: { event in
                                  if case .opened = event {
                                      NarrativeFeedback.play(.pageTurn)
                                  }
                              })
                    .frame(height: 205)
                    .clipShape(RoundedRectangle(cornerRadius: 16))
                    .accessibilityElement()
                    .accessibilityLabel("Your living storybook preview")
                    .accessibilityHint("Tap a book to explore it")
            } else {
                DoodleIcon(.clapperboard, size: 82)
                    .frame(height: 205)
            }

            Text(livingBookCaption)
                .font(Theme.Fonts.meta())
                .foregroundColor(Theme.Palette.inkSoft)
                .contentTransition(.opacity)
                .animation(reduceMotion ? nil : Theme.Motion.settle, value: livingBookCaption)
        }
        .padding(.horizontal, 12)
    }

    private var onboardingPreviewStory: CatalogStory? {
        guard !catalog.stories.isEmpty else { return nil }
        return catalog.stories
            .map { (story: $0, score: firstStoryScore($0)) }
            .sorted { $0.score > $1.score }
            .first?.story
    }

    private var livingBookCaption: String {
        if step == 0 { return "A shelf that follows your taste" }
        if step == 5 { return "Three paths, picked for you" }
        if !selectedGenres.isEmpty { return "Your shelf is changing with you" }
        return "Choose an answer — the book moves with you"
    }

    /// Steps slide in the direction of travel and shrink slightly on the way
    /// out, so the flow reads as a stack of cards rather than a filmstrip.
    /// Reduce Motion drops the travel and keeps the crossfade.
    private var stepTransition: AnyTransition {
        if reduceMotion { return .opacity }
        return .asymmetric(
            insertion: .move(edge: goingBack ? .leading : .trailing)
                .combined(with: .opacity),
            removal: .move(edge: goingBack ? .trailing : .leading)
                .combined(with: .opacity)
                .combined(with: .scale(scale: 0.96))
        )
    }

    // MARK: Navigation

    private func advance() {
        goingBack = false
        advancing = false
        withAnimation(stMotion(Theme.Motion.settle, reduced: reduceMotion)) { step += 1 }
    }

    private func back() {
        guard step > 0 else { return }
        goingBack = true
        advancing = false
        withAnimation(stMotion(Theme.Motion.settle, reduced: reduceMotion)) { step -= 1 }
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
        advancing = false
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

/// The taste-step genre chips, carrying their display order so the grid can
/// stagger them. A named type (not a tuple) so `ForEach` has an id.
struct TasteGenre: Identifiable {
    let order: Int
    let genre: StoryGenre
    let doodle: DoodleName
    var id: StoryGenre { genre }
}

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

    var body: some View {
        VStack(spacing: 22) {
            VStack(spacing: 10) {
                Text("StoryTime")
                    .font(Theme.Fonts.display())
                    .foregroundColor(Theme.Palette.ink)
                Text("Stories with more than one way to end.")
                    .font(Theme.Fonts.bodyItalic(14))
                    .foregroundColor(Theme.Palette.inkSoft)
            }

            VStack(spacing: 12) {
                Text("Pick a path. See what breaks.")
                    .font(Theme.Fonts.title())
                    .foregroundColor(Theme.Palette.ink)
                    .multilineTextAlignment(.center)
                    .padding(.horizontal, 24)
                Text("\(max(storyCount, 100))+ hand-authored stories from movies, shows, and books. Every choice is yours.")
                    .font(Theme.Fonts.body(15))
                    .foregroundColor(Theme.Palette.inkSoft)
                    .multilineTextAlignment(.center)
                    .padding(.horizontal, 32)
                    .lineSpacing(4)
            }

            VStack(spacing: 12) {
                SketchButton(title: "Open my shelf", trailingDoodle: .arrowRight, action: onContinue)
                Text("4 quick questions · about 30 seconds")
                    .font(Theme.Fonts.meta())
                    .foregroundColor(Theme.Palette.inkSoft)
            }
            .padding(.horizontal, 40)
        }
    }
}

private struct TasteStep: View {
    let genres: [TasteGenre]
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
                ForEach(genres) { item in
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
                    .stAppear(item.order, rise: 12, scale: 0.94)
                }
            }
            .padding(.horizontal, 32)

            SketchButton(title: selection.isEmpty ? "Pick at least one" : "Build my shelf",
                         trailingDoodle: .arrowRight,
                         action: onContinue)
                .padding(.horizontal, 40)
                .opacity(selection.isEmpty ? 0.5 : 1)
                .scaleEffect(selection.isEmpty ? 0.98 : 1)
                .animation(Theme.Motion.quick, value: selection.isEmpty)
                .disabled(selection.isEmpty)
        }
    }
}

private struct GenreChip: View {
    let title: String
    let doodle: DoodleName
    let selected: Bool
    let action: () -> Void

    @Environment(\.accessibilityReduceMotion) private var reduceMotion

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
                        .transition(.scale(scale: 0.3).combined(with: .opacity))
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
            .scaleEffect(selected && !reduceMotion ? 1.03 : 1)
            .animation(reduceMotion ? nil : Theme.Motion.bouncy, value: selected)
        }
        .stPressable(scale: 0.95)
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
                ForEach(options.indexed) { item in
                    let opt = item.value
                    Button {
                        UISelectionFeedbackGenerator().selectionChanged()
                        withAnimation(Theme.Motion.quick) { selection = opt.title }
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
                                    .transition(.scale(scale: 0.3).combined(with: .opacity))
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
                        .scaleEffect(selection == opt.title ? 1.02 : 1)
                        .animation(Theme.Motion.bouncy, value: selection)
                    }
                    .stPressable(scale: 0.97)
                    .stAppear(item.index, rise: 14)
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
        VStack(spacing: 20) {
                VStack(spacing: 12) {
                    Text(name.isEmpty ? "Your shelf is ready." : "Ready for you, \(name).")
                        .font(Theme.Fonts.title())
                        .foregroundColor(Theme.Palette.ink)
                        .multilineTextAlignment(.center)
                        .padding(.horizontal, 24)
                    Text(picks.isEmpty
                         ? "The catalog is warming up — head in and look around."
                         : "Three books tuned to your answers. Tap one to open it now.")
                        .font(Theme.Fonts.body(14))
                        .foregroundColor(Theme.Palette.inkSoft)
                        .multilineTextAlignment(.center)
                        .padding(.horizontal, 32)
                }

                if !picks.isEmpty {
                    ScrollView(.horizontal, showsIndicators: false) {
                        HStack(spacing: 12) {
                        ForEach(picks.indexed) { item in
                            Button {
                                onStart(item.value)
                            } label: {
                                PickCard(story: item.value)
                                    .frame(width: 270)
                            }
                            .stPressable(scale: 0.97, nudge: 1.5)
                            // The payoff is the moment the flow is built
                            // around — the three picks deal out one by one.
                            .stAppear(item.index, rise: 22, scale: 0.92,
                                      animation: Theme.Motion.bouncy)
                        }
                        }
                        .padding(.horizontal, 32)
                    }
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

private struct PickCard: View {
    let story: CatalogStory

    var body: some View {
        HStack(spacing: 14) {
            BookCoverThumbnail(story: story, compact: true)
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
