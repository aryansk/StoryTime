//
//  ContentView.swift
//  StoryTime2.0
//
//  Created by Aryan Signh on 27/01/25.
// version

import SwiftUI

struct ContentView: View {
    @StateObject private var userModel = UserModel()
    @StateObject private var settings = SettingsModel()
    @State private var showingSignUp = true
    @State private var selectedTab = 0
    
    var body: some View {
        TabView(selection: $selectedTab) {
            // Curated Stories Tab
            CuratedStoriesView(userModel: userModel, settings: settings)
                .tabItem {
                    Label("Stories", systemImage: "book.fill")
                }
                .tag(0)
                .tint(.orange)
            
            // AI Story Creator Tab
            NavigationStack {
                CustomStoryView(settings: settings)
            }
            .tabItem {
                Label("AI Stories", systemImage: "wand.and.stars")
            }
            .tag(1)
            .tint(.purple)
            
            // My Stories Tab
            MyStoriesView(settings: settings)
                .tabItem {
                    Label("My Stories", systemImage: "pencil")
                }
                .tag(2)
                .tint(.yellow)
            
            // Settings Tab
            SettingsTabView(settings: settings)
                .tabItem {
                    Label("Settings", systemImage: "gear")
                }
                .tag(3)
                .tint(.blue)
        }
        .sheet(isPresented: .constant(userModel.isFirstLaunch)) {
            SignUpView(userModel: userModel, isPresented: $showingSignUp)
        }
        .preferredColorScheme(settings.isDarkMode ? .dark : .light)
        .tint(tabColor(for: selectedTab))
        .onAppear {
            let appearance = UITabBarAppearance()
            appearance.shadowColor = .clear
            appearance.backgroundColor = .systemBackground
            UITabBar.appearance().scrollEdgeAppearance = appearance
            UITabBar.appearance().standardAppearance = appearance
        }
    }
    
    private func tabColor(for tab: Int) -> Color {
        switch tab {
        case 0: return .orange
        case 1: return .purple
        case 2: return .yellow
        case 3: return .blue
        default: return .blue
        }
    }
}


struct CategoryButton: View {
    let title: String
    let icon: String
    let isSelected: Bool
    let action: () -> Void
    @State private var isHovered = false
    
    var body: some View {
        Button(action: action) {
            HStack(spacing: 8) {
                Image(systemName: icon)
                    .font(.system(size: 16, weight: .medium))
                Text(title)
                    .font(.system(size: 16, weight: .medium))
            }
            .padding(.horizontal, 16)
            .padding(.vertical, 12)
            .background(
                RoundedRectangle(cornerRadius: 16)
                    .fill(isSelected ? Color.blue : Color.blue.opacity(0.1))
                    .shadow(
                        color: isSelected ? .blue.opacity(0.3) : .clear,
                        radius: 8,
                        y: 4
                    )
            )
            .foregroundColor(isSelected ? .white : .blue)
            .scaleEffect(isHovered ? 0.98 : 1)
        }
        .buttonStyle(.plain)
        .animation(.spring(response: 0.3), value: isSelected)
        .animation(.spring(response: 0.3), value: isHovered)
        .onHover { hovering in
            isHovered = hovering
        }
    }
}

struct ModernStoryCard: View {
    let story: Story
    @ObservedObject var settings: SettingsModel
    
    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            // Story Image/Icon
            RoundedRectangle(cornerRadius: 16)
                .fill(Color.orange.opacity(0.2))
                .frame(width: 160, height: 160)
                .overlay(
                    Image(systemName: "book.fill")
                        .font(.system(size: 40))
                        .foregroundColor(.orange)
                )
            
            // Story Details
            VStack(alignment: .leading, spacing: 4) {
                Text(story.title)
                    .font(.headline)
                    .foregroundColor(.primary)
                    .lineLimit(1)
                
                Text(story.description)
                    .font(.subheadline)
                    .foregroundColor(.secondary)
                    .lineLimit(2)
            }
            .frame(width: 160)
        }
        .padding(12)
        .background(Color(UIColor.secondarySystemGroupedBackground))
        .cornerRadius(20)
        .shadow(color: Color.black.opacity(0.1), radius: 5, y: 2)
    }
}

struct FeaturedStoryCard: View {
    @ObservedObject var settings: SettingsModel
    @State private var isHovered = false
    
