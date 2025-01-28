import Foundation

struct AIStory: Identifiable, Codable, Equatable {
    let id: UUID
    let text: String
    let choices: [AIStoryChoice]
    let timestamp: Date
    var title: String
    var isCompleted: Bool
    
    init(id: UUID = UUID(), text: String, choices: [AIStoryChoice], title: String = "Untitled Story", isCompleted: Bool = false) {
        self.id = id
        self.text = text
        self.choices = choices
        self.timestamp = Date()
        self.title = title
        self.isCompleted = isCompleted
    }
    
    static func == (lhs: AIStory, rhs: AIStory) -> Bool {
        lhs.id == rhs.id
    }
}

struct AIStoryChoice: Identifiable, Codable, Equatable {
    let id: UUID
    let text: String
    let prompt: String
    
    init(id: UUID = UUID(), text: String, prompt: String) {
        self.id = id
        self.text = text
        self.prompt = prompt
    }
    
    static func == (lhs: AIStoryChoice, rhs: AIStoryChoice) -> Bool {
        lhs.id == rhs.id
    }
}

struct SavedStory: Identifiable, Codable {
    let id: UUID
    let title: String
    let segments: [StorySegment]
    let createdAt: Date
    let lastModified: Date
    var coverImage: String? // SF Symbol name for story cover
    var tags: [String]
    var rating: Int // 1-5 stars
    
    struct StorySegment: Codable {
        let text: String
        let timestamp: Date
        let choiceMade: String?
    }
}

@MainActor
class AIStoryViewModel: ObservableObject {
    @Published var currentStory: AIStory?
    @Published var storyHistory: [AIStory] = []
    @Published var error: String?
    @Published var isLoading = false
    @Published var savedStories: [SavedStory] = []
    
    private let geminiService = GeminiService()
    private let userDefaults = UserDefaults.standard
    
    init() {
        loadSavedStories()
    }
    
    func generateStory(prompt: String) async {
        isLoading = true
        defer { isLoading = false }
        
        do {
            if let current = currentStory {
                storyHistory.append(current)
            }
            
            let response = try await geminiService.generateStoryContent(prompt: prompt)
            let choices = response.choices.map { choice in
                AIStoryChoice(text: choice.text, prompt: choice.prompt)
            }
            currentStory = AIStory(text: response.story_text, choices: choices)
        } catch {
            self.error = error.localizedDescription
        }
    }
    
    func saveCurrentStory(title: String, tags: [String] = [], rating: Int = 0) {
        guard !storyHistory.isEmpty || currentStory != nil else { return }
        
        var segments: [SavedStory.StorySegment] = []
        
        // Add segments from history
        for story in storyHistory {
            segments.append(SavedStory.StorySegment(
                text: story.text,
                timestamp: story.timestamp,
                choiceMade: story.choices.first?.text
            ))
        }
        
        // Add current story if exists
        if let current = currentStory {
            segments.append(SavedStory.StorySegment(
                text: current.text,
                timestamp: current.timestamp,
                choiceMade: nil
            ))
        }
        
        let savedStory = SavedStory(
            id: UUID(),
            title: title,
            segments: segments,
            createdAt: Date(),
            lastModified: Date(),
            coverImage: "book.closed.fill",
            tags: tags,
            rating: rating
        )
        
        savedStories.append(savedStory)
        saveToDisk()
    }
    
    private func saveToDisk() {
        if let encoded = try? JSONEncoder().encode(savedStories) {
            userDefaults.set(encoded, forKey: "SavedStories")
        }
    }
    
    private func loadSavedStories() {
        if let data = userDefaults.data(forKey: "SavedStories"),
           let decoded = try? JSONDecoder().decode([SavedStory].self, from: data) {
            savedStories = decoded
        }
    }
    
    func deleteStory(_ story: SavedStory) {
        savedStories.removeAll { story.id == $0.id }
        saveToDisk()
    }
} 