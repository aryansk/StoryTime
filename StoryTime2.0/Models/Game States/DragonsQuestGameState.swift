import Foundation

enum DQScenario: String {
    case dragonAwakening = "Dragon Awakening"
    case fieryTrial = "Fiery Trial"
    case treasureHoard = "Treasure Hoard"
    case dragonLair = "Dragon's Lair"
    case finalConfrontation = "Final Confrontation"
}

struct DQChoice {
    let text: String
    let consequence: String
    let nextScenario: DQScenario?
}

class DragonsQuestGameState: ObservableObject {
    @Published var currentScenario: DQScenario = .dragonAwakening
    @Published var storyText: String = ""
    @Published var choices: [DQChoice] = []
    @Published var showingConsequence = false
    @Published var consequenceText = ""
    
    func loadScenario(_ scenario: DQScenario) {
        currentScenario = scenario
        switch scenario {
        case .dragonAwakening:
            storyText = """
            The ancient dragon stirs in its slumber as you approach the cavern's dark mouth.
            A sense of awe and fear mixes within you. The atmosphere is heavy with destiny.
            """
            choices = [
                DQChoice(
                    text: "Approach cautiously",
                    consequence: "The dragon's eye flickers open, watching you intently...",
                    nextScenario: .fieryTrial
                ),
                DQChoice(
                    text: "Retreat silently",
                    consequence: "You back away into the twilight, safe for now.",
                    nextScenario: nil
                ),
                DQChoice(
                    text: "Challenge the beast",
                    consequence: "With valor, you step forward, ready for battle.",
                    nextScenario: .finalConfrontation
                )
            ]
            
        case .fieryTrial:
            storyText = """
            Suddenly, flames burst forth as the dragon tests your resolve.
            The trial by fire begins, and every step you take is fraught with peril.
            """
            choices = [
                DQChoice(
                    text: "Charge forward",
                    consequence: "The heat intensifies, but your spirit remains unbroken.",
                    nextScenario: .treasureHoard
                ),
                DQChoice(
                    text: "Seek cover",
                    consequence: "Your caution saves you from the worst of the blaze.",
                    nextScenario: nil
                ),
                DQChoice(
                    text: "Call out to the dragon",
                    consequence: "A deep rumble answers your call, stirring the cavern further.",
                    nextScenario: .dragonLair
                )
            ]
            
        case .treasureHoard:
            storyText = """
            Beyond the fiery trial, you discover a vast hoard of glittering treasures
            and relics that whisper secrets of a long-forgotten era.
            """
            choices = [
                DQChoice(
                    text: "Take a relic",
                    consequence: "A sudden surge of energy courses through you.",
                    nextScenario: nil
                ),
                DQChoice(
                    text: "Examine the treasures",
                    consequence: "Intricate details reveal stories of ancient conquests.",
                    nextScenario: nil
                ),
                DQChoice(
                    text: "Proceed deeper",
                    consequence: "The heart of the lair beckons you onward.",
                    nextScenario: .dragonLair
                )
            ]
            
        case .dragonLair:
            storyText = """
            You step into the very heart of the dragon's lair. Shadows dance across walls,
            and the air is thick with the scent of brimstone and ancient power.
            """
            choices = [
                DQChoice(
                    text: "Search for the beast's weakness",
                    consequence: "A strategy forms in your mind as you observe your surroundings.",
                    nextScenario: .finalConfrontation
                ),
                DQChoice(
                    text: "Loot the lair",
                    consequence: "You gather priceless artifacts, each with its own story.",
                    nextScenario: nil
                ),
                DQChoice(
                    text: "Hide and observe",
                    consequence: "Silence covers the chamber as you watch the dragon stir.",
                    nextScenario: nil
                )
            ]
            
        case .finalConfrontation:
            storyText = """
            At last, your destiny culminates in the final confrontation.
            With courage as your only shield, you face the dragon in a battle that will be remembered for ages.
            """
            choices = [
                DQChoice(
                    text: "Unleash your might",
                    consequence: "The battle ignites, and legends begin to form.",
                    nextScenario: nil
                ),
                DQChoice(
                    text: "Negotiate a truce",
                    consequence: "Words become your weapons as you seek peace over bloodshed.",
                    nextScenario: nil
                ),
                DQChoice(
                    text: "Retreat to fight another day",
                    consequence: "Wisdom guides your retreat, knowing that not every battle is won by the brave.",
                    nextScenario: nil
                )
            ]
        }
    }
} 
