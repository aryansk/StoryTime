import SwiftUI

struct StoryView: View {
    let story: Story
    @ObservedObject var settings: SettingsModel
    @StateObject private var gameState = GameState()
    @Environment(\.dismiss) var dismiss
    @State private var selectedChoice: Int? = nil
    @State private var currentText: String = ""
    @State private var showingConsequence = false
    @State private var previousScenarios: [Scenario] = []
    @State private var storyHistory: [(text: String, isConsequence: Bool)] = []
    
    var body: some View {
        ZStack {
            // Background
            Color(white: 0.98)
                .ignoresSafeArea()
            
            VStack(spacing: 0) {
                // Navigation Bar
                HStack {
                    Button(action: {
                        if let previousScenario = previousScenarios.popLast() {
                            withAnimation {
                                gameState.loadScenario(previousScenario)
                                currentText = gameState.storyText
                                showingConsequence = false
                                selectedChoice = nil
                                if !storyHistory.isEmpty {
                                    storyHistory.removeLast()
                                    if !storyHistory.isEmpty && storyHistory.last?.isConsequence == true {
                                        storyHistory.removeLast()
                                    }
                                }
                            }
                        } else {
                            dismiss()
                        }
                    }) {
                        HStack {
                            Image(systemName: "chevron.left")
                            Text("Back")
                        }
                        .foregroundColor(.blue)
                    }
                    .padding()
                    
                    Spacer()
                }
                .background(Color.white.opacity(0.95))
                .shadow(color: Color.black.opacity(0.05), radius: 2, y: 1)
                
                // Story Content
                ScrollView {
                    VStack(alignment: .leading, spacing: 24) {
                        // Story history
                        VStack(alignment: .leading, spacing: 24) {
                            if gameState.isFirstScene && storyHistory.isEmpty {
                                Text("Let us begin.")
                                    .font(.custom(settings.selectedFontName, size: 24))
                                    .padding(.bottom, 8)
                            }
                            
                            ForEach(Array(storyHistory.enumerated()), id: \.offset) { _, entry in
                                VStack(alignment: .leading, spacing: 8) {
                                    if entry.isConsequence {
                                        Text("→")
                                            .font(.title2)
                                            .foregroundColor(.gray)
                                    }
                                    TypewriterText(text: entry.text)
                                        .font(.custom(settings.selectedFontName, size: settings.textSize))
                                        .lineSpacing(8)
                                }
                            }
                            
                            // Current text if not in history
                            if !showingConsequence {
                                TypewriterText(text: gameState.storyText)
                                    .font(.custom(settings.selectedFontName, size: settings.textSize))
                                    .lineSpacing(8)
                            }
                        }
                        .foregroundColor(.black)
                        .padding(.horizontal)
                        .padding(.top, 24)
                        
                        Spacer(minLength: 100)
                    }
                    .frame(maxWidth: .infinity, alignment: .leading)
                }
                .background(settings.themeColor)
                
                // Fixed Bottom Navigation
                VStack(spacing: 12) {
                    // Choices
                    ForEach(Array(gameState.choices.enumerated()), id: \.element.text) { index, choice in
                        Button(action: {
                            withAnimation {
                                selectedChoice = index
                                showingConsequence = true
                                currentText = choice.consequence
                                previousScenarios.append(gameState.currentScenario)
                                // Add current text to history before showing consequence
                                if !showingConsequence {
                                    storyHistory.append((gameState.storyText, false))
                                }
                                // Add consequence to history
                                storyHistory.append((choice.consequence, true))
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
                                    .font(.custom(settings.selectedFontName, size: settings.textSize - 2))
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
                    
                    // Next button
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
                    }
                }
                .padding()
                .background(
                    Color.white.opacity(0.95)
                        .shadow(color: Color.black.opacity(0.05), radius: 4, y: -2)
                )
            }
        }
        .navigationBarHidden(true)
        .onAppear {
            gameState.loadScenario(.cleaningRitual)
            currentText = gameState.storyText
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

// Add this property to GameState
extension GameState {
    var isFirstScene: Bool {
        currentScenario == .cleaningRitual
    }
} 
