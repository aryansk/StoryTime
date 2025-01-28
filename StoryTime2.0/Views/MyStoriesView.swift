import SwiftUI
struct MyStoryReaderView: View {
    let story: UserStory
    @ObservedObject var settings: SettingsModel
    @State private var selectedScenario: UserScenario?
    @State private var isAnimating = false
    
    var body: some View {
        ScrollView {
            VStack(spacing: 32) {
                // Story Header
                VStack(alignment: .leading, spacing: 16) {
                    Text(story.title)
                        .font(.title.bold())
                        .foregroundColor(.primary)
                    
                    Text(story.description)
                        .font(.body)
                        .foregroundColor(.secondary)
                        .lineSpacing(4)
                }
                .padding(.horizontal)
                .padding(.top)
                
                // Story Progress
                HStack(spacing: 24) {
                    ProgressStat(
                        icon: "book.fill",
                        value: "\(story.scenarios.count)",
                        label: "Chapters",
                        color: .yellow
                    )
                    
                    ProgressStat(
                        icon: "chart.line.uptrend.xyaxis",
                        value: "\(Int((Double(story.scenarios.count) / 5.0) * 100))%",
                        label: "Complete",
                        color: .yellow
                    )
                }
                .padding(.vertical, 8)
                
                // Scenarios List
                VStack(spacing: 24) {
                    ForEach(Array(story.scenarios.enumerated()), id: \.element.id) { index, scenario in
                        ScenarioCard(
                            scenario: scenario,
                            index: index,
                            isSelected: selectedScenario?.id == scenario.id,
                            settings: settings,
                            onSelect: {
                                withAnimation(.spring(response: 0.3)) {
                                    selectedScenario = scenario
                                }
                            }
                        )
                    }
                }
                .padding(.horizontal)
            }
            .padding(.bottom, 32)
        }
        .background(Color(UIColor.systemGroupedBackground))
    }
}

struct ScenarioCard: View {
    let scenario: UserScenario
    let index: Int
    let isSelected: Bool
    let settings: SettingsModel
    let onSelect: () -> Void
    @State private var isHovered = false
    
    var body: some View {
        Button(action: onSelect) {
            VStack(alignment: .leading, spacing: 16) {
                // Chapter Header
                HStack {
                    Text("Chapter \(index + 1)")
                        .font(.headline)
                        .foregroundColor(.yellow)
                    
                    Spacer()
                    
                    Image(systemName: "chevron.right")
                        .font(.system(size: 14, weight: .semibold))
                        .foregroundColor(.secondary)
                        .opacity(isHovered ? 1 : 0.5)
                        .offset(x: isHovered ? 4 : 0)
                }
                
                // Story Content
                Text(scenario.storyText)
                    .font(.custom(settings.selectedFontName, size: settings.textSize))
                    .foregroundColor(.primary)
                    .lineLimit(2)
                    .padding(.bottom, 8)
                
                // Add a background and shadow for better visibility
                .padding()
                .background(
                    RoundedRectangle(cornerRadius: 12)
                        .fill(Color(UIColor.secondarySystemGroupedBackground))
                        .shadow(color: .black.opacity(0.1), radius: 5, y: 2)
                )
            }
            .padding(12)
            .frame(maxWidth: .infinity) // Ensure cards take full width
            .scaleEffect(isHovered ? 0.98 : 1)
            .animation(.spring(response: 0.3), value: isHovered)
            .onHover { hovering in
                isHovered = hovering
            }
        }
        .buttonStyle(PlainButtonStyle()) // Use plain button style for a cleaner look
    }
}

struct ProgressStat: View {
    let icon: String
    let value: String
    let label: String
    let color: Color
    @State private var isVisible = false
    
    var body: some View {
        VStack(spacing: 8) {
            ZStack {
                Circle()
                    .fill(color.opacity(0.1))
                    .frame(width: 44, height: 44)
                
                Image(systemName: icon)
                    .font(.system(size: 20))
                    .foregroundColor(color)
            }
            
            VStack(spacing: 4) {
                Text(value)
                    .font(.title3.bold())
                    .foregroundColor(.primary)
                
                Text(label)
                    .font(.caption)
                    .foregroundColor(.secondary)
            }
        }
        .opacity(isVisible ? 1 : 0)
        .offset(y: isVisible ? 0 : 20)
        .onAppear {
            withAnimation(.spring(response: 0.6, dampingFraction: 0.7)) {
                isVisible = true
            }
        }
    }
} 
