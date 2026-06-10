import SwiftUI

// (helpers at bottom of file)
struct SettingsView: View {
    @ObservedObject var settings: SettingsModel
    @EnvironmentObject var notificationService: NotificationService
    @EnvironmentObject var catalog: CatalogService
    @EnvironmentObject var statsStore: StatsStore
    @EnvironmentObject var endingsTracker: EndingsTracker
    @EnvironmentObject var choiceDNA: ChoiceDNAStore
    @State private var showResetConfirm: ResetTarget? = nil

    enum ResetTarget: String, Identifiable {
        case stats, endings, dna
        var id: String { rawValue }
        var label: String {
            switch self {
            case .stats:   return "Reset Stats"
            case .endings: return "Reset Endings Discovered"
            case .dna:     return "Reset Choice DNA"
            }
        }
        var message: String {
            switch self {
            case .stats:   return "Clear streak, scenes read, and choices made."
            case .endings: return "Forget which endings you've reached. Stories stay; you'll see endings again as ?? Undiscovered."
            case .dna:     return "Erase your tracked traits. Choice DNA rebuilds as you play."
            }
        }
    }

    @State private var catalogURLDraft: String =
        UserDefaults.standard.string(forKey: "CatalogBaseURL") ?? ""
    @State private var refreshing: Bool = false

    /// (Re)installs the daily-story notification using the latest catalog +
    /// progress state. Safe to call repeatedly; tears down if disabled.
    func rescheduleDailyStory() {
        guard settings.dailyStoryEnabled else {
            notificationService.cancelDailyStory()
            return
        }
        Task {
            let granted = notificationService.authState == .authorized
                ? true
                : await notificationService.requestAuthorization()
            await MainActor.run {
                guard granted else {
                    settings.dailyStoryEnabled = false
                    return
                }
                notificationService.scheduleDailyStory(
                    hour: settings.reminderHour,
                    minute: settings.reminderMinute,
                    from: catalog.stories,
                    startedKeys: statsStore.storiesStarted
                )
            }
        }
    }

    private var reminderTime: Binding<Date> {
        Binding(
            get: {
                var c = DateComponents()
                c.hour = settings.reminderHour
                c.minute = settings.reminderMinute
                return Calendar.current.date(from: c) ?? Date()
            },
            set: { newValue in
                let comps = Calendar.current.dateComponents([.hour, .minute], from: newValue)
                settings.reminderHour = comps.hour ?? 19
                settings.reminderMinute = comps.minute ?? 0
                if settings.reminderEnabled {
                    notificationService.scheduleDailyReminder(
                        hour: settings.reminderHour, minute: settings.reminderMinute
                    )
                }
            }
        )
    }

