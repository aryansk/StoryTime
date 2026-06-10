package com.storytime.android.data

import android.content.Context
import com.storytime.android.model.CatalogStory
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.serialization.builtins.ListSerializer
import kotlinx.serialization.json.Json
import java.io.File
import kotlin.random.Random

class PersonalStoriesStore(context: Context) {
    private val file: File = File(context.filesDir, "personal-stories.json")
    private val json = Json { ignoreUnknownKeys = true; prettyPrint = true }
    private val serializer = ListSerializer(CatalogStory.serializer())

    private val _stories = MutableStateFlow(load())
    val stories: StateFlow<List<CatalogStory>> = _stories

    fun add(story: CatalogStory) {
        val deduped = _stories.value.filterNot { it.id == story.id }
        commit(listOf(story) + deduped)
    }

    fun remove(id: String) {
        commit(_stories.value.filterNot { it.id == id })
    }

    fun story(id: String): CatalogStory? = _stories.value.firstOrNull { it.id == id }

    private fun commit(list: List<CatalogStory>) {
        _stories.value = list
        runCatching { file.writeText(json.encodeToString(serializer, list)) }
    }

    private fun load(): List<CatalogStory> {
        if (!file.exists()) return emptyList()
        return runCatching { json.decodeFromString(serializer, file.readText()) }.getOrDefault(emptyList())
    }

    companion object {
        fun makeId(title: String): String {
            val slug = title.lowercase()
                .split(Regex("[^a-z0-9]+"))
                .filter { it.isNotEmpty() }
                .joinToString("-")
                .take(40)
                .ifEmpty { "story" }
            return "user-$slug-${Random.nextInt(1000, 10000)}"
        }
    }
}
