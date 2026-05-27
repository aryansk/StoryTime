import Foundation

final class FavoritesStore: ObservableObject {
    @Published private(set) var favoriteTitles: Set<String> = []

    private let defaultsKey = "favoriteStoryTitles.v1"

    init() {
        if let saved = UserDefaults.standard.array(forKey: defaultsKey) as? [String] {
            favoriteTitles = Set(saved)
        }
    }

    func isFavorite(_ title: String) -> Bool {
        favoriteTitles.contains(title)
    }

    func toggle(_ title: String) {
        if favoriteTitles.contains(title) {
            favoriteTitles.remove(title)
        } else {
            favoriteTitles.insert(title)
        }
        persist()
    }

    private func persist() {
        UserDefaults.standard.set(Array(favoriteTitles), forKey: defaultsKey)
    }
}
