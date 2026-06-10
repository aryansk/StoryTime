import AVFoundation
import Foundation

// MARK: - Ambience
//
// Optional looping background audio per genre. The service looks up a
// short, royalty-free audio file in the bundle by genre. If the file
// isn't present (it isn't, by default — the user can drop in their own),
// the service stays silent and the UI toggle still works.
//
// File names expected, if present:
//   ambience-drama.m4a / ambience-thriller.m4a / ambience-scifi.m4a /
//   ambience-fantasy.m4a / ambience-horror.m4a / ambience-comedy.m4a /
//   ambience-action.m4a

@MainActor
final class AmbienceService: ObservableObject {
    @Published private(set) var isPlaying: Bool = false
    @Published private(set) var currentGenre: StoryGenre? = nil

    private var player: AVAudioPlayer?

    /// Returns true if a bundled audio file exists for the genre.
    func hasTrack(for genre: StoryGenre) -> Bool {
        Bundle.main.url(forResource: assetName(for: genre), withExtension: "m4a") != nil
    }

    /// Begin (or switch to) the ambience track for the given genre.
    /// If no asset is bundled, this is a no-op but the UI can still treat
    /// the call as "armed" — the next launch with an asset will play.
    func play(genre: StoryGenre, volume: Float = 0.25) {
        currentGenre = genre
        guard let url = Bundle.main.url(forResource: assetName(for: genre), withExtension: "m4a") else {
            // No bundled asset — silent success.
            isPlaying = false
            return
        }
        do {
            try AVAudioSession.sharedInstance().setCategory(.ambient, mode: .default, options: [.mixWithOthers])
            try AVAudioSession.sharedInstance().setActive(true)
            player?.stop()
            let p = try AVAudioPlayer(contentsOf: url)
            p.numberOfLoops = -1
            p.volume = volume
            p.prepareToPlay()
            p.play()
            player = p
            isPlaying = true
        } catch {
            isPlaying = false
        }
    }

    func stop() {
        player?.stop()
        player = nil
        isPlaying = false
    }

    func setVolume(_ v: Float) {
        player?.volume = max(0, min(1, v))
    }

    private func assetName(for genre: StoryGenre) -> String {
        switch genre {
        case .drama:    return "ambience-drama"
        case .thriller: return "ambience-thriller"
        case .sciFi:    return "ambience-scifi"
        case .fantasy:  return "ambience-fantasy"
        case .horror:   return "ambience-horror"
        case .comedy:   return "ambience-comedy"
        case .action:   return "ambience-action"
        case .all:      return "ambience-drama"
        }
    }
}
