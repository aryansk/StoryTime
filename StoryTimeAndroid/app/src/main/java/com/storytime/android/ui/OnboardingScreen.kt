package com.storytime.android.ui

import androidx.compose.foundation.layout.*
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
import com.storytime.android.ui.theme.SketchChip
import com.storytime.android.ui.theme.SketchPrimaryButton

@Composable
fun OnboardingScreen(onDone: () -> Unit) {
    val palette = LocalStPalette.current
    val user by app.user.profile.collectAsState()
    var step by remember { mutableStateOf(0) }
    var name by remember { mutableStateOf(user.username) }
    var goal by remember { mutableStateOf(user.goal) }
    var level by remember { mutableStateOf(user.experienceLevel) }

    PageBackground(Modifier.fillMaxSize()) {
        Column(
            Modifier.fillMaxSize().padding(28.dp),
            verticalArrangement = Arrangement.spacedBy(16.dp),
        ) {
            Spacer(Modifier.weight(0.1f))
            Text("StoryTime", fontSize = 40.sp, fontWeight = FontWeight.Black, color = palette.ink)
            Text("Interactive stories that remember your choices.",
                fontSize = 16.sp, color = palette.inkSoft)
            Spacer(Modifier.height(24.dp))

            when (step) {
                0 -> {
                    Text("What should we call you?", fontSize = 18.sp, fontWeight = FontWeight.SemiBold, color = palette.ink)
                    OutlinedTextField(value = name, onValueChange = { name = it },
                        singleLine = true, modifier = Modifier.fillMaxWidth(),
                        placeholder = { Text("Your name") })
                }
                1 -> {
                    Text("Why are you here?", fontSize = 18.sp, fontWeight = FontWeight.SemiBold, color = palette.ink)
                    Column(verticalArrangement = Arrangement.spacedBy(8.dp)) {
                        listOf("Wind down", "Sharpen taste", "Replay favorites", "Discover new").forEach { opt ->
                            SketchChip(label = opt, selected = goal == opt, onClick = { goal = opt })
                        }
                    }
                }
                2 -> {
                    Text("How often do you read fiction?",
                        fontSize = 18.sp, fontWeight = FontWeight.SemiBold, color = palette.ink)
                    Column(verticalArrangement = Arrangement.spacedBy(8.dp)) {
                        listOf("Rarely", "Sometimes", "Often", "Daily").forEach { opt ->
                            SketchChip(label = opt, selected = level == opt, onClick = { level = opt })
                        }
                    }
                }
            }

            Spacer(Modifier.weight(1f))

            Row(horizontalArrangement = Arrangement.spacedBy(10.dp), verticalAlignment = Alignment.CenterVertically) {
                if (step > 0) TextButton(onClick = { step-- }) { Text("Back", color = palette.ink) }
                Spacer(Modifier.weight(1f))
                SketchPrimaryButton(
                    text = if (step < 2) "Next" else "Begin",
                    onClick = {
                        if (step < 2) step++
                        else {
                            app.user.update { it.copy(username = name, goal = goal, experienceLevel = level, onboardingCompleted = true) }
                            onDone()
                        }
                    },
                )
            }
        }
    }
}
