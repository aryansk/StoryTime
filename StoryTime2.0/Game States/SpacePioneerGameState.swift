import Foundation

enum SpacePioneerScenario: String {
    case firstContact = "First Contact"
    case alienTechnology = "Ancient Technology"
    case spaceAnomaly = "Space Anomaly"
    case diplomaticCrisis = "Diplomatic Crisis"
    case cosmicThreat = "Cosmic Threat"
    case timeParadox = "Time Paradox"
    case end = "End"
}

struct SpacePioneerChoice {
    let text: String
    let consequence: String
    let nextScenario: SpacePioneerScenario?
}

class SpacePioneerGameState: ObservableObject {
    @Published var currentScenario: SpacePioneerScenario = .firstContact
    @Published var storyText: String = ""
    @Published var choices: [SpacePioneerChoice] = []
    @Published var showingConsequence = false
    @Published var consequenceText = ""
    
    func loadScenario(_ scenario: SpacePioneerScenario) {
        currentScenario = scenario
        switch scenario {
        case .firstContact:
            storyText = """
            Your deep space exploration vessel detects an unknown signal. As you approach, \
            a massive alien structure materializes. Its architecture defies physics, and \
            strange lights pulse within. Your crew awaits your command...
            """
            choices = [
                SpacePioneerChoice(
                    text: "Initiate peaceful contact protocol",
                    consequence: "The structure responds with a series of complex mathematical patterns...",
                    nextScenario: .alienTechnology
                ),
                SpacePioneerChoice(
                    text: "Analyze from safe distance",
                    consequence: "Your scanners detect technology beyond human comprehension...",
                    nextScenario: .spaceAnomaly
                ),
                SpacePioneerChoice(
                    text: "Send automated probe",
                    consequence: "The probe disappears into a dimensional rift...",
                    nextScenario: .timeParadox
                )
            ]
            
        case .alienTechnology:
            storyText = """
            The alien artifact interfaces with your ship's systems, revealing glimpses of \
            advanced civilizations and terrible warnings. Your neural implants begin \
            receiving vast amounts of data about an ancient threat that devoured galaxies...
            """
            choices = [
                SpacePioneerChoice(
                    text: "Download the alien database",
                    consequence: "The knowledge overwhelms your systems, triggering a chain reaction...",
                    nextScenario: .cosmicThreat
                ),
                SpacePioneerChoice(
                    text: "Establish two-way communication",
                    consequence: "The aliens request an urgent diplomatic meeting...",
                    nextScenario: .diplomaticCrisis
                ),
                SpacePioneerChoice(
                    text: "Quarantine the artifact",
                    consequence: "The artifact's energy signature begins destabilizing...",
                    nextScenario: .spaceAnomaly
                )
            ]
            
        case .spaceAnomaly:
            storyText = """
            Your ship's sensors detect a growing spatial distortion. Reality itself seems \
            to bend around the alien structure. Through the distortion, you glimpse parallel \
            versions of your crew, each making different choices...
            """
            choices = [
                SpacePioneerChoice(
                    text: "Navigate through the anomaly",
                    consequence: "Your ship phases between multiple realities...",
                    nextScenario: .timeParadox
                ),
                SpacePioneerChoice(
                    text: "Attempt to seal the rift",
                    consequence: "The concentrated energy reveals a hidden threat...",
                    nextScenario: .cosmicThreat
                ),
                SpacePioneerChoice(
                    text: "Contact parallel selves",
                    consequence: "Your alternate versions warn of impending doom...",
                    nextScenario: .diplomaticCrisis
                )
            ]
            
        case .diplomaticCrisis:
            storyText = """
            Representatives from multiple alien factions converge on your location. Each \
            claims the artifact belongs to their civilization, and each warns of catastrophe \
            if it falls into the wrong hands. The fate of multiple species hangs in balance...
            """
            choices = [
                SpacePioneerChoice(
                    text: "Broker an alliance",
                    consequence: "The species unite against a common enemy...",
                    nextScenario: .cosmicThreat
                ),
                SpacePioneerChoice(
                    text: "Destroy the artifact",
                    consequence: "The explosion tears a hole in spacetime...",
                    nextScenario: .timeParadox
                ),
                SpacePioneerChoice(
                    text: "Choose a side",
                    consequence: "Your decision triggers an interstellar war...",
                    nextScenario: nil
                )
            ]
            
        case .cosmicThreat:
            storyText = """
            The truth becomes clear: an ancient cosmic entity approaches, one that consumes \
            entire civilizations. The artifact was a warning system, and humanity's first \
            contact has awakened it. You have one chance to save not just Earth, but all \
            sentient life...
            """
            choices = [
                SpacePioneerChoice(
                    text: "Activate the artifact's weapon",
                    consequence: "You unleash power beyond comprehension...",
                    nextScenario: nil
                ),
                SpacePioneerChoice(
                    text: "Lead an evacuation",
                    consequence: "Humanity becomes a spacefaring refugee species...",
                    nextScenario: nil
                ),
                SpacePioneerChoice(
                    text: "Attempt transcendence",
                    consequence: "Your consciousness merges with the cosmos...",
                    nextScenario: nil
                )
            ]
            
        case .timeParadox:
            storyText = """
            The temporal distortions reach a critical point. You witness the birth and death \
            of galaxies in moments. The artifact reveals its true purpose: a reset switch \
            for reality itself. The ultimate choice lies before you...
            """
            choices = [
                SpacePioneerChoice(
                    text: "Reset the universe",
                    consequence: "Everything begins anew, but with hope for a better outcome...",
                    nextScenario: nil
                ),
                SpacePioneerChoice(
                    text: "Preserve this timeline",
                    consequence: "You accept the challenges ahead, facing them together...",
                    nextScenario: nil
                ),
                SpacePioneerChoice(
                    text: "Merge all timelines",
                    consequence: "Reality becomes a symphony of infinite possibilities...",
                    nextScenario: nil
                )
            ]
            
        case .end:
            storyText = """
            Your journey through the cosmos has changed not just humanity, but the very \
            fabric of reality. The choices you made will echo through eternity, shaping \
            the destiny of countless civilizations.
            """
            choices = []
        }
    }
} 