import SwiftUI

struct NextSceneView: View {
    let story: Story
    let scenario: Scenario
    let consequence: String
    @ObservedObject var settings: SettingsModel
    @StateObject private var gameState = GameState()
    @State private var selectedChoice: Int? = nil
    @State private var currentText: String = ""
    @State private var showingConsequence = true
    
    var body: some View {
        ZStack {
            // Background
            Color(white: 0.98)
                .ignoresSafeArea()
            
            VStack(spacing: 24) {
                ScrollView {
                    VStack(alignment: .leading, spacing: 24) {
                        // Story text with dynamic content
                        TypewriterText(text: currentText)
                            .font(.custom("New York", size: 20))
                            .foregroundColor(.black)
                            .lineSpacing(8)
                            .padding(.horizontal)
                            .animation(.easeInOut, value: currentText)
                        
                        // Choices
                        VStack(spacing: 12) {
                            ForEach(Array(gameState.choices.enumerated()), id: \.element.text) { index, choice in
                                Button(action: {
                                    withAnimation {
                                        selectedChoice = index
                                        showingConsequence = true
                                        currentText = choice.consequence
                                    }
                                }) {
                                    HStack {
                                        ZStack {
                                            Circle()
                                                .strokeBorder(Color.gray.opacity(0.3), lineWidth: 1)
                                                .frame(width: 24, height: 24)
                                            
                                            if selectedChoice == index {
                                                Circle()
                                                    .fill(Color.gray)
                                                    .frame(width: 16, height: 16)
                                            }
                                        }
                                        
                                        Text(choice.text)
                                            .font(.custom("New York", size: 18))
                                            .foregroundColor(.black)
                                            .multilineTextAlignment(.leading)
                                            .padding(.leading, 8)
                                    }
                                    .padding()
                                    .frame(maxWidth: .infinity, alignment: .leading)
                                    .background(
                                        RoundedRectangle(cornerRadius: 12)
                                            .fill(Color.white)
                                            .shadow(color: Color.black.opacity(0.05), radius: 2, x: 0, y: 1)
                                    )
                                }
                                .disabled(showingConsequence && selectedChoice != index)
                                .opacity(showingConsequence && selectedChoice != index ? 0.5 : 1)
                            }
                        }
                        .padding(.horizontal)
                    }
                    .padding(.vertical, 24)
                }
                
                if selectedChoice != nil {
                    Button(action: {
                        if let choice = selectedChoice {
                            navigateToNext(choice: gameState.choices[choice])
                        }
                    }) {
                        Text("Next")
                            .font(.headline)
                            .foregroundColor(.white)
                            .frame(maxWidth: .infinity)
                            .padding()
                            .background(
                                RoundedRectangle(cornerRadius: 12)
                                    .fill(Color.gray)
                            )
                    }
                    .padding(.horizontal)
                    .transition(.move(edge: .bottom).combined(with: .opacity))
                }
            }
        }
        .navigationBarTitleDisplayMode(.inline)
        .onAppear {
            gameState.loadScenario(scenario)
            currentText = consequence
            
            // After showing consequence, show the scenario text
            DispatchQueue.main.asyncAfter(deadline: .now() + 2) {
                withAnimation {
                    currentText = gameState.storyText
                    showingConsequence = false
                }
            }
        }
    }
    
    private func navigateToNext(choice: Choice) {
        if let nextScenario = choice.nextScenario {
            withAnimation {
                showingConsequence = false
                gameState.loadScenario(nextScenario)
                selectedChoice = nil
                currentText = gameState.storyText
            }
        }
    }
} 