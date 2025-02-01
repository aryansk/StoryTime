import SwiftUI

struct StoryEditorView: View {
    @State var story: UserStory
    @ObservedObject var settings: SettingsModel
    @State private var showingNewScenarioSheet = false
    @State private var showingEditDetailsSheet = false
    @State private var showingDeleteAlert = false
    @State private var showingDeleteStoryAlert = false
    @State private var scenarioToDelete: UserScenario?
    @State private var isDragging = false
    @Environment(\.dismiss) var dismiss
    @StateObject private var viewModel = StoryCreatorViewModel()
    @State private var navigateToFirstScenario = false
    
    var body: some View {
        ScrollView {
            VStack(spacing: 24) {
                // Story Header
                StoryHeaderSection(
                    story: story,
                    showingEditDetailsSheet: $showingEditDetailsSheet,
                    onDelete: { showingDeleteStoryAlert = true }
                )
                
                // Chapters Section
                VStack(alignment: .leading, spacing: 16) {
                    HStack {
                        Text("Chapters (\(story.scenarios.count))")
                            .font(.title2.bold())
                        
                        Spacer()
                        
                        Button(action: { showingNewScenarioSheet = true }) {
                            Label("Add Chapter", systemImage: "plus.circle.fill")
                                .font(.subheadline.bold())
                                .foregroundColor(.blue)
                        }
                    }
                    .padding(.horizontal)
                    
                    if story.scenarios.isEmpty {
                        EmptyChaptersView(
                            showingNewScenarioSheet: $showingNewScenarioSheet
                        )
                    } else {
                        LazyVStack(spacing: 16) {
                            ForEach(Array(story.scenarios.enumerated()), id: \.element.id) { index, scenario in
                                ChapterCard(
                                    scenario: scenario,
                                    chapterNumber: index + 1,
                                    settings: settings,
                                    onDelete: {
                                        scenarioToDelete = scenario
                                        showingDeleteAlert = true
                                    }
                                )
                            }
                        }
                        .padding(.horizontal)
                    }
                }
            }
            .padding(.vertical)
        }
        .background(Color(UIColor.systemGroupedBackground))
        .navigationTitle("Edit Story")
        .navigationBarTitleDisplayMode(.large)
        .toolbar {
            ToolbarItem(placement: .navigationBarTrailing) {
                Menu {
                    Button {
                        showingEditDetailsSheet = true
                    } label: {
                        Label("Edit Details", systemImage: "pencil")
                    }
                    
                    Button {
                        // Share functionality
                        shareStory()
                    } label: {
                        Label("Share Story", systemImage: "square.and.arrow.up")
                    }
                    
                    Button {
                        // Export functionality
                        exportStory()
                    } label: {
                        Label("Export Story", systemImage: "arrow.down.doc")
                    }
                    
                    Divider()
                    
                    Button(role: .destructive) {
                        showingDeleteStoryAlert = true
                    } label: {
                        Label("Delete Story", systemImage: "trash")
                    }
                } label: {
                    Image(systemName: "ellipsis.circle")
                        .font(.system(size: 20))
                }
            }
        }
        .sheet(isPresented: $showingNewScenarioSheet) {
            NewScenarioView(story: $story, settings: settings)
        }
        .sheet(isPresented: $showingEditDetailsSheet) {
            EditStoryDetailsView(story: $story, settings: settings)
        }
        .alert("Delete Chapter", isPresented: $showingDeleteAlert) {
            Button("Cancel", role: .cancel) {}
            Button("Delete", role: .destructive) {
                if let scenario = scenarioToDelete,
                   let index = story.scenarios.firstIndex(where: { $0.id == scenario.id }) {
                    story.scenarios.remove(at: index)
                    viewModel.saveStories()
                }
            }
        } message: {
            Text("Are you sure you want to delete this chapter? This action cannot be undone.")
        }
        .alert("Delete Story", isPresented: $showingDeleteStoryAlert) {
            Button("Cancel", role: .cancel) {}
            Button("Delete", role: .destructive) {
                viewModel.deleteStory(story)
                dismiss()
            }
        } message: {
            Text("Are you sure you want to delete this story? This action cannot be undone.")
        }
    }
    
