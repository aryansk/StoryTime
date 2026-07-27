import AVFoundation
import SwiftUI

// MARK: - Story reader
//
// The actual branching scene view. Reads a CatalogStory, walks the
// node graph driven by GameState. Sketchy, flat, ink on butter.
//
// Visual model:
//   - Top bar: back / story title / narrate
//   - Scene chip + scene title (chunky sans heading)
//   - Body text in serif, with a slightly oversized first character
//   - Numbered choice cards (1, 2, 3) — feels like a CYOA paperback
//   - Consequence appears as a torn-note overlay; user taps to continue
//   - Ending: large title, restart + back-to-library

struct StoryReaderView: View {
    let story: CatalogStory
    @ObservedObject var settings: SettingsModel

    @StateObject private var gameState = GameState()
    @EnvironmentObject var progressStore: ReadingProgressStore
    @EnvironmentObject var statsStore: StatsStore
    @EnvironmentObject var speechService: SpeechService
    @EnvironmentObject var endingsTracker: EndingsTracker
    @EnvironmentObject var choiceDNA: ChoiceDNAStore
    @EnvironmentObject var ambience: AmbienceService
    @EnvironmentObject var catalog: CatalogService
    @Environment(\.dismiss) private var dismiss
    @Environment(\.scenePhase) private var scenePhase
    @Environment(\.accessibilityReduceMotion) private var reduceMotion

    @State private var selectedChoiceIndex: Int? = nil
    @State private var consequenceVisible: Bool = false
    @State private var pendingNextNodeId: String? = nil
    @State private var pendingConsequence: String? = nil
    @State private var pendingChoiceText: String? = nil
    @State private var pendingFromNodeId: String? = nil
    @State private var showShareSheet: Bool = false
    @State private var shareItems: [Any] = []
    @State private var sagaDestination: CatalogStory? = nil
    @State private var isFocusMode: Bool = false
    @State private var showReaderControls: Bool = false
    @State private var didCelebrateEnding: Bool = false

    private var sceneIndex: Int { max(1, gameState.history.count) }
    private var totalScenes: Int { story.nodes.count }
    private var totalEndings: Int { story.nodes.filter { $0.isEnding }.count }

    /// Fill for the capped (max 8) progress dots, scaled to overall
    /// completion so long stories don't fill every dot in the first scenes.
    private var scaledDotFill: Int {
        let dots = min(totalScenes, 8)
        guard totalScenes > 0 else { return 0 }
        let ratio = Double(min(sceneIndex, totalScenes)) / Double(totalScenes)
        return min(dots, max(1, Int((ratio * Double(dots)).rounded())))
    }

    private var currentPlayerName: String {
        gameState.companionTurn == 0 ? settings.companionPlayerA : settings.companionPlayerB
    }

    private var promptLabel: String {
        if settings.companionEnabled {
            return "\(currentPlayerName), what do you do?"
        }
        return "What do you do?"
    }

    /// Page turn. Under Reduce Motion this collapses to a plain crossfade —
    /// still legible as a change, without the travel.
    private var pageTransition: AnyTransition {
        if reduceMotion { return .opacity }
        return .asymmetric(
            insertion: .offset(y: 26).combined(with: .opacity),
            removal:   .offset(y: -18).combined(with: .opacity)
        )
    }

