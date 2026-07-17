//
//  StoryTime2_0Tests.swift
//  StoryTime2.0Tests
//
//  Created by Aryan Signh on 27/01/25.
//

import Foundation
import Testing
@testable import StoryTime2_0

struct StoryTime2_0Tests {

    private func linearStory() -> CatalogStory {
        CatalogStory(
            id: "progress-test",
            title: "Progress",
            sourceTitle: "Progress",
            kind: .book,
            synopsis: "A test story.",
            releaseYear: nil,
            addedAt: Date(),
            genre: .drama,
            tags: [],
            rating: nil,
            loved: nil,
            nextStoryId: nil,
            startNodeId: "s1",
            nodes: [
                StoryNode(id: "s1", text: "The first scene opens with enough words to read.",
                          sceneTitle: "One", choices: [
                            StoryChoice(text: "Go left", consequence: "A thoughtful consequence follows.", nextNodeId: "s2"),
                            StoryChoice(text: "Go right", consequence: "Another thoughtful consequence follows.", nextNodeId: "s2"),
                          ], isEnding: false, endingTitle: nil),
                StoryNode(id: "s2", text: "The second scene continues the test.",
                          sceneTitle: "Two", choices: [
                            StoryChoice(text: "Finish now", consequence: "The ending moves closer now.", nextNodeId: "end"),
                            StoryChoice(text: "Finish later", consequence: "The ending still moves closer.", nextNodeId: "end"),
                          ], isEnding: false, endingTitle: nil),
                StoryNode(id: "end", text: "The story ends.", sceneTitle: "End",
                          choices: [], isEnding: true, endingTitle: "The End"),
            ]
        )
    }

    @Test func graphDepthProducesMonotonicProgress() {
        let story = linearStory()
        let start = story.progressFraction(at: "s1")
        let middle = story.progressFraction(at: "s2")
        let end = story.progressFraction(at: "end")
        #expect(start > 0)
        #expect(start < middle)
        #expect(middle < end)
        #expect(end == 1)
    }

    @Test func readingEstimateHasSensibleMinimum() {
        #expect(linearStory().estimatedMinutes >= 2)
    }

}
