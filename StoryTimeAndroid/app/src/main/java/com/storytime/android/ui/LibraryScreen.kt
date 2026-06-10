package com.storytime.android.ui

import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
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
import com.storytime.android.model.CatalogIndexEntry
import com.storytime.android.ui.theme.LocalStPalette
import com.storytime.android.ui.theme.PageBackground
import com.storytime.android.ui.theme.SketchCard
import com.storytime.android.ui.theme.SketchChip

@Composable
fun LibraryScreen(onPick: (String) -> Unit) {
    val ctx = LocalContext.current
    val palette = LocalStPalette.current
    val progress by app.progress.entries.collectAsState()
    val favorites by app.favorites.titles.collectAsState()
    val endings by app.endings.discovered.collectAsState()
    var all by remember { mutableStateOf<List<CatalogIndexEntry>>(emptyList()) }
    var tab by remember { mutableStateOf(LibTab.InProgress) }

    LaunchedEffect(Unit) {
        runCatching { CatalogRepository.loadIndex(ctx) }.onSuccess { all = it }
    }

    val byId = all.associateBy { it.id }

    PageBackground(Modifier.fillMaxSize()) {
        Column(Modifier.fillMaxSize().padding(horizontal = 18.dp)) {
            Spacer(Modifier.height(16.dp))
            Text("Library", fontSize = 32.sp, fontWeight = FontWeight.Black, color = palette.ink)
            Spacer(Modifier.height(12.dp))
            Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {
                LibTab.entries.forEach { t ->
                    SketchChip(label = t.label, selected = tab == t, onClick = { tab = t })
                }
            }
            Spacer(Modifier.height(12.dp))

            when (tab) {
                LibTab.InProgress -> {
                    val items = progress.values.sortedByDescending { it.lastUpdated }
                    if (items.isEmpty()) EmptyState("Nothing in progress.")
                    else LazyColumn(verticalArrangement = Arrangement.spacedBy(10.dp)) {
                        items(items, key = { it.storyKey }) { p ->
                            SketchCard(modifier = Modifier.fillMaxWidth(), onClick = { onPick(p.storyKey) }) {
                                Column {
                                    Text(p.title, fontWeight = FontWeight.SemiBold, color = palette.ink)
                                    p.sceneTitle?.let { Text("· $it", fontSize = 12.sp, color = palette.inkSoft) }
                                    Text(p.storyDescription, fontSize = 13.sp, color = palette.ink)
                                }
                            }
                        }
                    }
                }
                LibTab.Favorites -> {
                    val items = all.filter { it.title in favorites }
                    if (items.isEmpty()) EmptyState("No favorites yet. Tap ☆ on a story.")
                    else LazyColumn(verticalArrangement = Arrangement.spacedBy(10.dp)) {
                        items(items, key = { it.id }) { e ->
                            SimpleRow(e, onClick = { onPick(e.id) })
                        }
                    }
                }
                LibTab.Finished -> {
                    val items = endings.keys.mapNotNull { byId[it] }
                    if (items.isEmpty()) EmptyState("No endings discovered yet.")
                    else LazyColumn(verticalArrangement = Arrangement.spacedBy(10.dp)) {
                        items(items, key = { it.id }) { e ->
                            val count = endings[e.id]?.size ?: 0
                            SketchCard(modifier = Modifier.fillMaxWidth(), onClick = { onPick(e.id) }) {
                                Column {
                                    Text(e.title, fontWeight = FontWeight.SemiBold, color = palette.ink)
                                    Text("$count endings discovered", fontSize = 12.sp, color = palette.inkSoft)
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}

private enum class LibTab(val label: String) {
    InProgress("In Progress"), Favorites("Favorites"), Finished("Finished")
}

@Composable
private fun SimpleRow(e: CatalogIndexEntry, onClick: () -> Unit) {
    val palette = LocalStPalette.current
    SketchCard(modifier = Modifier.fillMaxWidth(), onClick = onClick) {
        Column {
            Text(e.title, fontWeight = FontWeight.SemiBold, color = palette.ink)
            Text("${e.kind.displayName} · ${e.genre}", fontSize = 12.sp, color = palette.inkSoft)
            Text(e.synopsis, fontSize = 13.sp, color = palette.ink)
        }
    }
}

@Composable
private fun EmptyState(text: String) {
    val palette = LocalStPalette.current
    Box(Modifier.fillMaxSize(), contentAlignment = Alignment.Center) {
        Text(text, color = palette.inkSoft)
    }
}
