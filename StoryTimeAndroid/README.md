# StoryTime Android

Kotlin + Jetpack Compose port of the iOS StoryTime 2.0 app — single-module Android project that mirrors the iOS feature set.

## What works
- **Discover catalog** with broad search, genre filters, curated **collections**, a personalized deterministic **Tonight's Pick**, "new this week" badges, and a "Continue reading" strip.
- **Story reader** with choice graph traversal, history back-stack, typewriter mode, ambience playback (no-op until you drop tracks in `res/raw/`), pass-and-play companion mode, ▶ Listen button (Android TTS), share-this-ending image card, and **saga chain** that offers "Continue the saga →" when the story has a `nextStoryId`.
- **Persistence**: reading progress, endings tracker, favorites, choice DNA tally, reading stats (streaks / scenes / choices / stories), personal AI-generated stories, narration rate.
- **Library tab** — In Progress / Favorites / Finished.
- **Profile** — display name, stats, ranked Choice DNA traits, endings list.
- **Settings** — text size, font, dark mode, paper tint, typewriter, narration rate, ambience, companion names, daily reminder (with **runtime notification-permission request** and exact-alarm settings CTA, plus optional "tonight's pick" content), Anthropic API key (stored in EncryptedSharedPreferences), AI daily cap counter, reset data, About / Privacy / Terms.
- **Onboarding** — 3-step name / goal / experience flow, gates the app on first launch.
- **Create tab** — generate a personal CYOA via the Anthropic Messages API using your own key.
- **Endings grid** — locked tiles until discovered.
- **Daily reminder** via `AlarmManager.setExactAndAllowWhileIdle` (when the OS allows it), rescheduled on fire and on device reboot via `BootReceiver`.
- **Share** — endings render to a 1080×1350 PNG (StoryTime brand bar, ending title, story name) and are exposed through a `FileProvider` to the system share sheet.
- **Sketch theme** — buttery-yellow paper, deep-ink linework, hand-drawn chip / card / button vocabulary in [Sketch.kt](app/src/main/java/com/storytime/android/ui/theme/Sketch.kt), palette in [Theme.kt](app/src/main/java/com/storytime/android/ui/theme/Theme.kt), 10 doodle vector icons in `res/drawable/doodle_*.xml` wired through [Doodle.kt](app/src/main/java/com/storytime/android/ui/theme/Doodle.kt).
- **App icon** — adaptive launcher icon (vector "S" on butter background) + monochrome notification icon.

## Layout
- `app/src/main/java/com/storytime/android/`
  - `model/` — serialization models (`CatalogStory`, `StoryNode`, `StoryChoice`, …) mirroring `CatalogStory.swift`.
  - `data/` — `ProgressStore`, `EndingsStore`, `FavoritesStore`, `ChoiceDnaStore`, `StatsStore`, `PersonalStoriesStore`, `SettingsStore`, `UserStore`, `SecretStore`, `CollectionsCatalog`, `CatalogRepository`.
  - `ai/AnthropicClient.kt` — bring-your-own-key Messages API wrapper.
  - `audio/AmbienceService.kt` — looping `MediaPlayer` background audio; silent if no `R.raw.ambience_<genre>` file exists.
  - `audio/SpeechService.kt` — `TextToSpeech` wrapper with a state flow for ▶/■ button state.
  - `notify/` — `ReminderReceiver`, `ReminderScheduler`, `BootReceiver`, and a `Permissions.kt` helper for `POST_NOTIFICATIONS` + `SCHEDULE_EXACT_ALARM`.
  - `share/EndingShare.kt` — canvas-rendered ending card + share intent via `FileProvider`.
  - `ui/` — `CatalogScreen`, `StoryStartScreen`, `StoryReaderScreen`, `LibraryScreen`, `SettingsScreen`, `ProfileScreen`, `OnboardingScreen`, `CreateStoryScreen`, `EndingsGridScreen`, `LegalPages`, `theme/`.
- `app/src/main/assets/Catalog/` — 176 story JSON files + index, shared verbatim with iOS.

## Release notes
CI and release signing are repository-owner concerns. Before publishing, configure a private signing key, add the store metadata, and run the debug build below on the supported Android versions.

## Build
Requires Android Studio Hedgehog+ (AGP 8.5, Kotlin 1.9.24, JDK 17). The Gradle wrapper jar is **not** committed — open in Android Studio once and it'll generate the wrapper, or run `gradle wrapper` from a local Gradle install.

```
./gradlew :app:assembleDebug
```

To enable AI generation, paste a key in **Settings → Anthropic API key**. It's stored encrypted on device and only ever sent to `api.anthropic.com`. The daily cap (`SettingsStore.Settings.AI_DAILY_CAP = 20`) protects against runaway use.

To enable ambience audio, drop short `.m4a` files into `app/src/main/res/raw/` named `ambience_drama`, `ambience_thriller`, `ambience_scifi`, `ambience_fantasy`, `ambience_horror`, `ambience_comedy`, `ambience_action` (resource names must be lowercase + underscores, hence `scifi`).

Notification reminders require granting `POST_NOTIFICATIONS` on Android 13+ — the Settings screen requests it the first time you flip the toggle. Exact alarms may also need a one-time user grant on Android 12+; Settings surfaces a link to the system page if the OS blocks them.
