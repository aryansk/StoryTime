# StoryTime

StoryTime is a native interactive-reading app for iPhone, iPad, and Android. Its visual language is ink on warm paper: hand-drawn doodles, gently imperfect cards, chunky editorial headings, and a readable serif story face.

The bundled catalog currently contains 182 validated stories and 572 endings. A growing set of signature originals—**The Last Lightkeeper**, **The Museum of Unsent Letters**, and the six after-midnight tales of **The Night Shelf**—set the quality bar for first-party, genuinely branching stories.

## Product highlights

- Personalized **Tonight's Pick** recommendations based on onboarding intent, reading history, and story length, plus a **Surprise Me** shuffle that leans toward stories you haven't opened.
- Search across titles, source titles, synopses, genres, formats, and tags, with sort by Featured, Newest, Top Rated, Shortest, or A–Z.
- Curated mood and format collections (including **The Night Shelf** of first-party originals), ratings, favorites, and saga links.
- Automatic checkpoints with visible completion estimates, a Continue Reading library, and a **Finished** shelf that tracks endings discovered and nudges replays.
- Multiple endings, an endings tracker, path-not-taken prompts, and shareable ending cards.
- Reader typography controls, adjustable line spacing, paper themes, dark mode, typewriter mode, and **Focus Mode**.
- Optional system narration, genre ambience, and pass-and-play companion mode.
- Daily scene goals, streaks, reading time, completions, Choice DNA, and achievements.
- Hand-authored personal stories plus optional bring-your-own-key generation. API keys are stored in Keychain on Apple platforms and encrypted preferences on Android.
- VoiceOver/content descriptions, Dynamic Type, Reduce Motion support, labeled controls, and 44-point minimum touch targets in shared Apple components.

## Repository layout

```text
StoryTime2.0/                 SwiftUI app
  Models/                     Catalog, persistence, reader state, services
  Theme/                      Tokens, motion, components, fonts, doodles
  Views/                      Discovery, reader, library, profile, settings
  Resources/Catalog/          Bundled story JSON and index
StoryTime2.0Tests/            Catalog and model tests
StoryTime2.0UITests/          Launch and navigation smoke tests
StoryTimeAndroid/             Jetpack Compose app
site/                         Static product website
scripts/                      Catalog authoring, validation, and asset tools
```

The apps do not use CocoaPods or third-party iOS runtime dependencies.

## Requirements

### Apple

- Xcode 26 or newer
- iOS/iPadOS 26.0 or newer (the app uses the system Liquid Glass tab bar and `tabBarMinimizeBehavior`)
- The `StoryTime2.0` scheme

Open `StoryTime2.0.xcodeproj`, choose an iPhone or iPad simulator, then build and run.

Command-line verification:

```bash
xcodebuild \
  -project StoryTime2.0.xcodeproj \
  -scheme StoryTime2.0 \
  -destination 'platform=iOS Simulator,name=iPhone 17' \
  -derivedDataPath /tmp/StoryTimeDerived \
  test CODE_SIGNING_ALLOWED=NO
```

### Android

- Android Studio Hedgehog or newer
- JDK 17
- Android SDK 34

```bash
cd StoryTimeAndroid
gradle :app:assembleDebug
```

## Architecture

`ContentView` owns the long-lived app stores and injects them through the SwiftUI environment. Each tab keeps its own `NavigationStack` mounted so tab switches preserve navigation, scroll, search, and filter state.

Stories use a data-driven graph:

```text
CatalogIndex → CatalogStory → StoryNode → StoryChoice → next StoryNode
```

`GameState` traverses that graph. `ReadingProgressStore`, `StatsStore`, `FavoritesStore`, `EndingsTracker`, and `ChoiceDNAStore` persist local reader state. The same catalog JSON is packaged into both native apps.

Catalog loading is offline-first. The Apple app loads bundled and cached content away from the main actor, then optionally merges a remote catalog when `CatalogBaseURL` is configured.

## Working with stories

The compact Python specs are the source of truth for story metadata and
branching. Existing catalog JSON is the source of truth for edited scene prose
and choice consequences. A normal build preserves that editorial copy while
regenerating structure.

Build all managed stories and the index:

```bash
python3 scripts/build_stories.py
```

To deliberately discard edited catalog prose and restore the compact spec copy,
use `python3 scripts/build_stories.py --refresh-editorial-copy`. This is an
editorial reset and should not be part of the normal build workflow.

Validate metadata parity, graph reachability, choice integrity, endings, and content fields:

```bash
python3 scripts/validate_catalog.py
```

After rebuilding, keep Android's bundled catalog in sync:

```bash
rsync -a --delete \
  StoryTime2.0/Resources/Catalog/ \
  StoryTimeAndroid/app/src/main/assets/Catalog/
```

The build pipeline expands compact consequence labels such as `Brave.` into deterministic narrative beats. The original label remains in the prose so Choice DNA can still classify the decision.

## Testing

The Swift test target checks every story file and fails on:

- duplicate story or node IDs;
- index/payload metadata drift;
- missing or unreachable nodes;
- choices without valid targets;
- empty text, scene titles, choices, consequences, or ending titles;
- repeated labels within a decision;
- endings that still contain choices;
- malformed generated JSON;
- consequence beats below the readability floor.

The Python validator mirrors the catalog checks for authoring and CI workflows.

## Privacy and external services

Reading state stays on device. Cross-device sync and analytics are not currently implemented.

AI creation is optional and requires a user-provided Anthropic API key. The key is sent only to Anthropic for generation, is never bundled with the app, and failed requests do not consume the local daily allowance.

Notification permission is requested only when a reader enables reminders. Narration uses the operating system's speech service.

## Website

The static site in `site/` has no build step. Serve it locally with any static server, for example:

```bash
python3 -m http.server 8080 --directory site
```
