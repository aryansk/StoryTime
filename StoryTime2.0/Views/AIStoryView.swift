import SwiftUI

struct AIStoryView: View {
    @StateObject private var viewModel = AIStoryViewModel()
    @ObservedObject var settings: SettingsModel
    @State private var showingPromptSheet = false
    @State private var showingSaveSheet = false
    @State private var prompt = ""
    @Environment(\.colorScheme) var colorScheme
    
    var body: some View {
        ZStack {
            // Background
            settings.themeColor
                .opacity(colorScheme == .dark ? 0.8 : 0.3)
                .ignoresSafeArea()
            
            VStack(spacing: 0) {
                // Story Content
                ScrollViewReader { proxy in
                    ScrollView {
                        VStack(alignment: .leading, spacing: 24) {
                            if viewModel.storyHistory.isEmpty && viewModel.currentStory == nil {
                                AIStoryEmptyStateView(showingNewStorySheet: $showingPromptSheet)
                            } else {
                                StoryContentView(
                                    history: viewModel.storyHistory,
                                    currentStory: viewModel.currentStory,
                                    settings: settings
                                )
                                .id("content")
                                .onChange(of: viewModel.currentStory) {
                                    withAnimation {
                                        proxy.scrollTo("latest", anchor: .bottom)
                                    }
                                }
                            }
                        }
                        .padding()
                    }
                }
                
                // Bottom Controls
                BottomControlsView(
                    viewModel: viewModel,
                    settings: settings,
                    showingPromptSheet: $showingPromptSheet,
                    showingSaveSheet: $showingSaveSheet
                )
            }
        }
        .alert("Error", isPresented: .constant(viewModel.error != nil)) {
            Button("OK") { viewModel.error = nil }
        } message: {
            Text(viewModel.error ?? "")
        }
        .sheet(isPresented: $showingPromptSheet) {
            PromptSheetView(
                prompt: $prompt,
                showingPromptSheet: $showingPromptSheet,
                viewModel: viewModel
            )
        }
        .sheet(isPresented: $showingSaveSheet) {
            SaveStorySheet(viewModel: viewModel, isPresented: $showingSaveSheet)
        }
        .navigationTitle("AI Story Creator")
        .navigationBarTitleDisplayMode(.large)
        .toolbar {
            if !viewModel.storyHistory.isEmpty || viewModel.currentStory != nil {
                ToolbarItem(placement: .navigationBarTrailing) {
                    Button {
                        showingSaveSheet = true
                    } label: {
                        Image(systemName: "square.and.arrow.down")
                    }
                }
            }
        }
    }
}

// MARK: - Save Story Sheet

private struct SaveStorySheet: View {
    @ObservedObject var viewModel: AIStoryViewModel
    @Binding var isPresented: Bool
    @State private var title = ""
    @State private var tags = ""
    @State private var rating = 3
    
    var body: some View {
        NavigationView {
            Form {
                Section(header: Text("Story Details")) {
                    TextField("Story Title", text: $title)
                    TextField("Tags (comma separated)", text: $tags)
                    
                    HStack {
                        Text("Rating")
                        Spacer()
                        ForEach(1...5, id: \.self) { star in
                            Image(systemName: star <= rating ? "star.fill" : "star")
                                .foregroundColor(.yellow)
                                .onTapGesture {
                                    rating = star
                                }
                        }
                    }
                }
                
                Section {
                    Button("Save Story") {
                        viewModel.saveCurrentStory(
                            title: title.isEmpty ? "Untitled Story" : title,
                            tags: tags.split(separator: ",").map(String.init),
                            rating: rating
                        )
                        isPresented = false
                    }
                    .frame(maxWidth: .infinity)
                    .foregroundColor(.blue)
                }
            }
            .navigationTitle("Save Story")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button("Cancel") {
                        isPresented = false
                    }
                }
            }
        }
    }
}

// MARK: - Subviews

private struct AIStoryEmptyStateView: View {
    @Binding var showingNewStorySheet: Bool
    @Environment(\.colorScheme) var colorScheme
    
    var body: some View {
        VStack(spacing: 24) {
            Image(systemName: "wand.and.stars")
                .font(.system(size: 80))
                .foregroundColor(.blue)
                .symbolEffect(.bounce)
            
            VStack(spacing: 12) {
                Text("Create Your AI Story")
                    .font(.title.bold())
                
                Text("Start with a prompt and let AI create\na unique story just for you")
                    .font(.body)
                    .multilineTextAlignment(.center)
                    .foregroundColor(.secondary)
            }
            
            Button {
                showingNewStorySheet = true
            } label: {
                Label("Begin Your Journey", systemImage: "plus.circle.fill")
                    .font(.headline)
                    .foregroundColor(.white)
                    .frame(maxWidth: .infinity)
                    .padding()
                    .background(
                        RoundedRectangle(cornerRadius: 12)
                            .fill(Color.blue)
                            .shadow(radius: 5)
                    )
                    .padding(.horizontal)
            }
        }
        .frame(maxWidth: .infinity, maxHeight: .infinity)
        .padding(.top, 100)
    }
}

private struct StoryContentView: View {
    let history: [AIStory]
    let currentStory: AIStory?
    let settings: SettingsModel
    @Environment(\.colorScheme) var colorScheme
    
