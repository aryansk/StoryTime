//
//  StoryTime2_0UITests.swift
//  StoryTime2.0UITests
//
//  Created by Aryan Signh on 27/01/25.
//

import XCTest

final class StoryTime2_0UITests: XCTestCase {

    override func setUpWithError() throws {
        continueAfterFailure = false
    }

    @MainActor
    func testDiscoveryShellAndTabsLaunch() throws {
        let app = XCUIApplication()
        app.launchArguments = [
            "-onboarding_completed", "YES",
            "-focusModeByDefault", "NO",
            "-startTab", "discover",
        ]
        app.launch()

        XCTAssertTrue(app.staticTexts["Adventures"].waitForExistence(timeout: 8))
        XCTAssertTrue(app.buttons["Discover"].exists)
        XCTAssertTrue(app.buttons["Library"].exists)
        XCTAssertTrue(app.buttons["Profile"].exists)
        XCTAssertTrue(app.buttons["Settings"].exists)
    }

    @MainActor
    func testReaderDeepLinkShowsChoicesAndControls() throws {
        let app = XCUIApplication()
        app.launchArguments = [
            "-onboarding_completed", "YES",
            "-focusModeByDefault", "NO",
            "-deepLinkStoryID", "mn-wrong-number",
        ]
        app.launch()

        XCTAssertTrue(app.staticTexts["Wrong Number"].waitForExistence(timeout: 8))
        XCTAssertTrue(app.staticTexts["Ring"].exists)
        XCTAssertTrue(app.buttons["Reading controls"].exists)
        XCTAssertTrue(app.buttons["Enter focus mode"].exists)
        XCTAssertTrue(app.buttons.containing(NSPredicate(format: "label CONTAINS 'Answer'")).firstMatch.exists)
    }

    @MainActor
    func testLaunchPerformance() throws {
        if #available(macOS 10.15, iOS 13.0, tvOS 13.0, watchOS 7.0, *) {
            // This measures how long it takes to launch your application.
            measure(metrics: [XCTApplicationLaunchMetric()]) {
                let app = XCUIApplication()
                app.launchArguments = [
                    "-onboarding_completed", "YES",
                    "-focusModeByDefault", "NO",
                ]
                app.launch()
            }
        }
    }
}
