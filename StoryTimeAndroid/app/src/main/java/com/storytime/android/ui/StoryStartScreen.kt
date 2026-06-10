package com.storytime.android.ui

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
import com.storytime.android.ui.theme.LocalStPalette
import com.storytime.android.ui.theme.PageBackground
import com.storytime.android.ui.theme.SketchPrimaryButton
import com.storytime.android.ui.theme.SketchSecondaryButton

@Composable
fun StoryStartScreen(
    storyId: String,
    onBegin: () -> Unit,
    onResume: (String) -> Unit,
    onBack: () -> Unit,
    onSeeEndings: () -> Unit,
) {
    val ctx = LocalContext.current
    val palette = LocalStPalette.current
    var story by remember { mutableStateOf<CatalogStory?>(null) }
    var error by remember { mutableStateOf<String?>(null) }
    val favorites by app.favorites.titles.collectAsState()
    val progress by app.progress.entries.collectAsState()
    val endings by app.endings.discovered.collectAsState()

    LaunchedEffect(storyId) {
        runCatching { CatalogRepository.loadStoryById(ctx, storyId) }
            .onSuccess { story = it }
            .onFailure { error = it.message }
    }

    val s = story
    val resume = progress[storyId]
    val totalEndings = s?.nodes?.count { it.isEnding } ?: 0
    val discoveredEndings = endings[storyId]?.size ?: 0

    PageBackground(Modifier.fillMaxSize()) {
        Column(Modifier.fillMaxSize().padding(20.dp).verticalScroll(rememberScrollState())) {
            Spacer(Modifier.height(12.dp))
            Row(verticalAlignment = Alignment.CenterVertically) {
                TextButton(onClick = onBack) { Text("← Back", color = palette.ink) }
                Spacer(Modifier.weight(1f))
                if (s != null) {
                    TextButton(onClick = { app.favorites.toggle(s.title) }) {
                        val on = s.title in favorites
                        Text(if (on) "★ Favorited" else "☆ Favorite", color = palette.ink)
                    }
                }
            }
            Spacer(Modifier.height(8.dp))
            when {
                error != null -> Text("Error: $error")
                s == null -> CircularProgressIndicator()
                else -> {
                    Text(s.title, fontSize = 32.sp, fontWeight = FontWeight.Black, color = palette.ink)
                    Spacer(Modifier.height(4.dp))
                    Text("${s.kind.displayName} · ${s.genre}" + (s.releaseYear?.let { " · $it" } ?: ""),
                        color = palette.inkSoft)
                    Spacer(Modifier.height(20.dp))
                    Text(s.synopsis, fontSize = 17.sp, lineHeight = 26.sp, color = palette.ink)
                    Spacer(Modifier.height(24.dp))

                    if (totalEndings > 0) {
                        Text("$discoveredEndings of $totalEndings endings discovered",
                            fontSize = 13.sp, color = palette.inkSoft)
                        Spacer(Modifier.height(12.dp))
                    }

                    if (resume != null) {
                        SketchPrimaryButton(
                            text = "Resume" + (resume.sceneTitle?.let { " · $it" } ?: ""),
                            onClick = { onResume(resume.nodeId) },
                            modifier = Modifier.fillMaxWidth(),
                        )
                        Spacer(Modifier.height(10.dp))
                        SketchSecondaryButton(
                            text = "Start over",
                            onClick = {
                                app.progress.clear(storyId)
                                onBegin()
                            },
                            modifier = Modifier.fillMaxWidth(),
                        )
                    } else {
                        SketchPrimaryButton(text = "Begin", onClick = onBegin, modifier = Modifier.fillMaxWidth())
                    }

                    Spacer(Modifier.height(10.dp))
                    if (discoveredEndings > 0) {
                        SketchSecondaryButton(text = "See endings ($discoveredEndings)",
                            onClick = onSeeEndings, modifier = Modifier.fillMaxWidth())
                    }
                }
            }
        }
    }
}
