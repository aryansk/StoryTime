//
//  CatalogGraphTests.swift
//  StoryTime2.0Tests
//
//  Walks every story JSON in the catalog and asserts the graph is
//  well-formed: index.json matches the per-story files, every node id
//  referenced by a choice resolves, the start node exists, endings
//  carry no choices, and every node is reachable from the start.
//
//  This catches the authoring regressions that used to only surface at
//  runtime ("why did the reader hit a dead-end on scene 11?"). It's the
//  Swift twin of scripts/validate_catalog.py and runs in CI without a
//  Python interpreter.

import Foundation
import Testing
@testable import StoryTime2_0

struct CatalogGraphTests {

    // MARK: - Catalog location
    //
    // Unit tests don't host the app bundle, so we can't lean on
    // Bundle.main for the JSON. Resolve the catalog path from this
    // source file's location instead — robust across Xcode and CI
    // checkouts.
    private static func catalogDir(file: StaticString = #file) -> URL {
        let here = URL(fileURLWithPath: "\(file)")
        // .../StoryTime2.0Tests/CatalogGraphTests.swift → repo root
        let repo = here.deletingLastPathComponent().deletingLastPathComponent()
        return repo
            .appendingPathComponent("StoryTime2.0")
            .appendingPathComponent("Resources")
            .appendingPathComponent("Catalog")
    }

    private static func loadIndex() throws -> CatalogIndex {
        let url = catalogDir().appendingPathComponent("index.json")
        let data = try Data(contentsOf: url)
        return try CatalogJSON.decoder.decode(CatalogIndex.self, from: data)
    }

    private static func loadStory(_ entry: CatalogIndexEntry) throws -> CatalogStory {
        let filename = entry.storyURL ?? "\(entry.id).json"
        let url = catalogDir().appendingPathComponent(filename)
        let data = try Data(contentsOf: url)
        return try CatalogJSON.decoder.decode(CatalogStory.self, from: data)
    }

    // MARK: - Tests

    @Test func indexFileLoadsAndHasStories() throws {
        let index = try Self.loadIndex()
        #expect(index.stories.count > 0, "index.json should list at least one story")
    }

    @Test func indexIdsAreUnique() throws {
        let index = try Self.loadIndex()
        let ids = index.stories.map(\.id)
        let unique = Set(ids)
        #expect(unique.count == ids.count,
                "duplicate story id(s) in index.json: \(ids.duplicates())")
    }

    @Test func everyStoryLoadsAndIdsAgree() throws {
        let index = try Self.loadIndex()
        for entry in index.stories {
            let story = try Self.loadStory(entry)
            #expect(story.id == entry.id,
                    "id mismatch: index has '\(entry.id)', file has '\(story.id)'")
        }
    }

    /// One pass of the shared validator over every story. Covers start
    /// node existence, dangling choice targets, endings with choices,
    /// dead-end decision nodes, reachability, and rating range — the same
    /// checks the AI generation flow runs before saving a story.
    @Test func everyStoryGraphIsWellFormed() throws {
        let index = try Self.loadIndex()
        for entry in index.stories {
            let story = try Self.loadStory(entry)
            let issues = StoryGraphValidator.validate(story)
            #expect(issues.isEmpty,
                    "[\(story.id)] \(issues.map(\.description).joined(separator: "; "))")
        }
    }
}

// MARK: - Validator unit tests
//
// Deliberately broken graphs, exercising each check the validator
// performs. These guard the generation-flow gate itself.

struct StoryGraphValidatorTests {

    private func makeStory(startNodeId: String = "s1",
                           rating: Int? = nil,
                           nodes: [StoryNode]) -> CatalogStory {
        CatalogStory(id: "test", title: "T", sourceTitle: "T", kind: .movie,
                     synopsis: "", releaseYear: nil, addedAt: Date(),
                     genre: .drama, tags: [], rating: rating, loved: nil,
                     nextStoryId: nil, startNodeId: startNodeId, nodes: nodes)
    }

    private func decision(_ id: String, to targets: [String]) -> StoryNode {
        StoryNode(id: id, text: "t", sceneTitle: nil,
                  choices: targets.map { StoryChoice(text: "c", consequence: "q", nextNodeId: $0) },
                  isEnding: false, endingTitle: nil)
    }

    private func ending(_ id: String, choices: [StoryChoice] = []) -> StoryNode {
        StoryNode(id: id, text: "t", sceneTitle: nil, choices: choices,
                  isEnding: true, endingTitle: "End")
    }