    var body: some View {
        NavigationStack {
            ZStack {
                PageBackground()

                ScrollView(showsIndicators: false) {
                    VStack(alignment: .leading, spacing: 24) {
                        // Title
                        VStack(alignment: .leading, spacing: 6) {
                            Text("Your")
                                .font(Theme.Fonts.body(20))
                                .foregroundColor(Theme.Palette.inkSoft)
                            HStack(alignment: .bottom, spacing: 8) {
                                Text("Settings")
                                    .font(Theme.Fonts.display())
                                    .foregroundColor(Theme.Palette.ink)
                                DoodleIcon(.gear, size: 36)
                                    .jitter(amplitude: 0.4)
                                Spacer()
                            }
                        }
                        .padding(.horizontal, 24)
                        .padding(.top, 16)

                        // Reading
                        VStack(alignment: .leading, spacing: 14) {
                            SketchSectionHeader("Reading")
                            SketchCard(seed: 11.5) {
                                VStack(alignment: .leading, spacing: 14) {
                                    Text("Text Size")
                                        .font(Theme.Fonts.label())
                                        .foregroundColor(Theme.Palette.inkSoft)
                                    HStack {
                                        Text("A").font(Theme.Fonts.body(settings.minTextSize))
                                            .foregroundColor(Theme.Palette.ink)
                                        Slider(value: $settings.textSize,
                                               in: settings.minTextSize...settings.maxTextSize,
                                               step: 1)
                                            .tint(Theme.Palette.ink)
                                        Text("A").font(Theme.Fonts.body(settings.maxTextSize))
                                            .foregroundColor(Theme.Palette.ink)
                                    }
                                    SketchDivider()
                                    Text("Preview")
                                        .font(Theme.Fonts.label())
                                        .foregroundColor(Theme.Palette.inkSoft)
                                    Text("The doors close. The procedure begins.")
                                        .font(settings.readerFont(settings.textSize))
                                        .foregroundColor(Theme.Palette.ink)

                                    SketchDivider()

                                    Toggle(isOn: $settings.typewriterEnabled) {
                                        HStack(spacing: 10) {
                                            DoodleIcon(.sparkle, size: 18)
                                            Text("Typewriter effect")
                                                .font(Theme.Fonts.body(15))
                                                .foregroundColor(Theme.Palette.ink)
                                        }
                                    }
                                    .tint(Theme.Palette.ink)

                                    if settings.typewriterEnabled {
                                        Text("Typing Speed")
                                            .font(Theme.Fonts.label())
                                            .foregroundColor(Theme.Palette.inkSoft)
                                        HStack {
                                            Text("Slow").font(Theme.Fonts.body(12))
                                                .foregroundColor(Theme.Palette.inkSoft)
                                            // Higher slider value = faster, so invert the stored interval.
                                            Slider(value: Binding(
                                                get: { settings.maxTypingSpeed + settings.minTypingSpeed - settings.typingSpeed },
                                                set: { settings.typingSpeed = settings.maxTypingSpeed + settings.minTypingSpeed - $0 }
                                            ), in: settings.minTypingSpeed...settings.maxTypingSpeed)
                                                .tint(Theme.Palette.ink)
                                            Text("Fast").font(Theme.Fonts.body(12))
                                                .foregroundColor(Theme.Palette.inkSoft)
                                        }
                                    }
                                }
                            }
                        }
                        .padding(.horizontal, 24)

                        // Appearance
                        VStack(alignment: .leading, spacing: 14) {
                            SketchSectionHeader("Appearance")
                            SketchCard(seed: 11.9) {
                                VStack(alignment: .leading, spacing: 16) {
                                    // Dark mode
                                    Toggle(isOn: $settings.isDarkMode) {
                                        HStack(spacing: 10) {
                                            DoodleIcon(.sparkle, size: 18)
                                            Text("Dark mode")
                                                .font(Theme.Fonts.body(15))
                                                .foregroundColor(Theme.Palette.ink)
                                        }
                                    }
                                    .tint(Theme.Palette.ink)

                                    SketchDivider()

                                    // Paper tint (light mode)
                                    Text("Paper")
                                        .font(Theme.Fonts.label())
                                        .foregroundColor(Theme.Palette.inkSoft)
                                    HStack(spacing: 10) {
                                        SketchPill(title: "Yellow",
                                                   selected: settings.selectedTheme == 0) {
                                            settings.selectedTheme = 0
                                        }
                                        SketchPill(title: "Grey",
                                                   selected: settings.selectedTheme == 1) {
                                            settings.selectedTheme = 1
                                        }
                                        SketchPill(title: "Custom",
                                                   selected: settings.selectedTheme == 2) {
                                            settings.selectedTheme = 2
                                        }
                                    }
                                    if settings.selectedTheme == 2 {
                                        ColorPicker(selection: Binding(
                                            get: { Color(hex: settings.customThemeColor) },
                                            set: { settings.customThemeColor = $0.toHex() }
                                        ), supportsOpacity: false) {
                                            Text("Custom paper color")
                                                .font(Theme.Fonts.body(14))
                                                .foregroundColor(Theme.Palette.ink)
                                        }
                                    }
                                    if settings.isDarkMode {
                                        Text("Paper tint applies in light mode.")
                                            .font(Theme.Fonts.bodyItalic(12))
                                            .foregroundColor(Theme.Palette.inkSoft)
                                    }

                                    SketchDivider()

                                    // Reading font
                                    Text("Reading Font")
                                        .font(Theme.Fonts.label())
                                        .foregroundColor(Theme.Palette.inkSoft)
                                    ScrollView(.horizontal, showsIndicators: false) {
                                        HStack(spacing: 10) {
                                            ForEach(settings.availableFonts, id: \.self) { font in
                                                SketchPill(title: font,
                                                           selected: settings.selectedFontName == font) {
                                                    settings.selectedFontName = font
                                                }
                                            }
                                        }
                                    }
                                    Text("The quick brown fox jumps over the lazy dog.")
                                        .font(settings.readerFont(16))
                                        .foregroundColor(Theme.Palette.ink)
                                }
                            }
                        }
                        .padding(.horizontal, 24)

                        // Narration
                        VStack(alignment: .leading, spacing: 14) {
                            SketchSectionHeader("Narration")
                            SketchCard(seed: 12.5) {
                                VStack(alignment: .leading, spacing: 12) {
                                    Text("Speech Rate")
                                        .font(Theme.Fonts.label())
                                        .foregroundColor(Theme.Palette.inkSoft)
                                    HStack {
                                        DoodleIcon(.speaker, size: 18)
                                        Slider(value: $settings.narrationRate,
                                               in: 0...1, step: 0.05)
                                            .tint(Theme.Palette.ink)
                                        DoodleIcon(.speakerPlaying, size: 18)
                                    }
                                }
                            }
                        }
                        .padding(.horizontal, 24)

                        // Reminders
                        VStack(alignment: .leading, spacing: 14) {
                            SketchSectionHeader("Reminders")
                            SketchCard(seed: 13.5) {
                                VStack(alignment: .leading, spacing: 12) {
                                    Toggle(isOn: Binding(
                                        get: { settings.reminderEnabled },
                                        set: { v in
                                            settings.reminderEnabled = v
                                            if v {
                                                Task {
                                                    let granted = await notificationService.requestAuthorization()
                                                    if granted {
                                                        notificationService.scheduleDailyReminder(
                                                            hour: settings.reminderHour,
                                                            minute: settings.reminderMinute
                                                        )
                                                    } else {
                                                        settings.reminderEnabled = false
                                                    }
                                                }
                                            } else {
                                                notificationService.cancelReminder()
                                            }
                                        }
                                    )) {
                                        HStack(spacing: 10) {
                                            DoodleIcon(.bell, size: 20)
                                            Text("Daily reminder")
                                                .font(Theme.Fonts.body(15))
                                                .foregroundColor(Theme.Palette.ink)
                                        }
                                    }
                                    .tint(Theme.Palette.ink)

                                    if settings.reminderEnabled {
                                        DatePicker("Time", selection: reminderTime,
                                                   displayedComponents: .hourAndMinute)
                                            .font(Theme.Fonts.body(15))
                                            .foregroundColor(Theme.Palette.ink)
                                    }

                                    if notificationService.authState == .denied {
                                        Text("Notifications are off in iOS Settings. Turn them on to receive reminders.")
                                            .font(Theme.Fonts.bodyItalic(13))
                                            .foregroundColor(Theme.Palette.inkSoft)
                                    }

                                    SketchDivider()

                                    Toggle(isOn: Binding(
                                        get: { settings.dailyStoryEnabled },
                                        set: { v in
                                            settings.dailyStoryEnabled = v
                                            rescheduleDailyStory()
                                        }
                                    )) {
                                        HStack(spacing: 10) {
                                            DoodleIcon(.sparkle, size: 20)
                                            VStack(alignment: .leading, spacing: 2) {
                                                Text("Tonight's story")
                                                    .font(Theme.Fonts.body(15))
                                                    .foregroundColor(Theme.Palette.ink)
                                                Text("Picks one you haven't started yet")
                                                    .font(Theme.Fonts.bodyItalic(12))
                                                    .foregroundColor(Theme.Palette.inkSoft)
                                            }
                                        }
                                    }
                                    .tint(Theme.Palette.ink)
                                }
                            }
                        }
                        .padding(.horizontal, 24)

                        // Companion mode
                        VStack(alignment: .leading, spacing: 14) {
                            SketchSectionHeader("Companion Mode")
                            SketchCard(seed: 14.3) {
                                VStack(alignment: .leading, spacing: 12) {
                                    Toggle(isOn: $settings.companionEnabled) {
                                        HStack(spacing: 10) {
                                            DoodleIcon(.person, size: 20)
                                            VStack(alignment: .leading, spacing: 2) {
                                                Text("Pass and play")
                                                    .font(Theme.Fonts.body(15))
                                                    .foregroundColor(Theme.Palette.ink)
                                                Text("Two readers, one device — take turns choosing")
                                                    .font(Theme.Fonts.bodyItalic(12))
                                                    .foregroundColor(Theme.Palette.inkSoft)
                                            }
                                        }
                                    }
                                    .tint(Theme.Palette.ink)

                                    if settings.companionEnabled {
                                        Text("Player names")
                                            .font(Theme.Fonts.label())
                                            .foregroundColor(Theme.Palette.inkSoft)
                                        SketchTextField(placeholder: "Player 1",
                                                        text: $settings.companionPlayerA)
                                        SketchTextField(placeholder: "Player 2",
                                                        text: $settings.companionPlayerB)
                                    }
                                }
                            }
                        }
                        .padding(.horizontal, 24)

                        // Ambience
                        VStack(alignment: .leading, spacing: 14) {
                            SketchSectionHeader("Ambience")
                            SketchCard(seed: 14.7) {
                                VStack(alignment: .leading, spacing: 12) {
                                    Toggle(isOn: $settings.ambienceEnabled) {
                                        HStack(spacing: 10) {
                                            DoodleIcon(.speaker, size: 20)
                                            VStack(alignment: .leading, spacing: 2) {
                                                Text("Background ambience")
                                                    .font(Theme.Fonts.body(15))
                                                    .foregroundColor(Theme.Palette.ink)
                                                Text("Loops a soft genre track while reading")
                                                    .font(Theme.Fonts.bodyItalic(12))
                                                    .foregroundColor(Theme.Palette.inkSoft)
                                            }
                                        }
                                    }
                                    .tint(Theme.Palette.ink)
                                }
                            }
                        }
                        .padding(.horizontal, 24)

                        // Catalog source
                        VStack(alignment: .leading, spacing: 14) {
                            SketchSectionHeader("Catalog Source")
                            SketchCard(seed: 13.9) {
                                VStack(alignment: .leading, spacing: 12) {
                                    Text("Remote catalog URL")
                                        .font(Theme.Fonts.label())
                                        .foregroundColor(Theme.Palette.inkSoft)
                                    SketchTextField(placeholder: "https://you.github.io/storytime/",
                                                    text: $catalogURLDraft)
                                    HStack(spacing: 10) {
                                        SketchButton(title: refreshing ? "Refreshing…" : "Save & Refresh",
                                                     doodle: .arrowRight,
                                                     style: .primary,
                                                     fullWidth: false) {
                                            catalog.setRemoteBaseURL(catalogURLDraft.trimmingCharacters(in: .whitespacesAndNewlines))
                                            Task {
                                                refreshing = true
                                                await catalog.refresh()
                                                refreshing = false
                                            }
                                        }
                                        SketchButton(title: "Clear", style: .ghost, fullWidth: false) {
                                            catalogURLDraft = ""
                                            UserDefaults.standard.removeObject(forKey: "CatalogBaseURL")
                                        }
                                    }
                                    if let updated = catalog.lastUpdated {
                                        Text("Last update: \(updated.formatted(date: .abbreviated, time: .shortened))")
                                            .font(Theme.Fonts.bodyItalic(12))
                                            .foregroundColor(Theme.Palette.inkSoft)
                                    }
                                    if let err = catalog.lastError {
                                        Text(err)
                                            .font(Theme.Fonts.bodyItalic(12))
                                            .foregroundColor(Theme.Palette.ink.opacity(0.7))
                                    }
                                }
                            }
                        }
                        .padding(.horizontal, 24)

                        // Data
                        VStack(alignment: .leading, spacing: 14) {
                            SketchSectionHeader("Data")
                            SketchCard(seed: 14.85) {
                                VStack(alignment: .leading, spacing: 12) {
                                    SketchButton(title: "Reset Stats",
                                                 doodle: .undo,
                                                 style: .secondary) {
                                        showResetConfirm = .stats
                                    }
                                    SketchButton(title: "Reset Endings Discovered",
                                                 doodle: .undo,
                                                 style: .secondary) {
                                        showResetConfirm = .endings
                                    }
                                    SketchButton(title: "Reset Choice DNA",
                                                 doodle: .undo,
                                                 style: .secondary) {
                                        showResetConfirm = .dna
                                    }
                                    Text("These are local-only. Your stories and favorites stay.")
                                        .font(Theme.Fonts.bodyItalic(12))
                                        .foregroundColor(Theme.Palette.inkSoft)
                                }
                            }
                        }
                        .padding(.horizontal, 24)

                        // About
                        VStack(alignment: .leading, spacing: 14) {
                            SketchSectionHeader("About")
                            SketchCard(seed: 14.5) {
                                VStack(alignment: .leading, spacing: 6) {
                                    HStack(spacing: 8) {
                                        DoodleIcon(.sparkle, size: 18)
                                        Text("StoryTime")
                                            .font(Theme.Fonts.cardTitle())
                                            .foregroundColor(Theme.Palette.ink)
                                    }
                                    Text("Choose-your-own-adventure stories after the latest movies and shows. Hand-authored, refreshed weekly.")
                                        .font(Theme.Fonts.bodyItalic(13))
                                        .foregroundColor(Theme.Palette.inkSoft)
                                        .lineSpacing(3)
                                }
                            }
                        }
                        .padding(.horizontal, 24)

                        Spacer(minLength: 40)
                    }
                }
                .onAppear { notificationService.refreshAuthState() }
            }
            .navigationBarHidden(true)
            .confirmationDialog(
                showResetConfirm?.label ?? "",
                isPresented: Binding(
                    get: { showResetConfirm != nil },
                    set: { if !$0 { showResetConfirm = nil } }
                ),
                titleVisibility: .visible,
                presenting: showResetConfirm
            ) { target in
                Button("Reset", role: .destructive) {
                    switch target {
                    case .stats:   statsStore.reset()
                    case .endings: endingsTracker.reset()
                    case .dna:     choiceDNA.reset()
                    }
                    showResetConfirm = nil
                }
                Button("Cancel", role: .cancel) { showResetConfirm = nil }
            } message: { target in
                Text(target.message)
            }
        }
    }
}

