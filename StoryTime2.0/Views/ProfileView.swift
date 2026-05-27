import SwiftUI

// MARK: - Profile tab
//
// User identity + stats + legal pages. Stats live here rather than in
// Settings because they belong to the storyteller, not to app configuration.

struct ProfileView: View {
    @ObservedObject var userModel: UserModel
    @EnvironmentObject var statsStore: StatsStore
    @EnvironmentObject var progressStore: ReadingProgressStore
    @EnvironmentObject var favoritesStore: FavoritesStore

    @State private var editingName: Bool = false
    @State private var nameDraft: String = ""

    var appVersion: String {
        let v = Bundle.main.infoDictionary?["CFBundleShortVersionString"] as? String ?? "1.0"
        let b = Bundle.main.infoDictionary?["CFBundleVersion"] as? String ?? "1"
        return "v\(v) (\(b))"
    }

    var body: some View {
        NavigationStack {
            ZStack {
                PageBackground()

                ScrollView(showsIndicators: false) {
                    VStack(alignment: .leading, spacing: 26) {
                        // Title
                        VStack(alignment: .leading, spacing: 6) {
                            Text("Your")
                                .font(Theme.Fonts.body(20))
                                .foregroundColor(Theme.Palette.inkSoft)
                            HStack(alignment: .bottom, spacing: 8) {
                                Text("Profile")
                                    .font(Theme.Fonts.display())
                                    .foregroundColor(Theme.Palette.ink)
                                DoodleIcon(.person, size: 36)
                                    .jitter(amplitude: 0.4)
                                Spacer()
                            }
                        }
                        .padding(.horizontal, 24)
                        .padding(.top, 16)

                        identityCard
                            .padding(.horizontal, 24)

                        statsBlock
                            .padding(.horizontal, 24)

                        legalBlock
                            .padding(.horizontal, 24)

                        aboutBlock
                            .padding(.horizontal, 24)

                        Spacer(minLength: 40)
                    }
                }
            }
            .navigationBarHidden(true)
        }
    }

    // MARK: Identity

    private var identityCard: some View {
        SketchCard(fill: Theme.Palette.mist, seed: 21.0) {
            HStack(alignment: .center, spacing: 16) {
                ZStack {
                    WobblyRect(jitter: 0.5, corner: 36, seed: 77)
                        .fill(Theme.Palette.butter)
                        .frame(width: 72, height: 72)
                    WobblyRect(jitter: 0.5, corner: 36, seed: 77)
                        .stroke(Theme.Palette.ink, lineWidth: Theme.Stroke.bold)
                        .frame(width: 72, height: 72)
                    DoodleIcon(.person, size: 42)
                        .jitter(amplitude: 0.3)
                }

                VStack(alignment: .leading, spacing: 6) {
                    if editingName {
                        SketchTextField(placeholder: "Your name", text: $nameDraft)
                        HStack(spacing: 8) {
                            SketchButton(title: "Save", style: .primary, fullWidth: false) {
                                let trimmed = nameDraft.trimmingCharacters(in: .whitespaces)
                                if !trimmed.isEmpty { userModel.username = trimmed }
                                editingName = false
                            }
                            SketchButton(title: "Cancel", style: .ghost, fullWidth: false) {
                                editingName = false
                            }
                        }
                    } else {
                        Text(userModel.username.isEmpty ? "Storyteller" : userModel.username)
                            .font(Theme.Fonts.cardTitle())
                            .foregroundColor(Theme.Palette.ink)
                        Text(userModel.greeting)
                            .font(Theme.Fonts.bodyItalic(13))
                            .foregroundColor(Theme.Palette.inkSoft)
                        Button {
                            nameDraft = userModel.username
                            editingName = true
                        } label: {
                            HStack(spacing: 4) {
                                Text("Edit name")
                                    .font(Theme.Fonts.headingMedium(12))
                                DoodleIcon(.chevronRightSmall, size: 12, color: Theme.Palette.ink)
                            }
                            .foregroundColor(Theme.Palette.ink)
                            .padding(.top, 2)
                        }
                        .buttonStyle(.plain)
                    }
                }
                Spacer()
            }
        }
    }

    // MARK: Stats

