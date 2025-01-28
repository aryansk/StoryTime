import SwiftUI

class CustomStoryViewModel: ObservableObject {
    private let geminiService = GeminiService()
    @Published var storyText: String = ""
    @Published var choices: [StoryChoice] = []
    @Published var isLoading: Bool = false
    @Published var error: String?
    
    @MainActor
    func generateStory(prompt: String) async {
        isLoading = true
        error = nil
        
        do {
            let response = try await geminiService.generateStoryContent(prompt: prompt)
            storyText = response.story_text
            choices = response.choices
        } catch {
            self.error = "Failed to generate story: \(error.localizedDescription)"
        }
        
        isLoading = false
    }
}

struct CustomStoryView: View {
    @StateObject private var viewModel = CustomStoryViewModel()
    @ObservedObject var settings: SettingsModel
    @State private var prompt: String = ""
    @State private var storyHistory: [(text: String, choices: [StoryChoice])] = []
    @State private var showingPromptSheet = false
    @State private var isAnimating = false
    
    var body: some View {
        ZStack {
            // Dynamic Background
            LinearGradient(
                colors: [
                    settings.themeColor.opacity(0.1),
                    Color(UIColor.systemBackground)
                ],
                startPoint: .top,
                endPoint: .bottom
            )
                .ignoresSafeArea()
            
            VStack(spacing: 0) {
                // Story Content
                ScrollView {
                    VStack(alignment: .leading, spacing: 24) {
                        if storyHistory.isEmpty && viewModel.storyText.isEmpty {
                            // Enhanced Initial State
                            VStack(spacing: 24) {
                                // Animated Icon
                                ZStack {
                                    Circle()
                                        .fill(settings.themeColor.opacity(0.1))
                                        .frame(width: 120, height: 120)
                                    
                                Image(systemName: "wand.and.stars")
                                        .font(.system(size: 50))
                                        .foregroundColor(.purple)
                                        .rotationEffect(.degrees(isAnimating ? 360 : 0))
                                        .animation(
                                            .linear(duration: 20).repeatForever(autoreverses: false),
                                            value: isAnimating
                                        )
                                }
                                
                                VStack(spacing: 12) {
                                Text("Create Your AI Story")
                                    .font(.title2.bold())
                                
                                Text("Start with a prompt and let AI create\na unique story just for you")
                                    .font(.body)
                                    .multilineTextAlignment(.center)
                                    .foregroundColor(.secondary)
                            }
                                
                                // Quick Prompts
                                VStack(alignment: .leading, spacing: 16) {
                                    Text("Quick Prompts")
                                        .font(.headline)
                                        .foregroundColor(.primary)
                                    
                                    ScrollView(.horizontal, showsIndicators: false) {
                                        HStack(spacing: 12) {
                                            ForEach(QuickPrompt.samples, id: \.title) { prompt in
                                                QuickPromptCard(
                                                    prompt: prompt,
                                                    action: {
                                                        self.prompt = prompt.prompt
                                                        showingPromptSheet = true
                                                    }
                                                )
                                            }
                                        }
                                    }
                                }
                                .padding(.top, 8)
                            }
                            .frame(maxWidth: .infinity, maxHeight: .infinity)
                            .padding(.top, 60)
                        } else {
                            SequentialStoryContainer(
                                storyHistory: storyHistory,
                                currentText: viewModel.storyText,
                                settings: settings
                            )
                        }
                    }
                    .padding()
                }
                
                // Bottom Controls
                VStack(spacing: 16) {
                    if viewModel.isLoading {
                        LoadingView()
                    } else if !viewModel.choices.isEmpty {
                        // Story Choices
                        ForEach(viewModel.choices, id: \.text) { choice in
                            AIStoryChoiceButton(
                                choice: choice,
                                settings: settings
                            ) {
                                storyHistory.append((viewModel.storyText, viewModel.choices))
                                Task {
                                    await viewModel.generateStory(prompt: choice.prompt)
                                }
                            }
                        }
                    } else {
                        // Start/Continue Button
                        Button(action: { showingPromptSheet = true }) {
                            Label(
                                storyHistory.isEmpty ? "Start Your Story" : "Continue Story",
                                systemImage: "plus.circle.fill"
                            )
                                .font(.headline)
                                .foregroundColor(.white)
                            .frame(maxWidth: .infinity)
                                .padding()
                            .background(
                                LinearGradient(
                                    colors: [.blue, .blue.opacity(0.8)],
                                    startPoint: .leading,
                                    endPoint: .trailing
                                )
                            )
                            .clipShape(Capsule())
                            .shadow(color: .blue.opacity(0.3), radius: 8, y: 4)
                        }
                        .buttonStyle(ScaleButtonStyle())
                    }
                }
                .padding()
                .background(
                    Rectangle()
                        .fill(.ultraThinMaterial)
                        .shadow(color: .black.opacity(0.05), radius: 8, y: -4)
                )
            }
        }
        .alert("Error", isPresented: .constant(viewModel.error != nil)) {
            Button("OK") { viewModel.error = nil }
        } message: {
            Text(viewModel.error ?? "")
        }
        .sheet(isPresented: $showingPromptSheet) {
            PromptInputView(
                prompt: $prompt,
                settings: settings,
                onSubmit: { promptText in
                    Task {
                        await viewModel.generateStory(prompt: promptText)
                    }
                }
            )
        }
        .navigationTitle("AI Story Creator")
        .navigationBarTitleDisplayMode(.large)
        .onAppear {
            isAnimating = true
        }
    }
}