    private func shareStory() {
        // Implement share functionality
        let storyText = """
        \(story.title)
        
        \(story.description)
        
        \(story.scenarios.map { "Chapter \($0.title):\n\($0.storyText)\n" }.joined())
        """
        
        let av = UIActivityViewController(
            activityItems: [storyText],
            applicationActivities: nil
        )
        
        if let windowScene = UIApplication.shared.connectedScenes.first as? UIWindowScene,
           let window = windowScene.windows.first,
           let rootVC = window.rootViewController {
            rootVC.present(av, animated: true)
        }
    }
    
    private func exportStory() {
        // Implement export functionality
        // This could be expanded to support different formats (PDF, DOCX, etc.)
        let storyText = """
        \(story.title)
        
        \(story.description)
        
        \(story.scenarios.map { "Chapter \($0.title):\n\($0.storyText)\n" }.joined())
        """
        
        let fileURL = FileManager.default.urls(for: .documentDirectory, in: .userDomainMask)[0]
            .appendingPathComponent("\(story.title).txt")
        
        do {
            try storyText.write(to: fileURL, atomically: true, encoding: .utf8)
            
            let av = UIActivityViewController(
                activityItems: [fileURL],
                applicationActivities: nil
            )
            
            if let windowScene = UIApplication.shared.connectedScenes.first as? UIWindowScene,
               let window = windowScene.windows.first,
               let rootVC = window.rootViewController {
                rootVC.present(av, animated: true)
            }
        } catch {
            print("Failed to export story: \(error)")
        }
    }
}

struct StoryHeaderSection: View {
    let story: UserStory
    @Binding var showingEditDetailsSheet: Bool
    let onDelete: () -> Void
    
    var body: some View {
        VStack(spacing: 16) {
            // Story Details
            HStack(alignment: .top) {
                VStack(alignment: .leading, spacing: 8) {
                    Text(story.title)
                        .font(.title.bold())
                        .foregroundColor(.primary)
                    
                    Text(story.description)
                        .font(.subheadline)
                        .foregroundColor(.secondary)
                        .fixedSize(horizontal: false, vertical: true)
                }
                
                Spacer()
                
                Menu {
                    Button {
                        showingEditDetailsSheet = true
                    } label: {
                        Label("Edit", systemImage: "pencil")
                    }
                    
                    Button(role: .destructive, action: onDelete) {
                        Label("Delete", systemImage: "trash")
                    }
                } label: {
                    Image(systemName: "ellipsis.circle.fill")
                        .font(.system(size: 24))
                        .foregroundColor(.secondary)
                }
            }
            
            Divider()
        }
        .padding(.horizontal)
    }
}

struct ChapterCard: View {
    let scenario: UserScenario
    let chapterNumber: Int
    let settings: SettingsModel
    let onDelete: () -> Void
    @State private var isExpanded = false
    @State private var isHovered = false
    
