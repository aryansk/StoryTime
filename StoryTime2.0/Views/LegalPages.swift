import SwiftUI

// MARK: - Legal document scaffold
//
// Three pages share a single layout: a sketchy doc page with a hand-drawn
// header doodle, a title, an effective date, and a body of sections.

private struct LegalSection {
    let title: String
    let body: String
}

private struct LegalPage: View {
    let headerDoodle: DoodleName
    let title: String
    let lede: String
    let effectiveDate: String
    let sections: [LegalSection]
    @Environment(\.dismiss) private var dismiss

    var body: some View {
        ZStack {
            PageBackground()

            ScrollView(showsIndicators: false) {
                VStack(alignment: .leading, spacing: 24) {
                    // Top bar
                    HStack {
                        DoodleButton(doodle: .chevronLeft, label: "Back") { dismiss() }
                        Spacer()
                    }
                    .padding(.horizontal, 12)
                    .padding(.top, 8)

                    // Header card
                    SketchCard(fill: Theme.Palette.mist, seed: 41) {
                        VStack(alignment: .leading, spacing: 14) {
                            HStack(alignment: .top, spacing: 12) {
                                DoodleIcon(headerDoodle, size: 44)
                                    .jitter(amplitude: 0.4)
                                VStack(alignment: .leading, spacing: 4) {
                                    Text(title)
                                        .font(Theme.Fonts.title())
                                        .foregroundColor(Theme.Palette.ink)
                                    Text("Effective \(effectiveDate)")
                                        .font(Theme.Fonts.bodyItalic(13))
                                        .foregroundColor(Theme.Palette.inkSoft)
                                }
                                Spacer()
                            }
                            Text(lede)
                                .font(Theme.Fonts.body(15))
                                .foregroundColor(Theme.Palette.ink)
                                .lineSpacing(4)
                        }
                    }
                    .padding(.horizontal, 24)

                    // Sections
                    VStack(alignment: .leading, spacing: 22) {
                        ForEach(Array(sections.enumerated()), id: \.offset) { idx, sec in
                            VStack(alignment: .leading, spacing: 10) {
                                HStack(spacing: 8) {
                                    SketchBadge(text: String(format: "§ %02d", idx + 1))
                                    Text(sec.title)
                                        .font(Theme.Fonts.cardTitle())
                                        .foregroundColor(Theme.Palette.ink)
                                }
                                Text(sec.body)
                                    .font(Theme.Fonts.body(15))
                                    .foregroundColor(Theme.Palette.ink)
                                    .lineSpacing(5)
                            }
                        }
                    }
                    .padding(.horizontal, 24)

                    // Footer
                    HStack(spacing: 8) {
                        DoodleIcon(.link, size: 16, color: Theme.Palette.inkSoft)
                        Text("Questions? hello@storytime.app")
                            .font(Theme.Fonts.bodyItalic(13))
                            .foregroundColor(Theme.Palette.inkSoft)
                        Spacer()
                    }
                    .padding(.horizontal, 24)
                    .padding(.top, 8)

                    Spacer(minLength: 60)
                }
            }
        }
        .navigationBarBackButtonHidden(true)
    }
}

// MARK: - Privacy Policy

struct PrivacyPolicyView: View {
    var body: some View {
        LegalPage(
            headerDoodle: .shield,
            title: "Privacy Policy",
            lede: "Short version: we collect almost nothing. No accounts, no analytics SDKs, no tracking pixels. Below is the slightly longer version, for the record.",
            effectiveDate: "May 27, 2026",
            sections: [
                LegalSection(
                    title: "What we collect",
                    body: "StoryTime stores your reading progress, favorites, and your chosen display name locally on your device using iOS UserDefaults. None of this leaves your phone. We do not run server-side analytics, we do not attach unique IDs to your activity, and we do not sell or share any of it because we do not have any of it to share."
                ),
                LegalSection(
                    title: "Network requests",
                    body: "The app fetches a public catalog of stories from a content host (for example, a static URL on GitHub Pages). That request is a plain GET for JSON files. It sends only the information any HTTP client sends: your IP address and a generic user-agent string. We do not log these requests on our side."
                ),
                LegalSection(
                    title: "Notifications",
                    body: "If you turn on the daily reading reminder, iOS schedules a local notification on your device. The reminder is generated locally; no push token is sent anywhere."
                ),
                LegalSection(
                    title: "Sharing",
                    body: "When you tap \"Share This Ending\", iOS opens the system share sheet. Anything you send from there (text messages, AirDrop, social posts) is handled entirely by iOS and the destination app. We never see what you share or who you share it with."
                ),
                LegalSection(
                    title: "Children",
                    body: "StoryTime is intended for general audiences. Some stories deal with adult themes. We do not knowingly collect any information from children under 13, and because we do not collect personal information from anyone, this is something we are confident about."
                ),
                LegalSection(
                    title: "Changes",
                    body: "If this policy ever changes, we'll update the effective date at the top and ship the new version with an app update. We won't quietly mutate the rules under your feet."
                ),
                LegalSection(
                    title: "Contact",
                    body: "Email hello@storytime.app with questions, gripes, or compliments. A real human reads them."
                )
            ]
        )
    }
}

