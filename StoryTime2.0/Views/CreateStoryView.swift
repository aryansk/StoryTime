import SwiftUI

// MARK: - Create Story
//
// Two-tabbed sheet for adding a personal story to the catalog:
//   1. Write — a small structured form for a hand-authored mini-story
//      (5 decision scenes, 2 endings).
//   2. Generate with AI — sends the title + premise to Anthropic, parses
//      the returned JSON, and saves the result locally.

struct CreateStoryView: View {
    @ObservedObject var settings: SettingsModel
    @EnvironmentObject var personalStore: PersonalStoriesStore
    @Environment(\.dismiss) private var dismiss

    enum Mode: Hashable { case write, generate }
    @State private var mode: Mode = .generate

    var body: some View {
        NavigationStack {
            ZStack {
                PageBackground()
                ScrollView(showsIndicators: false) {
                    VStack(alignment: .leading, spacing: 20) {
                        header
                        modePicker
                        if mode == .write {
                            WriteStoryForm(onSaved: dismissAfterSave)
                        } else {
                            GenerateStoryForm(settings: settings,
                                              onSaved: dismissAfterSave)
                        }
                        Spacer(minLength: 60)
                    }
                    .padding(.horizontal, 24)
                    .padding(.top, 12)
                    .padding(.bottom, 40)
                }
            }
            .toolbar {
                ToolbarItem(placement: .topBarTrailing) {
                    Button("Close") { dismiss() }
                        .font(Theme.Fonts.headingMedium(14))
                        .foregroundColor(Theme.Palette.ink)
                }
            }
        }
    }

    private var header: some View {
        VStack(alignment: .leading, spacing: 6) {
            Text("Your")
                .font(Theme.Fonts.body(18))
                .foregroundColor(Theme.Palette.inkSoft)
            HStack(alignment: .bottom, spacing: 8) {
                Text("Story")
                    .font(Theme.Fonts.display())
                    .foregroundColor(Theme.Palette.ink)
                DoodleIcon(.sparkle, size: 36)
                    .jitter(amplitude: 0.4)
                Spacer()
            }
            Text("Add a story to your library. Choose how you want to make it.")
                .font(Theme.Fonts.body(14))
                .foregroundColor(Theme.Palette.inkSoft)
                .padding(.top, 2)
        }
    }

    private var modePicker: some View {
        HStack(spacing: 10) {
            SketchPill(title: "Generate with AI", selected: mode == .generate) {
                withAnimation(.easeOut(duration: 0.15)) { mode = .generate }
            }
            SketchPill(title: "Write Your Own", selected: mode == .write) {
                withAnimation(.easeOut(duration: 0.15)) { mode = .write }
            }
        }
    }

    private func dismissAfterSave() {
        dismiss()
    }
}

// MARK: - Write form

private struct WriteStoryForm: View {
    @EnvironmentObject var personalStore: PersonalStoriesStore
    var onSaved: () -> Void

    @State private var title: String = ""
    @State private var synopsis: String = ""
    @State private var kind: StoryKind = .movie
    @State private var genre: StoryGenre = .drama

    /// Five decision scenes: text + two choice labels each, plus two endings.
    @State private var scenes: [SceneDraft] = Array(repeating: SceneDraft(), count: 5)
    @State private var endingA = EndingDraft(title: "", text: "")
    @State private var endingB = EndingDraft(title: "", text: "")

    @State private var saveError: String? = nil

