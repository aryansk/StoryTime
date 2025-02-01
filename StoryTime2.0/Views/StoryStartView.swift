import SwiftUI

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
        ZStack {
            // Background with dynamic color based on scroll
            Color(UIColor.systemBackground)
                .overlay(
                    LinearGradient(
                        colors: [
                            .blue.opacity(max(0, 0.3 - scrollOffset/400)),
                            .clear
                        ],
                        startPoint: .top,
                        endPoint: .bottom
                    )
                )
                .ignoresSafeArea()
            
            ScrollView {
                VStack(spacing: 0) {
                    // Hero Section with improved parallax
                    ParallaxHeader(
                        title: story.title,
                        description: story.description,
                        category: story.category,
                        scrollOffset: $scrollOffset
                    )
                    .overlay(
                        Rectangle()
                            .fill(Color.black.opacity(0.2))
                    )
                    
                    // Story Content with improved layout
                    VStack(alignment: .leading, spacing: 28) {
                        // Story Title and Metadata
                        VStack(alignment: .leading, spacing: 16) {
                            Text(story.title)
                                .font(.system(size: 34, weight: .bold))
                                .foregroundColor(.primary)
                                .padding(.horizontal)
                                .padding(.top)
                                .frame(maxWidth: .infinity, alignment: .leading)
                                .background(
                                    LinearGradient(
                                        colors: [.blue.opacity(0.1), .clear],
                                        startPoint: .top,
                                        endPoint: .bottom
                                    )
                                )
                            
                            // Story Metadata
                            HStack(spacing: 20) {
                                Label(story.category.rawValue, systemImage: story.category.icon)
                                    .font(.subheadline)
                                    .foregroundColor(.blue)
                                
                                Divider()
                                    .frame(height: 20)
                                
                                Label("\(estimatedReadTime) min", systemImage: "clock")
                                    .font(.subheadline)
                                    .foregroundColor(.secondary)
                                
                                Divider()
                                    .frame(height: 20)
                                
                                Label("4.8 ★", systemImage: "star.fill")
                                    .font(.subheadline)
                                    .foregroundColor(.orange)
                            }
                            .padding(.horizontal)
                        }
                        
                        // Story Preview with improved typography
                        VStack(alignment: .leading, spacing: 16) {
                            HStack {
                                Text("Preview")
                                    .font(.title3.bold())
                                    .foregroundColor(.primary)
                                
                                Spacer()
                                
                                // Updated category badge
                                HStack(spacing: 6) {
                                    Image(systemName: story.category.icon)
                                        .font(.system(size: 12))
                                    Text(story.category.rawValue)
                                        .font(.system(size: 12, weight: .medium))
                                }
                                .padding(.horizontal, 12)
                                .padding(.vertical, 6)
                                .background(
                                    Capsule()
                                        .fill(Color.blue.opacity(0.1))
                                        .shadow(color: .blue.opacity(0.1), radius: 2, y: 2)
                                )
                                .foregroundColor(.blue)
                            }
                            
                            Text(story.description)
                                .font(.custom(settings.selectedFontName, size: settings.textSize))
                                .foregroundColor(.primary)
                                .lineSpacing(6)
                                .padding()
                                .background(
                                    RoundedRectangle(cornerRadius: 16)
                                        .fill(Color(.secondarySystemBackground))
                                )
                        }
                        .padding()
                        .background(
                            RoundedRectangle(cornerRadius: 16)
                                .fill(Color(UIColor.secondarySystemBackground))
                                .shadow(color: .black.opacity(0.05), radius: 8, y: 4)
                        )
                        
                        // Start Button with improved animation
                        NavigationLink(destination: destinationView()) {
                            HStack(spacing: 10) {
                                Text("Begin Story")
                                    .font(.title2.bold())
                                    .foregroundColor(.white)
                                Image(systemName: "arrow.right.circle.fill")
                                    .font(.title2)
                                    .foregroundColor(.white)
                                    .padding(.leading, 4)
                            }
                            .padding(.vertical, 16)
                            .padding(.horizontal, 32)
                            .frame(maxWidth: .infinity)
                            .background(
                                LinearGradient(
                                    gradient: Gradient(colors: [Color.blue, Color.blue.opacity(0.8)]),
                                    startPoint: .leading,
                                    endPoint: .trailing
                                )
                            )
                            .clipShape(Capsule())
                            .shadow(color: Color.blue.opacity(0.5), radius: 12, x: 0, y: 6)
                            .scaleEffect(isAnimating ? 0.98 : 1)
                            .animation(.spring(response: 0.3, dampingFraction: 0.7), value: isAnimating)
                            .accessibilityLabel("Begin Story")
                        }
                        .buttonStyle(ScaleButtonStyle())
                        .padding(.horizontal)
                        .padding(.top, 8)
                    }
                    .background(Color(UIColor.systemBackground))
                    .cornerRadius(32, corners: [.topLeft, .topRight])
                    .offset(y: -30)
                }
            }
            .ignoresSafeArea()
            .coordinateSpace(name: "scroll")
            .onPreferenceChange(OffsetPreferenceKey.self) { offset in
                scrollOffset = offset
            }
            .preferredColorScheme(settings.isDarkMode ? .dark : .light)
        }
        .navigationBarTitleDisplayMode(.inline)
        .navigationBarBackButtonHidden(true)
        .toolbar {
            ToolbarItem(placement: .navigationBarLeading) {
                Button(action: { dismiss() }) {
                    Image(systemName: "chevron.left")
                        .font(.system(size: 16, weight: .semibold))
                        .foregroundColor(.primary)
                }
            }
        }
        .sheet(isPresented: $showSettings) {
            NavigationView {
                ReadingSettingsView(settings: settings)
                    .preferredColorScheme(settings.isDarkMode ? .dark : .light)
            }
        }
        .sheet(isPresented: $showShareSheet) {
            ShareSheet(activityItems: [
                "Check out this story: \(story.title)\n\n\(story.description)"
            ])
        }
        .onAppear {
            withAnimation(.spring(response: 0.6, dampingFraction: 0.7).delay(0.3)) {
                isAnimating = true
            }
        }
    }
    
    @ViewBuilder
    private func destinationView() -> some View {
        // Assuming that the game category is represented as .game
        if story.category == .game {
            SpacePioneerStoryView(settings: settings)
        } else {
            StoryView(story: story, settings: settings)
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
