package com.storytime.android.ui

import androidx.compose.animation.AnimatedContent
import androidx.compose.animation.fadeIn
import androidx.compose.animation.fadeOut
import androidx.compose.animation.togetherWith
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.interaction.MutableInteractionSource
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.runtime.collectAsState
import androidx.compose.runtime.saveable.listSaver
import androidx.compose.runtime.saveable.rememberSaveable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.ColorFilter
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.storytime.android.app
import com.storytime.android.data.CatalogRepository
import com.storytime.android.model.CatalogStory
import com.storytime.android.model.StoryChoice
import com.storytime.android.share.EndingShare
import com.storytime.android.ui.theme.DoodleIcon
import com.storytime.android.ui.theme.LocalStPalette
import com.storytime.android.ui.theme.PageBackground
import com.storytime.android.ui.theme.SketchCard
import com.storytime.android.ui.theme.SketchPrimaryButton
import com.storytime.android.ui.theme.SketchSecondaryButton
import com.storytime.android.ui.theme.readerFontFamily
import kotlinx.coroutines.delay

@Composable
fun StoryReaderScreen(
    storyId: String,
    resumeNodeId: String?,
    onExit: () -> Unit,
    onContinueSaga: (String) -> Unit = {},
) {
    val ctx = LocalContext.current
    val palette = LocalStPalette.current
    val settings by app.settings.state.collectAsState()
    val isSpeaking by app.speech.isSpeaking.collectAsState()
    val endings by app.endings.discovered.collectAsState()

    var story by remember { mutableStateOf<CatalogStory?>(null) }
    // Reader position survives configuration changes and process death.
    var currentId by rememberSaveable { mutableStateOf<String?>(null) }
    var history by rememberSaveable(
        stateSaver = listSaver<List<String>, String>(save = { it }, restore = { it }),
    ) { mutableStateOf(listOf<String>()) }
    // The consequence of the just-made choice, shown as an interstitial beat
    // *before* moving to the next scene (mirrors the iOS reader). While set,
    // the next node id waits in `pendingNext`.
    var pendingConsequence by rememberSaveable { mutableStateOf<String?>(null) }
    var pendingNext by rememberSaveable { mutableStateOf<String?>(null) }
    var turnIndex by rememberSaveable { mutableStateOf(0) }
    var typedChars by remember { mutableStateOf(0) }
    // Reset per node; tapping the passage skips the typewriter reveal.
    var skipTypewriter by remember(currentId) { mutableStateOf(false) }

    LaunchedEffect(storyId) {
        val s = CatalogRepository.loadStoryById(ctx, storyId) ?: return@LaunchedEffect
        story = s
        // Only seed the position on a fresh open — don't clobber a restored one.
        if (currentId == null) {
            currentId = resumeNodeId?.takeIf { id -> s.nodes.any { it.id == id } } ?: s.startNodeId
        }
        app.stats.recordStoryStarted(s.title)
        if (settings.ambienceEnabled) app.ambience.play(s.genre)
    }

    DisposableEffect(Unit) {
        onDispose {
            app.ambience.stop()
            app.speech.stop()
        }
    }

    val s = story
    val node = s?.let { it.node(currentId ?: it.startNodeId) }

    LaunchedEffect(node?.id) {
        val n = node
        val story = s
        if (n != null && story != null) {
            app.stats.recordSceneVisit()
            // A finished story shouldn't stay in "Continue reading" or resume
            // straight onto its ending; clear the checkpoint at an ending.
            if (n.isEnding) {
                app.endings.record(story.id, n.id)
                app.progress.clear(story.id)
            } else {
                app.progress.save(story.id, story.title, story.synopsis, n.id, n.sceneTitle)
            }
        }
        app.speech.stop()
        typedChars = 0
        if (settings.typewriterEnabled && n != null) {
            // Cap the reveal at ~33 fps: at fast speeds, step several
            // characters per tick instead of recomposing per character (each
            // recompose re-copies the visible substring — O(n²) over a scene).
            val delayMs = (settings.typingSpeed * 1000).toLong().coerceAtLeast(1)
            val tickMs = maxOf(30L, delayMs)
            val step = maxOf(1, (tickMs / delayMs).toInt())
            var i = 0
            while (i < n.text.length) {
                if (skipTypewriter) { typedChars = n.text.length; break }
                i = minOf(n.text.length, i + step)
                typedChars = i
                delay(tickMs)
            }
        } else {
            typedChars = n?.text?.length ?: 0
        }
    }

    PageBackground(Modifier.fillMaxSize()) {
        Column(Modifier.fillMaxSize().padding(horizontal = 20.dp)) {
            Spacer(Modifier.height(16.dp))
            Row(verticalAlignment = Alignment.CenterVertically) {
                TextButton(onClick = onExit) {
                    DoodleIcon("xmark", modifier = Modifier.size(16.dp), tint = ColorFilter.tint(palette.ink))
                    Spacer(Modifier.width(4.dp))
                    Text("Exit", color = palette.ink)
                }
                // Back sits next to Exit on the left — both are navigation.
                if (history.isNotEmpty()) {
                    TextButton(onClick = {
                        currentId = history.last()
                        history = history.dropLast(1)
                        pendingConsequence = null
                        pendingNext = null
                    }) {
                        DoodleIcon("chevronLeft", modifier = Modifier.size(16.dp), tint = ColorFilter.tint(palette.ink))
                        Spacer(Modifier.width(4.dp))
                        Text("Back", color = palette.ink)
                    }
                }
                Spacer(Modifier.weight(1f))
                node?.let { n ->
                    TextButton(onClick = {
                        if (isSpeaking) app.speech.stop()
                        else app.speech.speak((n.sceneTitle?.let { "$it. " } ?: "") + n.text)
                    }) {
                        DoodleIcon(
                            if (isSpeaking) "speakerPlaying" else "speaker",
                            modifier = Modifier.size(16.dp),
                            tint = ColorFilter.tint(palette.ink),
                        )
                        Spacer(Modifier.width(4.dp))
                        Text(if (isSpeaking) "Stop" else "Listen", color = palette.ink)
                    }
                }
            }
            Spacer(Modifier.height(8.dp))
            if (s == null || node == null) {
                Box(Modifier.fillMaxSize(), contentAlignment = Alignment.Center) { CircularProgressIndicator() }
                return@Column
            }

            AnimatedContent(
                targetState = node,
                transitionSpec = { fadeIn() togetherWith fadeOut() },
                label = "node",
            ) { n ->
                Column(Modifier.fillMaxSize().verticalScroll(rememberScrollState())) {
                    n.sceneTitle?.let {
                        Text(it.uppercase(), fontSize = 12.sp, fontWeight = FontWeight.SemiBold, color = palette.accent)
                        Spacer(Modifier.height(6.dp))
                    }
                    val visible = if (settings.typewriterEnabled) n.text.take(typedChars) else n.text
                    Text(
                        text = visible,
                        fontSize = settings.textSize.sp,
                        lineHeight = (settings.textSize * 1.5f).sp,
                        color = palette.ink,
                        fontFamily = readerFontFamily(settings.fontName),
                        modifier = if (settings.typewriterEnabled) {
                            Modifier.clickable(
                                interactionSource = remember { MutableInteractionSource() },
                                indication = null,
                            ) { skipTypewriter = true }
                        } else Modifier,
                    )

                    if (settings.companionEnabled && !n.isEnding) {
                        val who = if (turnIndex % 2 == 0) settings.companionA else settings.companionB
                        Spacer(Modifier.height(10.dp))
                        Text("$who's turn", fontSize = 12.sp, fontWeight = FontWeight.SemiBold, color = palette.accent)
                    }

                    Spacer(Modifier.height(28.dp))

                    if (n.isEnding) {
                        EndingCard(title = n.endingTitle ?: "The End")
                        val totalEndings = s.nodes.count { it.isEnding }
                        val discoveredEndings = endings[s.id]?.size ?: 0
                        if (totalEndings > 1) {
                            Spacer(Modifier.height(10.dp))
                            Text(
                                "You've found $discoveredEndings of $totalEndings endings.",
                                fontSize = 14.sp, color = palette.inkSoft,
                            )
                        }
                        Spacer(Modifier.height(16.dp))
                        SketchPrimaryButton(
                            text = "Share this ending",
                            onClick = { EndingShare.share(ctx, s.title, n.endingTitle ?: "The End") },
                            modifier = Modifier.fillMaxWidth(),
                        )
                        Spacer(Modifier.height(8.dp))
                        s.nextStoryId?.let { nextId ->
                            SketchPrimaryButton(
                                text = "Continue the saga →",
                                onClick = { onContinueSaga(nextId) },
                                modifier = Modifier.fillMaxWidth(),
                            )
                            Spacer(Modifier.height(8.dp))
                        }
                        SketchSecondaryButton(
                            text = "Replay from start",
                            onClick = {
                                app.progress.clear(storyId)
                                currentId = s.startNodeId
                                history = emptyList()
                                pendingConsequence = null
                                pendingNext = null
                                turnIndex = 0
                            },
                            modifier = Modifier.fillMaxWidth(),
                        )
                        Spacer(Modifier.height(8.dp))
                        SketchSecondaryButton(text = "Return to Catalog", onClick = onExit, modifier = Modifier.fillMaxWidth())
                    } else {
                        n.choices.forEachIndexed { idx, choice ->
                            ChoiceButton(number = idx + 1, choice = choice) {
                                // Record the decision now, but hold the scene
                                // transition until the consequence beat is
                                // acknowledged (see the overlay below).
                                history = history + n.id
                                app.dna.record(choice.consequence, choice.text)
                                app.stats.recordChoice()
                                turnIndex += 1
                                pendingConsequence = choice.consequence
                                pendingNext = choice.nextNodeId ?: n.id
                            }
                            Spacer(Modifier.height(10.dp))
                        }
                    }
                    Spacer(Modifier.height(40.dp))
                }
            }
        }

        // Consequence beat: a tap-to-continue interstitial shown over the
        // current scene before advancing to the next node.
        pendingConsequence?.let { text ->
            ConsequenceOverlay(text = text) {
                pendingNext?.let { currentId = it }
                pendingConsequence = null
                pendingNext = null
            }
        }
    }
}