    var body: some View {
        VStack(alignment: .leading, spacing: 16) {
            // Chapter Header
            HStack {
                VStack(alignment: .leading, spacing: 4) {
                    Text("Chapter \(chapterNumber)")
                        .font(.caption)
                        .foregroundColor(.secondary)
                    
                    Text(scenario.title)
                        .font(.headline)
                        .foregroundColor(.primary)
                }
                
                Spacer()
                
                Menu {
                    NavigationLink(destination: ScenarioEditorView(scenario: scenario, settings: settings)) {
                        Label("Edit Chapter", systemImage: "pencil")
                    }
                    
                    Button(role: .destructive, action: onDelete) {
                        Label("Delete Chapter", systemImage: "trash")
                    }
                } label: {
                    Image(systemName: "ellipsis.circle.fill")
                        .font(.system(size: 20))
                        .foregroundColor(.secondary)
                }
            }
            
            // Preview Text
            Text(scenario.storyText)
                .font(.subheadline)
                .foregroundColor(.secondary)
                .lineLimit(isExpanded ? nil : 3)
            
            // Expand/Collapse Button
            if scenario.storyText.count > 150 {
                Button(action: { withAnimation { isExpanded.toggle() }}) {
                    HStack {
                        Text(isExpanded ? "Show Less" : "Show More")
                            .font(.caption.bold())
                        
                        Image(systemName: isExpanded ? "chevron.up" : "chevron.down")
                            .font(.caption.bold())
                    }
                    .foregroundColor(.blue)
                }
            }
            
            if !scenario.choices.isEmpty {
                VStack(alignment: .leading, spacing: 8) {
                    Text("Choices")
                        .font(.caption)
                        .foregroundColor(.secondary)
                    
                    ForEach(scenario.choices) { choice in
                        HStack(alignment: .top, spacing: 8) {
                            Image(systemName: "arrow.turn.right.down")
                                .font(.caption)
                                .foregroundColor(.secondary)
                            
                            VStack(alignment: .leading, spacing: 4) {
                                Text(choice.text)
                                .font(.subheadline)
                                    .foregroundColor(.primary)
                                
                                if !choice.consequence.isEmpty {
                                    Text(choice.consequence)
                                        .font(.caption)
                                        .foregroundColor(.secondary)
                                }
                            }
                        }
                    }
                }
                .padding(.top, 8)
            }
        }
        .padding()
        .frame(maxWidth: .infinity, alignment: .leading)
        .background(
            RoundedRectangle(cornerRadius: 16)
                .fill(Color(UIColor.secondarySystemGroupedBackground))
                .shadow(
                    color: .black.opacity(isHovered ? 0.1 : 0.05),
                    radius: isHovered ? 8 : 4,
                    y: isHovered ? 4 : 2
                )
        )
        .overlay(
            RoundedRectangle(cornerRadius: 16)
                .strokeBorder(Color.blue.opacity(isHovered ? 0.2 : 0.1), lineWidth: 1)
        )
        .onHover { hovering in
            withAnimation(.spring(response: 0.3)) {
                isHovered = hovering
            }
        }
    }
}

struct EmptyChaptersView: View {
    @Binding var showingNewScenarioSheet: Bool
    
    var body: some View {
        VStack(spacing: 16) {
            Image(systemName: "book.closed")
                .font(.system(size: 40))
                .foregroundColor(.blue.opacity(0.5))
            
            Text("No Chapters Yet")
                .font(.headline)
            
            Text("Start adding chapters to build your story")
                .font(.subheadline)
                .foregroundColor(.secondary)
                .multilineTextAlignment(.center)
                
                Button(action: { showingNewScenarioSheet = true }) {
                Text("Add First Chapter")
                    .font(.headline)
                    .foregroundColor(.white)
                    .padding(.horizontal, 24)
                    .padding(.vertical, 12)
                    .background(Color.blue)
                    .clipShape(Capsule())
            }
        }
        .frame(maxWidth: .infinity)
        .padding(40)
    }
}

struct EditStoryDetailsView: View {
    @Binding var story: UserStory
    let settings: SettingsModel
    @Environment(\.dismiss) private var dismiss
    @State private var title: String
    @State private var description: String
    
    init(story: Binding<UserStory>, settings: SettingsModel) {
        self._story = story
        self.settings = settings
        self._title = State(initialValue: story.wrappedValue.title)
        self._description = State(initialValue: story.wrappedValue.description)
    }
    
    var body: some View {
        NavigationView {
            Form {
                Section("Story Details") {
                    TextField("Title", text: $title)
                    TextField("Description", text: $description, axis: .vertical)
                        .lineLimit(3...6)
                }
            }
            .navigationTitle("Edit Story Details")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button("Cancel") { dismiss() }
                }
                ToolbarItem(placement: .confirmationAction) {
                    Button("Save") {
                        story.title = title
                        story.description = description
                        dismiss()
                    }
                    .disabled(title.isEmpty || description.isEmpty)
                }
            }
        }
    }
}

struct ScenarioEditorView: View {
    @State var scenario: UserScenario
    @ObservedObject var settings: SettingsModel
    @State private var showingNewChoiceSheet = false
    
