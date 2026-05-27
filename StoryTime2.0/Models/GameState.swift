import Foundation

// MARK: - Game state
//
// Node-driven. Loads a CatalogStory and walks the user through its
// graph by node id. The previous hardcoded Scenario enum and switch
// have been removed entirely.

@MainActor
final class GameState: ObservableObject {

    @Published var story: CatalogStory?
    @Published private(set) var currentNode: StoryNode?
    @Published var showingConsequence: Bool = false
    @Published var consequenceText: String = ""
    @Published private(set) var history: [String] = []   // node ids visited

    private weak var progressStore: ReadingProgressStore?
    private weak var statsStore: StatsStore?

    func configure(story: CatalogStory,
                   progressStore: ReadingProgressStore?,
                   statsStore: StatsStore?) {
        self.story = story
        self.progressStore = progressStore
        self.statsStore = statsStore
    }

    /// Start (or resume) the story at the given node id, or the start node
    /// if none provided.
    func start(at nodeId: String? = nil) {
        guard let story else { return }
        let id = nodeId ?? story.startNodeId
        load(nodeId: id)
        statsStore?.recordStoryStarted(story.storageKey)
    }

    func restart() {
        guard let story else { return }
        history.removeAll()
        progressStore?.clear(storyKey: story.storageKey)
        load(nodeId: story.startNodeId)
    }

    func choose(_ choice: StoryChoice) {
        consequenceText = choice.consequence
        showingConsequence = true
        statsStore?.recordChoice()

        // Step to next node after a beat (caller can also drive this).
        DispatchQueue.main.asyncAfter(deadline: .now() + 1.8) { [weak self] in
            guard let self else { return }
            self.showingConsequence = false
            if let next = choice.nextNodeId {
                self.load(nodeId: next)
            }
        }
    }

    /// Immediate transition without consequence beat.
    func jump(to nodeId: String) {
        load(nodeId: nodeId)
    }

    var canGoBack: Bool { history.count > 1 }

    func goBack() {
        guard history.count > 1 else { return }
        history.removeLast()
        if let last = history.last { load(nodeId: last, recordHistory: false) }
    }

    private func load(nodeId: String, recordHistory: Bool = true) {
        guard let story, let node = story.node(id: nodeId) else { return }
        currentNode = node
        if recordHistory {
            history.append(nodeId)
        }
        statsStore?.recordSceneVisit()
        progressStore?.save(storyKey: story.storageKey,
                            title: story.title,
                            description: story.synopsis,
                            nodeId: nodeId,
                            sceneTitle: node.sceneTitle)
    }
}
