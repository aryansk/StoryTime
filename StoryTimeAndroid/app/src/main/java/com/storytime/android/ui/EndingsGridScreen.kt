package com.storytime.android.ui

import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.grid.GridCells
import androidx.compose.foundation.lazy.grid.LazyVerticalGrid
import androidx.compose.foundation.lazy.grid.items
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
import com.storytime.android.ui.theme.SketchCard

@Composable
fun EndingsGridScreen(storyId: String, onBack: () -> Unit) {
    val ctx = LocalContext.current
    val palette = LocalStPalette.current
    val endings by app.endings.discovered.collectAsState()
    var story by remember { mutableStateOf<CatalogStory?>(null) }

    LaunchedEffect(storyId) { story = CatalogRepository.loadStoryById(ctx, storyId) }

    PageBackground(Modifier.fillMaxSize()) {
        Column(Modifier.fillMaxSize().padding(horizontal = 16.dp)) {
            Spacer(Modifier.height(12.dp))
            Row(verticalAlignment = Alignment.CenterVertically) {
                TextButton(onClick = onBack) { Text("← Back", color = palette.ink) }
            }
            Text(story?.title ?: "Endings", fontSize = 28.sp, fontWeight = FontWeight.Black, color = palette.ink)
            val discovered = endings[storyId].orEmpty()
            val endingsList = story?.nodes?.filter { it.isEnding }.orEmpty()
            Text("${discovered.size} of ${endingsList.size} discovered",
                fontSize = 13.sp, color = palette.inkSoft)
            Spacer(Modifier.height(12.dp))

            LazyVerticalGrid(
                columns = GridCells.Fixed(2),
                horizontalArrangement = Arrangement.spacedBy(10.dp),
                verticalArrangement = Arrangement.spacedBy(10.dp),
            ) {
                items(endingsList, key = { it.id }) { e ->
                    val found = e.id in discovered
                    SketchCard(modifier = Modifier.fillMaxWidth().height(120.dp)) {
                        Column {
                            Text(if (found) "ENDING" else "???",
                                fontSize = 11.sp, fontWeight = FontWeight.Black, color = palette.accent)
                            Spacer(Modifier.height(6.dp))
                            Text(
                                if (found) (e.endingTitle ?: "Untitled") else "Undiscovered",
                                fontSize = 14.sp, fontWeight = FontWeight.SemiBold, color = palette.ink,
                            )
                        }
                    }
                }
            }
        }
    }
}
