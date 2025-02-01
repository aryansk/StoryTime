import SwiftUI

struct TimeTravelerStoryView: View {
    @ObservedObject var settings: SettingsModel
    @StateObject private var gameState = TimeTravelerGameState()
    @Environment(\.dismiss) var dismiss
    @State private var selectedChoice: Int? = nil
    @State private var currentText: String = ""
    @State private var showingConsequence = false
    @State private var previousScenarios: [TimeTravelerScenario] = []
    @State private var storyHistory: [(text: String, isConsequence: Bool)] = []
    
    var body: some View {
        ZStack {
            Color(white: 0.98)
                .ignoresSafeArea()
            
            VStack(spacing: 0) {
                // Navigation Bar
                HStack {
                    Button {
                        if let previous = previousScenarios.popLast() {
                            withAnimation {
                                gameState.loadScenario(previous)
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
                    } label: {
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
                        VStack(alignment: .leading, spacing: 24) {
                            if gameState.currentScenario == .discovery && storyHistory.isEmpty {
                                Text("Your time-travel begins now.")
                                    .font(.headline)
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
                                        .font(.body)
                                        .lineSpacing(8)
                                }
                            }
                            
                            if !showingConsequence {
                                TypewriterText(text: gameState.storyText)
                                    .font(.body)
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
                
                // Fixed Bottom Navigation: Choices & Next Button
                VStack(spacing: 12) {
                    ForEach(Array(gameState.choices.enumerated()), id: \.offset) { index, choice in
                        Button {
                            withAnimation {
                                selectedChoice = index
                                showingConsequence = true
                                currentText = choice.consequence
                                previousScenarios.append(gameState.currentScenario)
                                if !showingConsequence {
                                    storyHistory.append((gameState.storyText, false))
                                }
                                storyHistory.append((choice.consequence, true))
                            }
                        } label: {
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
                                    .font(.body)
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
                    
                    if selectedChoice != nil {
                        Button {
                            if let choiceIndex = selectedChoice {
                                navigateToNext(choice: gameState.choices[choiceIndex])
                            }
                        } label: {
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
            }
        }
    }
    
    private func navigateToNext(choice: TimeTravelerChoice) {
        withAnimation {
            if let next = choice.nextScenario {
                gameState.loadScenario(next)
                currentText = gameState.storyText
                selectedChoice = nil
                showingConsequence = false
            } else {
                dismiss()
            }
        }
    }
} 