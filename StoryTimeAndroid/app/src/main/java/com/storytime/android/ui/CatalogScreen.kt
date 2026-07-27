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
import androidx.compose.ui.graphics.ColorFilter
import androidx.compose.ui.platform.LocalContext
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.storytime.android.app
import com.storytime.android.data.CatalogRepository
import com.storytime.android.data.CollectionsCatalog
import com.storytime.android.data.StoryCollection
import com.storytime.android.model.CatalogIndexEntry
import com.storytime.android.ui.theme.DoodleIcon
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
    val profile by app.user.profile.collectAsState()
    val stats by app.stats.state.collectAsState()

    LaunchedEffect(personal) {
        runCatching { CatalogRepository.loadIndex(ctx) }
            .onSuccess { entries = it.sortedByDescending { e -> e.addedAt } }
            .onFailure { error = it.message }
    }

    val genres = remember(entries) {
        listOf("All") + entries.map { it.genre }.distinct().sorted()
    }
    // Precompute the "new this week" ids once per entries change, rather than
    // parsing an OffsetDateTime per row on every recomposition.
    val newIds = remember(entries) {
        entries.filter { isNewThisWeek(it.addedAt) }.map { it.id }.toSet()
    }
    // Memoize filtering so it doesn't re-run on unrelated recompositions.
    val filtered = remember(entries, genre, query, activeCollection) {
        val base = activeCollection?.let { col -> entries.filter(col.matches) } ?: entries
        base.filter { e ->
            (genre == "All" || e.genre == genre) &&
                (query.isBlank() || e.title.contains(query, true) ||
                    e.sourceTitle.contains(query, true) || e.synopsis.contains(query, true) ||
                    e.genre.contains(query, true) || e.kind.displayName.contains(query, true) ||
                    e.tags.any { it.contains(query, true) })
        }
    }

    val tonightPick = remember(entries, profile.goal, profile.experienceLevel, stats.storiesStarted) {
        val day = java.time.LocalDate.now().dayOfYear
        entries.maxByOrNull { entry ->
            var score = (entry.rating ?: 3) * 4 + if (entry.loved == true) 6 else 0
            if (entry.id !in stats.storiesStarted) score += 8
            score += when (profile.goal) {
                "Unwind" -> if (entry.genre in listOf("Comedy", "Drama")) 12 else 0
                "Get Hooked" -> if (entry.genre in listOf("Thriller", "Horror")) 12 else 0
                "Roleplay" -> if (entry.genre in listOf("Fantasy", "Action", "Sci-Fi")) 12 else 0
                "Bedtime" -> if ("mini" in entry.tags) 16 else 0
                else -> 0
            }
            score + Math.floorMod("${entry.id}-$day".hashCode(), 9)
        }
    }

    val resume = remember(progressMap) {
        progressMap.values.sortedByDescending { it.lastUpdated }.take(3)
    }

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

            tonightPick?.let { pick ->
                item {
                    Column {
                        Text("Tonight's pick", fontSize = 14.sp,
                            fontWeight = FontWeight.SemiBold, color = palette.ink)
                        Spacer(Modifier.height(6.dp))
                        SketchCard(modifier = Modifier.fillMaxWidth(), onClick = { onPick(pick.id) }) {
                            Row(verticalAlignment = Alignment.CenterVertically) {
                                BookCoverThumbnail(
                                    title = pick.title,
                                    genre = pick.genre,
                                    modifier = Modifier.width(64.dp).height(84.dp),
                                )
                                Spacer(Modifier.width(14.dp))
                                Column(Modifier.weight(1f)) {
                                    Text(
                                        if (profile.goal.isBlank()) "CURATED FOR TONIGHT"
                                        else "FOR ${profile.goal.uppercase()}",
                                        fontSize = 10.sp, fontWeight = FontWeight.Bold,
                                        color = palette.inkSoft,
                                    )
                                    Text(pick.title, fontSize = 19.sp,
                                        fontWeight = FontWeight.Bold, color = palette.ink)
                                    Text("${pick.kind.displayName} · ${pick.genre}",
                                        fontSize = 12.sp, color = palette.inkSoft)
                                }
                                DoodleIcon(
                                    name = "chevronRight",
                                    modifier = Modifier.size(20.dp),
                                    tint = ColorFilter.tint(palette.ink),
                                )
                            }
                        }
                    }
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
                    placeholder = { Text("Search titles, moods, or tags", color = palette.inkSoft) },
                    singleLine = true,
                    modifier = Modifier.fillMaxWidth(),
                    colors = OutlinedTextFieldDefaults.colors(
                        focusedBorderColor = palette.ink,
                        unfocusedBorderColor = palette.inkHair,
                        focusedTextColor = palette.ink,
                        unfocusedTextColor = palette.ink,
                        cursorColor = palette.ink,
                        focusedContainerColor = Color.Transparent,
                        unfocusedContainerColor = Color.Transparent,
                    ),
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
                error != null -> item { Text("Error: $error", color = palette.accent) }
                entries.isEmpty() -> item {
                    Box(Modifier.fillMaxWidth().padding(top = 40.dp), contentAlignment = Alignment.Center) {
                        CircularProgressIndicator(color = palette.ink)
                    }
                }
                filtered.isEmpty() -> item {
                    Column(
                        modifier = Modifier.fillMaxWidth().padding(top = 48.dp),
                        horizontalAlignment = Alignment.CenterHorizontally,
                    ) {
                        Text("Nothing here yet", fontSize = 18.sp, fontWeight = FontWeight.SemiBold, color = palette.ink)
                        Spacer(Modifier.height(6.dp))
                        Text(
                            if (query.isNotBlank()) "No stories match \"$query.\"" else "Try another genre or collection.",
                            fontSize = 14.sp, color = palette.inkSoft,
                        )
                    }
                }
                else -> items(filtered, key = { it.id }) { entry ->
                    StoryRow(entry, isNew = entry.id in newIds, onClick = { onPick(entry.id) })
                }
            }
            item { Spacer(Modifier.height(40.dp)) }
        }
    }
}

