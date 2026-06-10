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

    /// Per-step record of (decision node id, chosen choice index, choice text,
    /// consequence text). Used by the branch-peek and DNA features.
    struct ChoiceRecord: Hashable {
        let nodeId: String
        let choiceIndex: Int
        let choiceText: String
        let consequence: String
    }
    @Published private(set) var choiceLog: [ChoiceRecord] = []
    /// Companion mode: 0 = player A's turn, 1 = player B's turn. The
    /// reader rotates this after each recorded decision.
    @Published var companionTurn: Int = 0

    /// The most recent decision the reader made. Used by the ending
    /// screen's "what if you'd picked..." peek.
    var lastDecisionRecord: ChoiceRecord? { choiceLog.last }

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
        choiceLog.removeAll()
        companionTurn = 0
        progressStore?.clear(storyKey: story.storageKey)
        load(nodeId: story.startNodeId)
    }

    /// Flip whose turn it is in companion mode. Caller invokes after a
    /// decision has been recorded.
    func advanceCompanionTurn() {
        companionTurn = (companionTurn + 1) % 2
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

    /// Immediate transition without consequence beat. Caller passes the
    /// originating decision data so we can populate the choice log.
    func jump(to nodeId: String,
              fromNodeId: String? = nil,
              choiceIndex: Int? = nil,
              choiceText: String? = nil,
              consequence: String? = nil) {
        if let fromNodeId, let choiceIndex, let choiceText, let consequence {
            choiceLog.append(ChoiceRecord(
                nodeId: fromNodeId,
                choiceIndex: choiceIndex,
                choiceText: choiceText,
                consequence: consequence
            ))
        }
        load(nodeId: nodeId)
    }

    var canGoBack: Bool { history.count > 1 }

    func goBack() {
        guard history.count > 1 else { return }
        history.removeLast()
        // Drop the most recent decision too so the log stays in sync.
        if !choiceLog.isEmpty { choiceLog.removeLast() }
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
