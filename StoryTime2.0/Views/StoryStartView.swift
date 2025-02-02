//
//  StoryStartView.swift
//  StoryTime2.0
//
//  Created by Aryan Signh on 27/01/25.
//

import SwiftUI

// MARK: - StoryStartView
struct StoryStartView: View {
    let story: Story
    @ObservedObject var settings: SettingsModel
    @State private var startStory = false
    @State private var isAnimating = false
    @State private var scrollOffset: CGFloat = 0
    @State private var showSettings = false
    @State private var isBookmarked = false
    @State private var showShareSheet = false
    @Environment(\.dismiss) private var dismiss
    
    // Computed properties for story statistics
    private var wordCount: Int {
        story.description.split(separator: " ").count
    }
    
    private var estimatedReadTime: Int {
        // Average reading speed: 200 words per minute
        max(1, Int(ceil(Double(wordCount) / 200.0)))
    }
    
    var body: some View {
        ScrollView {
            VStack(alignment: .leading, spacing: 32) {
                // Story Title & Description Section
                VStack(alignment: .leading, spacing: 8) {
                    Text(story.title)
                        .font(.system(.largeTitle, design: .rounded))
                        .fontWeight(.bold)
                        .foregroundColor(.primary)
                        .accessibilityAddTraits(.isHeader)
                    
                    Text(story.description)
                        .font(.system(.body, design: .rounded))
                        .foregroundColor(.secondary)
                }
                .padding([.horizontal, .top])
                
                // Optional Illustrative Image
                Image(systemName: "book.fill")
                    .resizable()
                    .scaledToFit()
                    .frame(maxWidth: 200)
                    .foregroundColor(.accentColor)
                    .padding()
                    .frame(maxWidth: .infinity)
                
                // Story Summary
                VStack(alignment: .leading, spacing: 12) {
                    Text("Story Summary")
                        .font(.headline)
                        .padding(.horizontal)
                    
                    Text(story.summary)
                        .font(.body)
                        .foregroundColor(.secondary)
                        .padding(.horizontal)
                }
                
                // Call-to-Action Navigation Link with enhanced animation
                NavigationLink(destination: destinationView()) {
                    Text("Start Story")
                        .font(.headline)
                        .frame(maxWidth: .infinity)
                        .padding()
                        .background(Color.accentColor)
                        .foregroundColor(.white)
                        .cornerRadius(12)
                        .padding(.horizontal)
                }
                .buttonStyle(AnimatedButtonStyle())
                .padding(.bottom, 40)
            }
        }
        .background(Color(UIColor.systemBackground))
        .navigationTitle("Story")
        .navigationBarTitleDisplayMode(.inline)
    }
    
    @ViewBuilder
    private func destinationView() -> some View {
        switch story.title.trimmingCharacters(in: .whitespacesAndNewlines) {
        case "Dragon's Quest":
            // Navigates to the Dragons Quest game view.
            DragonsQuestGameView(settings: settings)
        case "Mystery Manor":
            // Navigates to the Mystery Manor game view.
            MysteryManorGameView(settings: settings)
        case "Space Pioneer":
            // Navigates to the Space Pioneer game view.
            SpaceGameView()
        case "Time Traveler":
            // Navigates to the Time Traveler game view.
            TimeTravelerGameView(settings: settings)
        case "The Lost City":
            // Navigates to the Lost City game view.
            LostCityGameView()
        default:
            // Fallback view if none of the specific game views is matched.
            StoryView(story: story, settings: settings)
        }
    }
}

struct StoryStartView_Previews: PreviewProvider {
    static var previews: some View {
        NavigationStack {
            StoryStartView(story: Story.featured, settings: SettingsModel())
        }
    }
}

// Update Story model to include optional chapters count
extension Story {
    var chapters: Int? {
        // Return the actual number of chapters if available
        // For now returning a default value
        return 5
    }
}

// MARK: - Story Summary Extension
extension Story {
    var summary: String {
        switch title.trimmingCharacters(in: .whitespacesAndNewlines) {
        case "The Lost City":
            return "Journey through ancient ruins as you unravel the mystery of a lost civilization, uncover hidden artifacts, and rediscover forgotten lore."
        case "Space Pioneer":
            return "Embark on an interstellar adventure where the cosmos is your playground, and deep space reveals secrets beyond imagination."
        case "Mystery Manor":
            return "Step into a haunted mansion full of secrets and unexpected twists, where every door may lead you closer to the truth."
        case "Dragon's Quest":
            return "Enter a realm of magic and myth where fierce dragons roam and ancient prophecies come alive in epic battles."
        case "Time Traveler":
            return "Experience a thrilling journey through time where every decision reshapes the past, present, and future in extraordinary ways."
        case "The Buried Haven":
            return "Survive the perils of an underground facility where hidden truths and unspoken challenges test your resolve."
        default:
            return "Embark on an unforgettable adventure filled with challenges, mystery, and intrigue."
        }
    }
}

// Helper Views
struct ParallaxHeader: View {
    let title: String
    let description: String
    let category: StoryCategory
    @Binding var scrollOffset: CGFloat
    
