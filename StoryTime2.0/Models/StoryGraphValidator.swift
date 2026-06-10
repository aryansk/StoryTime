import Foundation

// MARK: - Story graph validator
//
// Structural checks for a CatalogStory's node graph, shared by the
// catalog unit tests and the AI generation flow. Model output is the
// main source of malformed graphs (dangling nextNodeId, unreachable
// scenes, endings with choices), so generated stories are validated
// here before they're saved to the library.

enum StoryGraphValidator {

    struct Issue: CustomStringConvertible, Equatable {
        let nodeId: String?
        let message: String
        var description: String {
            if let nodeId { return "node '\(nodeId)': \(message)" }
            return message
        }
    }

    /// Returns every structural problem found; an empty array means the
    /// graph is well-formed.
    static func validate(_ story: CatalogStory) -> [Issue] {
        var issues: [Issue] = []

        if story.nodes.isEmpty {
            return [Issue(nodeId: nil, message: "story has no nodes")]
        }

        // Duplicate node ids.
        var counts: [String: Int] = [:]
        for node in story.nodes { counts[node.id, default: 0] += 1 }
        for (id, n) in counts where n > 1 {
            issues.append(Issue(nodeId: id, message: "appears \(n) times"))
        }
        let ids = Set(counts.keys)

        // Start node must exist.
        if !ids.contains(story.startNodeId) {
            issues.append(Issue(nodeId: nil,
                                message: "startNodeId '\(story.startNodeId)' is not in nodes"))
        }

        for node in story.nodes {
            // Every choice target must resolve.
            for choice in node.choices {
                if let target = choice.nextNodeId, !ids.contains(target) {
                    issues.append(Issue(nodeId: node.id,
                                        message: "choice targets missing node '\(target)'"))
                }
            }
            // Endings carry no choices; decision nodes must offer some.
            if node.isEnding && !node.choices.isEmpty {
                issues.append(Issue(nodeId: node.id,
                                    message: "ending node must not have choices"))
            }
            if !node.isEnding && node.choices.isEmpty {
                issues.append(Issue(nodeId: node.id,
                                    message: "decision node has no choices (dead end)"))
            }
        }

        // Every node must be reachable from the start.
        let byId = Dictionary(story.nodes.map { ($0.id, $0) },
                              uniquingKeysWith: { first, _ in first })
        var visited = Set<String>()
        var frontier = [story.startNodeId]
        while let id = frontier.popLast() {
            guard visited.insert(id).inserted, let node = byId[id] else { continue }
            for choice in node.choices {
                if let next = choice.nextNodeId, byId[next] != nil {
                    frontier.append(next)
                }
            }
        }
        for id in ids.subtracting(visited).sorted() {
            issues.append(Issue(nodeId: id, message: "unreachable from start"))
        }

        // A story the reader can never finish is malformed too.
        if !story.nodes.contains(where: { $0.isEnding && visited.contains($0.id) }) {
            issues.append(Issue(nodeId: nil, message: "no ending is reachable from start"))
        }

        if let r = story.rating, !(1...5).contains(r) {
            issues.append(Issue(nodeId: nil, message: "rating must be 1...5, got \(r)"))
        }

        return issues
    }
}