// MARK: - Terms of Service

struct TermsOfServiceView: View {
    var body: some View {
        LegalPage(
            headerDoodle: .scroll,
            title: "Terms of Service",
            lede: "By using StoryTime you're agreeing to the terms below. They're written in plain English on purpose.",
            effectiveDate: "May 27, 2026",
            sections: [
                LegalSection(
                    title: "Your license",
                    body: "We grant you a personal, non-exclusive, non-transferable license to use StoryTime on devices you own. You may not resell the app, republish the story content as your own work, or attempt to extract the catalog for redistribution."
                ),
                LegalSection(
                    title: "The stories",
                    body: "Each interactive story is an original work inspired by movies and television we admire. The original films and shows referenced as source material remain the property of their respective rights holders; StoryTime is not affiliated with, endorsed by, or sponsored by any of them. The interactive scripts themselves are ours."
                ),
                LegalSection(
                    title: "Acceptable use",
                    body: "Be a person about it. Don't try to reverse-engineer the app, don't use it to harass anyone, don't attempt to bypass any safety or rate-limiting mechanisms we add over time."
                ),
                LegalSection(
                    title: "No warranty",
                    body: "StoryTime is provided \"as is\". We do our best, but we can't guarantee the app will be bug-free, available at all times, or that your phone won't make a typewriter noise at a quiet moment if you forgot it was unmuted."
                ),
                LegalSection(
                    title: "Limitation of liability",
                    body: "To the maximum extent allowed by law, we are not liable for any indirect, incidental, or consequential damages arising from your use of the app. Our total liability is capped at the amount you paid for the app (which is, currently, nothing)."
                ),
                LegalSection(
                    title: "Termination",
                    body: "You can stop using StoryTime at any time by deleting the app. We can suspend or end the service for anyone we reasonably believe is abusing it. Neither party has to give the other notice for ordinary departures."
                ),
                LegalSection(
                    title: "Governing law",
                    body: "These terms are governed by the laws of the jurisdiction in which StoryTime is published. Disputes that can't be resolved by emailing us are resolved in that jurisdiction's courts."
                ),
                LegalSection(
                    title: "Changes",
                    body: "If we update these terms in a way that materially changes your rights, we'll surface the change inside the app before the new version takes effect."
                )
            ]
        )
    }
}

// MARK: - Acknowledgements

struct AcknowledgementsView: View {
    var body: some View {
        LegalPage(
            headerDoodle: .sparkle,
            title: "Acknowledgements",
            lede: "StoryTime stands on the shoulders of many small, good things. Here are the ones whose licenses ask us to say so out loud, plus a few who don't.",
            effectiveDate: "May 27, 2026",
            sections: [
                LegalSection(
                    title: "Space Grotesk",
                    body: "Headline typeface by Florian Karsten. Licensed under the SIL Open Font License 1.1."
                ),
                LegalSection(
                    title: "Source Serif 4",
                    body: "Body typeface by Frank Grießhammer and Adobe. Licensed under the SIL Open Font License 1.1."
                ),
                LegalSection(
                    title: "Apple platforms",
                    body: "Built with Swift, SwiftUI, and AVFoundation. iOS handles the heavy lifting."
                ),
                LegalSection(
                    title: "The shows and films",
                    body: "Each story is an interactive love letter to the work that inspired it. The brilliance is theirs; any flaws in our interactive versions are ours."
                )
            ]
        )
    }
}
