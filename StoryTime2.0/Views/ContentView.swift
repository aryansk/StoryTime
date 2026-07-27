//
//  ContentView.swift
//  StoryTime2.0
//

import SwiftUI

struct ContentView: View {
    @StateObject private var userModel = UserModel()
    @StateObject private var settings = SettingsModel()
    @StateObject private var progressStore = ReadingProgressStore()
    @StateObject private var speechService = SpeechService()
    @StateObject private var favoritesStore = FavoritesStore()
    @StateObject private var statsStore = StatsStore()
    @StateObject private var notificationService = NotificationService()
    @StateObject private var catalog = CatalogService()
    @StateObject private var endingsTracker = EndingsTracker()
    @StateObject private var choiceDNA = ChoiceDNAStore()
    @StateObject private var ambience = AmbienceService()
    @StateObject private var personalStore = PersonalStoriesStore()
    @State private var selectedTab: AppTab = ContentView.initialTab()
    /// Story the user chose from the onboarding payoff screen; presented
    /// as soon as the onboarding cover has finished dismissing.
    @State private var onboardingStoryToStart: CatalogStory?

    private static func initialTab() -> AppTab {
        #if DEBUG
        let args = ProcessInfo.processInfo.arguments
        if let idx = args.firstIndex(of: "-startTab"), idx + 1 < args.count {
            switch args[idx + 1] {
            case "shows", "discover": return .discover
            case "library": return .library
            case "profile": return .profile
            case "settings": return .settings
            default: break
            }
        }
        #endif
        return .discover
    }

    /// Named `AppTab`, not `Tab`: a nested type called `Tab` would shadow
    /// SwiftUI's `Tab` inside this view's body, and every tab declaration
    /// below would resolve to the enum instead.
    enum AppTab: Hashable { case discover, library, profile, settings }

    /// Recompute and re-install the daily-story notification, picking a
    /// fresh "tonight's story" using the latest catalog and progress.
    /// Called on launch and after catalog refresh so the notification
    /// stays interesting even if the user never re-opens Settings.
    private func scheduleDailyStoryIfEnabled() {
        guard settings.dailyStoryEnabled else { return }
        guard notificationService.authState == .authorized else { return }
        notificationService.scheduleDailyStory(
            hour: settings.reminderHour,
            minute: settings.reminderMinute,
            from: catalog.stories,
            startedKeys: statsStore.storiesStarted
        )
    }

    private var debugShowPrivacy: Binding<Bool> {
        Binding(
            get: {
                #if DEBUG
                return ProcessInfo.processInfo.arguments.contains("-showPrivacy")
                #else
                return false
                #endif
            },
            set: { _ in }
        )
    }
    private var debugShowTerms: Binding<Bool> {
        Binding(
            get: {
                #if DEBUG
                return ProcessInfo.processInfo.arguments.contains("-showTerms")
                #else
                return false
                #endif
            },
            set: { _ in }
        )
    }

    private var debugDeepLink: Binding<CatalogStory?> {
        Binding(
            get: {
                #if DEBUG
                let args = ProcessInfo.processInfo.arguments
                guard let idx = args.firstIndex(of: "-deepLinkStoryID"),
                      idx + 1 < args.count else { return nil }
                return catalog.story(id: args[idx + 1])
                #else
                return nil
                #endif
            },
            set: { _ in }
        )
    }

    /// Freezes stop-motion jitter in the three inactive tabs so they aren't
    /// redrawing their doodle canvases behind the visible one. `TabView`
    /// keeps every tab's view alive to preserve scroll position and filter
    /// state, so without this the hidden tabs keep animating.
    private func paused(_ tab: AppTab) -> Bool { selectedTab != tab }

