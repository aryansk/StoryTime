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
import com.storytime.android.data.SecretStore
import com.storytime.android.data.SettingsStore
import com.storytime.android.notify.NOTIFICATION_PERMISSION
import com.storytime.android.notify.canScheduleExactAlarms
import com.storytime.android.notify.hasNotificationPermission
import com.storytime.android.notify.openExactAlarmSettings
import com.storytime.android.notify.rememberNotificationPermission
import com.storytime.android.ui.theme.LocalStPalette
import com.storytime.android.ui.theme.PageBackground
import com.storytime.android.ui.theme.SketchCard
import com.storytime.android.ui.theme.SketchChip

@Composable
fun SettingsScreen(onLegal: (LegalPage) -> Unit) {
    val palette = LocalStPalette.current
    val ctx = LocalContext.current
    val s by app.settings.state.collectAsState()
    var apiKey by remember { mutableStateOf(app.secrets.get(SecretStore.Keys.ANTHROPIC).orEmpty()) }
    var notifAllowed by remember { mutableStateOf(hasNotificationPermission(ctx)) }
    val askNotif = rememberNotificationPermission { granted ->
        notifAllowed = granted
        if (granted) app.reminders.schedule(s.reminderHour, s.reminderMinute, s.dailyStoryEnabled)
    }

    PageBackground(Modifier.fillMaxSize()) {
        Column(Modifier.fillMaxSize().padding(20.dp).verticalScroll(rememberScrollState())) {
            Spacer(Modifier.height(8.dp))
            Text("Settings", fontSize = 32.sp, fontWeight = FontWeight.Black, color = palette.ink)
            Spacer(Modifier.height(20.dp))

            Section("Reading") {
                LabeledSlider(
                    label = "Text size  (${s.textSize.toInt()})",
                    value = s.textSize,
                    range = SettingsStore.Settings.TEXT_SIZE_RANGE,
                    onValue = { v -> app.settings.update { it.copy(textSize = v) } },
                )
                Spacer(Modifier.height(6.dp))
                Text("Font", fontSize = 13.sp, color = palette.inkSoft)
                Row(Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                    SettingsStore.Settings.FONTS.forEach { f ->
                        SketchChip(label = f, selected = s.fontName == f,
                            onClick = { app.settings.update { it.copy(fontName = f) } })
                    }
                }
                SwitchRow("Typewriter effect", s.typewriterEnabled) { v ->
                    app.settings.update { it.copy(typewriterEnabled = v) }
                }
                if (s.typewriterEnabled) {
                    LabeledSlider(
                        label = "Typing speed (${"%.2f".format(s.typingSpeed)}s)",
                        value = s.typingSpeed, range = 0.01f..0.1f,
                        onValue = { v -> app.settings.update { it.copy(typingSpeed = v) } },
                    )
                }
            }

            Section("Appearance") {
                SwitchRow("Dark mode", s.darkMode) { v -> app.settings.update { it.copy(darkMode = v) } }
                Spacer(Modifier.height(6.dp))
                Text("Paper", fontSize = 13.sp, color = palette.inkSoft)
                Row(Modifier.fillMaxWidth(), horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                    listOf("Yellow" to 0, "Grey" to 1).forEach { (lbl, v) ->
                        SketchChip(label = lbl, selected = s.paperTheme == v,
                            onClick = { app.settings.update { it.copy(paperTheme = v) } })
                    }
                }
            }

            Section("Narration") {
                Text("Reader has a ▶ Listen button that uses Android's built-in text-to-speech.",
                    fontSize = 12.sp, color = palette.inkSoft)
                Spacer(Modifier.height(6.dp))
                LabeledSlider(
                    label = "Speech rate (${"%.1fx".format(s.narrationRate)})",
                    value = s.narrationRate, range = 0.5f..2.0f,
                    onValue = { v ->
                        app.settings.update { it.copy(narrationRate = v) }
                        app.speech.setRate(v)
                    },
                )
            }

            Section("Ambience & Companion") {
                SwitchRow("Loop genre ambience", s.ambienceEnabled) { v ->
                    app.settings.update { it.copy(ambienceEnabled = v) }
                    if (!v) app.ambience.stop()
                }
                SwitchRow("Pass-and-play companion", s.companionEnabled) { v ->
                    app.settings.update { it.copy(companionEnabled = v) }
                }
                if (s.companionEnabled) {
                    OutlinedTextField(
                        value = s.companionA, onValueChange = { v -> app.settings.update { it.copy(companionA = v) } },
                        label = { Text("Player 1 name") }, singleLine = true, modifier = Modifier.fillMaxWidth(),
                    )
                    Spacer(Modifier.height(6.dp))
                    OutlinedTextField(
                        value = s.companionB, onValueChange = { v -> app.settings.update { it.copy(companionB = v) } },
                        label = { Text("Player 2 name") }, singleLine = true, modifier = Modifier.fillMaxWidth(),
                    )
                }
            }

            Section("Reminders") {
                SwitchRow("Daily reminder", s.reminderEnabled) { v ->
                    app.settings.update { it.copy(reminderEnabled = v) }
                    if (v) {
                        if (!notifAllowed) askNotif.launch(NOTIFICATION_PERMISSION)
                        else app.reminders.schedule(s.reminderHour, s.reminderMinute, s.dailyStoryEnabled)
                    } else {
                        app.reminders.cancel()
                    }
                }
                if (s.reminderEnabled) {
                    if (!notifAllowed) {
                        Spacer(Modifier.height(6.dp))
                        Text("Notifications are blocked. Enable them to receive reminders.",
                            fontSize = 12.sp, color = palette.inkSoft)
                        TextButton(onClick = { askNotif.launch(NOTIFICATION_PERMISSION) }) {
                            Text("Request notification permission", color = palette.ink)
                        }
                    }
                    if (!canScheduleExactAlarms(ctx)) {
                        Spacer(Modifier.height(6.dp))
                        Text("Exact alarms are restricted — reminders may fire late.",
                            fontSize = 12.sp, color = palette.inkSoft)
                        TextButton(onClick = { openExactAlarmSettings(ctx) }) {
                            Text("Allow exact alarms", color = palette.ink)
                        }
                    }
                    Row(verticalAlignment = Alignment.CenterVertically, horizontalArrangement = Arrangement.spacedBy(6.dp)) {
                        Text("Time", color = palette.ink)
                        OutlinedTextField(
                            value = s.reminderHour.toString().padStart(2, '0'),
                            onValueChange = { v -> v.toIntOrNull()?.coerceIn(0, 23)?.let { h -> app.settings.update { it.copy(reminderHour = h) } } },
                            singleLine = true, modifier = Modifier.width(72.dp), label = { Text("HH") },
                        )
                        Text(":", color = palette.ink)
                        OutlinedTextField(
                            value = s.reminderMinute.toString().padStart(2, '0'),
                            onValueChange = { v -> v.toIntOrNull()?.coerceIn(0, 59)?.let { m -> app.settings.update { it.copy(reminderMinute = m) } } },
                            singleLine = true, modifier = Modifier.width(72.dp), label = { Text("MM") },
                        )
                    }
                    SwitchRow("Use tonight's pick", s.dailyStoryEnabled) { v ->
                        app.settings.update { it.copy(dailyStoryEnabled = v) }
                        app.reminders.schedule(s.reminderHour, s.reminderMinute, v)
                    }
                }
            }

            Section("AI Generation") {
                Text("Anthropic API key", fontSize = 13.sp, color = palette.inkSoft)
                OutlinedTextField(
                    value = apiKey, onValueChange = {
                        apiKey = it
                        app.secrets.set(SecretStore.Keys.ANTHROPIC, it)
                    },
                    placeholder = { Text("sk-ant-…") },
                    singleLine = true, modifier = Modifier.fillMaxWidth(),
                )
                Spacer(Modifier.height(8.dp))
                Text("Used today: ${s.aiGenerationsToday} / ${SettingsStore.Settings.AI_DAILY_CAP}",
                    fontSize = 12.sp, color = palette.inkSoft)
            }

            Section("Data") {
                TextButton(onClick = {
                    app.progress.entries.value.keys.forEach { app.progress.clear(it) }
                    app.endings.reset()
                    app.dna.reset()
                    app.stats.reset()
                }) { Text("Reset reading data", color = palette.ink) }
            }

            Section("About") {
                TextButton(onClick = { onLegal(LegalPage.About) })   { Text("About StoryTime", color = palette.ink) }
                TextButton(onClick = { onLegal(LegalPage.Privacy) }) { Text("Privacy",          color = palette.ink) }
                TextButton(onClick = { onLegal(LegalPage.Terms) })   { Text("Terms",            color = palette.ink) }
            }

            Spacer(Modifier.height(48.dp))
        }
    }
}

@Composable
private fun Section(title: String, content: @Composable ColumnScope.() -> Unit) {
    val palette = LocalStPalette.current
    Text(title, fontSize = 14.sp, fontWeight = FontWeight.SemiBold, color = palette.accent)
    Spacer(Modifier.height(6.dp))
    SketchCard(modifier = Modifier.fillMaxWidth()) {
        Column(content = content)
    }
    Spacer(Modifier.height(20.dp))
}

@Composable
private fun SwitchRow(label: String, value: Boolean, onChange: (Boolean) -> Unit) {
    val palette = LocalStPalette.current
    Row(Modifier.fillMaxWidth(), verticalAlignment = Alignment.CenterVertically) {
        Text(label, modifier = Modifier.weight(1f), color = palette.ink)
        Switch(checked = value, onCheckedChange = onChange)
    }
}

@Composable
private fun LabeledSlider(label: String, value: Float, range: ClosedFloatingPointRange<Float>, onValue: (Float) -> Unit) {
    val palette = LocalStPalette.current
    Text(label, fontSize = 13.sp, color = palette.inkSoft)
    Slider(value = value, onValueChange = onValue, valueRange = range)
}
