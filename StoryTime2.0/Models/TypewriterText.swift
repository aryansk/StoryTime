import SwiftUI
import AVFoundation

class TypewriterSoundManager {
    static let shared = TypewriterSoundManager()
    private var audioPlayer: AVAudioPlayer?
    
    init() {
        if let soundURL = Bundle.main.url(forResource: "typewriter", withExtension: "mp3") {
            do {
                audioPlayer = try AVAudioPlayer(contentsOf: soundURL)
                audioPlayer?.volume = 0.3
                audioPlayer?.prepareToPlay()
            } catch {
                print("Error loading typewriter sound: \(error)")
            }
        }
    }
    
    func playTypewriterSound() {
        audioPlayer?.currentTime = 0
        audioPlayer?.play()
    }
    
    func stopTypewriterSound() {
        audioPlayer?.stop()
    }
}

struct TypewriterText: View {
    let text: String
    @StateObject private var settings = SettingsModel()
    @State private var displayedText: String = ""
    @State private var isAnimating: Bool = false
    private let impactGenerator = UIImpactFeedbackGenerator(style: .light)
    
    var body: some View {
        Text(displayedText)
            .font(.system(size: settings.textSize))
            .lineSpacing(8)
            .onAppear {
                if !isAnimating {
                    isAnimating = true
                    impactGenerator.prepare()
                    animateText()
                }
            }
            .onDisappear {
                TypewriterSoundManager.shared.stopTypewriterSound()
            }
    }
    
    private func animateText() {
        var charIndex = 0
        Timer.scheduledTimer(withTimeInterval: settings.typingSpeed, repeats: true) { timer in
            if charIndex < text.count {
                let index = text.index(text.startIndex, offsetBy: charIndex)
                displayedText += String(text[index])
                charIndex += 1
                
                // Play sound and trigger haptic for each character
                if text[index] != " " {
                    TypewriterSoundManager.shared.playTypewriterSound()
                    impactGenerator.impactOccurred(intensity: 0.3)
                }
            } else {
                timer.invalidate()
                isAnimating = false
                TypewriterSoundManager.shared.stopTypewriterSound()
            }
        }
    }
} 