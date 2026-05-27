import SwiftUI

struct OnboardingView: View {
    @ObservedObject var userModel: UserModel
    @Binding var isPresented: Bool
    @State private var currentStep = 0
    @State private var name = ""
    @State private var selectedGoal = ""
    @State private var selectedExperience = ""

    let goals = ["Unwind", "Get Hooked", "Roleplay", "Bedtime"]
    let experiences = ["Casual", "Devoted", "Obsessed"]

    var body: some View {
        ZStack {
            PageBackground()

            VStack(spacing: 0) {
                if currentStep > 0 && currentStep < 5 {
                    progressBar
                        .padding(.horizontal, 28)
                        .padding(.top, 24)
                }

                Spacer()

                Group {
                    switch currentStep {
                    case 0: WelcomeStep(onContinue: advance, onSkip: complete)
                    case 1: NameStep(name: $name, onContinue: advance)
                    case 2: PickerStep(title: "What brings you here?",
                                       subtitle: "We'll pick stories that fit.",
                                       options: goals,
                                       selection: $selectedGoal,
                                       onContinue: advance)
                    case 3: PickerStep(title: "How deep do you watch?",
                                       subtitle: "Casual one-shot or franchise marathon?",
                                       options: experiences,
                                       selection: $selectedExperience,
                                       onContinue: advance)
                    case 4: OutcomeStep(goal: selectedGoal, onContinue: advance)
                    case 5: FinaleStep(onComplete: complete)
                    default: EmptyView()
                    }
                }
                .transition(.asymmetric(
                    insertion: .move(edge: .trailing).combined(with: .opacity),
                    removal:   .move(edge: .leading).combined(with: .opacity)
                ))

                Spacer()
            }
        }
    }

    private var progressBar: some View {
        VStack(spacing: 6) {
            HStack(spacing: 6) {
                ForEach(0..<4) { idx in
                    WobblyRect(jitter: 0.4, corner: 3, seed: CGFloat(idx))
                        .fill(idx < currentStep ? Theme.Palette.ink : Theme.Palette.inkHair)
                        .frame(height: 5)
                }
            }
            Text("Step \(min(4, currentStep)) of 4")
                .font(Theme.Fonts.meta())
                .foregroundColor(Theme.Palette.inkSoft)
        }
    }

    private func advance() {
        withAnimation(.easeOut(duration: 0.2)) { currentStep += 1 }
    }

    private func complete() {
        userModel.username = name.isEmpty ? "Storyteller" : name
        userModel.goal = selectedGoal
        userModel.experienceLevel = selectedExperience
        userModel.onboardingCompleted = true
        isPresented = false
    }
}

// MARK: - Steps

private struct WelcomeStep: View {
    let onContinue: () -> Void
    let onSkip: () -> Void

    var body: some View {
        VStack(spacing: 32) {
            VStack(spacing: 18) {
                DoodleIcon(.clapperboard, size: 96)
                    .jitter(amplitude: 0.4)
                Text("StoryTime")
                    .font(Theme.Fonts.display())
                    .foregroundColor(Theme.Palette.ink)
            }

            VStack(spacing: 12) {
                Text("Step inside the stories you love.")
                    .font(Theme.Fonts.title())
                    .foregroundColor(Theme.Palette.ink)
                    .multilineTextAlignment(.center)
                    .padding(.horizontal, 24)
                Text("Choose-your-own-adventure tales after the latest movies and shows. A fresh handful, every week.")
                    .font(Theme.Fonts.body(15))
                    .foregroundColor(Theme.Palette.inkSoft)
                    .multilineTextAlignment(.center)
                    .padding(.horizontal, 32)
                    .lineSpacing(4)
            }

            VStack(spacing: 12) {
                SketchButton(title: "Begin", trailingDoodle: .arrowRight, action: onContinue)
                Button(action: onSkip) {
                    Text("Skip the tour")
                        .font(Theme.Fonts.headingMedium(13))
                        .foregroundColor(Theme.Palette.inkSoft)
                }
            }
            .padding(.horizontal, 40)
        }
    }
}

private struct NameStep: View {
    @Binding var name: String
    let onContinue: () -> Void

