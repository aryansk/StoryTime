import SwiftUI

struct StoryEditorView: View {
    @State var story: UserStory
    @ObservedObject var settings: SettingsModel
    @State private var showingNewScenarioSheet = false
    @Environment(\.dismiss) var dismiss
    @StateObject private var viewModel = StoryCreatorViewModel()
    
    var body: some View {
        List {
            Section("Story Details") {
                VStack(alignment: .leading, spacing: 8) {
                    Text("Title: \(story.title)")
                        .font(.headline)
                        .foregroundColor(settings.isDarkMode ? .white : .black)
                    Text(story.description)
                        .font(.subheadline)
                        .foregroundStyle(.secondary)
                }
            }
            
            Section("Scenarios") {
                ForEach(story.scenarios) { scenario in
                    NavigationLink(destination: ScenarioEditorView(scenario: scenario, settings: settings)) {
                        VStack(alignment: .leading) {
                            Text(scenario.title)
                                .font(.headline)
                            Text(scenario.storyText.prefix(50) + "...")
                                .font(.subheadline)
                                .foregroundStyle(.secondary)
                        }
                    }
                }
                
                Button(action: { showingNewScenarioSheet = true }) {
                    Label("Add Scenario", systemImage: "plus.circle")
                }
            }
        }
        .navigationTitle("Edit Story")
        .navigationBarTitleDisplayMode(.inline)
        .sheet(isPresented: $showingNewScenarioSheet) {
            NewScenarioView(story: $story, settings: settings)
        }
    }
}

struct ScenarioEditorView: View {
    @State var scenario: UserScenario
    @ObservedObject var settings: SettingsModel
    @State private var showingNewChoiceSheet = false
    
    var body: some View {
        List {
            Section("Scenario Details") {
                VStack(alignment: .leading, spacing: 8) {
                    Text("Title: \(scenario.title)")
                        .font(.headline)
                        .foregroundColor(settings.isDarkMode ? .white : .black)
                    Text(scenario.storyText)
                        .font(.body)
                }
            }
            
            Section("Choices") {
                ForEach(scenario.choices) { choice in
                    VStack(alignment: .leading) {
                        Text(choice.text)
                            .font(.headline)
                            .foregroundColor(settings.isDarkMode ? .white : .black)
                        Text("Consequence: \(choice.consequence)")
                            .font(.subheadline)
                            .foregroundStyle(.secondary)
                    }
                }
                
                Button(action: { showingNewChoiceSheet = true }) {
                    Label("Add Choice", systemImage: "plus.circle")
                }
            }
        }
        .navigationTitle("Edit Scenario")
        .navigationBarTitleDisplayMode(.inline)
        .sheet(isPresented: $showingNewChoiceSheet) {
            NewChoiceView(scenario: $scenario, settings: settings)
        }
    }
}

struct NewScenarioView: View {
    @Binding var story: UserStory
    @ObservedObject var settings: SettingsModel
    @Environment(\.dismiss) var dismiss
    @State private var title = ""
    @State private var storyText = ""
    
    var body: some View {
        NavigationView {
            Form {
                TextField("Scenario Title", text: $title)
                    .foregroundColor(settings.isDarkMode ? .white : .black)
                TextField("Story Text", text: $storyText, axis: .vertical)
                    .lineLimit(5...10)
                    .foregroundColor(settings.isDarkMode ? .white : .black)
            }
            .navigationTitle("New Scenario")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button("Cancel") { dismiss() }
                }
                ToolbarItem(placement: .confirmationAction) {
                    Button("Add") {
                        let newScenario = UserScenario(
                            title: title,
                            storyText: storyText
                        )
                        story.scenarios.append(newScenario)
                        dismiss()
                    }
                    .disabled(title.isEmpty || storyText.isEmpty)
                }
            }
        }
    }
}

struct NewChoiceView: View {
    @Binding var scenario: UserScenario
    @ObservedObject var settings: SettingsModel
    @Environment(\.dismiss) var dismiss
    @State private var text = ""
    @State private var consequence = ""
    
    var body: some View {
        NavigationView {
            Form {
                TextField("Choice Text", text: $text)
                    .foregroundColor(settings.isDarkMode ? .white : .black)
                TextField("Consequence", text: $consequence, axis: .vertical)
                    .lineLimit(3...6)
                    .foregroundColor(settings.isDarkMode ? .white : .black)
            }
            .navigationTitle("New Choice")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button("Cancel") { dismiss() }
                }
                ToolbarItem(placement: .confirmationAction) {
                    Button("Add") {
                        let newChoice = UserChoice(
                            text: text,
                            consequence: consequence
                        )
                        scenario.choices.append(newChoice)
                        dismiss()
                    }
                    .disabled(text.isEmpty || consequence.isEmpty)
                }
            }
        }
    }
} 