    var body: some View {
        VStack(alignment: .leading, spacing: 18) {
            SketchCard(seed: 9.1) {
                VStack(alignment: .leading, spacing: 10) {
                    Text("Basics")
                        .font(Theme.Fonts.label())
                        .foregroundColor(Theme.Palette.inkSoft)
                    SketchTextField(placeholder: "Title (e.g. Inception)", text: $title)
                    SketchTextField(placeholder: "One-line synopsis (second-person)", text: $synopsis)

                    HStack(spacing: 12) {
                        Picker("Kind", selection: $kind) {
                            ForEach(StoryKind.allCases, id: \.self) { k in
                                Text(k.displayName).tag(k)
                            }
                        }
                        .pickerStyle(.segmented)
                    }
                    Picker("Genre", selection: $genre) {
                        ForEach(StoryGenre.allCases.filter { $0 != .all }) { g in
                            Text(g.rawValue).tag(g)
                        }
                    }
                    .pickerStyle(.menu)
                }
            }

            ForEach(scenes.indices, id: \.self) { i in
                SketchCard(seed: 10.0 + Double(i)) {
                    VStack(alignment: .leading, spacing: 8) {
                        Text("Scene \(i + 1)")
                            .font(Theme.Fonts.label())
                            .foregroundColor(Theme.Palette.inkSoft)
                        SketchTextField(placeholder: "Scene title",
                                        text: scenesBinding(i, \.title))
                        SketchTextField(placeholder: "Scene text (one or two sentences)",
                                        text: scenesBinding(i, \.text))
                        SketchTextField(placeholder: "Choice A",
                                        text: scenesBinding(i, \.choiceA))
                        SketchTextField(placeholder: "Choice B",
                                        text: scenesBinding(i, \.choiceB))
                    }
                }
            }

            SketchCard(seed: 20.5) {
                VStack(alignment: .leading, spacing: 8) {
                    Text("Ending A")
                        .font(Theme.Fonts.label())
                        .foregroundColor(Theme.Palette.inkSoft)
                    SketchTextField(placeholder: "Ending A title", text: $endingA.title)
                    SketchTextField(placeholder: "Ending A text", text: $endingA.text)
                }
            }
            SketchCard(seed: 20.9) {
                VStack(alignment: .leading, spacing: 8) {
                    Text("Ending B")
                        .font(Theme.Fonts.label())
                        .foregroundColor(Theme.Palette.inkSoft)
                    SketchTextField(placeholder: "Ending B title", text: $endingB.title)
                    SketchTextField(placeholder: "Ending B text", text: $endingB.text)
                }
            }

            if let err = saveError {
                Text(err)
                    .font(Theme.Fonts.bodyItalic(13))
                    .foregroundColor(Theme.Palette.ink)
            }

            SketchButton(title: "Save to Library", doodle: .bookmarkFill, style: .primary) {
                save()
            }
        }
    }

    private func scenesBinding<T>(_ i: Int, _ keyPath: WritableKeyPath<SceneDraft, T>) -> Binding<T> {
        Binding(
            get: { scenes[i][keyPath: keyPath] },
            set: { scenes[i][keyPath: keyPath] = $0 }
        )
    }

    private func save() {
        saveError = nil
        let trimmed = title.trimmingCharacters(in: .whitespaces)
        guard !trimmed.isEmpty else {
            saveError = "Give the story a title."
            return
        }
        guard !endingA.title.isEmpty, !endingB.title.isEmpty else {
            saveError = "Both endings need a title."
            return
        }
        // Build a linear-spine story: each scene's two choices go to the
        // next scene; the last scene's choices go to the two endings.
        var nodes: [StoryNode] = []
        for (i, s) in scenes.enumerated() {
            let id = "s\(i + 1)"
            let nextTarget: String = (i == scenes.count - 1) ? "end_a" : "s\(i + 2)"
            let otherTarget: String = (i == scenes.count - 1) ? "end_b" : "s\(i + 2)"
            let choices: [StoryChoice] = [
                StoryChoice(text: s.choiceA.isEmpty ? "Take action" : s.choiceA,
                            consequence: "You chose to move forward.",
                            nextNodeId: nextTarget),
                StoryChoice(text: s.choiceB.isEmpty ? "Stay still" : s.choiceB,
                            consequence: "You chose another way.",
                            nextNodeId: otherTarget),
            ]
            nodes.append(StoryNode(
                id: id,
                text: s.text.isEmpty ? "A scene unfolds." : s.text,
                sceneTitle: s.title.isEmpty ? "Scene \(i + 1)" : s.title,
                choices: choices,
                isEnding: false,
                endingTitle: nil
            ))
        }
        nodes.append(StoryNode(
            id: "end_a",
            text: endingA.text.isEmpty ? "The story ends here." : endingA.text,
            sceneTitle: endingA.title,
            choices: [],
            isEnding: true,
            endingTitle: endingA.title
        ))
        nodes.append(StoryNode(
            id: "end_b",
            text: endingB.text.isEmpty ? "The story ends here." : endingB.text,
            sceneTitle: endingB.title,
            choices: [],
            isEnding: true,
            endingTitle: endingB.title
        ))

        let id = PersonalStoriesStore.makeId(from: trimmed)
        let story = CatalogStory(
            id: id,
            title: trimmed,
            sourceTitle: trimmed,
            kind: kind,
            synopsis: synopsis.isEmpty ? "Your story." : synopsis,
            releaseYear: nil,
            addedAt: Date(),
            genre: genre,
            tags: ["personal"],
            rating: nil,
            loved: nil,
            nextStoryId: nil,
            startNodeId: "s1",
            nodes: nodes
        )
        personalStore.add(story)
        onSaved()
    }