    var body: some View {
        VStack(alignment: .leading, spacing: 16) {
            // Story Image
            ZStack(alignment: .topLeading) {
                RoundedRectangle(cornerRadius: 24)
                    .fill(
                        LinearGradient(
                            colors: [.orange.opacity(0.3), .orange.opacity(0.1)],
                            startPoint: .topLeading,
                            endPoint: .bottomTrailing
                        )
                    )
                    .frame(height: 200)
                    .overlay(
                        Image(systemName: "book.fill")
                            .font(.system(size: 60))
                            .foregroundColor(.orange)
                    )
                
                // Featured Badge
                Label("Featured", systemImage: "star.fill")
                    .font(.caption.bold())
                    .foregroundColor(.white)
                    .padding(.horizontal, 12)
                    .padding(.vertical, 6)
                    .background(
                        Capsule()
                            .fill(Color.orange)
                    )
                    .padding(16)
            }
            
            VStack(alignment: .leading, spacing: 8) {
                Text(Story.featured.title)
                    .font(.title2.bold())
                    .foregroundColor(.primary)
                
                Text(Story.featured.description)
                    .font(.subheadline)
                    .foregroundColor(.secondary)
                    .lineLimit(2)
                
                HStack {
                    Label("4.9", systemImage: "star.fill")
                        .foregroundColor(.orange)
                    
                    Text("•")
                        .foregroundColor(.secondary)
                    
                    Label("15 min", systemImage: "clock")
                        .foregroundColor(.secondary)
                }
                .font(.caption.bold())
            }
            .padding(.horizontal, 16)
            .padding(.bottom, 16)
        }
        .background(
            RoundedRectangle(cornerRadius: 24)
                .fill(Color(UIColor.secondarySystemGroupedBackground))
                .shadow(color: .black.opacity(0.1), radius: 15, y: 5)
        )
        .scaleEffect(isHovered ? 0.98 : 1)
        .animation(.spring(response: 0.3), value: isHovered)
        .onHover { hovering in
            isHovered = hovering
        }
    }
}

struct ScaledButtonStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .scaleEffect(configuration.isPressed ? 0.98 : 1)
            .animation(.easeInOut(duration: 0.2), value: configuration.isPressed)
    }
}

struct StoryCard: View {
    let story: Story
    @ObservedObject var settings: SettingsModel
    
    var body: some View {
        VStack(alignment: .leading) {
            RoundedRectangle(cornerRadius: 8)
                .fill(settings.isDarkMode ? Color.orange.opacity(0.3) : Color.orange.opacity(0.2))
                .frame(width: 150, height: 100)
                .overlay(
                    Image(systemName: "book.fill")
                        .font(.largeTitle)
                        .foregroundColor(settings.isDarkMode ? .orange.opacity(0.7) : .orange)
                )
            
            Text(story.title)
                .font(.headline)
                .foregroundColor(settings.isDarkMode ? .white : .black)
                .lineLimit(1)
            
            Text(story.description)
                .font(.caption)
                .foregroundStyle(.secondary)
                .lineLimit(2)
        }
        .frame(width: 150)
        .padding(8)
        .background(settings.isDarkMode ? Color(.systemGray6).opacity(0.1) : Color(.systemGray6).opacity(0.5))
        .cornerRadius(12)
    }
}

struct MyStoriesView: View {
    @StateObject private var viewModel = StoryCreatorViewModel()
    @ObservedObject var settings: SettingsModel
    @State private var showingNewStorySheet = false
    @State private var searchText = ""
    @State private var selectedFilter = StoryFilter.all
    @State private var showingSortMenu = false
    @State private var sortOrder = SortOrder.newest
    @State private var selectedStoryForReading: UserStory?
    
    var filteredStories: [UserStory] {
        let filtered = viewModel.userStories.filter { story in
            if searchText.isEmpty { return true }
            return story.title.localizedCaseInsensitiveContains(searchText) ||
                   story.description.localizedCaseInsensitiveContains(searchText)
        }
        
        let filterResult = switch selectedFilter {
        case .all: filtered
        case .inProgress: filtered.filter { !$0.scenarios.isEmpty && $0.scenarios.count < 5 }
        case .completed: filtered.filter { $0.scenarios.count >= 5 }
        case .drafts: filtered.filter { $0.scenarios.isEmpty }
        }
        
        return switch sortOrder {
        case .newest: filterResult.sorted { $0.id.uuidString > $1.id.uuidString }
        case .oldest: filterResult.sorted { $0.id.uuidString < $1.id.uuidString }
        case .alphabetical: filterResult.sorted { $0.title < $1.title }
        }
    }
    