    var body: some View {
        VStack(spacing: 28) {
            VStack(spacing: 10) {
                Text("What should we call you?")
                    .font(Theme.Fonts.title())
                    .foregroundColor(Theme.Palette.ink)
                    .multilineTextAlignment(.center)
                Text("So we can address the storyteller by name.")
                    .font(Theme.Fonts.body(14))
                    .foregroundColor(Theme.Palette.inkSoft)
            }
            SketchTextField(placeholder: "Your name", text: $name)
                .padding(.horizontal, 40)
            SketchButton(title: "Continue", trailingDoodle: .arrowRight, action: onContinue)
                .padding(.horizontal, 40)
                .opacity(name.isEmpty ? 0.5 : 1)
                .disabled(name.isEmpty)
        }
    }
}

private struct PickerStep: View {
    let title: String
    let subtitle: String
    let options: [String]
    @Binding var selection: String
    let onContinue: () -> Void

    var body: some View {
        VStack(spacing: 26) {
            VStack(spacing: 8) {
                Text(title)
                    .font(Theme.Fonts.title())
                    .foregroundColor(Theme.Palette.ink)
                    .multilineTextAlignment(.center)
                Text(subtitle)
                    .font(Theme.Fonts.body(14))
                    .foregroundColor(Theme.Palette.inkSoft)
            }
            VStack(spacing: 10) {
                ForEach(options, id: \.self) { opt in
                    Button {
                        selection = opt
                    } label: {
                        HStack {
                            Text(opt)
                                .font(Theme.Fonts.headingMedium(15))
                                .foregroundColor(Theme.Palette.ink)
                            Spacer()
                            if selection == opt {
                                DoodleIcon(.checkmark, size: 18)
                            }
                        }
                        .padding(.horizontal, 18)
                        .padding(.vertical, 14)
                        .background(
                            WobblyRect(jitter: 0.4, corner: 6, seed: CGFloat(opt.hashValue % 100))
                                .fill(selection == opt ? Theme.Palette.butterDeep : Color.clear)
                        )
                        .overlay(
                            WobblyRect(jitter: 0.4, corner: 6, seed: CGFloat(opt.hashValue % 100))
                                .stroke(Theme.Palette.ink,
                                        lineWidth: selection == opt ? Theme.Stroke.bold : Theme.Stroke.line)
                        )
                    }
                    .buttonStyle(.plain)
                }
            }
            .padding(.horizontal, 40)

            SketchButton(title: "Continue", trailingDoodle: .arrowRight, action: onContinue)
                .padding(.horizontal, 40)
                .opacity(selection.isEmpty ? 0.5 : 1)
                .disabled(selection.isEmpty)
        }
    }
}

private struct OutcomeStep: View {
    let goal: String
    let onContinue: () -> Void

    var body: some View {
        VStack(spacing: 28) {
            DoodleIcon(.sparkle, size: 90)
                .jitter(amplitude: 0.5)
            VStack(spacing: 12) {
                Text("Set. We'll tune the catalog for \"\(goal)\".")
                    .font(Theme.Fonts.title())
                    .foregroundColor(Theme.Palette.ink)
                    .multilineTextAlignment(.center)
                    .padding(.horizontal, 24)
                Text("New stories drop every week. You'll find them up top, marked NEW.")
                    .font(Theme.Fonts.body(14))
                    .foregroundColor(Theme.Palette.inkSoft)
                    .multilineTextAlignment(.center)
                    .padding(.horizontal, 32)
            }
            SketchButton(title: "Show me", trailingDoodle: .arrowRight, action: onContinue)
                .padding(.horizontal, 40)
        }
    }
}

private struct FinaleStep: View {
    let onComplete: () -> Void

    var body: some View {
        VStack(spacing: 28) {
            VStack(spacing: 12) {
                Text("Ready?")
                    .font(Theme.Fonts.display())
                    .foregroundColor(Theme.Palette.ink)
                Text("The first story is loaded. Pick a path and see where it lands.")
                    .font(Theme.Fonts.body(15))
                    .foregroundColor(Theme.Palette.inkSoft)
                    .multilineTextAlignment(.center)
                    .padding(.horizontal, 32)
            }
            SketchButton(title: "Enter the catalog", trailingDoodle: .arrowRight, action: onComplete)
                .padding(.horizontal, 40)
        }
    }
}