    var body: some View {
        List {
            Section("Scenario Details") {
                VStack(alignment: .leading, spacing: 8) {
                    Text("Title: \(scenario.title)")
                        .font(.headline)
                        .foregroundColor(settings.isDarkMode ? .white : .black)
                    Text(scenario.storyText)
                        .font(.body)
                }
            }
            
            Section("Choices") {
                ForEach(scenario.choices) { choice in
                    VStack(alignment: .leading) {
                        Text(choice.text)
                            .font(.headline)
                            .foregroundColor(settings.isDarkMode ? .white : .black)
                        Text("Consequence: \(choice.consequence)")
                            .font(.subheadline)
                            .foregroundStyle(.secondary)
                    }
                }
                
                Button(action: { showingNewChoiceSheet = true }) {
                    Label("Add Choice", systemImage: "plus.circle")
                }
            }
        }
        .navigationTitle("Edit Scenario")
        .navigationBarTitleDisplayMode(.inline)
        .sheet(isPresented: $showingNewChoiceSheet) {
            NewChoiceView(scenario: $scenario, settings: settings)
        }
    }
}

struct NewScenarioView: View {
    @Binding var story: UserStory
    @ObservedObject var settings: SettingsModel
    @Environment(\.dismiss) var dismiss
    @State private var title = ""
    @State private var storyText = ""
    
    var body: some View {
        NavigationView {
            Form {
                TextField("Scenario Title", text: $title)
                    .foregroundColor(settings.isDarkMode ? .white : .black)
                TextField("Story Text", text: $storyText, axis: .vertical)
                    .lineLimit(5...10)
                    .foregroundColor(settings.isDarkMode ? .white : .black)
            }
            .navigationTitle("New Scenario")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button("Cancel") { dismiss() }
                }
                ToolbarItem(placement: .confirmationAction) {
                    Button("Add") {
                        let newScenario = UserScenario(
                            title: title,
                            storyText: storyText
                        )
                        story.scenarios.append(newScenario)
                        dismiss()
                    }
                    .disabled(title.isEmpty || storyText.isEmpty)
                }
            }
        }
    }
}

struct NewChoiceView: View {
    @Binding var scenario: UserScenario
    @ObservedObject var settings: SettingsModel
    @Environment(\.dismiss) var dismiss
    @State private var text = ""
    @State private var consequence = ""
    
    var body: some View {
        NavigationView {
            Form {
                TextField("Choice Text", text: $text)
                    .foregroundColor(settings.isDarkMode ? .white : .black)
                TextField("Consequence", text: $consequence, axis: .vertical)
                    .lineLimit(3...6)
                    .foregroundColor(settings.isDarkMode ? .white : .black)
            }
            .navigationTitle("New Choice")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button("Cancel") { dismiss() }
                }
                ToolbarItem(placement: .confirmationAction) {
                    Button("Add") {
                        let newChoice = UserChoice(
                            text: text,
                            consequence: consequence
                        )
                        scenario.choices.append(newChoice)
                        dismiss()
                    }
                    .disabled(text.isEmpty || consequence.isEmpty)
                }
            }
        }
    }
}

struct StoryBeginView: View {
    let story: UserStory
    let settings: SettingsModel
    @Environment(\.dismiss) private var dismiss
    @State private var isAnimating = false
    @State private var showContent = false
    @State private var scrollOffset: CGFloat = 0
    @State private var navigateToFirstScenario = false
    