    var body: some View {
        NavigationStack {
            ZStack {
                Color(UIColor.systemGroupedBackground)
                    .ignoresSafeArea()
                
                if viewModel.userStories.isEmpty {
                    EmptyStateView(
                        showingNewStorySheet: $showingNewStorySheet,
                        category: .all
                    )
                } else {
                    ScrollView {
                        LazyVStack(spacing: 16) {
                            // Filter Pills
                            ScrollView(.horizontal, showsIndicators: false) {
                                HStack(spacing: 8) {
                                    ForEach(StoryFilter.allCases, id: \.self) { filter in
                                        FilterPill(filter: filter, selectedFilter: $selectedFilter)
                                    }
                                }
                                .padding(.horizontal)
                            }
                            .padding(.vertical, 8)
                            
                            // Stories Grid
                            LazyVGrid(columns: [
                                GridItem(.flexible())
                            ], spacing: 20) {
                                ForEach(filteredStories) { story in
                                    NavigationLink(destination: StoryEditorView(story: story, settings: settings)) {
                                        MyStoryCard(
                                            story: story,
                                            onPlayTapped: {
                                                selectedStoryForReading = story
                                            }
                                        )
                                        .contentShape(Rectangle())
                                    }
                                    .buttonStyle(ScaledButtonStyle())
                                }
                            }
                            .padding(.horizontal)
                        }
                        .padding(.vertical)
                    }
                }
            }
            .navigationTitle("My Stories")
            .searchable(text: $searchText, prompt: "Search your stories")
            .toolbar {
                ToolbarItem(placement: .navigationBarTrailing) {
                    HStack(spacing: 16) {
                        Menu {
                            Picker("Sort Order", selection: $sortOrder) {
                                Label("Newest First", systemImage: "arrow.down").tag(SortOrder.newest)
                                Label("Oldest First", systemImage: "arrow.up").tag(SortOrder.oldest)
                                Label("Alphabetical", systemImage: "textformat.abc").tag(SortOrder.alphabetical)
                            }
                        } label: {
                            Image(systemName: "arrow.up.arrow.down")
                                .foregroundColor(.primary)
                        }
                        
                        Button(action: { showingNewStorySheet = true }) {
                            Image(systemName: "plus.circle.fill")
                                .font(.system(size: 24))
                                .foregroundColor(.blue)
                        }
                    }
                }
            }
            .sheet(isPresented: $showingNewStorySheet) {
                CreateStoryView(viewModel: viewModel, settings: settings)
            }
            .navigationDestination(item: $selectedStoryForReading) { story in
                StoryStartView(
                    story: Story(
                        title: story.title,
                        description: story.description
                    ),
                    settings: settings
                )
            }
        }
        .tint(.yellow)
    }
}

struct MyStoryCard: View {
    let story: UserStory
    let onPlayTapped: () -> Void
    @Environment(\.colorScheme) var colorScheme
    @State private var isHovered = false
    @State private var showingContextMenu = false
    
    var body: some View {
        VStack(alignment: .leading, spacing: 20) {
            // Header Section
            VStack(alignment: .leading, spacing: 16) {
                HStack(alignment: .top) {
                    // Title and Status
                    VStack(alignment: .leading, spacing: 8) {
                        Text(story.title)
                            .font(.title3.bold())
                            .foregroundColor(.primary)
                        
                        Text(story.description)
                            .font(.subheadline)
                            .foregroundColor(.secondary)
                            .lineLimit(2)
                    }
                    
                    Spacer()
                    
                    // Status Badge
                    StatusBadge(status: storyStatus, color: statusColor)
                }
            }
            
            // Story Preview
            StoryPreviewSection(story: story)
            
            // Action Buttons
            HStack(spacing: 16) {
                // Write Story Button
                ActionButton(
                    title: story.scenarios.isEmpty ? "Start Writing" : "Continue Writing",
                    icon: "pencil.line",
                    color: .blue,
                    action: onPlayTapped
                )
                
                Spacer()
                
                // More Options Button
                Menu {
                    Button {
                        // Share action
                    } label: {
                        Label("Share Story", systemImage: "square.and.arrow.up")
                    }
                    
                    Button {
                        // Export action
                    } label: {
                        Label("Export Story", systemImage: "arrow.down.doc")
                    }
                    
                    Divider()
                    
                    Button(role: .destructive) {
                        // Delete action
                    } label: {
                        Label("Delete Story", systemImage: "trash")
                    }
                } label: {
                    Image(systemName: "ellipsis.circle.fill")
                        .font(.system(size: 24))
                        .foregroundColor(.secondary)
                }
            }
        }
        .padding(20)
        .background(
            RoundedRectangle(cornerRadius: 24)
                .fill(Color(UIColor.secondarySystemGroupedBackground))
                .shadow(
                    color: .black.opacity(isHovered ? 0.12 : 0.08),
                    radius: isHovered ? 15 : 10,
                    y: isHovered ? 8 : 4
                )
        )
        .overlay(
            RoundedRectangle(cornerRadius: 24)
                .strokeBorder(
                    LinearGradient(
                        colors: [.blue.opacity(0.5), .purple.opacity(0.5)],
                        startPoint: .topLeading,
                        endPoint: .bottomTrailing
                    ),
                    lineWidth: 1
                )
        )
        .scaleEffect(isHovered ? 0.98 : 1)
        .animation(.spring(response: 0.3), value: isHovered)
        .onHover { hovering in
            isHovered = hovering
        }
    }
    