// MARK: - Supporting Views

struct StorySegment: View {
    let text: String
    let settings: SettingsModel
    let index: Int?
    var isLatest: Bool
    @State private var isVisible = false
    
    var body: some View {
        VStack(alignment: .leading, spacing: 16) {
            // Chapter indicator with improved design
            HStack(spacing: 8) {
                if let index = index {
                    Circle()
                        .fill(isLatest ? .purple : .secondary)
                        .frame(width: 8, height: 8)
                    
                    Text("Chapter \(index + 1)")
                        .font(.subheadline.weight(.medium))
                        .foregroundColor(isLatest ? .primary : .secondary)
                }
            }
            
            // Story content with modern card design
            HStack(alignment: .top, spacing: 16) {
                // Vertical connection line
                if index != nil {
                    Rectangle()
                        .fill(Color.secondary.opacity(0.2))
                        .frame(width: 2)
                        .frame(maxHeight: .infinity)
                        .padding(.vertical, 8)
                }
                
                // Story content
                Text(text)
                    .font(.custom(settings.selectedFontName, size: settings.textSize))
                    .padding()
                    .frame(maxWidth: .infinity, alignment: .leading)
                    .background(
                        RoundedRectangle(cornerRadius: 16)
                            .fill(Color(UIColor.secondarySystemBackground))
                            .shadow(
                                color: .black.opacity(isLatest ? 0.1 : 0.05),
                                radius: isLatest ? 8 : 4,
                                y: 4
                            )
                    )
                    .overlay(
                        RoundedRectangle(cornerRadius: 16)
                            .strokeBorder(
                                isLatest ? Color.purple.opacity(0.3) : Color.clear,
                                lineWidth: 1
                            )
                    )
            }
        }
        .opacity(isVisible ? 1 : 0)
        .offset(y: isVisible ? 0 : 20)
        .onAppear {
            withAnimation(.spring(response: 0.6, dampingFraction: 0.7)) {
                isVisible = true
            }
        }
    }
}

struct AIStoryChoiceButton: View {
    let choice: StoryChoice
    let settings: SettingsModel
    let action: () -> Void
    @State private var isHovered = false
    @State private var isPressed = false
    
    var body: some View {
        Button(action: action) {
            HStack {
                Text(choice.text)
                    .font(.custom(settings.selectedFontName, size: settings.textSize - 2))
                    .foregroundColor(.primary)
                    .multilineTextAlignment(.leading)
                
                Spacer()
                
                Image(systemName: "chevron.right")
                    .font(.system(size: 14, weight: .semibold))
                    .foregroundColor(.secondary)
                    .opacity(isHovered ? 1 : 0.5)
                    .offset(x: isHovered ? 4 : 0)
            }
            .padding()
            .frame(maxWidth: .infinity, alignment: .leading)
            .background(
                RoundedRectangle(cornerRadius: 16)
                    .fill(Color(UIColor.secondarySystemBackground))
                    .shadow(
                        color: .black.opacity(isHovered ? 0.1 : 0.05),
                        radius: isHovered ? 8 : 4,
                        y: isHovered ? 4 : 2
                    )
            )
            .overlay(
                RoundedRectangle(cornerRadius: 16)
                    .strokeBorder(Color.purple.opacity(isHovered ? 0.4 : 0.2), lineWidth: 1)
            )
            .scaleEffect(isPressed ? 0.98 : 1)
        }
        .buttonStyle(.plain)
        .onHover { hovering in
            withAnimation(.spring(response: 0.3)) {
                isHovered = hovering
            }
        }
        .pressEvents {
            withAnimation(.spring(response: 0.2)) {
                isPressed = true
            }
        } onRelease: {
            withAnimation(.spring(response: 0.2)) {
                isPressed = false
            }
        }
    }
}

struct LoadingView: View {
    @State private var rotation: Double = 0
    
    var body: some View {
        VStack(spacing: 16) {
            ZStack {
                Circle()
                    .stroke(Color.purple.opacity(0.2), lineWidth: 4)
                    .frame(width: 44, height: 44)
                
                Circle()
                    .trim(from: 0, to: 0.7)
                    .stroke(Color.purple, lineWidth: 4)
                    .frame(width: 44, height: 44)
                    .rotationEffect(.degrees(rotation))
            }
            
            Text("Generating story...")
                .font(.headline)
                .foregroundColor(.secondary)
        }
        .onAppear {
            withAnimation(.linear(duration: 1).repeatForever(autoreverses: false)) {
                rotation = 360
            }
        }
    }
}

