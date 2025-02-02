//
//  LostCityGameState.swift
//  StoryTime2.0
//
//  Created by Aryan Signh on 27/01/25.
//

import Foundation

enum LostCityScenario: String {
    case awakening = "City Awakening"
    case ruinsExploration = "Ruins Exploration"
    case secretChamber = "Secret Chamber"
    case finalRevelation = "Final Revelation"
}

struct LostCityChoice {
    let text: String
    let consequence: String
    let nextScenario: LostCityScenario?
}

class LostCityGameState: ObservableObject {
    @Published var currentScenario: LostCityScenario = .awakening
    @Published var storyText: String = ""
    @Published var choices: [LostCityChoice] = []
    @Published var showingConsequence = false
    @Published var consequenceText = ""
    
    func loadScenario(_ scenario: LostCityScenario) {
        currentScenario = scenario
        switch scenario {
        case .awakening:
            storyText = """
            The ancient city awakens as you step onto its forgotten streets. Crumbling statues and overgrown temples whisper the secrets of a lost civilization.
            """
            choices = [
                LostCityChoice(
                    text: "Explore the central plaza",
                    consequence: "You discover intricate carvings and symbols that hint at hidden lore.",
                    nextScenario: .ruinsExploration
                ),
                LostCityChoice(
                    text: "Search for hidden artifacts",
                    consequence: "A glimmer among the rubble catches your eye – something extraordinary lies beneath.",
                    nextScenario: .secretChamber
                ),
                LostCityChoice(
                    text: "Leave it undisturbed",
                    consequence: "The silent ruins keep their secrets as you walk away.",
                    nextScenario: nil
                )
            ]
            
        case .ruinsExploration:
            storyText = """
            Wandering deeper into the city, you uncover ancient shrines and broken mosaics that recount tales of a once-glorious people.
            """
            choices = [
                LostCityChoice(
                    text: "Decipher the inscriptions",
                    consequence: "Flickering images of the past surface as you piece together ancient wisdom.",
                    nextScenario: .secretChamber
                ),
                LostCityChoice(
                    text: "Rest and absorb the atmosphere",
                    consequence: "Time seems to slow as you soak in the magnificence of the ruins.",
                    nextScenario: nil
                )
            ]
            
        case .secretChamber:
            storyText = """
            Behind a collapsed archway, you stumble upon a secret chamber filled with relics and mysterious symbols pulsating with ancient energy.
            """
            choices = [
                LostCityChoice(
                    text: "Unravel the chamber's mystery",
                    consequence: "The chamber unlocks its secrets, revealing the lost history of the city.",
                    nextScenario: .finalRevelation
                ),
                LostCityChoice(
                    text: "Return to the surface",
                    consequence: "Some mysteries, you decide, are best left untouched.",
                    nextScenario: nil
                )
            ]
            
        case .finalRevelation:
            storyText = """
            In a moment of profound clarity, the lost city's secrets are laid bare before you, forever altering your destiny.
            """
            choices = [
                LostCityChoice(
                    text: "Embrace the legacy",
                    consequence: "You pledge to safeguard the wisdom of the ancient world.",
                    nextScenario: nil
                ),
                LostCityChoice(
                    text: "Turn away from the allure",
                    consequence: "Overwhelmed by the truth, you choose a life away from the past.",
                    nextScenario: nil
                )
            ]
        }
    }
} 