    var body: some View {
        ZStack {
            PageBackground()

            VStack(spacing: 0) {
                if isFocusMode {
                    focusBar
                        .transition(.move(edge: .top).combined(with: .opacity))
                } else {
                    topBar
                        .transition(.move(edge: .top).combined(with: .opacity))
                }
                ScrollViewReader { proxy in
                    ScrollView(showsIndicators: false) {
                        VStack(alignment: .leading, spacing: 22) {
                            sceneHeader
                                .id("top")

                            // The whole scene body is one transition unit
                            // keyed on node id: the outgoing page lifts and
                            // fades up while the incoming one rises from
                            // below, so advancing reads as turning a page
                            // rather than swapping text in place.
                            if let node = gameState.currentNode {
                                VStack(alignment: .leading, spacing: 22) {
                                    bodyText(node.text)

                                    if node.isEnding {
                                        endingBlock(title: node.endingTitle ?? "The End")
                                    } else if !consequenceVisible {
                                        choicesBlock(choices: node.choices)
                                    }
                                }
                                .id(node.id)
                                .transition(pageTransition)
                            }

                            Spacer(minLength: 80)
                        }
                        .padding(.vertical, 12)
                        .animation(reduceMotion ? nil : Theme.Motion.page,
                                   value: gameState.currentNode?.id)
                    }
                    .onChange(of: gameState.currentNode?.id) { _, _ in
                        withAnimation(stMotion(Theme.Motion.settle, reduced: reduceMotion)) {
                            proxy.scrollTo("top", anchor: .top)
                        }
                    }
                }
            }

            // Consequence overlay
            if consequenceVisible, let text = pendingConsequence {
                consequenceOverlay(text: text)
                    .zIndex(10)
            }
        }
        .navigationBarBackButtonHidden(true)
        .onAppear {
            gameState.configure(story: story,
                                progressStore: progressStore,
                                statsStore: statsStore)
            let resume = progressStore.progress(for: story.storageKey)?.nodeId
            gameState.start(at: resume)
            isFocusMode = settings.focusModeByDefault
            statsStore.beginReadingSession()
            if settings.ambienceEnabled {
                ambience.play(genre: story.genre)
            }
        }
        .onDisappear {
            speechService.stop()
            ambience.stop()
            statsStore.endReadingSession()
        }
        .sheet(isPresented: $showShareSheet) {
            ShareSheet(activityItems: shareItems)
        }
        .sheet(isPresented: $showReaderControls) {
            ReaderControlsSheet(settings: settings, isFocusMode: $isFocusMode)
                .presentationDetents([.medium, .large])
                .presentationDragIndicator(.visible)
        }
        .onChange(of: scenePhase) { _, phase in
            if phase == .active {
                statsStore.beginReadingSession()
            } else {
                statsStore.endReadingSession()
            }
        }
        .navigationDestination(item: $sagaDestination) { story in
            StoryReaderView(story: story, settings: settings)
        }
    }

    // MARK: Top bar

    private var topBar: some View {
        ZStack {
            VStack(spacing: 0) {
                Text(story.title)
                    .font(Theme.Fonts.headingMedium(15))
                    .foregroundColor(Theme.Palette.ink)
                    .lineLimit(1)
                Text(story.kind.displayName)
                    .font(Theme.Fonts.bodyItalic(11))
                    .foregroundColor(Theme.Palette.inkSoft)
                    .lineLimit(1)
            }
            .padding(.horizontal, 138)

            HStack(spacing: 0) {
                DoodleButton(doodle: .chevronLeft, label: "Back") {
                    if gameState.canGoBack {
                        withAnimation(stMotion(Theme.Motion.page, reduced: reduceMotion)) {
                            gameState.goBack()
                            resetTransientState()
                        }
                    } else {
                        dismiss()
                    }
                }
                Spacer()
                DoodleButton(doodle: .gear, label: "Reading controls") {
                    showReaderControls = true
                }
                DoodleButton(doodle: speechService.isSpeaking ? .speakerPlaying : .speaker,
                             label: "Narrate") { toggleNarration() }
                DoodleButton(doodle: .focus, label: "Enter focus mode") {
                    withAnimation(stMotion(Theme.Motion.settle, reduced: reduceMotion)) {
                        isFocusMode = true
                    }
                }
            }
        }
        .padding(.horizontal, 12)
        .padding(.top, 8)
        .padding(.bottom, 6)
        .overlay(alignment: .bottom) {
            SketchDivider().padding(.horizontal, 24)
        }
    }

    private var focusBar: some View {
        HStack(spacing: 8) {
            Text(story.title)
                .font(Theme.Fonts.bodyItalic(12))
                .foregroundColor(Theme.Palette.inkSoft)
                .lineLimit(1)
            Spacer()
            DoodleButton(doodle: .focus, label: "Exit focus mode") {
                withAnimation(stMotion(Theme.Motion.settle, reduced: reduceMotion)) {
                    isFocusMode = false
                }
            }
        }
        .padding(.leading, 24)
        .padding(.trailing, 12)
        .padding(.top, 8)
    }