struct QuickPromptCard: View {
    let prompt: QuickPrompt
    let action: () -> Void
    
    var body: some View {
        Button(action: action) {
            VStack(alignment: .leading, spacing: 8) {
                Image(systemName: prompt.icon)
                    .font(.system(size: 24))
                    .foregroundColor(.purple)
                
                Text(prompt.title)
                    .font(.headline)
                    .foregroundColor(.primary)
                
                Text(prompt.description)
                    .font(.caption)
                    .foregroundColor(.secondary)
                    .lineLimit(2)
            }
            .frame(width: 160, height: 120)
            .padding()
            .background(
                RoundedRectangle(cornerRadius: 16)
                    .fill(Color(UIColor.secondarySystemBackground))
                    .overlay(
                        RoundedRectangle(cornerRadius: 16)
                            .strokeBorder(Color.purple.opacity(0.2), lineWidth: 1)
                    )
                    .shadow(color: .black.opacity(0.05), radius: 8, y: 4)
            )
        }
        .buttonStyle(ScaleButtonStyle())
    }
}

struct PromptInputView: View {
    @Binding var prompt: String
    let settings: SettingsModel
    let onSubmit: (String) -> Void
    @Environment(\.dismiss) private var dismiss
    
    var body: some View {
        NavigationView {
            VStack(spacing: 24) {
                Text("What's your story about?")
                    .font(.title2.bold())
                
                Text("Be creative! The more detailed your prompt,\nthe better the story will be.")
                    .font(.subheadline)
                    .foregroundColor(.secondary)
                    .multilineTextAlignment(.center)
                
                TextEditor(text: $prompt)
                    .font(.body)
                    .padding(12)
                    .frame(height: 150)
                    .background(
                        RoundedRectangle(cornerRadius: 12)
                            .fill(Color(UIColor.secondarySystemBackground))
                    )
                    .overlay(
                        RoundedRectangle(cornerRadius: 12)
                            .strokeBorder(Color(.systemGray4), lineWidth: 1)
                    )
                
                Button(action: {
                    onSubmit(prompt)
                    dismiss()
                    prompt = ""
                }) {
                    Text("Generate Story")
                    .font(.headline)
                    .foregroundColor(.white)
                        .frame(maxWidth: .infinity)
                    .padding()
                        .background(
                            LinearGradient(
                                colors: [.blue, .blue.opacity(0.8)],
                                startPoint: .leading,
                                endPoint: .trailing
                            )
                        )
                        .clipShape(Capsule())
                        .shadow(color: .blue.opacity(0.3), radius: 8, y: 4)
                }
                .buttonStyle(ScaleButtonStyle())
                .disabled(prompt.isEmpty)
                .opacity(prompt.isEmpty ? 0.6 : 1)
                }
                .padding()
                .navigationBarTitleDisplayMode(.inline)
                .toolbar {
                ToolbarItem(placement: .navigationBarTrailing) {
                        Button("Cancel") {
                        dismiss()
                    }
                }
            }
        }
    }
}

// MARK: - Models

struct QuickPrompt {
    let title: String
    let description: String
    let prompt: String
    let icon: String
    
    static let samples = [
        QuickPrompt(
            title: "Fantasy Adventure",
            description: "Embark on a magical journey",
            prompt: "Create a fantasy story about a young wizard discovering their powers",
            icon: "wand.and.stars"
        ),
        QuickPrompt(
            title: "Mystery",
            description: "Solve an intriguing case",
            prompt: "Write a detective story set in a small town with a mysterious disappearance",
            icon: "magnifyingglass"
        ),
        QuickPrompt(
            title: "Sci-Fi",
            description: "Explore the unknown",
            prompt: "Tell a story about first contact with an alien civilization",
            icon: "star"
        )
    ]
}

// Add a sequential story container
struct SequentialStoryContainer: View {
    let storyHistory: [(text: String, choices: [StoryChoice])]
    let currentText: String
    let settings: SettingsModel
    
    var body: some View {
        VStack(alignment: .leading, spacing: 32) {
            ForEach(Array(storyHistory.enumerated()), id: \.offset) { index, entry in
                StorySegment(
                    text: entry.text,
                    settings: settings,
                    index: index,
                    isLatest: false
                )
            }
            
            if !currentText.isEmpty {
                StorySegment(
                    text: currentText,
                    settings: settings,
                    index: storyHistory.count,
                    isLatest: true
                )
            }
        }
    }
}

// Add this helper for button press events
extension View {
    func pressEvents(onPress: @escaping () -> Void, onRelease: @escaping () -> Void) -> some View {
        self.simultaneousGesture(
            DragGesture(minimumDistance: 0)
                .onChanged { _ in
                    onPress()
                }
                .onEnded { _ in
                    onRelease()
                }
        )
    }
} 