    private var statusColor: Color {
        switch storyStatus {
        case "Draft": return .orange
        case "Complete": return .green
        default: return .blue
        }
    }
    
    private var storyStatus: String {
        if story.scenarios.isEmpty {
            return "Draft"
        } else if story.scenarios.count >= 5 {
            return "Complete"
        } else {
            return "In Progress"
        }
    }
}

struct StatusBadge: View {
    let status: String
    let color: Color
    
    var body: some View {
        Text(status)
            .font(.system(size: 12, weight: .semibold))
            .padding(.horizontal, 12)
            .padding(.vertical, 6)
            .background(
                Capsule()
                    .fill(color.opacity(0.15))
                    .overlay(
                        Capsule()
                            .strokeBorder(color.opacity(0.3), lineWidth: 1)
                    )
            )
            .foregroundColor(color)
    }
}

struct StoryPreviewSection: View {
    let story: UserStory
    
    var body: some View {
        VStack(alignment: .leading, spacing: 12) {
            if let lastScenario = story.scenarios.last {
                Text(lastScenario.storyText)
                    .font(.subheadline)
                    .foregroundColor(.secondary)
                    .lineLimit(3)
                    .padding()
                    .frame(maxWidth: .infinity, alignment: .leading)
                    .background(
                        RoundedRectangle(cornerRadius: 12)
                            .fill(Color(UIColor.tertiarySystemGroupedBackground))
                    )
            } else {
                Text("Start writing your story...")
                    .font(.subheadline)
                    .foregroundColor(.secondary)
                    .padding()
                    .frame(maxWidth: .infinity, alignment: .leading)
                    .background(
                        RoundedRectangle(cornerRadius: 12)
                            .fill(Color(UIColor.tertiarySystemGroupedBackground))
                    )
            }
        }
    }
}

struct ActionButton: View {
    let title: String
    let icon: String
    let color: Color
    let action: () -> Void
    @State private var isHovered = false
    
    var body: some View {
        Button(action: action) {
            HStack(spacing: 8) {
                Image(systemName: icon)
                    .font(.system(size: 14, weight: .medium))
                Text(title)
                    .font(.system(size: 14, weight: .medium))
            }
            .padding(.horizontal, 16)
            .padding(.vertical, 8)
            .background(
                RoundedRectangle(cornerRadius: 12)
                    .fill(color.opacity(0.1))
                    .overlay(
                        RoundedRectangle(cornerRadius: 12)
                            .strokeBorder(color.opacity(0.2), lineWidth: 1)
                    )
            )
            .foregroundColor(color)
            .scaleEffect(isHovered ? 0.95 : 1)
        }
        .buttonStyle(.plain)
        .onHover { hovering in
            withAnimation(.spring(response: 0.3)) {
                isHovered = hovering
            }
        }
    }
}

// Supporting Views
struct StatItem: View {
    let title: String
    let value: String
    var total: String? = nil
    var unit: String? = nil
    let icon: String
    
