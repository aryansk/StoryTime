import Foundation

enum MysteryManorScenario: String {
    case arrival = "The Arrival"
    case hiddenPassages = "Hidden Passages"
    case familySecrets = "Family Secrets"
    case ghostlyEncounter = "Ghostly Encounter"
    case ancientRitual = "Ancient Ritual"
    case finalTruth = "The Final Truth"
}

struct MysteryManorChoice {
    let text: String
    let consequence: String
    let nextScenario: MysteryManorScenario?
}

class MysteryManorGameState: ObservableObject {
    @Published var currentScenario: MysteryManorScenario = .arrival
    @Published var storyText: String = ""
    @Published var choices: [MysteryManorChoice] = []
    @Published var showingConsequence = false
    @Published var consequenceText = ""
    
    func loadScenario(_ scenario: MysteryManorScenario) {
        currentScenario = scenario
        switch scenario {
        case .arrival:
            storyText = """
            The old manor looms before you, its windows like hollow eyes watching your approach. \
            As the executor of your grandmother's estate, you've come to investigate her \
            mysterious disappearance. The key feels ice-cold in your hand...
            """
            choices = [
                MysteryManorChoice(
                    text: "Enter through the front door",
                    consequence: "The door creaks open, revealing a grand foyer frozen in time...",
                    nextScenario: .hiddenPassages
                ),
                MysteryManorChoice(
                    text: "Check the garden first",
                    consequence: "You discover strange symbols carved into the ancient trees...",
                    nextScenario: .familySecrets
                ),
                MysteryManorChoice(
                    text: "Follow the sound of whispers",
                    consequence: "The whispers lead you to a hidden cellar entrance...",
                    nextScenario: .ghostlyEncounter
                )
            ]
            
        case .hiddenPassages:
            storyText = """
            Behind the dusty wallpaper, you find a map of the manor's secret passages. \
            Footprints in the dust suggest recent activity, and a faint humming emanates \
            from behind the walls. Strange symbols mark specific locations throughout the house...
            """
            choices = [
                MysteryManorChoice(
                    text: "Follow the footprints",
                    consequence: "They lead to a hidden study filled with occult artifacts...",
                    nextScenario: .familySecrets
                ),
                MysteryManorChoice(
                    text: "Investigate the humming",
                    consequence: "You discover an ancient ritual in progress...",
                    nextScenario: .ancientRitual
                ),
                MysteryManorChoice(
                    text: "Decode the symbols",
                    consequence: "The markings reveal a supernatural presence...",
                    nextScenario: .ghostlyEncounter
                )
            ]
            
        case .familySecrets:
            storyText = """
            In your grandmother's hidden study, you uncover generations of family journals. \
            They speak of a pact made centuries ago with otherworldly beings. Your \
            grandmother was the latest guardian, protecting a boundary between worlds...
            """
            choices = [
                MysteryManorChoice(
                    text: "Accept the guardian's role",
                    consequence: "Ancient power courses through your veins...",
                    nextScenario: .ancientRitual
                ),
                MysteryManorChoice(
                    text: "Search for your grandmother",
                    consequence: "You find traces of her last ritual...",
                    nextScenario: .ghostlyEncounter
                ),
                MysteryManorChoice(
                    text: "Break the family pact",
                    consequence: "The manor's supernatural bonds begin to unravel...",
                    nextScenario: .finalTruth
                )
            ]
            
        case .ghostlyEncounter:
            storyText = """
            Spectral figures materialize around you - the spirits of past guardians, \
            including your grandmother. They reveal that the manor exists in multiple \
            dimensions, and a dark entity seeks to merge these realities...
            """
            choices = [
                MysteryManorChoice(
                    text: "Channel the spirits' power",
                    consequence: "Their combined energy flows through you...",
                    nextScenario: .ancientRitual
                ),
                MysteryManorChoice(
                    text: "Learn the truth",
                    consequence: "Your grandmother shows you her final moments...",
                    nextScenario: .finalTruth
                ),
                MysteryManorChoice(
                    text: "Reject the supernatural",
                    consequence: "The spirits fade, but the darkness grows stronger...",
                    nextScenario: .finalTruth
                )
            ]
            
        case .ancientRitual:
            storyText = """
            In the manor's heart, you find the ritual chamber. The boundary between \
            worlds grows thin, and the dark entity begins to manifest. Your grandmother's \
            spirit guides your hands as you face the ultimate test of guardianship...
            """
            choices = [
                MysteryManorChoice(
                    text: "Complete the sealing ritual",
                    consequence: "You become the manor's eternal guardian...",
                    nextScenario: nil
                ),
                MysteryManorChoice(
                    text: "Modify the ritual",
                    consequence: "You forge a new pact with the otherworld...",
                    nextScenario: nil
                ),
                MysteryManorChoice(
                    text: "Destroy the boundary",
                    consequence: "Realities begin to merge in unexpected ways...",
                    nextScenario: .finalTruth
                )
            ]
            
        case .finalTruth:
            storyText = """
            The manor reveals its deepest secret: it's a living entity, born from the \
            convergence of countless realities. Your grandmother didn't disappear - she \
            became one with the manor. Now you must decide its fate, and yours...
            """
            choices = [
                MysteryManorChoice(
                    text: "Merge with the manor",
                    consequence: "You transcend humanity, becoming a guardian of realities...",
                    nextScenario: nil
                ),
                MysteryManorChoice(
                    text: "Free all spirits",
                    consequence: "The manor's power disperses, releasing centuries of trapped souls...",
                    nextScenario: nil
                ),
                MysteryManorChoice(
                    text: "Reset the cycle",
                    consequence: "The manor returns to its original state, awaiting the next guardian...",
                    nextScenario: nil
                )
            ]
            
        default:
            storyText = """
            The Mystery Manor's secrets have changed you forever. Whether as its guardian, \
            its destroyer, or something in between, your choices have written a new \
            chapter in its endless story.
            """
            choices = []
        }
    }
} 