    private struct SceneDraft: Hashable {
        var title: String = ""
        var text: String = ""
        var choiceA: String = ""
        var choiceB: String = ""
    }
    private struct EndingDraft: Hashable {
        var title: String
        var text: String
    }
}

// MARK: - Generate form

private struct GenerateStoryForm: View {
    @ObservedObject var settings: SettingsModel
    @EnvironmentObject var personalStore: PersonalStoriesStore
    var onSaved: () -> Void

    @State private var title: String = ""
    @State private var premise: String = ""
    @State private var kind: StoryKind = .movie
    @State private var genre: StoryGenre = .drama
    @State private var isGenerating = false
    @State private var status: String? = nil
    @State private var apiKeyDraft: String = ""

    var body: some View {
        VStack(alignment: .leading, spacing: 18) {
            SketchCard(seed: 30.1) {
                VStack(alignment: .leading, spacing: 10) {
                    Text("Anthropic API key")
                        .font(Theme.Fonts.label())
                        .foregroundColor(Theme.Palette.inkSoft)
                    SketchSecureField(placeholder: "sk-ant-…", text: apiKeyBinding)
                    Text("Stored on this device only. Get a key at console.anthropic.com.")
                        .font(Theme.Fonts.bodyItalic(12))
                        .foregroundColor(Theme.Palette.inkSoft)
                }
            }

            SketchCard(seed: 31.1) {
                VStack(alignment: .leading, spacing: 10) {
                    Text("Story")
                        .font(Theme.Fonts.label())
                        .foregroundColor(Theme.Palette.inkSoft)
                    SketchTextField(placeholder: "Title (the source movie/book)", text: $title)
                    SketchTextField(placeholder: "Optional premise (one line)",
                                    text: $premise)
                    HStack(spacing: 12) {
                        Picker("Kind", selection: $kind) {
                            ForEach(StoryKind.allCases, id: \.self) { k in
                                Text(k.displayName).tag(k)
                            }
                        }
                        .pickerStyle(.segmented)
                    }
                    Picker("Genre", selection: $genre) {
                        ForEach(StoryGenre.allCases.filter { $0 != .all }) { g in
                            Text(g.rawValue).tag(g)
                        }
                    }
                    .pickerStyle(.menu)
                }
            }

            if let status = status {
                Text(status)
                    .font(Theme.Fonts.bodyItalic(13))
                    .foregroundColor(Theme.Palette.inkSoft)
            }

            SketchButton(title: isGenerating ? "Generating…" : "Generate with Claude",
                         doodle: .sparkle, style: .primary) {
                Task { await generate() }
            }
            .disabled(isGenerating)
        }
    }

    private var apiKeyBinding: Binding<String> {
        Binding(
            get: { settings.anthropicAPIKey },
            set: { settings.anthropicAPIKey = $0 }
        )
    }

    private func generate() async {
        let trimmed = title.trimmingCharacters(in: .whitespaces)
        guard !trimmed.isEmpty else { status = "Add a title first."; return }
        // Daily-cap guard: a stolen key shouldn't be able to run up a bill.
        guard settings.recordAIGeneration() else {
            status = "You've hit today's generation cap (\(settings.aiDailyCap)). Try again tomorrow."
            return
        }
        isGenerating = true
        defer { isGenerating = false }
        status = "Asking Claude to write your story… (\(settings.aiGenerationsRemaining) left today)"
        do {
            let client = AnthropicClient(apiKey: settings.anthropicAPIKey)
            var story = try await client.generateStory(
                title: trimmed,
                premise: premise,
                kind: kind,
                genre: genre
            )
            // Ensure id is namespaced + dates are sane regardless of what
            // the model returned.
            story = renamed(story, newId: PersonalStoriesStore.makeId(from: trimmed))
            await MainActor.run {
                personalStore.add(story)
                status = nil
                onSaved()
            }
        } catch {
            settings.refundAIGeneration()
            status = (error as? LocalizedError)?.errorDescription ?? error.localizedDescription
        }
    }

    /// Force the namespaced id (the model sometimes invents its own).
    private func renamed(_ story: CatalogStory, newId: String) -> CatalogStory {
        CatalogStory(
            id: newId,
            title: story.title,
            sourceTitle: story.sourceTitle.isEmpty ? story.title : story.sourceTitle,
            kind: story.kind,
            synopsis: story.synopsis,
            releaseYear: story.releaseYear,
            addedAt: Date(),
            genre: story.genre,
            tags: story.tags,
            rating: nil,
            loved: nil,
            nextStoryId: nil,
            startNodeId: story.startNodeId,
            nodes: story.nodes
        )
    }
}