    private var statsBlock: some View {
        VStack(alignment: .leading, spacing: 14) {
            SketchSectionHeader("Your Stats")
            HStack(spacing: 12) {
                ProfileStatTile(doodle: .flame,
                                value: "\(statsStore.currentStreak)",
                                label: "Day streak")
                ProfileStatTile(doodle: .books,
                                value: "\(statsStore.storiesStarted.count)",
                                label: "Stories")
            }
            HStack(spacing: 12) {
                ProfileStatTile(doodle: .stack,
                                value: "\(statsStore.scenesRead)",
                                label: "Scenes read")
                ProfileStatTile(doodle: .branch,
                                value: "\(statsStore.choicesMade)",
                                label: "Choices made")
            }
            HStack(spacing: 12) {
                ProfileStatTile(doodle: .bookmarkFill,
                                value: "\(progressStore.inProgress.count)",
                                label: "In progress")
                ProfileStatTile(doodle: .heartFill,
                                value: "\(favoritesStore.favoriteTitles.count)",
                                label: "Favorites")
            }
        }
    }

    // MARK: Legal

    private var legalBlock: some View {
        VStack(alignment: .leading, spacing: 14) {
            SketchSectionHeader("Legal")
            SketchCard(padding: 4, seed: 22.0) {
                VStack(spacing: 0) {
                    NavigationLink(destination: PrivacyPolicyView()) {
                        ProfileRow(doodle: .shield, title: "Privacy Policy",
                                   subtitle: "What we collect, what we don't")
                    }
                    SketchDivider()
                        .padding(.horizontal, 14)
                    NavigationLink(destination: TermsOfServiceView()) {
                        ProfileRow(doodle: .scroll, title: "Terms of Service",
                                   subtitle: "The deal between you and us")
                    }
                    SketchDivider()
                        .padding(.horizontal, 14)
                    NavigationLink(destination: AcknowledgementsView()) {
                        ProfileRow(doodle: .sparkle, title: "Acknowledgements",
                                   subtitle: "Fonts, tools, thanks")
                    }
                }
            }
        }
    }

    // MARK: About

    private var aboutBlock: some View {
        VStack(alignment: .leading, spacing: 14) {
            SketchSectionHeader("About")
            SketchCard(seed: 23.0) {
                VStack(alignment: .leading, spacing: 6) {
                    HStack(spacing: 8) {
                        DoodleIcon(.sparkle, size: 18)
                        Text("StoryTime")
                            .font(Theme.Fonts.cardTitle())
                            .foregroundColor(Theme.Palette.ink)
                        Spacer()
                        Text(appVersion)
                            .font(Theme.Fonts.bodyItalic(12))
                            .foregroundColor(Theme.Palette.inkSoft)
                    }
                    Text("Choose-your-own-adventure stories after the latest movies and shows. Hand-authored, refreshed weekly.")
                        .font(Theme.Fonts.bodyItalic(13))
                        .foregroundColor(Theme.Palette.inkSoft)
                        .lineSpacing(3)
                }
            }
        }
    }
}

// MARK: - Stat tile

private struct ProfileStatTile: View {
    let doodle: DoodleName
    let value: String
    let label: String

    var body: some View {
        SketchCard(fill: Theme.Palette.mist, padding: 14, seed: CGFloat(label.hashValue % 100)) {
            VStack(alignment: .leading, spacing: 8) {
                DoodleIcon(doodle, size: 22)
                Text(value)
                    .font(Theme.Fonts.heading(24))
                    .foregroundColor(Theme.Palette.ink)
                Text(label)
                    .font(Theme.Fonts.body(12))
                    .foregroundColor(Theme.Palette.inkSoft)
            }
            .frame(maxWidth: .infinity, alignment: .leading)
        }
    }
}

// MARK: - Row used by Legal block

private struct ProfileRow: View {
    let doodle: DoodleName
    let title: String
    let subtitle: String

    var body: some View {
        HStack(spacing: 14) {
            DoodleIcon(doodle, size: 22)
                .frame(width: 28)
            VStack(alignment: .leading, spacing: 2) {
                Text(title)
                    .font(Theme.Fonts.headingMedium(15))
                    .foregroundColor(Theme.Palette.ink)
                Text(subtitle)
                    .font(Theme.Fonts.bodyItalic(12))
                    .foregroundColor(Theme.Palette.inkSoft)
            }
            Spacer()
            DoodleIcon(.chevronRightSmall, size: 14, color: Theme.Palette.inkSoft)
        }
        .padding(.horizontal, 14)
        .padding(.vertical, 14)
        .contentShape(Rectangle())
    }
}