    var body: some View {
        VStack(alignment: .leading, spacing: 6) {
            Text(title)
                .font(.system(size: 11, weight: .medium))
                .foregroundColor(.secondary)
            
            HStack(alignment: .firstTextBaseline, spacing: 4) {
                Image(systemName: icon)
                    .font(.system(size: 14))
                    .foregroundColor(.secondary)
                
                Text(value)
                    .font(.system(size: 24, weight: .bold))
                
                if let total = total {
                    Text(total)
                        .font(.system(size: 16))
                        .foregroundColor(.secondary)
                }
                
                if let unit = unit {
                    Text(unit)
                        .font(.system(size: 16))
                        .foregroundColor(.secondary)
                }
            }
        }
    }
}

struct FilterPill: View {
    let filter: StoryFilter
    @Binding var selectedFilter: StoryFilter
    
    var body: some View {
        Button(action: { 
            withAnimation(.spring(response: 0.3)) {
                selectedFilter = filter
            }
        }) {
            HStack(spacing: 8) {
                Image(systemName: filterIcon)
                    .font(.system(size: 16, weight: .medium))
                Text(filter.rawValue)
                    .font(.system(size: 16, weight: .medium))
            }
            .padding(.horizontal, 16)
            .padding(.vertical, 12)
            .background(
                RoundedRectangle(cornerRadius: 12)
                    .fill(selectedFilter == filter ? Color.blue : Color.blue.opacity(0.1))
            )
            .foregroundColor(selectedFilter == filter ? .white : .blue)
        }
    }
    
    private var filterIcon: String {
        switch filter {
        case .all: return "square.stack.3d.up"
        case .inProgress: return "clock"
        case .completed: return "checkmark.circle"
        case .drafts: return "doc.text"
        }
    }
}

struct EmptyStateView: View {
    @Binding var showingNewStorySheet: Bool
    let category: StoryCategory
    
    // Add a computed property for contextual color
    private var contextualColor: Color {
        // Determine color based on category or navigation context
        if category == .all {
            return .yellow  // For My Stories tab
        }
        return .blue     // For Stories tab
    }
    
    var body: some View {
        VStack(spacing: 20) {
            Image(systemName: category.icon)
                .font(.system(size: 60))
                .foregroundColor(contextualColor.opacity(0.5))
            
            Text("No \(category.rawValue) Stories Yet")
                .font(.title2.bold())
            
            Text("Check back later for new stories")
                .font(.body)
                .multilineTextAlignment(.center)
                .foregroundColor(.secondary)
            
            if category == .all {
                Button(action: { showingNewStorySheet = true }) {
                    Text("Create New Story")
                        .font(.headline)
                        .foregroundColor(.white)
                        .padding(.horizontal, 24)
                        .padding(.vertical, 12)
                        .background(contextualColor)
                        .clipShape(Capsule())
                }
                .padding(.top, 8)
            }
        }
        .padding()
    }
}

struct SettingsTabView: View {
    @ObservedObject var settings: SettingsModel
    
    var body: some View {
        NavigationStack {
            SettingsView(settings: settings)
        }
        .tint(.blue)
    }
}

#Preview {
    ContentView()
}

// Update the Story struct to conform to Equatable
struct Story: Identifiable, Equatable {
    let id = UUID()
    let title: String
    let description: String
    
    // Add static func == for Equatable conformance
    static func == (lhs: Story, rhs: Story) -> Bool {
        lhs.id == rhs.id
    }
    
    static let featured = Story(
        title: "The Buried Haven",
        description: "A journey of survival and truth in an underground facility"
    )
    
    static let samples = [
        Story(title: "The Lost City ", description: "Explore ancient ruins"),
        Story(title: "Space Pioneer", description: "Adventure in deep space"),
        Story(title: "Mystery Manor", description: "Solve the haunted mystery"),
        Story(title: "Dragon's Quest", description: "Epic fantasy journey"),
        Story(title: "Time Traveler", description: "Change the course of history")
    ]
    
    var category: StoryCategory {
        // In a real app, this would be stored in the model
        // For now, randomly assign categories to sample stories
        switch title {
        case "The Lost City": return .adventure
        case "Space Pioneer": return .sciFi
        case "Mystery Manor": return .mystery
        case "Dragon's Quest": return .fantasy
        case "Time Traveler": return .sciFi
        default: return .adventure
        }
    }
}

enum StoryFilter: String, CaseIterable {
    case all = "All"
    case inProgress = "In Progress"
    case completed = "Completed"
    case drafts = "Drafts"
}

enum SortOrder {
    case newest, oldest, alphabetical
}


