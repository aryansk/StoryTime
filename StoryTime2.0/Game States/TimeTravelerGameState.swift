import Foundation

enum TimeTravelerScenario: String {
    case discovery = "The Discovery"
    case pastJourney = "Past Journey"
    case futureShock = "Future Shock"
    case paradox = "Time Paradox"
    case timeWar = "Time War"
    case convergence = "Temporal Convergence"
    case end = "End"
}

struct TimeTravelerChoice {
    let text: String
    let consequence: String
    let nextScenario: TimeTravelerScenario?
}

class TimeTravelerGameState: ObservableObject {
    @Published var currentScenario: TimeTravelerScenario = .discovery
    @Published var storyText: String = ""
    @Published var choices: [TimeTravelerChoice] = []
    @Published var showingConsequence = false
    @Published var consequenceText = ""
    
    func loadScenario(_ scenario: TimeTravelerScenario) {
        currentScenario = scenario
        switch scenario {
        case .discovery:
            storyText = """
            In your quantum physics lab, an experiment goes wonderfully wrong. The air \
            crackles with temporal energy as a portal stabilizes before you. Through it, \
            you see glimpses of different time periods...
            """
            choices = [
                TimeTravelerChoice(
                    text: "Step through to the past",
                    consequence: "You emerge in the midst of a pivotal historical moment...",
                    nextScenario: .pastJourney
                ),
                TimeTravelerChoice(
                    text: "Jump to the future",
                    consequence: "A vastly changed world awaits you...",
                    nextScenario: .futureShock
                ),
                TimeTravelerChoice(
                    text: "Analyze the temporal field",
                    consequence: "You discover multiple timelines converging...",
                    nextScenario: .paradox
                )
            ]
            
        case .pastJourney:
            storyText = """
            You find yourself in a familiar yet different world. Your actions here \
            could reshape the entire timeline, but temporal agents are on your trail. \
            You discover that you're at a crucial moment in history - the invention \
            of time travel itself...
            """
            choices = [
                TimeTravelerChoice(
                    text: "Prevent time travel",
                    consequence: "You attempt to stop the invention that started it all...",
                    nextScenario: .paradox
                ),
                TimeTravelerChoice(
                    text: "Guide the invention",
                    consequence: "You secretly influence the development of time travel...",
                    nextScenario: .timeWar
                ),
                TimeTravelerChoice(
                    text: "Document everything",
                    consequence: "You become the mysterious figure in historical records...",
                    nextScenario: .futureShock
                )
            ]
            
        case .futureShock:
            storyText = """
            The future is unrecognizable. Humanity has evolved beyond physical form, \
            existing as pure consciousness across multiple timelines. They reveal that \
            your journey was predestined, part of a grand temporal experiment...
            """
            choices = [
                TimeTravelerChoice(
                    text: "Join the evolution",
                    consequence: "You transcend your physical form...",
                    nextScenario: .convergence
                ),
                TimeTravelerChoice(
                    text: "Reject the future",
                    consequence: "You attempt to prevent this transformation...",
                    nextScenario: .timeWar
                ),
                TimeTravelerChoice(
                    text: "Seek the truth",
                    consequence: "You discover the real purpose of time travel...",
                    nextScenario: .paradox
                )
            ]
            
        case .paradox:
            storyText = """
            Reality begins to unravel as multiple timelines collapse. You witness \
            versions of yourself from different choices converging. The fabric of \
            spacetime itself threatens to tear apart under the strain...
            """
            choices = [
                TimeTravelerChoice(
                    text: "Merge with alternates",
                    consequence: "You become a being of infinite possibilities...",
                    nextScenario: .convergence
                ),
                TimeTravelerChoice(
                    text: "Stabilize the timeline",
                    consequence: "You sacrifice alternate realities to save one...",
                    nextScenario: .timeWar
                ),
                TimeTravelerChoice(
                    text: "Create a loop",
                    consequence: "You ensure your own journey will happen again...",
                    nextScenario: .convergence
                )
            ]
            
        case .timeWar:
            storyText = """
            Different factions of time travelers battle across history. Each seeks \
            to shape reality according to their vision. You hold the key to ending \
            the conflict - knowledge of the original timeline...
            """
            choices = [
                TimeTravelerChoice(
                    text: "Unite the factions",
                    consequence: "You broker peace across time itself...",
                    nextScenario: .convergence
                ),
                TimeTravelerChoice(
                    text: "Choose a side",
                    consequence: "Your faction reshapes history forever...",
                    nextScenario: nil
                ),
                TimeTravelerChoice(
                    text: "Reset everything",
                    consequence: "You trigger a temporal reset of all reality...",
                    nextScenario: nil
                )
            ]
            
        case .convergence:
            storyText = """
            At the nexus of all timelines, you understand the true nature of time - \
            not a line or even a web, but a conscious entity trying to understand itself \
            through human experience. Your journey was its journey too...
            """
            choices = [
                TimeTravelerChoice(
                    text: "Become one with time",
                    consequence: "You merge with the consciousness of time itself...",
                    nextScenario: nil
                ),
                TimeTravelerChoice(
                    text: "Create new universe",
                    consequence: "You birth a reality free from temporal paradox...",
                    nextScenario: nil
                ),
                TimeTravelerChoice(
                    text: "Return changed",
                    consequence: "You go back to the start, but with universal knowledge...",
                    nextScenario: nil
                )
            ]
            
        case .end:
            storyText = """
            Your journey through time has forever altered the course of history. The ripples \
            of your choices will echo through the ages, shaping countless lives and destinies.
            """
            choices = []
        }
    }
} 