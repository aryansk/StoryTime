import SwiftUI

struct SettingsView: View {
    @ObservedObject var settings: SettingsModel
    @EnvironmentObject var notificationService: NotificationService
    @EnvironmentObject var catalog: CatalogService

    @State private var catalogURLDraft: String =
        UserDefaults.standard.string(forKey: "CatalogBaseURL") ?? ""
    @State private var refreshing: Bool = false

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
                                        .font(Theme.Fonts.body(settings.textSize))
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
        }
    }
}

