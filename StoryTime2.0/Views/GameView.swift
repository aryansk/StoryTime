import SwiftUI

struct GameView: View {
    @StateObject private var gameState = GameState()
    @StateObject private var settings = SettingsModel()
    @Environment(\.dismiss) var dismiss
    
    var body: some View {
        ScrollView {
            VStack(spacing: 24) {
                // Story Title
                Text(gameState.currentScenario.rawValue)
                    .font(.title.bold())
                    .padding(.top)
                
                // Story Text with typewriter effect
                TypewriterText(text: gameState.storyText)
                    .padding(.horizontal)
                
                // Choices
                VStack(spacing: 16) {
                    ForEach(gameState.choices, id: \.text) { choice in
                        Button(action: {
                            withAnimation {
                                gameState.showingConsequence = true
                                gameState.consequenceText = choice.consequence
                                
                                // Delay the scenario transition
                                DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
                                    if let nextScenario = choice.nextScenario {
                                        withAnimation {
                                            gameState.loadScenario(nextScenario)
                                            gameState.showingConsequence = false
                                        }
                                    }
                                }
                            }
                        }) {
                            Text(choice.text)
                                .font(.system(size: settings.textSize))
                                .foregroundColor(settings.isDarkMode ? .black : .white)
                                .frame(maxWidth: .infinity)
                                .padding()
                                .background(
                                    RoundedRectangle(cornerRadius: 12)
                                        .fill(settings.isDarkMode ? .white : .black)
                                )
                        }
                    }
                }
                .padding()
                
                // Consequence Text
                if gameState.showingConsequence {
                    Text(gameState.consequenceText)
                        .font(.title3)
                        .multilineTextAlignment(.center)
                        .padding()
                        .frame(maxWidth: .infinity)
                        .background(Color.black.opacity(0.8))
                        .foregroundColor(.white)
                        .cornerRadius(12)
                        .padding()
                        .transition(.opacity)
                }
            }
        }
        .onAppear {
            gameState.loadScenario(.cleaningRitual)
        }
    }
} 
