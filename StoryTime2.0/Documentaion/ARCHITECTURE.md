# Technical Architecture
## StoryTime iOS Application

### Overview
StoryTime follows the MVVM (Model-View-ViewModel) architecture pattern and is built using SwiftUI. The application is structured to maintain separation of concerns, maximize code reuse, and ensure scalability.

### Directory Structure
```
StoryTime/
├── Features/
│   ├── Story/
│   │   ├── Views/
│   │   │   ├── StoryStartView.swift
│   │   │   ├── StoryView.swift
│   │   │   └── StoryEditorView.swift
│   │   ├── ViewModels/
│   │   │   └── StoryViewModel.swift
│   │   └── Models/
│   │       └── Story.swift
│   ├── Creation/
│   │   ├── Views/
│   │   │   ├── CustomStoryView.swift
│   │   │   └── AIStoryView.swift
│   │   ├── ViewModels/
│   │   │   └── AIStoryModel.swift
│   │   └── Services/
│   │       └── AIService.swift
│   └── Settings/
│       ├── Views/
│       │   └── SettingsView.swift
│       └── Models/
│           └── SettingsModel.swift
├── Core/
│   ├── Models/
│   │   ├── UserModel.swift
│   │   └── TypewriterText.swift
│   ├── ViewModels/
│   │   └── StoryCreatorViewModel.swift
│   └── Services/
│       └── StorageService.swift
├── UI/
│   ├── Components/
│   │   ├── FeaturedStoryCard.swift
│   │   ├── StoryCard.swift
│   │   └── CategoryButton.swift
│   └── Styles/
│       └── CustomStyles.swift
└── Resources/
    ├── Assets.xcassets
    └── Localizable.strings
```

### Core Components

#### Models
- **Story**: Represents story data structure
- **UserModel**: Manages user preferences and state
- **SettingsModel**: Handles app-wide settings
- **TypewriterText**: Manages text animation effects

#### ViewModels
- **StoryViewModel**: Story presentation logic
- **AIStoryModel**: AI integration and story generation
- **StoryCreatorViewModel**: Story creation and management

#### Views
- **ContentView**: Main app container
- **CuratedStoriesView**: Story browsing interface
- **CustomStoryView**: Story creation interface
- **SettingsView**: App settings interface

### Key Features Implementation

#### Theme System
```swift
class SettingsModel: ObservableObject {
    @AppStorage("selectedTheme") var selectedTheme: Int = 0
    let themeColors: [(name: String, color: String)] = [
        ("Light Yellow", "FFFBE6"),
        ("Light Grey", "F5F5F5"),
        ("Sepia", "F4ECD8"),
        ("Mint", "F1F7ED"),
        ("Lavender", "F3E5F5")
    ]
}
```

#### Accessibility Implementation
```swift
struct AccessibleView: View {
    @ObservedObject var settings: SettingsModel
    
    var body: some View {
        content
            .accessibility(label: Text("Story Content"))
            .reducedMotionEnabled(settings.isReduceMotionEnabled)
            .highContrastEnabled(settings.isHighContrastEnabled)
    }
}
```

#### State Management
```swift
class UserModel: ObservableObject {
    @Published var currentStory: Story?
    @Published var userPreferences: Preferences
    @Published var isFirstLaunch: Bool
}
```

### Data Flow

#### MVVM Pattern
1. View observes ViewModel
2. ViewModel manages Model updates
3. Model notifies ViewModel of changes
4. ViewModel updates View state

```swift
struct StoryView: View {
    @StateObject private var viewModel: StoryViewModel
    @ObservedObject var settings: SettingsModel
    
    var body: some View {
        content
            .onChange(of: viewModel.storyContent) { updateUI() }
    }
}
```

### Performance Optimizations

#### Lazy Loading
```swift
ScrollView {
    LazyVStack {
        ForEach(stories) { story in
            StoryCard(story: story)
        }
    }
}
```

#### Memory Management
- Proper use of weak references
- Efficient resource cleanup
- Background task handling

### Testing Strategy

#### Unit Tests
- ViewModel logic testing
- Model validation
- Utility function verification

#### UI Tests
- User flow validation
- Accessibility testing
- Performance testing

### Security Considerations

#### Data Protection
- Local storage encryption
- Secure state management
- Privacy-focused design

#### Error Handling
```swift
enum StoryError: Error {
    case loadFailed
    case saveFailed
    case invalidData
}

func handleError(_ error: StoryError) {
    // Error handling logic
}
```

### Accessibility Features

#### VoiceOver Support
- Meaningful labels
- Clear navigation
- Proper grouping

#### Dynamic Type
- Scalable fonts
- Adaptive layouts
- Proper contrast

### Future Considerations

#### Scalability
- Modular design
- Extensible architecture
- Clean interfaces

#### Maintenance
- Documentation
- Code organization
- Version control

---

This architecture document is part of the Swift Student Challenge 2024 submission. 