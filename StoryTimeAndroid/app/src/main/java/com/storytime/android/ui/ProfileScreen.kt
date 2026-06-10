package com.storytime.android.ui

import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.runtime.collectAsState
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.storytime.android.app
import com.storytime.android.ui.theme.LocalStPalette
import com.storytime.android.ui.theme.PageBackground
import com.storytime.android.ui.theme.SketchCard

@Composable
fun ProfileScreen(onSeeEndings: (String) -> Unit) {
    val palette = LocalStPalette.current
    val user by app.user.profile.collectAsState()
    val stats by app.stats.state.collectAsState()
    val dna by app.dna.state.collectAsState()
    val endings by app.endings.discovered.collectAsState()

    PageBackground(Modifier.fillMaxSize()) {
        Column(Modifier.fillMaxSize().padding(20.dp).verticalScroll(rememberScrollState())) {
            Spacer(Modifier.height(8.dp))
            Text(app.user.greeting, fontSize = 16.sp, color = palette.inkSoft)
            Text(user.username.ifEmpty { "Reader" }, fontSize = 32.sp, fontWeight = FontWeight.Black, color = palette.ink)
            Spacer(Modifier.height(20.dp))

            OutlinedTextField(
                value = user.username, onValueChange = { v -> app.user.update { it.copy(username = v) } },
                label = { Text("Display name") }, singleLine = true, modifier = Modifier.fillMaxWidth(),
            )
            Spacer(Modifier.height(20.dp))

            Text("Stats", fontWeight = FontWeight.SemiBold, color = palette.accent)
            Spacer(Modifier.height(6.dp))
            SketchCard(modifier = Modifier.fillMaxWidth()) {
                Column {
                    StatLine("Stories started", stats.storiesStarted.size.toString())
                    StatLine("Scenes read",     stats.scenesRead.toString())
                    StatLine("Choices made",    stats.choicesMade.toString())
                    StatLine("Current streak",  "${stats.currentStreak} day${if (stats.currentStreak == 1) "" else "s"}")
                }
            }

            Spacer(Modifier.height(20.dp))
            Text("Choice DNA", fontWeight = FontWeight.SemiBold, color = palette.accent)
            Spacer(Modifier.height(6.dp))
            SketchCard(modifier = Modifier.fillMaxWidth()) {
                Column {
                    val ranked = app.dna.ranked
                    if (ranked.isEmpty()) {
                        Text("Make a few choices to see your DNA.", color = palette.inkSoft)
                    } else {
                        ranked.forEach { (trait, _) ->
                            Row(verticalAlignment = Alignment.CenterVertically) {
                                Text(trait.display, modifier = Modifier.weight(1f), color = palette.ink, fontWeight = FontWeight.SemiBold)
                                Text("${app.dna.percent(trait)}%", color = palette.inkSoft)
                            }
                            Text(trait.blurb, fontSize = 12.sp, color = palette.inkSoft)
                            Spacer(Modifier.height(6.dp))
                        }
                    }
                }
            }

            Spacer(Modifier.height(20.dp))
            Text("Endings discovered", fontWeight = FontWeight.SemiBold, color = palette.accent)
            Spacer(Modifier.height(6.dp))
            if (endings.isEmpty()) {
                SketchCard(modifier = Modifier.fillMaxWidth()) {
                    Text("Reach an ending to unlock its card.", color = palette.inkSoft)
                }
            } else {
                endings.keys.forEach { storyId ->
                    SketchCard(modifier = Modifier.fillMaxWidth().padding(vertical = 4.dp),
                        onClick = { onSeeEndings(storyId) }) {
                        Text(storyId, color = palette.ink)
                    }
                }
            }
            Spacer(Modifier.height(48.dp))
        }
    }
}

@Composable
private fun StatLine(label: String, value: String) {
    val palette = LocalStPalette.current
    Row(Modifier.fillMaxWidth().padding(vertical = 2.dp), verticalAlignment = Alignment.CenterVertically) {
        Text(label, modifier = Modifier.weight(1f), color = palette.ink)
        Text(value, color = palette.ink, fontWeight = FontWeight.SemiBold)
    }
}