    // MARK: Scene header

    private var sceneHeader: some View {
        VStack(alignment: .leading, spacing: 12) {
            if !isFocusMode {
                HStack(spacing: 8) {
                    SketchBadge(text: "Scene \(sceneIndex)")
                    SketchBadge(text: story.genre.rawValue)
                    Spacer()
                    ProgressDots(count: min(totalScenes, 8),
                                 filled: scaledDotFill)
                        .accessibilityLabel("Scene \(min(sceneIndex, totalScenes)) of \(totalScenes)")
                }
            }

            if let scene = gameState.currentNode?.sceneTitle {
                Text(scene)
                    .font(Theme.Fonts.title())
                    .foregroundColor(Theme.Palette.ink)
                    .padding(.top, 2)
            }
        }
        .padding(.horizontal, 24)
        .padding(.top, 8)
    }

    // MARK: Body text
    //
    // Honors the user's Text Size, reading Font, and Typewriter settings.

    @ViewBuilder
    private func bodyText(_ text: String) -> some View {
        let trimmed = text.trimmingCharacters(in: .whitespacesAndNewlines)
        if settings.typewriterEnabled {
            TypewriterText(full: trimmed,
                           font: settings.readerFont(settings.textSize),
                           lineSpacing: settings.textSize * settings.readerLineSpacing,
                           interval: settings.typingSpeed)
                .padding(.horizontal, 24)
        } else {
            dropCapText(trimmed)
                .padding(.horizontal, 24)
        }
    }

    private func dropCapText(_ trimmed: String) -> some View {
        let first = String(trimmed.prefix(1))
        let rest  = String(trimmed.dropFirst())

        // A raised versal initial rather than a floated drop cap. The old
        // HStack put the *entire* paragraph beside the cap, so every line was
        // indented by the cap's width — leaving a tall empty gutter beneath
        // it. Concatenating the oversized initial into the same Text lets the
        // body wrap full-width with no gutter, while still opening the passage
        // with a decorative capital.
        let cap = Text(first)
            .font(settings.readerFont(settings.textSize * 2.1))
            .foregroundColor(Theme.Palette.ink)
        let body = Text(rest)
            .font(settings.readerFont(settings.textSize))
            .foregroundColor(Theme.Palette.ink)

        return (cap + body)
            .lineSpacing(settings.textSize * settings.readerLineSpacing)
            .frame(maxWidth: .infinity, alignment: .leading)
            .accessibilityLabel(trimmed)
    }

    // MARK: Choices

    private func choicesBlock(choices: [StoryChoice]) -> some View {
        VStack(alignment: .leading, spacing: 14) {
            HStack(spacing: 8) {
                DoodleIcon(.branch, size: 18)
                Text(promptLabel)
                    .font(Theme.Fonts.label())
                    .tracking(1.2)
                    .foregroundColor(Theme.Palette.inkSoft)
                Spacer()
                if settings.companionEnabled {
                    SketchBadge(text: "Turn: \(currentPlayerName)")
                }
            }

            VStack(spacing: 10) {
                ForEach(Array(choices.enumerated()), id: \.offset) { idx, choice in
                    NumberedChoiceRow(
                        number: idx + 1,
                        text: choice.text,
                        selected: selectedChoiceIndex == idx,
                        dimmed: selectedChoiceIndex != nil && selectedChoiceIndex != idx
                    ) {
                        guard selectedChoiceIndex == nil else { return }
                        withAnimation(stMotion(Theme.Motion.quick, reduced: reduceMotion)) {
                            selectedChoiceIndex = idx
                        }
                        pendingConsequence = choice.consequence
                        pendingNextNodeId = choice.nextNodeId
                        pendingChoiceText = choice.text
                        pendingFromNodeId = gameState.currentNode?.id
                        statsStore.recordChoice()
                        NarrativeFeedback.play(.selection, enabled: settings.hapticsEnabled)
                        // Score this choice against the Choice DNA traits.
                        choiceDNA.record(consequence: choice.consequence,
                                         choiceText: choice.text)
                        withAnimation(stMotion(Theme.Motion.settle, reduced: reduceMotion)) {
                            consequenceVisible = true
                        }
                    }
                    // Choices arrive one after another, so the reader's eye
                    // lands on option 1 first instead of on a wall of cards.
                    .stAppear(idx + 1, rise: 16)
                }
            }
        }
        .padding(.horizontal, 24)
        .padding(.top, 6)
    }