@Composable
private fun StoryRow(entry: CatalogIndexEntry, isNew: Boolean, onClick: () -> Unit) {
    val palette = LocalStPalette.current
    SketchCard(modifier = Modifier.fillMaxWidth(), onClick = onClick) {
        Row(verticalAlignment = Alignment.Top) {
            BookCoverThumbnail(
                title = entry.title,
                genre = entry.genre,
                modifier = Modifier.width(72.dp).height(104.dp),
            )
            Spacer(Modifier.width(12.dp))
            Column(Modifier.weight(1f)) {
                Row(verticalAlignment = Alignment.CenterVertically) {
                    Text(entry.title, fontWeight = FontWeight.SemiBold, fontSize = 18.sp,
                        color = palette.ink, modifier = Modifier.weight(1f))
                    if (entry.loved == true) {
                        DoodleIcon(
                            name = "starFill",
                            modifier = Modifier.size(16.dp),
                            tint = ColorFilter.tint(palette.accent),
                        )
                    }
                    if (isNew) {
                        Spacer(Modifier.width(6.dp))
                        Text("NEW", fontSize = 9.sp, fontWeight = FontWeight.Black, color = palette.accent)
                    }
                }
                Spacer(Modifier.height(2.dp))
                Row(verticalAlignment = Alignment.CenterVertically) {
                    Text(entry.kind.displayName, fontSize = 12.sp, color = palette.inkSoft)
                    Text(" · ${entry.genre}", fontSize = 12.sp, color = palette.inkSoft)
                    entry.releaseYear?.let { Text(" · $it", fontSize = 12.sp, color = palette.inkSoft) }
                    entry.stars?.let { stars ->
                        Spacer(Modifier.width(6.dp))
                        repeat(stars) {
                            DoodleIcon(
                                name = "starFill",
                                modifier = Modifier.size(11.dp),
                                tint = ColorFilter.tint(palette.inkSoft),
                            )
                        }
                    }
                }
                Spacer(Modifier.height(6.dp))
                Text(entry.synopsis, fontSize = 14.sp, color = palette.ink)
            }
        }
    }
}

private val CatalogIndexEntry.stars: Int? get() = rating?.coerceIn(0, 5)

private fun isNewThisWeek(addedAt: String): Boolean = runCatching {
    val instant = java.time.OffsetDateTime.parse(addedAt).toInstant()
    val now = java.time.Instant.now()
    java.time.Duration.between(instant, now).toDays() < 7
}.getOrDefault(false)