    var body: some View {
        // The system tab bar. On iOS 26+ this renders as Liquid Glass: a
        // floating capsule that refracts the page beneath it, minimizes to a
        // pill as the reader scrolls down, and expands again on scroll up —
        // which is why each tab's ScrollView is allowed to run edge to edge
        // underneath it rather than being inset by a hand-drawn bar.
        TabView(selection: $selectedTab) {
            Tab("Discover", systemImage: "sparkles", value: AppTab.discover) {
                CatalogShowsView(catalog: catalog, settings: settings, userModel: userModel)
                    .environment(\.stJitterPaused, paused(.discover))
            }
            Tab("Library", systemImage: "books.vertical", value: AppTab.library) {
                LibraryView(catalog: catalog, settings: settings)
                    .environment(\.stJitterPaused, paused(.library))
            }
            Tab("Profile", systemImage: "person.crop.circle", value: AppTab.profile) {
                ProfileView(userModel: userModel, settings: settings)
                    .environment(\.stJitterPaused, paused(.profile))
            }
            Tab("Settings", systemImage: "gearshape", value: AppTab.settings) {
                SettingsView(settings: settings)
                    .environment(\.stJitterPaused, paused(.settings))
            }
        }
        // Content-heavy reading app: give the page back its vertical space
        // as soon as the reader starts scrolling.
        .tabBarMinimizeBehavior(.onScrollDown)
        .tint(Theme.Palette.storyBlue)
        .background(PageBackground())
        .onChange(of: selectedTab) { _, _ in
            UISelectionFeedbackGenerator().selectionChanged()
        }
        // First-run onboarding. A full-screen cover (not a sheet) so the
        // first impression has no grabber and can't be swiped away half-done.
        .fullScreenCover(isPresented: Binding(
            get: { !userModel.onboardingCompleted },
            set: { presented in if !presented { userModel.onboardingCompleted = true } }
        )) {
            OnboardingView(userModel: userModel, catalog: catalog) { story in
                guard let story else { return }
                // Let the onboarding cover finish dismissing before
                // presenting the story cover, or the second presentation
                // is silently dropped.
                DispatchQueue.main.asyncAfter(deadline: .now() + 0.6) {
                    onboardingStoryToStart = story
                }
            }
        }
        // The story chosen on the onboarding payoff screen.
        .fullScreenCover(item: $onboardingStoryToStart) { story in
            NavigationStack {
                StoryStartView(story: story, settings: settings)
            }
            .environmentObject(progressStore)
            .environmentObject(speechService)
            .environmentObject(favoritesStore)
            .environmentObject(statsStore)
            .environmentObject(notificationService)
            .environmentObject(catalog)
            .environmentObject(endingsTracker)
            .environmentObject(choiceDNA)
            .environmentObject(ambience)
            .environmentObject(personalStore)
        }
        .environmentObject(progressStore)
        .environmentObject(speechService)
        .environmentObject(favoritesStore)
        .environmentObject(statsStore)
        .environmentObject(notificationService)
        .environmentObject(catalog)
        .environmentObject(endingsTracker)
        .environmentObject(choiceDNA)
        .environmentObject(ambience)
        .environmentObject(personalStore)
        .preferredColorScheme(settings.isDarkMode ? .dark : .light)
        .task {
            await catalog.refresh()
            // After the catalog is fresh, re-pick "tonight's story" so the
            // notification body reflects the latest title pool.
            scheduleDailyStoryIfEnabled()
        }
        .onAppear {
            scheduleDailyStoryIfEnabled()
        }
        .onChange(of: catalog.stories.count) { _, _ in
            scheduleDailyStoryIfEnabled()
        }
        // Debug deep-link: `-deepLinkStoryID <id>` opens straight into the reader.
        .fullScreenCover(item: debugDeepLink) { story in
            NavigationStack {
                StoryReaderView(story: story, settings: settings)
                    .environmentObject(progressStore)
                    .environmentObject(speechService)
                    .environmentObject(favoritesStore)
                    .environmentObject(statsStore)
                    .environmentObject(notificationService)
                    .environmentObject(catalog)
                    .environmentObject(endingsTracker)
                    .environmentObject(choiceDNA)
                    .environmentObject(ambience)
                    .environmentObject(personalStore)
            }
        }
        .fullScreenCover(isPresented: debugShowPrivacy) {
            NavigationStack { PrivacyPolicyView() }
        }
        .fullScreenCover(isPresented: debugShowTerms) {
            NavigationStack { TermsOfServiceView() }
        }
    }
}

#Preview {
    ContentView()
}