    // MARK: Consequence overlay (tap to continue)

    private func consequenceOverlay(text: String) -> some View {
        ZStack {
            // Scrim. Fades on its own so the note can spring in over a
            // settled background rather than dragging the dim with it.
            Theme.Palette.ink.opacity(0.18)
                .ignoresSafeArea()
                .onTapGesture { advanceFromConsequence() }
                .accessibilityHidden(true)
                .transition(.opacity)

            VStack(spacing: 0) {
                Spacer()
                VStack(alignment: .leading, spacing: 14) {
                    HStack(spacing: 8) {
                        DoodleIcon(.branch, size: 20)
                        Text("Consequence")
                            .font(Theme.Fonts.label())
                            .tracking(1.4)
                            .foregroundColor(Theme.Palette.inkSoft)
                        Spacer()
                    }
                    Text(text)
                        .font(Theme.Fonts.bodyItalic(17))
                        .foregroundColor(Theme.Palette.ink)
                        .lineSpacing(5)
                    HStack(spacing: 8) {
                        Spacer()
                        Text("Tap to continue")
                            .font(Theme.Fonts.headingMedium(13))
                            .foregroundColor(Theme.Palette.inkSoft)
                        DoodleIcon(.arrowRight, size: 16)
                            .jitter(amplitude: 0.3)
                    }
                    .padding(.top, 4)
                }
                .padding(20)
                .background(Theme.Palette.paperSpeckle)
                .overlay(
                    WobblyRect(jitter: 0.6, corner: 8, seed: 33)
                        .stroke(Theme.Palette.storyCoral, lineWidth: Theme.Stroke.bold)
                )
                .padding(.horizontal, 20)
                .padding(.bottom, 28)
                .onTapGesture { advanceFromConsequence() }
                // VoiceOver: the overlay advanced only via a raw tap gesture,
                // which VoiceOver can't reach — a user got stuck here. Expose
                // it as a single button with an explicit activation action.
                .accessibilityElement(children: .combine)
                .accessibilityAddTraits(.isButton)
                .accessibilityHint("Continue to the next scene")
                .accessibilityAction { advanceFromConsequence() }
                // The note is a physical object: it slides up from the
                // bottom edge with a little overshoot, like a card being
                // dealt onto the page.
                .transition(reduceMotion
                            ? .opacity
                            : .move(edge: .bottom).combined(with: .opacity))
            }
        }
    }

    private func advanceFromConsequence() {
        let next = pendingNextNodeId
        let fromId = pendingFromNodeId
        let idx = selectedChoiceIndex
        let choiceText = pendingChoiceText
        let consequence = pendingConsequence
        // Drive the scene transition off the overlay's dismiss animation
        // finishing, rather than a hand-tuned asyncAfter delay.
        // Never `nil` here, even under Reduce Motion: the scene advance is
        // driven by this animation's completion handler, so it needs a real
        // (if imperceptibly short) animation to complete against.
        withAnimation(reduceMotion ? .linear(duration: 0.01) : Theme.Motion.quick) {
            consequenceVisible = false
        } completion: {
            NarrativeFeedback.play(.pageTurn, enabled: settings.hapticsEnabled)
            if let next {
                gameState.jump(
                    to: next,
                    fromNodeId: fromId,
                    choiceIndex: idx,
                    choiceText: choiceText,
                    consequence: consequence
                )
                if settings.companionEnabled {
                    gameState.advanceCompanionTurn()
                }
                // If the next node is itself an ending, mark it discovered.
                if let endingNode = story.node(id: next), endingNode.isEnding {
                    endingsTracker.record(storyKey: story.storageKey,
                                          endingNodeId: endingNode.id)
                }
            }
            selectedChoiceIndex = nil
            pendingConsequence = nil
            pendingNextNodeId = nil
            pendingChoiceText = nil
            pendingFromNodeId = nil
        }
    }

