import SwiftUI

class StoryCreatorViewModel: ObservableObject {
    @Published var userStories: [UserStory] = []
    
    init() {
        loadStories()
    }
    
    func loadStories() {
        if let data = UserDefaults.standard.data(forKey: "UserStories"),
           let stories = try? JSONDecoder().decode([UserStory].self, from: data) {
            userStories = stories
        }
    }
    
    func saveStories() {
        if let encoded = try? JSONEncoder().encode(userStories) {
            UserDefaults.standard.set(encoded, forKey: "UserStories")
        }
    }
    
    func addStory(_ story: UserStory) {
        userStories.append(story)
        saveStories()
    }
    
    func deleteStory(_ story: UserStory) {
        userStories.removeAll { $0.id == story.id }
        saveStories()
    }
}

struct StoryCreatorView: View {
    @StateObject private var viewModel = StoryCreatorViewModel()
    @ObservedObject var settings: SettingsModel
    @State private var showingNewStorySheet = false
    @Environment(\.dismiss) var dismiss
    
    var body: some View {
        NavigationView {
            List {
                ForEach(viewModel.userStories) { story in
                    NavigationLink(destination: StoryEditorView(story: story, settings: settings)) {
                        VStack(alignment: .leading) {
                            Text(story.title)
                                .font(.headline)
                                .foregroundColor(settings.isDarkMode ? .white : .black)
                            Text(story.description)
                                .font(.subheadline)
                                .foregroundStyle(.secondary)
                        }
                    }
                }
                .onDelete { indexSet in
                    indexSet.forEach { index in
                        viewModel.deleteStory(viewModel.userStories[index])
                    }
                }
            }
            .navigationTitle("My Stories")
            .toolbar {
                ToolbarItem(placement: .navigationBarTrailing) {
                    Button(action: { showingNewStorySheet = true }) {
                        Image(systemName: "plus")
                    }
                }
                ToolbarItem(placement: .navigationBarLeading) {
                    Button("Done") { dismiss() }
                }
            }
        }
        .sheet(isPresented: $showingNewStorySheet) {
            CreateStoryView(viewModel: viewModel, settings: settings)
        }
    }
}

struct NewStoryView: View {
    @Environment(\.dismiss) var dismiss
    @ObservedObject var viewModel: StoryCreatorViewModel
    @State private var title = ""
    @State private var description = ""
    
    var body: some View {
        NavigationView {
            Form {
                TextField("Story Title", text: $title)
                TextField("Description", text: $description, axis: .vertical)
                    .lineLimit(3...6)
            }
            .navigationTitle("New Story")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button("Cancel") { dismiss() }
                }
                ToolbarItem(placement: .confirmationAction) {
                    Button("Create") {
                        let newStory = UserStory(title: title, description: description)
                        viewModel.addStory(newStory)
                        dismiss()
                    }
                    .disabled(title.isEmpty)
                }
            }
        }
    }
} 
