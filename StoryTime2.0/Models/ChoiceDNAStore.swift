import Foundation

// MARK: - Choice DNA
//
// Aggregate tally of the small vocabulary of trait keywords that appear
// in the `consequence` text of choices across all stories. Each choice
// the reader takes contributes to a few traits; the result is a quiet
// personality reading shown on the profile.
//
// Trait keywords are chosen to match the actual consequence vocabulary
// used across the generator (Brave, Wise, Honor, Cunning, Heart, Honest,
// Mercy, Joy, Cold, etc.). Matching is case-insensitive substring.

enum ChoiceTrait: String, CaseIterable, Codable, Hashable {
    case brave    = "Brave"
    case wise     = "Wise"
    case honor    = "Honor"
    case cunning  = "Cunning"
    case heart    = "Heart"
    case honest   = "Honest"
    case mercy    = "Mercy"
    case spirit   = "Spirit"
    case quiet    = "Quiet"
    case cold     = "Cold"

    /// Substrings to search for in a consequence (case-insensitive).
    var keywords: [String] {
        switch self {
        case .brave:   return ["brave", "courage"]
        case .wise:    return ["wise", "wisdom", "patient", "patience", "discipline", "strategic", "smart"]
        case .honor:   return ["honor", "vow", "honour"]
        case .cunning: return ["cunning", "clever", "trick"]
        case .heart:   return ["heart", "love", "friend", "care", "kind"]
        case .honest:  return ["honest", "truth", "plain", "honesty"]
        case .mercy:   return ["mercy", "spare", "forgive"]
        case .spirit:  return ["spirit", "joy", "defiance", "defiant"]
        case .quiet:   return ["quiet", "still", "modest"]
        case .cold:    return ["cold", "pride", "anger", "rage"]
        }
    }

    var blurb: String {
        switch self {
        case .brave:   return "You step toward what scares you."
        case .wise:    return "You read the room before you act."
        case .honor:   return "You keep the vows you make."
        case .cunning: return "You bend the rules cleverly."
        case .heart:   return "You lead with love and friendship."
        case .honest:  return "You say the true thing aloud."
        case .mercy:   return "You spare what you don't have to."
        case .spirit:  return "You refuse to be diminished."
        case .quiet:   return "You let the moment breathe."
        case .cold:    return "You hold the line, even chilled."
        }
    }
}

final class ChoiceDNAStore: ObservableObject {
    @Published private(set) var tally: [ChoiceTrait: Int] = [:]
    @Published private(set) var totalChoices: Int = 0

    private let defaultsKey = "choiceDNA.v1"

    init() {
        load()
    }

    /// Score one taken choice against every trait that matches its consequence.
    func record(consequence: String, choiceText: String) {
        let combined = (consequence + " " + choiceText).lowercased()
        var matched = false
        for trait in ChoiceTrait.allCases {
            if trait.keywords.contains(where: { combined.contains($0) }) {
                tally[trait, default: 0] += 1
                matched = true
            }
        }
        if matched { totalChoices += 1 }
        persist()
    }

    /// Traits sorted by descending count.
    var ranked: [(trait: ChoiceTrait, count: Int)] {
        ChoiceTrait.allCases
            .map { ($0, tally[$0] ?? 0) }
            .filter { $0.1 > 0 }
            .sorted { $0.1 > $1.1 }
    }

    /// Percent share of a single trait (0-100), rounded.
    func percent(for trait: ChoiceTrait) -> Int {
        let total = tally.values.reduce(0, +)
        guard total > 0 else { return 0 }
        let v = Double(tally[trait] ?? 0) / Double(total)
        return Int((v * 100).rounded())
    }

    func reset() {
        tally = [:]
        totalChoices = 0
        persist()
    }

    // MARK: Persistence

    private struct Snapshot: Codable {
        var tally: [String: Int]
        var totalChoices: Int
    }

    private func persist() {
        let stringTally = Dictionary(uniqueKeysWithValues: tally.map { ($0.key.rawValue, $0.value) })
        let snap = Snapshot(tally: stringTally, totalChoices: totalChoices)
        if let data = try? JSONEncoder().encode(snap) {
            UserDefaults.standard.set(data, forKey: defaultsKey)
        }
    }

    private func load() {
        guard let data = UserDefaults.standard.data(forKey: defaultsKey),
              let snap = try? JSONDecoder().decode(Snapshot.self, from: data) else {
            return
        }
        var t: [ChoiceTrait: Int] = [:]
        for (k, v) in snap.tally {
            if let trait = ChoiceTrait(rawValue: k) { t[trait] = v }
        }
        tally = t
        totalChoices = snap.totalChoices
    }
}