    var body: some View {
        VStack(alignment: .leading, spacing: 24) {
            // Story History
            ForEach(history) { story in
                StorySegmentView(story: story, settings: settings)
            }
            
            // Current Story
            if let current = currentStory {
                StorySegmentView(story: current, settings: settings, isTyping: true)
            }
        }
    }
}

private struct StorySegmentView: View {
    let story: AIStory
    let settings: SettingsModel
    var isTyping: Bool = false
    @Environment(\.colorScheme) var colorScheme
    
    var body: some View {
        VStack(alignment: .leading, spacing: 16) {
            if isTyping {
                TypewriterText(text: story.text)
                    .font(.custom(settings.selectedFontName, size: settings.textSize))
            } else {
                Text(story.text)
                    .font(.custom(settings.selectedFontName, size: settings.textSize))
            }
        }
        .padding()
        .background(
            RoundedRectangle(cornerRadius: 12)
                .fill(colorScheme == .dark ? Color.black.opacity(0.6) : Color.white.opacity(0.8))
                .shadow(radius: 5)
        )
    }
}

private struct BottomControlsView: View {
    @ObservedObject var viewModel: AIStoryViewModel
    let settings: SettingsModel
    @Binding var showingPromptSheet: Bool
    @Binding var showingSaveSheet: Bool
    @Environment(\.colorScheme) var colorScheme
    
    var body: some View {
        VStack(spacing: 16) {
            if viewModel.isLoading {
                ProgressView("Generating story...")
                    .padding()
            } else if let story = viewModel.currentStory {
                ForEach(story.choices) { choice in
                    ChoiceButton(
                        choice: choice,
                        settings: settings
                    ) {
                        Task {
                            await viewModel.generateStory(prompt: choice.prompt)
                        }
                    }
                }
                
                Button {
                    showingSaveSheet = true
                } label: {
                    Label("Save Story", systemImage: "square.and.arrow.down")
                        .font(.subheadline)
                        .foregroundColor(.blue)
                }
            } else {
                StartButton(
                    storyHistory: viewModel.storyHistory,
                    showingPromptSheet: $showingPromptSheet
                )
            }
        }
        .padding()
        .background(
            Rectangle()
                .fill(colorScheme == .dark ? Color.black.opacity(0.8) : Color.white.opacity(0.95))
                .shadow(radius: 10, y: -5)
        )
    }
}

private struct ChoiceButton: View {
    let choice: AIStoryChoice
    let settings: SettingsModel
    let action: () -> Void
    @Environment(\.colorScheme) var colorScheme
    
    var body: some View {
        Button(action: action) {
            Text(choice.text)
                .font(.custom(settings.selectedFontName, size: settings.textSize - 2))
                .foregroundColor(.primary)
                .multilineTextAlignment(.leading)
                .padding()
                .frame(maxWidth: .infinity, alignment: .leading)
                .background(
                    RoundedRectangle(cornerRadius: 12)
                        .fill(colorScheme == .dark ? Color.black.opacity(0.6) : Color.white)
                        .shadow(radius: 5)
                )
        }
    }
}

private struct StartButton: View {
    let storyHistory: [AIStory]
    @Binding var showingPromptSheet: Bool
    
    var body: some View {
        Button(action: { showingPromptSheet = true }) {
            Label(storyHistory.isEmpty ? "Start Your Story" : "Continue Story", systemImage: "plus.circle.fill")
                .font(.headline)
                .foregroundColor(.white)
                .padding()
                .frame(maxWidth: .infinity)
                .background(
                    RoundedRectangle(cornerRadius: 12)
                        .fill(Color.blue)
                        .shadow(radius: 5)
                )
        }
    }
}

private struct PromptSheetView: View {
    @Binding var prompt: String
    @Binding var showingPromptSheet: Bool
    @ObservedObject var viewModel: AIStoryViewModel
    @Environment(\.colorScheme) var colorScheme
    @FocusState private var isPromptFocused: Bool
    
    var body: some View {
        NavigationView {
            VStack(spacing: 20) {
                Text("What would you like to happen next?")
                    .font(.headline)
                
                TextEditor(text: $prompt)
                    .frame(height: 150)
                    .padding(8)
                    .background(
                        RoundedRectangle(cornerRadius: 8)
                            .fill(colorScheme == .dark ? Color.black.opacity(0.3) : Color(.systemGray6))
                    )
                    .focused($isPromptFocused)
                
                Button("Generate Story") {
                    Task {
                        await viewModel.generateStory(prompt: prompt)
                        showingPromptSheet = false
                        prompt = ""
                    }
                }
                .font(.headline)
                .foregroundColor(.white)
                .padding()
                .frame(maxWidth: .infinity)
                .background(
                    RoundedRectangle(cornerRadius: 12)
                        .fill(Color.blue)
                        .shadow(radius: 5)
                )
                .disabled(prompt.isEmpty)
            }
            .padding()
            .navigationTitle("Story Prompt")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button("Cancel") {
                        showingPromptSheet = false
                    }
                }
            }
            .onAppear {
                isPromptFocused = true
            }
        }
    }
} 
