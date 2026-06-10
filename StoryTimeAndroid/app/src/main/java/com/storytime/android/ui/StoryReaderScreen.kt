package com.storytime.android.ui

import androidx.compose.animation.AnimatedContent
import androidx.compose.animation.fadeIn
import androidx.compose.animation.fadeOut
import androidx.compose.animation.togetherWith
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.runtime.collectAsState
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.storytime.android.app
import com.storytime.android.data.CatalogRepository
import com.storytime.android.model.CatalogStory
import com.storytime.android.model.StoryChoice
import com.storytime.android.share.EndingShare
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

    var story by remember { mutableStateOf<CatalogStory?>(null) }
    var currentId by remember { mutableStateOf<String?>(null) }
    var history by remember { mutableStateOf(listOf<String>()) }
    var lastConsequence by remember { mutableStateOf<String?>(null) }
    var turnIndex by remember { mutableStateOf(0) }
    var typedChars by remember { mutableStateOf(0) }

    LaunchedEffect(storyId) {
        val s = CatalogRepository.loadStoryById(ctx, storyId) ?: return@LaunchedEffect
        story = s
        currentId = resumeNodeId?.takeIf { id -> s.nodes.any { it.id == id } } ?: s.startNodeId
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
            app.progress.save(story.id, story.title, story.synopsis, n.id, n.sceneTitle)
            if (n.isEnding) app.endings.record(story.id, n.id)
        }
        app.speech.stop()
        typedChars = 0
        if (settings.typewriterEnabled && n != null) {
            val delayMs = (settings.typingSpeed * 1000).toLong().coerceAtLeast(10)
            for (i in 1..n.text.length) {
                typedChars = i
                delay(delayMs)
            }
        } else {
            typedChars = n?.text?.length ?: 0
        }
    }

    PageBackground(Modifier.fillMaxSize()) {
        Column(Modifier.fillMaxSize().padding(horizontal = 20.dp)) {
            Spacer(Modifier.height(16.dp))
            Row(verticalAlignment = Alignment.CenterVertically) {
                TextButton(onClick = onExit) { Text("✕ Exit", color = palette.ink) }
                Spacer(Modifier.weight(1f))
                node?.let { n ->
                    TextButton(onClick = {
                        if (isSpeaking) app.speech.stop()
                        else app.speech.speak((n.sceneTitle?.let { "$it. " } ?: "") + n.text)
                    }) { Text(if (isSpeaking) "■ Stop" else "▶ Listen", color = palette.ink) }
                }
                if (history.isNotEmpty()) {
                    TextButton(onClick = {
                        currentId = history.last()
                        history = history.dropLast(1)
                        lastConsequence = null
                    }) { Text("← Back", color = palette.ink) }
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
                    )

                    if (settings.companionEnabled && !n.isEnding) {
                        val who = if (turnIndex % 2 == 0) settings.companionA else settings.companionB
                        Spacer(Modifier.height(10.dp))
                        Text("$who's turn", fontSize = 12.sp, fontWeight = FontWeight.SemiBold, color = palette.accent)
                    }

                    lastConsequence?.let {
                        Spacer(Modifier.height(12.dp))
                        Text("— $it", fontSize = 14.sp, color = palette.inkSoft)
                    }

                    Spacer(Modifier.height(28.dp))

                    if (n.isEnding) {
                        EndingCard(title = n.endingTitle ?: "The End")
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
                                lastConsequence = null
                                turnIndex = 0
                            },
                            modifier = Modifier.fillMaxWidth(),
                        )
                        Spacer(Modifier.height(8.dp))
                        SketchSecondaryButton(text = "Return to Catalog", onClick = onExit, modifier = Modifier.fillMaxWidth())
                    } else {
                        n.choices.forEach { choice ->
                            ChoiceButton(choice) {
                                history = history + n.id
                                lastConsequence = choice.consequence
                                app.dna.record(choice.consequence, choice.text)
                                app.stats.recordChoice()
                                turnIndex += 1
                                currentId = choice.nextNodeId ?: n.id
                            }
                            Spacer(Modifier.height(10.dp))
                        }
                    }
                    Spacer(Modifier.height(40.dp))
                }
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
private fun ChoiceButton(choice: StoryChoice, onClick: () -> Unit) {
    val palette = LocalStPalette.current
    SketchCard(modifier = Modifier.fillMaxWidth(), onClick = onClick) {
        Column {
            Text(choice.text, fontSize = 16.sp, fontWeight = FontWeight.SemiBold, color = palette.ink)
            if (choice.consequence.isNotBlank()) {
                Spacer(Modifier.height(2.dp))
                Text(choice.consequence, fontSize = 12.sp, color = palette.inkSoft)
            }
        }
    }
}
