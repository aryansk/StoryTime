import Foundation

enum Scenario: String {
    case cleaningRitual = "The Cleaning Ritual"
    case ceremonyHorror = "Ceremony Horror"
    case confinement = "Forbidden Confinement"
    case interrogation = "Loyalty Test"
    case rebelPath = "Underground Resistance"
    case surfaceBreach = "Surface Breach"
    case desertion = "Abandoned Tunnels"
    case truthWar = "War for Truth"
    case exile = "Eternal Exile"
    case newDawn = "New Dawn"
    case systemCollapse = "System Collapse"
    case utopia = "Forgotten Utopia"
}

struct Choice {
    let text: String
    let consequence: String
    let nextScenario: Scenario?
}

class GameState: ObservableObject {
    @Published var currentScenario: Scenario = .cleaningRitual
    @Published var storyText: String = ""
    @Published var choices: [Choice] = []
    @Published var showingConsequence = false
    @Published var consequenceText = ""
    
    func loadScenario(_ scenario: Scenario) {
        currentScenario = scenario
        switch scenario {
        case .cleaningRitual:
            storyText = """
            The air recycler hums ominously as you prepare for Selection Day. The ritualistic lottery determines \
            who maintains the external sensors beyond The Haven's protective dome. Your neighbor whispers: \
            "They never really clean sensors, do they?" Before you can respond, the alarms blare...
            """
            choices = [
                Choice(
                    text: "Take your designated position",
                    consequence: "The lottery machine glitches, selecting you unexpectedly...",
                    nextScenario: .ceremonyHorror
                ),
                Choice(
                    text: "Sabotage the lottery machine",
                    consequence: "Your tampering triggers security protocols...",
                    nextScenario: .confinement
                ),
                Choice(
                    text: "Reveal hidden contamination data",
                    consequence: "The crowd erupts as you show proof of breathable air...",
                    nextScenario: .interrogation
                )
            ]
            
        case .ceremonyHorror:
            storyText = """
            Strapped into the cleaning suit, you're ejected into the toxic atmosphere. But your filters \
            show green... the air is pure. Through your visor, you see flourishing vegetation and intact \
            ruins. The Haven's dome shimmers behind you - a prison, not a sanctuary.
            """
            choices = [
                Choice(
                    text: "Cut oxygen lines and play dead",
                    consequence: "Recovery drones bring you back inside, thinking you expired...",
                    nextScenario: .rebelPath
                ),
                Choice(
                    text: "Follow mysterious heat signatures",
                    consequence: "You discover a surface settlement watching The Haven...",
                    nextScenario: .surfaceBreach
                ),
                Choice(
                    text: "Return and demand answers",
                    consequence: "The airlock rejects your reentry request...",
                    nextScenario: .desertion
                )
            ]
            
        case .confinement:
            storyText = """
            In the cold detention cell, you find carvings: "Follow the rats." A small creature gnaws \
            through weakened flooring. Beyond lies the undercity - a maze of abandoned sectors and \
            rebel hideouts. The walls vibrate with distant machinery.
            """
            choices = [
                Choice(
                    text: "Follow the rodent colony",
                    consequence: "You emerge in a rebel stronghold beneath the agriculture sector...",
                    nextScenario: .rebelPath
                ),
                Choice(
                    text: "Overload the cell security",
                    consequence: "The explosion alerts both rebels and security forces...",
                    nextScenario: .truthWar
                ),
                Choice(
                    text: "Meditate and await fate",
                    consequence: "A mysterious voice interfaces with your neural implant...",
                    nextScenario: .utopia
                )
            ]
            
        case .interrogation:
            storyText = """
            The Overseer examines your evidence. "You think you're the first to discover this?" \
            They reveal centuries of controlled population reduction. "Join us in managing the herd, \
            or become statistics."
            """
            choices = [
                Choice(
                    text: "Accept the offer",
                    consequence: "You're given access to the control matrix...",
                    nextScenario: .systemCollapse
                ),
                Choice(
                    text: "Activate emergency broadcast",
                    consequence: "The truth floods every screen in The Haven...",
                    nextScenario: .newDawn
                ),
                Choice(
                    text: "Trigger implant self-destruct",
                    consequence: "Your final act corrupts the central AI...",
                    nextScenario: .exile
                )
            ]
            
        case .rebelPath:
            storyText = """
            The underground network reveals The Haven's true purpose: humanity's traits are being \
            systematically eliminated. You hold the genetic archive that could restore emotions.
            """
            choices = [
                Choice(
                    text: "Inject the genetic sequence",
                    consequence: "Your body becomes a vector for emotional awakening...",
                    nextScenario: .newDawn
                ),
                Choice(
                    text: "Destroy the archive",
                    consequence: "You preserve the controlled society...",
                    nextScenario: .systemCollapse
                ),
                Choice(
                    text: "Merge with the central AI",
                    consequence: "You become the new arbiter of human evolution...",
                    nextScenario: .utopia
                )
            ]
            
        case .surfaceBreach:
            storyText = """
            The surface dwellers reveal they're original survivors. The Haven was built by the \
            paranoid wealthy during climate collapse. Your dome is slowly poisoning the planet.
            """
            choices = [
                Choice(
                    text: "Disable the dome reactors",
                    consequence: "The energy shield flickers as surface air pours in...",
                    nextScenario: .truthWar
                ),
                Choice(
                    text: "Lead surface troops inside",
                    consequence: "The Haven becomes battleground for humanity's future...",
                    nextScenario: .truthWar
                ),
                Choice(
                    text: "Initiate fusion protocol",
                    consequence: "Dome and surface merge into new ecosystem...",
                    nextScenario: .utopia
                )
            ]
            
        // Additional scenario handlers continue with unique branches...
            
        case .truthWar:
            storyText = """
            The final confrontation erupts between surface dwellers, rebels, and loyalists. \
            The ancient climate control system awaits activation - it could restore Earth or \
            complete its destruction.
            """
            choices = [
                Choice(
                    text: "Restore pre-collapse atmosphere",
                    consequence: "The planet heals but The Haven's systems fail...",
                    nextScenario: nil
                ),
                Choice(
                    text: "Enhance dome containment",
                    consequence: "The Haven becomes humanity's last vault...",
                    nextScenario: nil
                ),
                Choice(
                    text: "Merge consciousness with Earth",
                    consequence: "You become the planetary neural network...",
                    nextScenario: nil
                )
            ]
            
        // Handling remaining scenarios similarly...
            
        default:
            storyText = "End of your journey. The consequences of your choices will ripple through generations."
            choices = []
        }
    }
}
