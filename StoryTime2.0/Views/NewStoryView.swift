import SwiftUI

struct CreateStoryView: View {
    @Environment(\.dismiss) var dismiss
    @ObservedObject var viewModel: StoryCreatorViewModel
    @ObservedObject var settings: SettingsModel
    @State private var title = ""
    @State private var description = ""
    
    var body: some View {
        NavigationView {
            Form {
                TextField("Story Title", text: $title)
                    .foregroundColor(settings.isDarkMode ? .white : .black)
                TextField("Description", text: $description, axis: .vertical)
                    .lineLimit(3...6)
                    .foregroundColor(settings.isDarkMode ? .white : .black)
            }
            .navigationTitle("New Story")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button("Cancel") { dismiss() }
                }
                ToolbarItem(placement: .confirmationAction) {
                    Button("Create") {
                        let newStory = UserStory(title: title, description: description)
                        viewModel.addStory(newStory)
                        dismiss()
                    }
                    .disabled(title.isEmpty)
                }
            }
        }
    }
} 
