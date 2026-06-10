package com.storytime.android.ui

import androidx.compose.foundation.horizontalScroll
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.runtime.collectAsState
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.storytime.android.ai.AnthropicClient
import com.storytime.android.app
import com.storytime.android.data.SecretStore
import com.storytime.android.model.StoryKind
import com.storytime.android.ui.theme.LocalStPalette
import com.storytime.android.ui.theme.PageBackground
import com.storytime.android.ui.theme.SketchChip
import com.storytime.android.ui.theme.SketchPrimaryButton
import kotlinx.coroutines.launch

@Composable
fun CreateStoryScreen(onCreated: (String) -> Unit) {
    val palette = LocalStPalette.current
    val scope = rememberCoroutineScope()
    val settings by app.settings.state.collectAsState()

    var title by remember { mutableStateOf("") }
    var premise by remember { mutableStateOf("") }
    var kind by remember { mutableStateOf(StoryKind.MOVIE) }
    var genre by remember { mutableStateOf("Drama") }
    var working by remember { mutableStateOf(false) }
    var error by remember { mutableStateOf<String?>(null) }
    val genres = listOf("Drama", "Comedy", "Thriller", "Sci-Fi", "Horror", "Fantasy", "Action")

    PageBackground(Modifier.fillMaxSize()) {
        Column(Modifier.fillMaxSize().padding(20.dp).verticalScroll(rememberScrollState())) {
            Spacer(Modifier.height(8.dp))
            Text("Create a story", fontSize = 32.sp, fontWeight = FontWeight.Black, color = palette.ink)
            Text("Generate a personal CYOA with Claude.", fontSize = 14.sp, color = palette.inkSoft)
            Spacer(Modifier.height(20.dp))

            OutlinedTextField(
                value = title, onValueChange = { title = it },
                label = { Text("Title (e.g. \"Dune: Part Three\")") }, singleLine = true,
                modifier = Modifier.fillMaxWidth(),
            )
            Spacer(Modifier.height(8.dp))
            OutlinedTextField(
                value = premise, onValueChange = { premise = it },
                label = { Text("Premise (optional)") }, modifier = Modifier.fillMaxWidth(),
                minLines = 3, maxLines = 5,
            )
            Spacer(Modifier.height(12.dp))

            Text("Kind", fontSize = 13.sp, color = palette.inkSoft)
            Row(
                Modifier.fillMaxWidth().horizontalScroll(rememberScrollState()),
                horizontalArrangement = Arrangement.spacedBy(8.dp),
            ) {
                StoryKind.entries.forEach { k ->
                    SketchChip(label = k.displayName, selected = kind == k, onClick = { kind = k })
                }
            }
            Spacer(Modifier.height(12.dp))
            Text("Genre", fontSize = 13.sp, color = palette.inkSoft)
            Row(
                Modifier.fillMaxWidth().horizontalScroll(rememberScrollState()),
                horizontalArrangement = Arrangement.spacedBy(8.dp),
            ) {
                genres.forEach { g ->
                    SketchChip(label = g, selected = genre == g, onClick = { genre = g })
                }
            }
            Spacer(Modifier.height(20.dp))

            Text("Remaining today: ${app.settings.aiGenerationsRemaining}",
                fontSize = 12.sp, color = palette.inkSoft)
            Spacer(Modifier.height(10.dp))

            error?.let {
                Text(it, color = Color.Red, fontSize = 13.sp)
                Spacer(Modifier.height(8.dp))
            }

            if (working) {
                Row { CircularProgressIndicator(); Spacer(Modifier.width(12.dp)); Text("Writing your story…", color = palette.ink) }
            } else {
                SketchPrimaryButton(
                    text = "Generate",
                    enabled = title.isNotBlank(),
                    modifier = Modifier.fillMaxWidth(),
                    onClick = onClick@{
                        error = null
                        val key = app.secrets.get(SecretStore.Keys.ANTHROPIC).orEmpty()
                        if (key.isBlank()) {
                            error = "Add an Anthropic API key in Settings first."
                            return@onClick
                        }
                        if (!app.settings.recordAiGeneration()) {
                            error = "Daily limit reached. Try again tomorrow."
                            return@onClick
                        }
                        working = true
                        scope.launch {
                            runCatching { AnthropicClient(key).generateStory(title, premise, kind, genre) }
                                .onSuccess { story ->
                                    app.personal.add(story)
                                    working = false
                                    onCreated(story.id)
                                }
                                .onFailure {
                                    error = it.message ?: "Failed."
                                    working = false
                                }
                        }
                    },
                )
            }
            Spacer(Modifier.height(40.dp))
        }
    }
}
