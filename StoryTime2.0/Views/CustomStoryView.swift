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
    @State private var showingAllPrompts = false
    @State private var isAnimating = false
    
    var body: some View {
        ZStack {
            // Dynamic Background with smooth transition
            LinearGradient(
                colors: [
                    settings.themeColor.opacity(0.1),
                    Color(UIColor.systemBackground)
                ],
                startPoint: .top,
                endPoint: .bottom
            )
            .ignoresSafeArea()
            .animation(.spring(response: 0.6, dampingFraction: 0.8), value: settings.themeColor)
            
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
                                    HStack {
                                        Text("Quick Prompts")
                                            .font(.headline)
                                            .foregroundColor(.primary)
                                        
                                        Spacer()
                                        
                                        Button(action: { showingAllPrompts = true }) {
                                            HStack(spacing: 4) {
                                                Text("View All")
                                                    .font(.subheadline)
                                                Image(systemName: "chevron.right")
                                                    .font(.system(size: 12))
                                            }
                                            .foregroundColor(.purple)
                                        }
                                    }
                                    
                                    ScrollView(.horizontal, showsIndicators: false) {
                                        HStack(spacing: 12) {
                                            ForEach(QuickPrompt.samples.prefix(5), id: \.title) { prompt in
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
        .sheet(isPresented: $showingAllPrompts) {
            AllPromptsView(settings: settings) { selectedPrompt in
                self.prompt = selectedPrompt.prompt
                showingPromptSheet = true
                showingAllPrompts = false
            }
        }
        .navigationTitle("AI Story Creator")
        .navigationBarTitleDisplayMode(.large)
        .onAppear {
            isAnimating = true
        }
        .onChange(of: settings.selectedTheme) { oldValue, newValue in
            // Add haptic feedback for theme changes
            let generator = UIImpactFeedbackGenerator(style: .light)
            generator.impactOccurred()
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

struct QuickPrompt: Identifiable {
    let id = UUID()
    let title: String
    let description: String
    let prompt: String
    let icon: String
    let category: PromptCategory
    
    static let samples = [
        QuickPrompt(
            title: "Fantasy Adventure",
            description: "Embark on a magical journey",
            prompt: "Create a fantasy story about a young wizard discovering their powers",
            icon: "wand.and.stars",
            category: .fantasy
        ),
        QuickPrompt(
            title: "Mystery",
            description: "Solve an intriguing case",
            prompt: "Write a detective story set in a small town with a mysterious disappearance",
            icon: "magnifyingglass",
            category: .mystery
        ),
        QuickPrompt(
            title: "Sci-Fi",
            description: "Explore the unknown",
            prompt: "Tell a story about first contact with an alien civilization",
            icon: "star",
            category: .sciFi
        ),
        QuickPrompt(
            title: "Time Travel",
            description: "Change history's course",
            prompt: "Write a story about a historian who discovers a way to visit any moment in time",
            icon: "clock.fill",
            category: .sciFi
        ),
        QuickPrompt(
            title: "Cyberpunk",
            description: "High tech, low life",
            prompt: "Create a story in a neon-lit future where AI and humans coexist",
            icon: "cpu.fill",
            category: .sciFi
        ),
        QuickPrompt(
            title: "Horror",
            description: "Face your fears",
            prompt: "Tell a suspenseful story about strange occurrences in an abandoned mansion",
            icon: "moon.stars.fill",
            category: .horror
        ),
        QuickPrompt(
            title: "Adventure",
            description: "Discover hidden treasures",
            prompt: "Write about an archaeologist uncovering an ancient civilization's secrets",
            icon: "map.fill",
            category: .adventure
        ),
        QuickPrompt(
            title: "Superhero",
            description: "Become extraordinary",
            prompt: "Create a story about an ordinary person who suddenly develops unique abilities",
            icon: "bolt.fill",
            category: .action
        ),
        QuickPrompt(
            title: "Fairy Tale",
            description: "Once upon a time...",
            prompt: "Write a modern twist on a classic fairy tale with unexpected turns",
            icon: "sparkles",
            category: .fantasy
        ),
        QuickPrompt(
            title: "Post-Apocalyptic",
            description: "Survive the aftermath",
            prompt: "Tell a story about rebuilding society after a global catastrophe",
            icon: "sunrise.fill",
            category: .sciFi
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

// Add AllPromptsView
struct AllPromptsView: View {
    @Environment(\.dismiss) private var dismiss
    @Environment(\.colorScheme) private var colorScheme
    let settings: SettingsModel
    let onPromptSelected: (QuickPrompt) -> Void
    @State private var searchText = ""
    @State private var selectedCategory: PromptCategory = .all
    @State private var showingPromptDetail: QuickPrompt?
    
    var filteredPrompts: [QuickPrompt] {
        let filtered = QuickPrompt.samples.filter { prompt in
            if searchText.isEmpty { return true }
            return prompt.title.localizedCaseInsensitiveContains(searchText) ||
                   prompt.description.localizedCaseInsensitiveContains(searchText)
        }
        
        if selectedCategory == .all {
            return filtered
        }
        return filtered.filter { $0.category == selectedCategory }
    }
    
    var featuredPrompts: [QuickPrompt] {
        QuickPrompt.samples.prefix(3).map { $0 }
    }
    
    var body: some View {
        NavigationView {
            ScrollView {
                VStack(spacing: 24) {
                    // Featured Section - Now always visible
                    VStack(alignment: .leading, spacing: 16) {
                        Text("Featured Prompts")
                            .font(.title2.bold())
                            .padding(.horizontal)
                        
                        ScrollView(.horizontal, showsIndicators: false) {
                            HStack(spacing: 16) {
                                ForEach(featuredPrompts, id: \.title) { prompt in
                                    FeaturedPromptCard(prompt: prompt) {
                                        showingPromptDetail = prompt
                                    }
                                }
                            }
                            .padding(.horizontal)
                        }
                    }
                    
                    // Categories
                    VStack(alignment: .leading, spacing: 12) {
                        Text("Categories")
                            .font(.title3.bold())
                            .padding(.horizontal)
                        
                        ScrollView(.horizontal, showsIndicators: false) {
                            HStack(spacing: 12) {
                                ForEach(PromptCategory.allCases, id: \.self) { category in
                                    EnhancedCategoryPill(
                                        category: category,
                                        isSelected: selectedCategory == category,
                                        action: { selectedCategory = category }
                                    )
                                }
                            }
                            .padding(.horizontal)
                        }
                    }
                    
                    // All Prompts Grid
                    VStack(alignment: .leading, spacing: 16) {
                        Text(selectedCategory == .all ? "All Prompts" : selectedCategory.name)
                            .font(.title3.bold())
                            .padding(.horizontal)
                        
                        if filteredPrompts.isEmpty {
                            EmptyPromptView(searchText: searchText)
                        } else {
                            LazyVGrid(
                                columns: [
                                    GridItem(.adaptive(minimum: 160), spacing: 16)
                                ],
                                spacing: 16
                            ) {
                                ForEach(filteredPrompts, id: \.title) { prompt in
                                    EnhancedPromptCard(prompt: prompt) {
                                        showingPromptDetail = prompt
                                    }
                                }
                            }
                            .padding(.horizontal)
                        }
                    }
                }
                .padding(.vertical)
            }
            .navigationTitle("Story Prompts")
            .navigationBarTitleDisplayMode(.large)
            .searchable(
                text: $searchText,
                placement: .navigationBarDrawer,
                prompt: "Search prompts"
            )
            .toolbar {
                ToolbarItem(placement: .navigationBarTrailing) {
                    Button("Done") { dismiss() }
                }
            }
        }
        .sheet(item: $showingPromptDetail, content: { prompt in
            PromptDetailView(
                prompt: prompt,
                settings: settings,
                onSelect: { selectedPrompt in
                    onPromptSelected(selectedPrompt)
                }
            )
        })
    }
}

struct EnhancedCategoryPill: View {
    let category: PromptCategory
    let isSelected: Bool
    let action: () -> Void
    @State private var isHovered = false
    
    var body: some View {
        Button(action: action) {
            HStack(spacing: 8) {
                Image(systemName: category.icon)
                    .font(.system(size: 16, weight: .medium))
                Text(category.name)
                    .font(.system(size: 16, weight: .medium))
            }
            .padding(.horizontal, 16)
            .padding(.vertical, 12)
            .background(
                RoundedRectangle(cornerRadius: 16)
                    .fill(isSelected ? Color.purple : Color.purple.opacity(0.1))
                    .shadow(
                        color: isSelected ? Color.purple.opacity(0.3) : .clear,
                        radius: 8,
                        y: 4
                    )
            )
            .foregroundColor(isSelected ? .white : .purple)
            .scaleEffect(isHovered ? 0.98 : 1)
        }
        .buttonStyle(.plain)
        .onHover { hovering in
            withAnimation(.spring(response: 0.3)) {
                isHovered = hovering
            }
        }
    }
}

struct FeaturedPromptCard: View {
    let prompt: QuickPrompt
    let action: () -> Void
    @State private var isHovered = false
    
    var body: some View {
        Button(action: action) {
            VStack(alignment: .leading, spacing: 12) {
                // Icon
                ZStack {
                    Circle()
                        .fill(LinearGradient(
                            colors: [.purple.opacity(0.2), .blue.opacity(0.2)],
                            startPoint: .topLeading,
                            endPoint: .bottomTrailing
                        ))
                        .frame(width: 50, height: 50)
                    
                    Image(systemName: prompt.icon)
                        .font(.system(size: 24))
                        .foregroundColor(.purple)
                }
                
                VStack(alignment: .leading, spacing: 8) {
                    Text(prompt.title)
                        .font(.headline)
                        .foregroundColor(.primary)
                    
                    Text(prompt.description)
                        .font(.subheadline)
                        .foregroundColor(.secondary)
                        .lineLimit(2)
                    
                    Text("Featured")
                        .font(.caption.weight(.medium))
                        .padding(.horizontal, 8)
                        .padding(.vertical, 4)
                        .background(
                            Capsule()
                                .fill(.purple.opacity(0.1))
                        )
                        .foregroundColor(.purple)
                }
            }
            .frame(width: 200)
            .padding()
            .background(
                RoundedRectangle(cornerRadius: 20)
                    .fill(Color(UIColor.secondarySystemBackground))
                    .shadow(color: .black.opacity(0.1), radius: isHovered ? 10 : 5, y: isHovered ? 5 : 2)
            )
            .scaleEffect(isHovered ? 0.98 : 1)
        }
        .buttonStyle(.plain)
        .onHover { hovering in
            withAnimation(.spring(response: 0.3)) {
                isHovered = hovering
            }
        }
    }
}

struct EnhancedPromptCard: View {
    let prompt: QuickPrompt
    let action: () -> Void
    @State private var isHovered = false
    
    var body: some View {
        Button(action: action) {
            VStack(alignment: .leading, spacing: 12) {
                HStack {
                    Image(systemName: prompt.icon)
                        .font(.system(size: 20))
                        .foregroundColor(.purple)
                    
                    Spacer()
                    
                    Image(systemName: "chevron.right.circle.fill")
                        .font(.system(size: 20))
                        .foregroundColor(.purple.opacity(0.3))
                        .opacity(isHovered ? 1 : 0)
                }
                
                VStack(alignment: .leading, spacing: 8) {
                    Text(prompt.title)
                        .font(.headline)
                        .foregroundColor(.primary)
                    
                    Text(prompt.description)
                        .font(.subheadline)
                        .foregroundColor(.secondary)
                        .lineLimit(2)
                }
            }
            .padding()
            .frame(height: 140)
            .frame(maxWidth: .infinity)
            .background(
                RoundedRectangle(cornerRadius: 16)
                    .fill(Color(UIColor.secondarySystemBackground))
                    .shadow(color: .black.opacity(isHovered ? 0.1 : 0.05), radius: isHovered ? 8 : 4, y: isHovered ? 4 : 2)
            )
            .overlay(
                RoundedRectangle(cornerRadius: 16)
                    .strokeBorder(Color.purple.opacity(isHovered ? 0.3 : 0.1), lineWidth: 1)
            )
            .scaleEffect(isHovered ? 0.98 : 1)
        }
        .buttonStyle(.plain)
        .onHover { hovering in
            withAnimation(.spring(response: 0.3)) {
                isHovered = hovering
            }
        }
    }
}

struct PromptDetailView: View {
    let prompt: QuickPrompt
    let settings: SettingsModel
    let onSelect: (QuickPrompt) -> Void
    @Environment(\.dismiss) private var dismiss
    
    var body: some View {
        NavigationView {
            ScrollView {
                VStack(spacing: 24) {
                    // Header
                    VStack(spacing: 16) {
                        ZStack {
                            Circle()
                                .fill(LinearGradient(
                                    colors: [.purple.opacity(0.2), .blue.opacity(0.2)],
                                    startPoint: .topLeading,
                                    endPoint: .bottomTrailing
                                ))
                                .frame(width: 80, height: 80)
                            
                            Image(systemName: prompt.icon)
                                .font(.system(size: 40))
                                .foregroundColor(.purple)
                        }
                        
                        Text(prompt.title)
                            .font(.title.bold())
                        
                        Text(prompt.description)
                            .font(.title3)
                            .foregroundColor(.secondary)
                            .multilineTextAlignment(.center)
                    }
                    .padding(.top)
                    
                    // Category Badge
                    HStack {
                        Image(systemName: prompt.category.icon)
                        Text(prompt.category.name)
                    }
                    .font(.subheadline.weight(.medium))
                    .padding(.horizontal, 16)
                    .padding(.vertical, 8)
                    .background(
                        Capsule()
                            .fill(.purple.opacity(0.1))
                    )
                    .foregroundColor(.purple)
                    
                    // Prompt Preview
                    VStack(alignment: .leading, spacing: 12) {
                        Text("Story Prompt")
                            .font(.headline)
                            .foregroundColor(.secondary)
                        
                        Text(prompt.prompt)
                            .font(.body)
                            .padding()
                            .frame(maxWidth: .infinity, alignment: .leading)
                            .background(
                                RoundedRectangle(cornerRadius: 12)
                                    .fill(Color(UIColor.tertiarySystemBackground))
                            )
                    }
                    .padding(.horizontal)
                    
                    // Start Button
                    Button(action: {
                        onSelect(prompt)
                        dismiss()
                    }) {
                        Text("Start Story")
                            .font(.headline)
                            .foregroundColor(.white)
                            .frame(maxWidth: .infinity)
                            .padding()
                            .background(
                                LinearGradient(
                                    colors: [.purple, .purple.opacity(0.8)],
                                    startPoint: .leading,
                                    endPoint: .trailing
                                )
                            )
                            .clipShape(Capsule())
                            .shadow(color: .purple.opacity(0.3), radius: 8, y: 4)
                    }
                    .padding(.horizontal)
                }
            }
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .navigationBarTrailing) {
                    Button("Done") { dismiss() }
                }
            }
        }
    }
}

struct EmptyPromptView: View {
    let searchText: String
    
    var body: some View {
        VStack(spacing: 16) {
            Image(systemName: "magnifyingglass")
                .font(.system(size: 40))
                .foregroundColor(.purple.opacity(0.5))
            
            Text(searchText.isEmpty ? "No prompts in this category" : "No matching prompts")
                .font(.headline)
            
            Text(searchText.isEmpty ? "Try selecting a different category" : "Try a different search term")
                .font(.subheadline)
                .foregroundColor(.secondary)
        }
        .frame(maxWidth: .infinity)
        .padding(.vertical, 40)
    }
}

// Add category icons
extension PromptCategory {
    var icon: String {
        switch self {
        case .all: return "square.stack.3d.up"
        case .fantasy: return "wand.and.stars"
        case .mystery: return "magnifyingglass"
        case .sciFi: return "cpu"
        case .horror: return "moon.stars"
        case .adventure: return "map"
        case .action: return "bolt"
        case .other: return "sparkles"
        }
    }
}

enum PromptCategory: CaseIterable {
    case all
    case fantasy
    case mystery
    case sciFi
    case horror
    case adventure
    case action
    case other
    
    var name: String {
        switch self {
        case .all: return "All"
        case .fantasy: return "Fantasy"
        case .mystery: return "Mystery"
        case .sciFi: return "Sci-Fi"
        case .horror: return "Horror"
        case .adventure: return "Adventure"
        case .action: return "Action"
        case .other: return "Other"
        }
    }
} 