    @Test func wellFormedGraphHasNoIssues() {
        let story = makeStory(nodes: [
            decision("s1", to: ["end_a", "end_b"]),
            ending("end_a"),
            ending("end_b"),
        ])
        #expect(StoryGraphValidator.validate(story).isEmpty)
    }

    @Test func emptyStoryIsFlagged() {
        let story = makeStory(nodes: [])
        #expect(!StoryGraphValidator.validate(story).isEmpty)
    }

    @Test func missingStartNodeIsFlagged() {
        let story = makeStory(startNodeId: "nope", nodes: [
            decision("s1", to: ["end_a"]),
            ending("end_a"),
        ])
        #expect(StoryGraphValidator.validate(story).contains {
            $0.message.contains("startNodeId")
        })
    }

    @Test func danglingChoiceTargetIsFlagged() {
        let story = makeStory(nodes: [
            decision("s1", to: ["missing", "end_a"]),
            ending("end_a"),
        ])
        #expect(StoryGraphValidator.validate(story).contains {
            $0.nodeId == "s1" && $0.message.contains("missing node")
        })
    }

    @Test func endingWithChoicesIsFlagged() {
        let story = makeStory(nodes: [
            decision("s1", to: ["end_a"]),
            ending("end_a", choices: [StoryChoice(text: "c", consequence: "q", nextNodeId: nil)]),
        ])
        #expect(StoryGraphValidator.validate(story).contains {
            $0.nodeId == "end_a" && $0.message.contains("must not have choices")
        })
    }

    @Test func deadEndDecisionNodeIsFlagged() {
        let story = makeStory(nodes: [
            decision("s1", to: ["s2", "end_a"]),
            StoryNode(id: "s2", text: "t", sceneTitle: nil, choices: [],
                      isEnding: false, endingTitle: nil),
            ending("end_a"),
        ])
        #expect(StoryGraphValidator.validate(story).contains {
            $0.nodeId == "s2" && $0.message.contains("dead end")
        })
    }

    @Test func unreachableNodeIsFlagged() {
        let story = makeStory(nodes: [
            decision("s1", to: ["end_a"]),
            decision("orphan", to: ["end_a"]),
            ending("end_a"),
        ])
        #expect(StoryGraphValidator.validate(story).contains {
            $0.nodeId == "orphan" && $0.message.contains("unreachable")
        })
    }

    @Test func duplicateNodeIdsAreFlagged() {
        let story = makeStory(nodes: [
            decision("s1", to: ["end_a"]),
            decision("s1", to: ["end_a"]),
            ending("end_a"),
        ])
        #expect(StoryGraphValidator.validate(story).contains {
            $0.nodeId == "s1" && $0.message.contains("appears 2 times")
        })
    }

    @Test func noReachableEndingIsFlagged() {
        let story = makeStory(nodes: [
            decision("s1", to: ["s2"]),
            decision("s2", to: ["s1"]),
        ])
        #expect(StoryGraphValidator.validate(story).contains {
            $0.message.contains("no ending is reachable")
        })
    }

    @Test func outOfRangeRatingIsFlagged() {
        let story = makeStory(rating: 9, nodes: [
            decision("s1", to: ["end_a"]),
            ending("end_a"),
        ])
        #expect(StoryGraphValidator.validate(story).contains {
            $0.message.contains("rating")
        })
    }
}

// MARK: - JSON extraction tests

struct AnthropicJSONExtractionTests {

    @Test func extractsBareObject() {
        let s = #"{"a": 1}"#
        #expect(AnthropicClient.extractFirstJSONObject(from: s) == s)
    }

    @Test func ignoresPreambleAndTrailingProse() {
        let s = #"Here you go: {"a": {"b": 2}} hope that helps!"#
        #expect(AnthropicClient.extractFirstJSONObject(from: s) == #"{"a": {"b": 2}}"#)
    }

    @Test func bracesInsideStringsDoNotConfuseDepth() {
        let s = #"{"text": "a } inside \" and { too"}"#
        #expect(AnthropicClient.extractFirstJSONObject(from: s) == s)
    }

    @Test func unbalancedObjectReturnsNil() {
        #expect(AnthropicClient.extractFirstJSONObject(from: #"{"a": 1"#) == nil)
        #expect(AnthropicClient.extractFirstJSONObject(from: "no json here") == nil)
    }
}

// MARK: - Diagnostics helper

private extension Array where Element: Hashable {
    /// Returns the elements that appear more than once, useful for
    /// duplicate-id error messages.
    func duplicates() -> [Element] {
        var counts: [Element: Int] = [:]
        for x in self { counts[x, default: 0] += 1 }
        return counts.filter { $0.value > 1 }.map(\.key)
    }
}