    // MARK: Ending

    private func endingBlock(title: String) -> some View {
        SketchCard(fill: Theme.Palette.mist, seed: 12.0) {
            VStack(alignment: .leading, spacing: 14) {
                BookSceneView(story: story,
                              mode: .ending,
                              endingTitle: title,
                              onEvent: { event in
                                  if case .pageTurned = event {
                                      NarrativeFeedback.play(.pageTurn, enabled: settings.hapticsEnabled)
                                  }
                              })
                    .frame(height: 175)
                    .clipShape(RoundedRectangle(cornerRadius: 10))
                    .accessibilityElement()
                    .accessibilityLabel("Ending book for (title)")

                HStack(spacing: 8) {
                    DoodleIcon(.starFill, size: 22, filled: true)
                    Text("ENDING")
                        .font(Theme.Fonts.label())
                        .tracking(1.4)
                        .foregroundColor(Theme.Palette.inkSoft)
                    Spacer()
                    SketchBadge(text: "Path \(sceneIndex)")
                }
                HStack(spacing: 10) {
                    ZStack {
                        RoundedRectangle(cornerRadius: 4)
                            .fill(Theme.Palette.storyCoral)
                            .frame(width: 24, height: 38)
                        DoodleIcon(.starFill, size: 13, color: Theme.Palette.butter, filled: true)
                    }
                    Text("A new bookmark is on your shelf")
                        .font(Theme.Fonts.bodyItalic(13))
                        .foregroundColor(Theme.Palette.inkSoft)
                    Spacer()
                }
                Text(title)
                    .font(Theme.Fonts.title())
                    .foregroundColor(Theme.Palette.ink)

                // Discovered / total endings progress.
                let discovered = endingsTracker.count(for: story.storageKey)
                if totalEndings > 1 {
                    Text("You've found \(discovered) of \(totalEndings) endings.")
                        .font(Theme.Fonts.bodyItalic(14))
                        .foregroundColor(Theme.Palette.inkSoft)
                }

                // Branch peek — show the choice not taken at the last
                // decision point, with its consequence flavor.
                if let peek = branchPeek() {
                    branchPeekRow(label: peek.label, consequence: peek.consequence)
                }

                VStack(spacing: 10) {
                    SketchButton(title: "Start Over", doodle: .undo, style: .primary) {
                        withAnimation(stMotion(Theme.Motion.page, reduced: reduceMotion)) {
                            gameState.restart()
                            resetTransientState()
                        }
                    }
                    if let next = sagaNext() {
                        SketchButton(title: "Continue → \(next.sourceTitle)",
                                     doodle: .arrowRight,
                                     style: .secondary) {
                            sagaDestination = next
                        }
                    }
                    SketchButton(title: "Share Ending Card", doodle: .share, style: .secondary) {
                        prepareShare(endingTitle: title)
                    }
                    SketchButton(title: "Back to Library", style: .ghost) { dismiss() }
                }
                .padding(.top, 6)
            }
        }
        .padding(.horizontal, 24)
        .padding(.top, 8)
        // An ending has earned a flourish: the card lands with a bounce
        // rather than sliding in like any other scene.
        .stAppear(0, rise: 24, scale: 0.94, animation: Theme.Motion.bouncy)
        .onAppear {
            guard !didCelebrateEnding else { return }
            didCelebrateEnding = true
            NarrativeFeedback.play(.ending, enabled: settings.hapticsEnabled)
        }
    }

    private func branchPeek() -> (label: String, consequence: String)? {
        // Find the last decision (most recent record) and the choice not taken.
        guard let last = gameState.lastDecisionRecord,
              let node = story.node(id: last.nodeId) else { return nil }
        let other = node.choices.enumerated().first { (idx, _) in idx != last.choiceIndex }
        guard let pair = other else { return nil }
        return (pair.element.text, pair.element.consequence)
    }

