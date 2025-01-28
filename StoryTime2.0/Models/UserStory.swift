import Foundation

struct UserStory: Codable, Identifiable, Hashable {
    let id: UUID
    var title: String
    var description: String
    var scenarios: [UserScenario]
    
    init(id: UUID = UUID(), title: String, description: String, scenarios: [UserScenario] = []) {
        self.id = id
        self.title = title
        self.description = description
        self.scenarios = scenarios
    }
    
    func hash(into hasher: inout Hasher) {
        hasher.combine(id)
    }
    
    static func == (lhs: UserStory, rhs: UserStory) -> Bool {
        lhs.id == rhs.id
    }
}

struct UserScenario: Codable, Identifiable, Hashable {
    let id: UUID
    var title: String
    var storyText: String
    var choices: [UserChoice]
    
    init(id: UUID = UUID(), title: String, storyText: String, choices: [UserChoice] = []) {
        self.id = id
        self.title = title
        self.storyText = storyText
        self.choices = choices
    }
    
    func hash(into hasher: inout Hasher) {
        hasher.combine(id)
    }
    
    static func == (lhs: UserScenario, rhs: UserScenario) -> Bool {
        lhs.id == rhs.id
    }
}

struct UserChoice: Codable, Identifiable, Hashable {
    let id: UUID
    var text: String
    var consequence: String
    var nextScenarioId: UUID?
    
    init(id: UUID = UUID(), text: String, consequence: String, nextScenarioId: UUID? = nil) {
        self.id = id
        self.text = text
        self.consequence = consequence
        self.nextScenarioId = nextScenarioId
    }
    
    func hash(into hasher: inout Hasher) {
        hasher.combine(id)
    }
    
    static func == (lhs: UserChoice, rhs: UserChoice) -> Bool {
        lhs.id == rhs.id
    }
} 