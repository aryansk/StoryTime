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
    @State private var showingSignUp = true
    @State private var selectedTab: Tab = ContentView.initialTab()

    private static func initialTab() -> Tab {
        #if DEBUG
        let args = ProcessInfo.processInfo.arguments
        if let idx = args.firstIndex(of: "-startTab"), idx + 1 < args.count {
            switch args[idx + 1] {
            case "shows": return .shows
            case "library": return .library
            case "profile": return .profile
            case "settings": return .settings
            default: break
            }
        }
        #endif
        return .shows
    }

    enum Tab: Hashable { case shows, library, profile, settings }

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

    var body: some View {
        ZStack(alignment: .bottom) {
            PageBackground()

            Group {
                switch selectedTab {
                case .shows:
                    CatalogShowsView(catalog: catalog, settings: settings)
                case .library:
                    LibraryView(catalog: catalog, settings: settings)
                case .profile:
                    ProfileView(userModel: userModel)
                case .settings:
                    SettingsView(settings: settings)
                }
            }
            .padding(.bottom, 84)   // leave room for the tab bar
            .frame(maxWidth: .infinity, maxHeight: .infinity)

            SketchTabBar(selected: $selectedTab)
        }
        .sheet(isPresented: .constant(userModel.isFirstLaunch)) {
            OnboardingView(userModel: userModel, isPresented: $showingSignUp)
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

// MARK: - Sketchy tab bar

struct SketchTabBar: View {
    @Binding var selected: ContentView.Tab

    var body: some View {
        HStack(spacing: 0) {
            tab(.shows, label: "Shows", doodle: .clapperboard)
            tab(.library, label: "Library", doodle: .books)
            tab(.profile, label: "Profile", doodle: .person)
            tab(.settings, label: "Settings", doodle: .gear)
        }
        .padding(.horizontal, 14)
        .padding(.vertical, 10)
        .background(
            WobblyRect(jitter: 0.5, corner: 14, seed: 9.0)
                .fill(Theme.Palette.butter)
        )
        .overlay(
            WobblyRect(jitter: 0.5, corner: 14, seed: 9.0)
                .stroke(Theme.Palette.ink, lineWidth: Theme.Stroke.bold)
        )
        .padding(.horizontal, 18)
        .padding(.bottom, 14)
    }

    private func tab(_ tab: ContentView.Tab, label: String, doodle: DoodleName) -> some View {
        let active = selected == tab
        return Button {
            withAnimation(.easeOut(duration: 0.15)) { selected = tab }
            UIImpactFeedbackGenerator(style: .light).impactOccurred()
        } label: {
            VStack(spacing: 4) {
                DoodleIcon(doodle, size: 22,
                           color: Theme.Palette.ink,
                           stroke: active ? Theme.Stroke.bold : Theme.Stroke.line)
                    .jitter(active, amplitude: 0.4)
                Text(label)
                    .font(Theme.Fonts.headingMedium(10))
                    .foregroundColor(Theme.Palette.ink)
                    .tracking(0.4)
            }
            .padding(.vertical, 4)
            .frame(maxWidth: .infinity)
            .background(
                Group {
                    if active {
                        WobblyRect(jitter: 0.3, corner: 8,
                                    seed: CGFloat(label.hashValue % 100))
                            .fill(Theme.Palette.butterDeep)
                    }
                }
            )
        }
        .buttonStyle(.plain)
    }
}

#Preview {
    ContentView()
}