    private func branchPeekRow(label: String, consequence: String) -> some View {
        VStack(alignment: .leading, spacing: 6) {
            HStack(spacing: 6) {
                DoodleIcon(.branch, size: 14)
                Text("THE PATH NOT TAKEN")
                    .font(Theme.Fonts.label())
                    .tracking(1.2)
                    .foregroundColor(Theme.Palette.inkSoft)
            }
            Text("If you had: \(label)")
                .font(Theme.Fonts.body(15))
                .foregroundColor(Theme.Palette.ink)
            Text("Replay the story to discover where that choice leads.")
                .font(Theme.Fonts.bodyItalic(14))
                .foregroundColor(Theme.Palette.inkSoft)
                .lineSpacing(3)
        }
        .padding(12)
        .background(
            WobblyRect(jitter: 0.4, corner: 6, seed: 28)
                .fill(Theme.Palette.butterDeep)
        )
        .overlay(
            WobblyRect(jitter: 0.4, corner: 6, seed: 28)
                .stroke(Theme.Palette.inkHair, lineWidth: Theme.Stroke.line)
        )
    }

    private func sagaNext() -> CatalogStory? {
        guard let nextId = story.nextStoryId else { return nil }
        return catalog.story(id: nextId)
    }

    private func prepareShare(endingTitle: String) {
        let total = story.nodes.count
        let label = "\(sceneIndex) of \(total) scenes"
        let image = ShareEndingCard.render(story: story,
                                            endingTitle: endingTitle,
                                            pathLabel: label)
        let text = "I just played \(story.sourceTitle) on StoryTime — my ending: \(endingTitle)."
        var items: [Any] = [text]
        if let image { items.insert(image, at: 0) }
        shareItems = items
        showShareSheet = true
    }

    private func resetTransientState() {
        selectedChoiceIndex = nil
        consequenceVisible = false
        didCelebrateEnding = false
        pendingConsequence = nil
        pendingNextNodeId = nil
    }

    private func toggleNarration() {
        guard let text = gameState.currentNode?.text else { return }
        if speechService.isSpeaking && !speechService.isPaused {
            speechService.pause()
        } else if speechService.isPaused {
            speechService.resume()
        } else {
            let minRate = AVSpeechUtteranceMinimumSpeechRate
            let maxRate = AVSpeechUtteranceMaximumSpeechRate
            let rate = minRate + Float(settings.narrationRate) * (maxRate - minRate)
            speechService.speak(text, rate: rate)
        }
    }
}

// MARK: - In-reader controls

