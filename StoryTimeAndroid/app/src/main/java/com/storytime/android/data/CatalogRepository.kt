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

    /// Parsed bundled index, cached after the first read. The asset file
    /// never changes at runtime, so re-reading and re-parsing it on every
    /// navigation (each story open went through here) was pure waste.
    @Volatile private var cachedBundled: List<CatalogIndexEntry>? = null

    /// Parsed bundled stories, cached by asset path. Bundled assets are
    /// immutable at runtime, so re-reading and re-decoding a story's JSON on
    /// every open (and every saga-continue) was needless IO + parse work.
    /// Bounded so we never hold the whole catalog resident. Personal stories
    /// are never cached here — they change.
    private val storyCache = android.util.LruCache<String, CatalogStory>(32)

    private suspend fun bundledIndex(context: Context): List<CatalogIndexEntry> {
        cachedBundled?.let { return it }
        return withContext(Dispatchers.IO) {
            val text = context.assets.open("$CATALOG_DIR/index.json").bufferedReader().use { it.readText() }
            val parsed = json.decodeFromString<CatalogIndex>(text).stories
            cachedBundled = parsed
            parsed
        }
    }

    suspend fun loadIndex(context: Context, includePersonal: Boolean = true): List<CatalogIndexEntry> {
        val bundled = bundledIndex(context)
        if (!includePersonal) return bundled

        val personal = runCatching { app.personal.stories.value }.getOrDefault(emptyList())
        if (personal.isEmpty()) return bundled

        val personalEntries = personal.map { s ->
            CatalogIndexEntry(
                id = s.id, title = s.title, sourceTitle = s.sourceTitle,
                kind = s.kind, synopsis = s.synopsis, releaseYear = s.releaseYear,
                addedAt = s.addedAt, genre = s.genre, tags = s.tags,
                rating = s.rating, loved = s.loved, nextStoryId = s.nextStoryId,
                storyURL = "__personal__/${s.id}.json",
            )
        }
        return personalEntries + bundled
    }

    suspend fun loadStory(context: Context, entry: CatalogIndexEntry): CatalogStory = withContext(Dispatchers.IO) {
        if (entry.storyURL?.startsWith("__personal__/") == true) {
            return@withContext app.personal.story(entry.id)
                ?: error("Personal story ${entry.id} not found")
        }
        val file = entry.storyURL ?: "${entry.id}.json"
        storyCache.get(file)?.let { return@withContext it }
        val text = context.assets.open("$CATALOG_DIR/$file").bufferedReader().use { it.readText() }
        json.decodeFromString<CatalogStory>(text).also { storyCache.put(file, it) }
    }

    suspend fun loadStoryById(context: Context, id: String): CatalogStory? = withContext(Dispatchers.IO) {
        app.personal.story(id)?.let { return@withContext it }
        val index = loadIndex(context, includePersonal = false)
        val entry = index.firstOrNull { it.id == id } ?: return@withContext null
        loadStory(context, entry)
    }
}