    var body: some View {
        GeometryReader { geometry in
            ScrollView {
                VStack(spacing: 0) {
                    // Hero Section
                    ZStack(alignment: .bottom) {
                        // Background
                        LinearGradient(
                            colors: [
                                .blue.opacity(0.8),
                                .purple.opacity(0.8)
                            ],
                            startPoint: .topLeading,
                            endPoint: .bottomTrailing
                        )
                        .overlay {
                            // Dynamic circles background
                            ZStack {
                                Circle()
                                    .fill(.white.opacity(0.1))
                                    .frame(width: 150, height: 150)
                                    .offset(x: isAnimating ? 50 : -50, y: isAnimating ? -30 : 30)
                                    .blur(radius: 20)
                                
                                Circle()
                                    .fill(.white.opacity(0.1))
                                    .frame(width: 200, height: 200)
                                    .offset(x: isAnimating ? -50 : 50, y: isAnimating ? 30 : -30)
                                    .blur(radius: 25)
                            }
                        }
                        .frame(height: 300)
                        
                        // Story Icon and Title
                        VStack(spacing: 20) {
                            ZStack {
                                Circle()
                                    .fill(.ultraThinMaterial)
                                    .frame(width: 120, height: 120)
                                
                                Image(systemName: "book.pages.fill")
                                    .font(.system(size: 50))
                                    .foregroundColor(.white)
                            }
                            .offset(y: isAnimating ? 0 : 50)
                            .opacity(isAnimating ? 1 : 0)
                            
                            VStack(spacing: 8) {
                                Text(story.title)
                                    .font(.title.bold())
                                    .foregroundColor(.white)
                                
                                Text(story.description)
                                    .font(.subheadline)
                                    .foregroundColor(.white.opacity(0.9))
                                    .multilineTextAlignment(.center)
                                    .padding(.horizontal)
                            }
                            .offset(y: isAnimating ? 0 : 30)
                            .opacity(isAnimating ? 1 : 0)
                        }
                        .padding(.bottom, 40)
                    }
                    
                    // Content Section
                    VStack(spacing: 24) {
                        // Chapter Preview
                        if let firstChapter = story.scenarios.first {
                            VStack(alignment: .leading, spacing: 16) {
                                Text("Chapter Preview")
                                    .font(.title2.bold())
                                
                                Text(firstChapter.storyText)
                                    .font(.body)
                                    .foregroundColor(.secondary)
                                    .lineLimit(5)
                                    .padding()
                                    .frame(maxWidth: .infinity, alignment: .leading)
                                    .background(
                                        RoundedRectangle(cornerRadius: 16)
                                            .fill(Color(UIColor.secondarySystemGroupedBackground))
                                    )
                            }
                            .transition(.move(edge: .bottom).combined(with: .opacity))
                        }
                        
                        // Story Stats
                        HStack(spacing: 40) {
                            StoryStatItem(
                                icon: "book.closed.fill",
                                value: "\(story.scenarios.count)",
                                label: "Chapters"
                            )
                            
                            StoryStatItem(
                                icon: "arrow.triangle.branch",
                                value: "\(story.scenarios.reduce(0) { $0 + $1.choices.count })",
                                label: "Choices"
                            )
                        }
                        .padding(.vertical)
                        
                        // Begin Button
                        Button(action: {
                            withAnimation(.spring()) {
                                // Check if the story has at least one scenario
                                if story.scenarios.first != nil {
                                    navigateToFirstScenario = true
                                }
                            }
                        }) {
                            Text("Begin Story")
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
                        .padding(.top)
                    }
                    .padding(24)
                    .background(Color(UIColor.systemBackground))
                    .clipShape(
                        RoundedRectangle(cornerRadius: 32, style: .continuous)
                    )
                    .offset(y: -30)
                }
            }
            .ignoresSafeArea()
        }
        .navigationBarTitleDisplayMode(.inline)
        .toolbar {
            ToolbarItem(placement: .navigationBarLeading) {
                Button(action: { dismiss() }) {
                    Image(systemName: "xmark.circle.fill")
                        .font(.system(size: 24))
                        .foregroundColor(.white)
                }
            }
            
            ToolbarItem(placement: .navigationBarTrailing) {
                ShareLink(item: story.title) {
                    Image(systemName: "square.and.arrow.up.circle.fill")
                        .font(.system(size: 24))
                        .foregroundColor(.white)
                }
            }
        }
        .onAppear {
            withAnimation(.spring(response: 0.6, dampingFraction: 0.8)) {
                isAnimating = true
            }
        }

        // Add a hidden NavigationLink to trigger navigation to the first scenario's view
        if let firstScenario = story.scenarios.first {
            NavigationLink(
                destination: ScenarioEditorView(scenario: firstScenario, settings: settings),
                isActive: $navigateToFirstScenario,
                label: { EmptyView() }
            )
            .hidden()
        }
    }
}

struct StoryStatItem: View {
    let icon: String
    let value: String
    let label: String
    
    var body: some View {
        VStack(spacing: 8) {
            Image(systemName: icon)
                .font(.system(size: 24))
                .foregroundColor(.blue)
            
            Text(value)
                .font(.title2.bold())
            
            Text(label)
                .font(.subheadline)
                .foregroundColor(.secondary)
        }
        .frame(maxWidth: .infinity)
        .padding()
        .background(
            RoundedRectangle(cornerRadius: 16)
                .fill(Color(UIColor.secondarySystemGroupedBackground))
        )
    }
} 