private struct ReaderControlsSheet: View {
    @ObservedObject var settings: SettingsModel
    @Binding var isFocusMode: Bool
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        NavigationStack {
            ZStack {
                PageBackground()
                ScrollView(showsIndicators: false) {
                    VStack(alignment: .leading, spacing: 22) {
                        VStack(alignment: .leading, spacing: 6) {
                            Text("Reading Controls")
                                .font(Theme.Fonts.title())
                                .foregroundColor(Theme.Palette.ink)
                            Text("Tune the page without leaving your story.")
                                .font(Theme.Fonts.bodyItalic(14))
                                .foregroundColor(Theme.Palette.inkSoft)
                        }

                        SketchCard(fill: Theme.Palette.butterDeep, seed: 71) {
                            Text("The room goes quiet. Somewhere beyond the page, a choice waits.")
                                .font(settings.readerFont(settings.textSize))
                                .foregroundColor(Theme.Palette.ink)
                                .lineSpacing(settings.textSize * settings.readerLineSpacing)
                                .frame(maxWidth: .infinity, alignment: .leading)
                        }

                        VStack(alignment: .leading, spacing: 12) {
                            Text("TEXT SIZE")
                                .font(Theme.Fonts.label())
                                .foregroundColor(Theme.Palette.inkSoft)
                            HStack(spacing: 12) {
                                SketchButton(title: "A−", style: .secondary, fullWidth: false) {
                                    settings.textSize = max(settings.minTextSize, settings.textSize - 1)
                                }
                                Spacer()
                                Text("\(Int(settings.textSize)) pt")
                                    .font(Theme.Fonts.headingMedium(14))
                                    .foregroundColor(Theme.Palette.ink)
                                Spacer()
                                SketchButton(title: "A+", style: .secondary, fullWidth: false) {
                                    settings.textSize = min(settings.maxTextSize, settings.textSize + 1)
                                }
                            }
                        }

                        VStack(alignment: .leading, spacing: 12) {
                            Text("READING FONT")
                                .font(Theme.Fonts.label())
                                .foregroundColor(Theme.Palette.inkSoft)
                            ScrollView(.horizontal, showsIndicators: false) {
                                HStack(spacing: 10) {
                                    ForEach(settings.availableFonts, id: \.self) { font in
                                        SketchPill(title: font,
                                                   selected: settings.selectedFontName == font) {
                                            settings.selectedFontName = font
                                        }
                                    }
                                }
                            }
                        }

                        VStack(alignment: .leading, spacing: 10) {
                            Text("LINE SPACING")
                                .font(Theme.Fonts.label())
                                .foregroundColor(Theme.Palette.inkSoft)
                            Slider(value: $settings.readerLineSpacing, in: 0.35...0.8, step: 0.05)
                                .tint(Theme.Palette.ink)
                                .accessibilityLabel("Line spacing")
                        }

                        SketchCard(seed: 73) {
                            VStack(spacing: 14) {
                                Toggle("Typewriter effect", isOn: $settings.typewriterEnabled)
                                    .font(Theme.Fonts.body(15))
                                    .tint(Theme.Palette.ink)
                                SketchDivider()
                                Toggle("Start stories in focus mode", isOn: $settings.focusModeByDefault)
                                    .font(Theme.Fonts.body(15))
                                    .tint(Theme.Palette.ink)
                            }
                            .foregroundColor(Theme.Palette.ink)
                        }

                        SketchButton(title: isFocusMode ? "Exit Focus Mode" : "Enter Focus Mode",
                                     doodle: .focus,
                                     style: .primary) {
                            isFocusMode.toggle()
                            dismiss()
                        }
                    }
                    .padding(.horizontal, 24)
                    .padding(.top, 20)
                    .padding(.bottom, 36)
                }
            }
            .toolbar {
                ToolbarItem(placement: .topBarTrailing) {
                    Button("Done") { dismiss() }
                        .font(Theme.Fonts.headingMedium(14))
                        .foregroundColor(Theme.Palette.ink)
                }
            }
        }
    }
}

// MARK: - Numbered choice row

private struct NumberedChoiceRow: View {
    let number: Int
    let text: String
    let selected: Bool
    /// True for the options *not* picked. They recede so the chosen path is
    /// unmistakable in the beat before the consequence appears.
    var dimmed: Bool = false
    let action: () -> Void

    @Environment(\.accessibilityReduceMotion) private var reduceMotion

    var body: some View {
        Button(action: {
            UIImpactFeedbackGenerator(style: .medium).impactOccurred()
            action()
        }) {
            HStack(alignment: .top, spacing: 14) {
                // Numbered medallion
                ZStack {
                    WobblyRect(jitter: 0.5, corner: 16,
                                seed: CGFloat(number * 7))
                        .fill(selected ? Theme.Palette.ink : Theme.Palette.butter)
                        .frame(width: 36, height: 36)
                    WobblyRect(jitter: 0.5, corner: 16,
                                seed: CGFloat(number * 7))
                        .stroke(Theme.Palette.ink, lineWidth: Theme.Stroke.bold)
                        .frame(width: 36, height: 36)
                    Text("\(number)")
                        .font(Theme.Fonts.heading(16))
                        .foregroundColor(selected ? Theme.Palette.butter : Theme.Palette.ink)
                }
                .jitter(selected, amplitude: 0.4)

                Text(text)
                    .font(Theme.Fonts.body(16))
                    .foregroundColor(Theme.Palette.ink)
                    .multilineTextAlignment(.leading)
                    .lineSpacing(5)
                    .padding(.top, 6)
                Spacer(minLength: 0)
                DoodleIcon(.arrowRight, size: 16, color: Theme.Palette.inkSoft)
                    .padding(.top, 10)
                    .opacity(selected ? 1 : 0.4)
                    .offset(x: selected ? 4 : 0)
            }
            .padding(14)
            .frame(maxWidth: .infinity, alignment: .leading)
            .background(
                WobblyRect(jitter: 0.4, corner: 6,
                            seed: CGFloat(text.stableSeed(100)))
                    .fill(selected ? Theme.Palette.butterDeep : Theme.Palette.mist.opacity(0.55))
            )
            .overlay(
                WobblyRect(jitter: 0.4, corner: 6,
                            seed: CGFloat(text.stableSeed(100)))
                    .stroke(Theme.Palette.ink,
                            lineWidth: selected ? Theme.Stroke.bold : Theme.Stroke.line)
            )
            .scaleEffect(selected && !reduceMotion ? 1.02 : 1)
            .opacity(dimmed ? 0.42 : 1)
            .animation(reduceMotion ? nil : Theme.Motion.quick, value: selected)
            .animation(reduceMotion ? nil : Theme.Motion.settle, value: dimmed)
        }
        .stPressable(scale: 0.975)
        .disabled(dimmed)
    }
}

