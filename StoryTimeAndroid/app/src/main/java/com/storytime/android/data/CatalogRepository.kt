package com.storytime.android.data

import android.content.Context
import com.storytime.android.app
import com.storytime.android.model.CatalogIndex
import com.storytime.android.model.CatalogIndexEntry
import com.storytime.android.model.CatalogStory
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import kotlinx.serialization.json.Json

object CatalogRepository {

    private val json = Json {
        ignoreUnknownKeys = true
        coerceInputValues = true
    }

    private const val CATALOG_DIR = "Catalog"

    suspend fun loadIndex(context: Context, includePersonal: Boolean = true): List<CatalogIndexEntry> = withContext(Dispatchers.IO) {
        val text = context.assets.open("$CATALOG_DIR/index.json").bufferedReader().use { it.readText() }
        val bundled = json.decodeFromString<CatalogIndex>(text).stories
        if (!includePersonal) return@withContext bundled

        val personal = runCatching { app.personal.stories.value }.getOrDefault(emptyList())
        if (personal.isEmpty()) return@withContext bundled

        val personalEntries = personal.map { s ->
            CatalogIndexEntry(
                id = s.id, title = s.title, sourceTitle = s.sourceTitle,
                kind = s.kind, synopsis = s.synopsis, releaseYear = s.releaseYear,
                addedAt = s.addedAt, genre = s.genre, tags = s.tags,
                rating = s.rating, loved = s.loved, nextStoryId = s.nextStoryId,
                storyURL = "__personal__/${s.id}.json",
            )
        }
        personalEntries + bundled
    }

    suspend fun loadStory(context: Context, entry: CatalogIndexEntry): CatalogStory = withContext(Dispatchers.IO) {
        if (entry.storyURL?.startsWith("__personal__/") == true) {
            return@withContext app.personal.story(entry.id)
                ?: error("Personal story ${entry.id} not found")
        }
        val file = entry.storyURL ?: "${entry.id}.json"
        val text = context.assets.open("$CATALOG_DIR/$file").bufferedReader().use { it.readText() }
        json.decodeFromString<CatalogStory>(text)
    }

    suspend fun loadStoryById(context: Context, id: String): CatalogStory? = withContext(Dispatchers.IO) {
        app.personal.story(id)?.let { return@withContext it }
        val index = loadIndex(context, includePersonal = false)
        val entry = index.firstOrNull { it.id == id } ?: return@withContext null
        loadStory(context, entry)
    }
}
