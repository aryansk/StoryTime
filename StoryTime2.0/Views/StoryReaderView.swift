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
    @Environment(\.dismiss) private var dismiss

    @State private var selectedChoiceIndex: Int? = nil
    @State private var consequenceVisible: Bool = false
    @State private var pendingNextNodeId: String? = nil
    @State private var pendingConsequence: String? = nil
    @State private var showShareSheet: Bool = false

    private var sceneIndex: Int { max(1, gameState.history.count) }
    private var totalScenes: Int { story.nodes.count }

    var body: some View {
        ZStack {
            PageBackground()

            VStack(spacing: 0) {
                topBar
                ScrollViewReader { proxy in
                    ScrollView(showsIndicators: false) {
                        VStack(alignment: .leading, spacing: 22) {
                            sceneHeader
                                .id("top")

                            if let node = gameState.currentNode {
                                bodyText(node.text)

                                if node.isEnding {
                                    endingBlock(title: node.endingTitle ?? "The End")
                                } else if !consequenceVisible {
                                    choicesBlock(choices: node.choices)
                                }
                            }

                            Spacer(minLength: 80)
                        }
                        .padding(.vertical, 12)
                    }
                    .onChange(of: gameState.currentNode?.id) { _, _ in
                        withAnimation { proxy.scrollTo("top", anchor: .top) }
                    }
                }
            }

            // Consequence overlay
            if consequenceVisible, let text = pendingConsequence {
                consequenceOverlay(text: text)
                    .transition(.opacity.combined(with: .move(edge: .bottom)))
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
        }
        .onDisappear { speechService.stop() }
    }

    // MARK: Top bar

    private var topBar: some View {
        HStack(spacing: 4) {
            DoodleButton(doodle: .chevronLeft, label: "Back") {
                if gameState.canGoBack {
                    withAnimation {
                        gameState.goBack()
                        resetTransientState()
                    }
                } else {
                    dismiss()
                }
            }
            Spacer()
            VStack(spacing: 0) {
                Text(story.title)
                    .font(Theme.Fonts.headingMedium(15))
                    .foregroundColor(Theme.Palette.ink)
                    .lineLimit(1)
                Text("After \(story.sourceTitle)")
                    .font(Theme.Fonts.bodyItalic(11))
                    .foregroundColor(Theme.Palette.inkSoft)
                    .lineLimit(1)
            }
            Spacer()
            DoodleButton(doodle: speechService.isSpeaking ? .speakerPlaying : .speaker,
                         label: "Narrate") { toggleNarration() }
        }
        .padding(.horizontal, 12)
        .padding(.top, 8)
        .padding(.bottom, 6)
        .overlay(alignment: .bottom) {
            SketchDivider().padding(.horizontal, 24)
        }
    }

    // MARK: Scene header

    private var sceneHeader: some View {
        VStack(alignment: .leading, spacing: 12) {
            HStack(spacing: 8) {
                SketchBadge(text: "Scene \(sceneIndex)")
                SketchBadge(text: story.genre.rawValue)
                Spacer()
                ProgressDots(count: min(totalScenes, 8),
                             filled: min(sceneIndex, totalScenes))
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

    // MARK: Body text with drop cap

    private func bodyText(_ text: String) -> some View {
        let trimmed = text.trimmingCharacters(in: .whitespacesAndNewlines)
        let first = String(trimmed.prefix(1))
        let rest  = String(trimmed.dropFirst())

        return HStack(alignment: .top, spacing: 0) {
            // Drop cap (chunky sans)
            Text(first)
                .font(Theme.Fonts.heading(54))
                .foregroundColor(Theme.Palette.ink)
                .frame(height: 50, alignment: .top)
                .padding(.trailing, 8)
                .baselineOffset(-6)
                .accessibilityHidden(true)

            (
                Text(rest)
                    .font(Theme.Fonts.body(17))
                    .foregroundColor(Theme.Palette.ink)
            )
            .lineSpacing(7)
            .accessibilityLabel(trimmed)
        }
        .padding(.horizontal, 24)
    }

    // MARK: Choices

    private func choicesBlock(choices: [StoryChoice]) -> some View {
        VStack(alignment: .leading, spacing: 14) {
            HStack(spacing: 8) {
                DoodleIcon(.branch, size: 18)
                Text("What do you do?")
                    .font(Theme.Fonts.label())
                    .tracking(1.2)
                    .foregroundColor(Theme.Palette.inkSoft)
            }

            VStack(spacing: 10) {
                ForEach(Array(choices.enumerated()), id: \.offset) { idx, choice in
                    NumberedChoiceRow(
                        number: idx + 1,
                        text: choice.text,
                        selected: selectedChoiceIndex == idx
                    ) {
                        guard selectedChoiceIndex == nil else { return }
                        selectedChoiceIndex = idx
                        pendingConsequence = choice.consequence
                        pendingNextNodeId = choice.nextNodeId
                        statsStore.recordChoice()
                        withAnimation(.easeOut(duration: 0.25)) {
                            consequenceVisible = true
                        }
                    }
                }
            }
        }
        .padding(.horizontal, 24)
        .padding(.top, 6)
    }

    // MARK: Consequence overlay (tap to continue)

    private func consequenceOverlay(text: String) -> some View {
        ZStack {
            // Scrim
            Theme.Palette.ink.opacity(0.18)
                .ignoresSafeArea()
                .onTapGesture { advanceFromConsequence() }

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
                .background(
                    WobblyRect(jitter: 0.6, corner: 8, seed: 33)
                        .fill(Theme.Palette.butterDeep)
                )
                .overlay(
                    WobblyRect(jitter: 0.6, corner: 8, seed: 33)
                        .stroke(Theme.Palette.ink, lineWidth: Theme.Stroke.bold)
                )
                .padding(.horizontal, 20)
                .padding(.bottom, 28)
                .onTapGesture { advanceFromConsequence() }
            }
        }
    }

    private func advanceFromConsequence() {
        withAnimation(.easeOut(duration: 0.2)) {
            consequenceVisible = false
        }
        let next = pendingNextNodeId
        // Hand off the scene transition after the overlay finishes dismissing.
        DispatchQueue.main.asyncAfter(deadline: .now() + 0.22) {
            if let next { gameState.jump(to: next) }
            selectedChoiceIndex = nil
            pendingConsequence = nil
            pendingNextNodeId = nil
        }
    }

    // MARK: Ending

    private func endingBlock(title: String) -> some View {
        SketchCard(fill: Theme.Palette.mist, seed: 12.0) {
            VStack(alignment: .leading, spacing: 14) {
                HStack(spacing: 8) {
                    DoodleIcon(.starFill, size: 22, filled: true)
                    Text("ENDING")
                        .font(Theme.Fonts.label())
                        .tracking(1.4)
                        .foregroundColor(Theme.Palette.inkSoft)
                    Spacer()
                    SketchBadge(text: "Path \(sceneIndex)")
                }
                Text(title)
                    .font(Theme.Fonts.title())
                    .foregroundColor(Theme.Palette.ink)
                Text("You followed this path to its conclusion. Other roads remain. Want to take one?")
                    .font(Theme.Fonts.bodyItalic(14))
                    .foregroundColor(Theme.Palette.inkSoft)
                    .lineSpacing(4)

                VStack(spacing: 10) {
                    SketchButton(title: "Start Over", doodle: .undo, style: .primary) {
                        withAnimation { gameState.restart(); resetTransientState() }
                    }
                    SketchButton(title: "Share This Ending", doodle: .share, style: .secondary) {
                        showShareSheet = true
                    }
                    SketchButton(title: "Back to Library", style: .ghost) { dismiss() }
                }
                .padding(.top, 6)
            }
        }
        .padding(.horizontal, 24)
        .padding(.top, 8)
        .sheet(isPresented: $showShareSheet) {
            ShareSheet(activityItems: [shareText(endingTitle: title)])
        }
    }

    private func shareText(endingTitle: String) -> String {
        "I got the \"\(endingTitle)\" ending in \(story.title) — a choose-your-own-adventure after \(story.sourceTitle), on StoryTime."
    }

    private func resetTransientState() {
        selectedChoiceIndex = nil
        consequenceVisible = false
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

// MARK: - Numbered choice row

private struct NumberedChoiceRow: View {
    let number: Int
    let text: String
    let selected: Bool
    let action: () -> Void

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
                    .lineSpacing(3)
                    .padding(.top, 6)
                Spacer(minLength: 0)
                DoodleIcon(.arrowRight, size: 16, color: Theme.Palette.inkSoft)
                    .padding(.top, 10)
                    .opacity(selected ? 1 : 0.4)
            }
            .padding(14)
            .frame(maxWidth: .infinity, alignment: .leading)
            .background(
                WobblyRect(jitter: 0.4, corner: 6,
                            seed: CGFloat(text.hashValue % 100))
                    .fill(selected ? Theme.Palette.butterDeep : Theme.Palette.mist.opacity(0.55))
            )
            .overlay(
                WobblyRect(jitter: 0.4, corner: 6,
                            seed: CGFloat(text.hashValue % 100))
                    .stroke(Theme.Palette.ink,
                            lineWidth: selected ? Theme.Stroke.bold : Theme.Stroke.line)
            )
        }
        .buttonStyle(.plain)
    }
}

// MARK: - Progress dots

private struct ProgressDots: View {
    let count: Int
    let filled: Int

    var body: some View {
        HStack(spacing: 4) {
            ForEach(0..<count, id: \.self) { i in
                Circle()
                    .stroke(Theme.Palette.ink, lineWidth: Theme.Stroke.line)
                    .background(
                        Circle()
                            .fill(i < filled ? Theme.Palette.ink : Color.clear)
                    )
                    .frame(width: 6, height: 6)
            }
        }
    }
}