// MARK: - Typewriter body text
//
// Reveals the scene text one character at a time at the user's chosen
// typing speed. Tap anywhere on the text to skip straight to the full
// passage. Restarts whenever the scene changes (the parent applies `.id`).

private struct TypewriterText: View {
    let full: String
    let font: Font
    var lineSpacing: CGFloat = 8
    let interval: Double

    // Pre-split into an array of characters once. The old version called
    // `full.prefix(shown)` every tick, which re-walks the String's grapheme
    // boundaries from the start each time — O(n) per tick, O(n²) overall.
    // Array indexing is O(1), so each tick's substring is just O(shown).
    @State private var chars: [Character] = []
    @State private var shown: Int = 0
    @State private var timer: Timer?

    var body: some View {
        Text(String(chars.prefix(shown)))
            .font(font)
            .foregroundColor(Theme.Palette.ink)
            .lineSpacing(lineSpacing)
            .frame(maxWidth: .infinity, alignment: .leading)
            .contentShape(Rectangle())
            .onAppear { begin() }
            .onDisappear { timer?.invalidate() }
            .onTapGesture { revealAll() }
            .accessibilityLabel(full)
    }

    private func begin() {
        chars = Array(full)
        shown = 0
        timer?.invalidate()
        let count = chars.count
        // Cap the redraw rate at ~33 fps. At fast typing speeds the old code
        // fired up to 100 times/sec, and each tick re-lays-out the whole
        // visible string — O(n) layouts per scene. Revealing several
        // characters per tick keeps the same perceived pace with a third of
        // the work.
        let minTick = 0.03
        let tick = max(minTick, interval)
        let step = max(1, Int((tick / max(interval, 0.001)).rounded()))
        timer = Timer.scheduledTimer(withTimeInterval: tick, repeats: true) { t in
            if shown < count {
                shown = min(count, shown + step)
            } else {
                t.invalidate()
            }
        }
    }

    private func revealAll() {
        timer?.invalidate()
        shown = chars.count
    }
}

// MARK: - Progress dots

private struct ProgressDots: View {
    let count: Int
    let filled: Int

    @Environment(\.accessibilityReduceMotion) private var reduceMotion

    var body: some View {
        HStack(spacing: 4) {
            ForEach(0..<count, id: \.self) { i in
                let isFilled = i < filled
                Circle()
                    .stroke(Theme.Palette.ink, lineWidth: Theme.Stroke.line)
                    .background(
                        Circle()
                            .fill(isFilled ? Theme.Palette.ink : Color.clear)
                            // The newest dot pops in slightly oversized and
                            // settles, marking progress without a label.
                            .scaleEffect(isFilled ? 1 : 0.1)
                    )
                    .frame(width: 6, height: 6)
                    .animation(reduceMotion
                               ? nil
                               : Theme.Motion.bouncy.delay(Double(i) * 0.03),
                               value: isFilled)
            }
        }
    }
}