    var body: some View {
        GeometryReader { geo in
            let minY = geo.frame(in: .named("scroll")).minY
            let height = geo.size.height + (minY > 0 ? minY : 0)
            
            ZStack(alignment: .bottom) {
                LinearGradient(
                    colors: [
                        .blue.opacity(0.9),
                        .purple.opacity(0.7)
                    ],
                    startPoint: .topLeading,
                    endPoint: .bottomTrailing
                )
                .overlay(
                    AngularGradient(
                        gradient: Gradient(colors: [.blue, .purple, .blue]),
                        center: .topTrailing,
                        angle: .degrees(45)
                    )
                    .opacity(0.2)
                )
                .frame(height: height)
                .offset(y: minY > 0 ? -minY : 0)
            }
        }
        .frame(height: 400)
    }
}

//// Improved StatItem with animation
//struct StatItem: View {
//    let icon: String
//    let value: String
//    let label: String
//    let delay: Double
//    @State private var isShown = false
//    
//    var body: some View {
//        VStack(spacing: 12) {
//            ZStack {
//                Circle()
//                    .fill(Color.blue.opacity(0.1))
//                    .frame(width: 44, height: 44)
//                
//                Image(systemName: icon)
//                    .font(.system(size: 20, weight: .medium))
//                    .foregroundColor(.blue)
//            }
//            
//            VStack(spacing: 4) {
//                Text(value)
//                    .font(.title3.bold())
//                    .foregroundColor(.primary)
//                
//                Text(label)
//                    .font(.caption)
//                    .foregroundColor(.secondary)
//            }
//        }
//        .frame(maxWidth: .infinity)
//        .opacity(isShown ? 1 : 0)
//        .offset(y: isShown ? 0 : 20)
//        .onAppear {
//            withAnimation(.spring(response: 0.6, dampingFraction: 0.7).delay(delay)) {
//                isShown = true
//            }
//        }
//    }
//}

// Custom button style for consistent interaction
struct ScaleButtonStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .scaleEffect(configuration.isPressed ? 0.98 : 1)
            .animation(.spring(response: 0.3), value: configuration.isPressed)
    }
}

// Share sheet helper
struct ShareSheet: UIViewControllerRepresentable {
    let activityItems: [Any]
    
    func makeUIViewController(context: Context) -> UIActivityViewController {
        UIActivityViewController(activityItems: activityItems, applicationActivities: nil)
    }
    
    func updateUIViewController(_ uiViewController: UIActivityViewController, context: Context) {}
}

// Helper for tracking scroll offset
struct OffsetPreferenceKey: PreferenceKey {
    static var defaultValue: CGFloat = 0
    static func reduce(value: inout CGFloat, nextValue: () -> CGFloat) {
        value = nextValue()
    }
}

// Helper for rounded corners
extension View {
    func cornerRadius(_ radius: CGFloat, corners: UIRectCorner) -> some View {
        clipShape(RoundedCorner(radius: radius, corners: corners))
    }
}

struct RoundedCorner: Shape {
    var radius: CGFloat = .infinity
    var corners: UIRectCorner = .allCorners
    
    func path(in rect: CGRect) -> Path {
        let path = UIBezierPath(
            roundedRect: rect,
            byRoundingCorners: corners,
            cornerRadii: CGSize(width: radius, height: radius)
        )
        return Path(path.cgPath)
    }
}

struct ReadingSettingsView: View {
    @ObservedObject var settings: SettingsModel
    @Environment(\.dismiss) var dismiss
    
    var body: some View {
        NavigationView {
            Form {
                Section {
                    VStack(spacing: 16) {
                        HStack {
                            Text("A")
                                .font(.system(size: settings.minTextSize))
                            Slider(
                                value: $settings.textSize,
                                in: settings.minTextSize...settings.maxTextSize,
                                step: 1
                            )
                            Text("A")
                                .font(.system(size: settings.maxTextSize))
                        }
                        .padding(.vertical, 8)
                        
                        Text("Preview Text")
                            .font(.custom(settings.selectedFontName, size: settings.textSize))
                            .frame(maxWidth: .infinity, alignment: .leading)
                            .padding(.vertical, 8)
                    }
                } header: {
                    Text("Text Size")
                }
                
                Section("Font") {
                    Picker("Font", selection: $settings.selectedFontName) {
                        ForEach(settings.availableFonts, id: \.self) { font in
                            Text(font)
                                .font(.custom(font, size: 17))
                        }
                    }
                }
                
                Section("Theme") {
                    Toggle("Dark Mode", isOn: $settings.isDarkMode)
                        .tint(.blue)
                }
            }
            .navigationTitle("Reading Settings")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .navigationBarTrailing) {
                    Button("Done") { 
                        dismiss() 
                    }
                    .font(.system(size: 17, weight: .semibold))
                }
            }
        }
    }
}

// MARK: - AnimatedButtonStyle
struct AnimatedButtonStyle: ButtonStyle {
    func makeBody(configuration: Configuration) -> some View {
        configuration.label
            .scaleEffect(configuration.isPressed ? 0.95 : 1)
            .shadow(
                color: configuration.isPressed ? Color.accentColor.opacity(0.6) : Color.clear,
                radius: configuration.isPressed ? 10 : 0,
                x: 0,
                y: configuration.isPressed ? 5 : 0
            )
            .animation(.easeInOut(duration: 0.2), value: configuration.isPressed)
    }
} 