@Composable
private fun EndingCard(title: String) {
    val palette = LocalStPalette.current
    SketchCard(modifier = Modifier.fillMaxWidth()) {
        Column {
            Text("ENDING", fontSize = 12.sp, fontWeight = FontWeight.Black, color = palette.accent)
            Spacer(Modifier.height(4.dp))
            Text(title, fontSize = 22.sp, fontWeight = FontWeight.SemiBold, color = palette.ink)
        }
    }
}

@Composable
private fun ChoiceButton(number: Int, choice: StoryChoice, onClick: () -> Unit) {
    val palette = LocalStPalette.current
    // Only the choice text is shown. The consequence is deliberately hidden
    // until *after* the choice is made (revealed by the reader as a beat) —
    // showing it here would spoil the whole point of the decision. A numbered
    // medallion echoes the CYOA-paperback feel of the iOS reader.
    SketchCard(modifier = Modifier.fillMaxWidth(), onClick = onClick) {
        Row(verticalAlignment = Alignment.CenterVertically) {
            Box(
                modifier = Modifier
                    .size(28.dp)
                    .clip(RoundedCornerShape(8.dp))
                    .background(palette.mist)
                    .border(1.5.dp, palette.ink, RoundedCornerShape(8.dp)),
                contentAlignment = Alignment.Center,
            ) {
                Text("$number", fontSize = 14.sp, fontWeight = FontWeight.Black, color = palette.ink)
            }
            Spacer(Modifier.width(12.dp))
            Text(
                choice.text,
                fontSize = 16.sp,
                fontWeight = FontWeight.SemiBold,
                color = palette.ink,
                modifier = Modifier.weight(1f),
            )
        }
    }
}

@Composable
private fun ConsequenceOverlay(text: String, onContinue: () -> Unit) {
    val palette = LocalStPalette.current
    Box(
        modifier = Modifier
            .fillMaxSize()
            .background(palette.ink.copy(alpha = 0.18f))
            .clickable(
                interactionSource = remember { MutableInteractionSource() },
                indication = null,
            ) { onContinue() },
        contentAlignment = Alignment.BottomCenter,
    ) {
        SketchCard(
            modifier = Modifier.fillMaxWidth().padding(20.dp),
            onClick = onContinue,
        ) {
            Column {
                Text("CONSEQUENCE", fontSize = 12.sp, fontWeight = FontWeight.Black, color = palette.accent)
                Spacer(Modifier.height(8.dp))
                Text(text, fontSize = 16.sp, color = palette.ink)
                Spacer(Modifier.height(12.dp))
                Text("Tap to continue →", fontSize = 13.sp, fontWeight = FontWeight.SemiBold, color = palette.inkSoft)
            }
        }
    }
}
