package com.storytime.android.ui

import androidx.compose.foundation.horizontalScroll
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.LazyRow
import androidx.compose.foundation.lazy.items
import androidx.compose.foundation.rememberScrollState
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.runtime.collectAsState
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.storytime.android.app
import com.storytime.android.data.CatalogRepository
import com.storytime.android.data.CollectionsCatalog
import com.storytime.android.data.StoryCollection
import com.storytime.android.model.CatalogIndexEntry
import com.storytime.android.ui.theme.LocalStPalette
import com.storytime.android.ui.theme.PageBackground
import com.storytime.android.ui.theme.SketchCard
import com.storytime.android.ui.theme.SketchChip

@Composable
fun CatalogScreen(onPick: (String) -> Unit) {
    val ctx = LocalContext.current
    val palette = LocalStPalette.current
    var entries by remember { mutableStateOf<List<CatalogIndexEntry>>(emptyList()) }
    var error by remember { mutableStateOf<String?>(null) }
    var query by remember { mutableStateOf("") }
    var genre by remember { mutableStateOf("All") }
    var activeCollection by remember { mutableStateOf<StoryCollection?>(null) }
    val progressMap by app.progress.entries.collectAsState()
    val personal by app.personal.stories.collectAsState()

    LaunchedEffect(personal) {
        runCatching { CatalogRepository.loadIndex(ctx) }
            .onSuccess { entries = it.sortedByDescending { e -> e.addedAt } }
            .onFailure { error = it.message }
    }

    val genres = remember(entries) {
        listOf("All") + entries.map { it.genre }.distinct().sorted()
    }
    val collectionFiltered = activeCollection?.let { col -> entries.filter(col.matches) } ?: entries
    val filtered = collectionFiltered.filter { e ->
        (genre == "All" || e.genre == genre) &&
            (query.isBlank() || e.title.contains(query, true) || e.tags.any { it.contains(query, true) })
    }

    val resume = progressMap.values.sortedByDescending { it.lastUpdated }.take(3)

    PageBackground(Modifier.fillMaxSize()) {
        LazyColumn(
            modifier = Modifier.fillMaxSize().padding(horizontal = 18.dp),
            verticalArrangement = Arrangement.spacedBy(12.dp),
        ) {
            item {
                Column {
                    Spacer(Modifier.height(18.dp))
                    Text("StoryTime", fontSize = 36.sp, fontWeight = FontWeight.Black, color = palette.ink)
                    Text("Pick a story. Make a choice. Live with it.", fontSize = 14.sp, color = palette.inkSoft)
                }
            }

            if (resume.isNotEmpty()) {
                item {
                    Column {
                        Text("Continue reading", fontSize = 14.sp, fontWeight = FontWeight.SemiBold, color = palette.ink)
                        Spacer(Modifier.height(6.dp))
                        LazyRow(horizontalArrangement = Arrangement.spacedBy(10.dp)) {
                            items(resume, key = { it.storyKey }) { p ->
                                SketchCard(
                                    modifier = Modifier.width(220.dp),
                                    onClick = { onPick(p.storyKey) },
                                ) {
                                    Column {
                                        Text(p.title, fontWeight = FontWeight.SemiBold, color = palette.ink)
                                        p.sceneTitle?.let {
                                            Text("· $it", fontSize = 12.sp, color = palette.inkSoft)
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }

            item {
                OutlinedTextField(
                    value = query,
                    onValueChange = { query = it },
                    placeholder = { Text("Search titles or tags") },
                    singleLine = true,
                    modifier = Modifier.fillMaxWidth(),
                )
            }

            item {
                Column {
                    Text("Collections", fontSize = 14.sp, fontWeight = FontWeight.SemiBold, color = palette.ink)
                    Spacer(Modifier.height(6.dp))
                    Row(
                        modifier = Modifier.fillMaxWidth().horizontalScroll(rememberScrollState()),
                        horizontalArrangement = Arrangement.spacedBy(8.dp),
                    ) {
                        SketchChip(
                            label = "All",
                            selected = activeCollection == null,
                            onClick = { activeCollection = null },
                        )
                        CollectionsCatalog.all.forEach { col ->
                            SketchChip(
                                label = col.title,
                                selected = activeCollection?.id == col.id,
                                onClick = { activeCollection = if (activeCollection?.id == col.id) null else col },
                                doodle = col.doodle,
                            )
                        }
                    }
                }
            }

            item {
                Row(
                    modifier = Modifier.fillMaxWidth().horizontalScroll(rememberScrollState()),
                    horizontalArrangement = Arrangement.spacedBy(8.dp),
                ) {
                    genres.forEach { g ->
                        SketchChip(label = g, selected = genre == g, onClick = { genre = g })
                    }
                }
            }

            when {
                error != null -> item { Text("Error: $error", color = Color.Red) }
                entries.isEmpty() -> item { CircularProgressIndicator() }
                else -> items(filtered, key = { it.id }) { entry ->
                    StoryRow(entry, onClick = { onPick(entry.id) })
                }
            }
            item { Spacer(Modifier.height(40.dp)) }
        }
    }
}

@Composable
private fun StoryRow(entry: CatalogIndexEntry, onClick: () -> Unit) {
    val palette = LocalStPalette.current
    SketchCard(modifier = Modifier.fillMaxWidth(), onClick = onClick) {
        Column {
            Row(verticalAlignment = Alignment.CenterVertically) {
                Text(entry.title, fontWeight = FontWeight.SemiBold, fontSize = 18.sp,
                    color = palette.ink, modifier = Modifier.weight(1f))
                if (entry.loved == true) Text("★", color = palette.accent)
                if (isNewThisWeek(entry.addedAt)) {
                    Spacer(Modifier.width(6.dp))
                    Text("NEW", fontSize = 9.sp, fontWeight = FontWeight.Black, color = palette.accent)
                }
            }
            Spacer(Modifier.height(2.dp))
            Row {
                Text(entry.kind.displayName, fontSize = 12.sp, color = palette.inkSoft)
                Text(" · ${entry.genre}", fontSize = 12.sp, color = palette.inkSoft)
                entry.releaseYear?.let { Text(" · $it", fontSize = 12.sp, color = palette.inkSoft) }
                entry.stars?.let { Text(" · ${"★".repeat(it)}", fontSize = 12.sp, color = palette.inkSoft) }
            }
            Spacer(Modifier.height(6.dp))
            Text(entry.synopsis, fontSize = 14.sp, color = palette.ink)
        }
    }
}

private val CatalogIndexEntry.stars: Int? get() = rating?.coerceIn(0, 5)

private fun isNewThisWeek(addedAt: String): Boolean = runCatching {
    val instant = java.time.OffsetDateTime.parse(addedAt).toInstant()
    val now = java.time.Instant.now()
    java.time.Duration.between(instant, now).toDays() < 7
}.getOrDefault(false)
