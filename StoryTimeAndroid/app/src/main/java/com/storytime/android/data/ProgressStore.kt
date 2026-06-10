package com.storytime.android.data

import android.content.Context
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.serialization.Serializable
import kotlinx.serialization.builtins.MapSerializer as KMapSerializer
import kotlinx.serialization.builtins.serializer
import kotlinx.serialization.json.Json

@Serializable
data class ReadingProgress(
    val storyKey: String,
    val title: String,
    val storyDescription: String,
    val nodeId: String,
    val sceneTitle: String? = null,
    val lastUpdated: Long,
)

class ProgressStore(context: Context) {
    private val prefs = context.getSharedPreferences("readingProgress.v2", Context.MODE_PRIVATE)
    private val json = Json { ignoreUnknownKeys = true }

    private val _entries = MutableStateFlow(load())
    val entries: StateFlow<Map<String, ReadingProgress>> = _entries

    val inProgress: List<ReadingProgress>
        get() = _entries.value.values.sortedByDescending { it.lastUpdated }

    fun progress(storyKey: String): ReadingProgress? = _entries.value[storyKey]

    fun save(storyKey: String, title: String, description: String, nodeId: String, sceneTitle: String? = null) {
        val next = _entries.value.toMutableMap()
        next[storyKey] = ReadingProgress(storyKey, title, description, nodeId, sceneTitle, System.currentTimeMillis())
        commit(next)
    }

    fun clear(storyKey: String) {
        val next = _entries.value.toMutableMap()
        next.remove(storyKey)
        commit(next)
    }

    private fun commit(map: Map<String, ReadingProgress>) {
        _entries.value = map
        prefs.edit().putString(KEY, json.encodeToString(MapSerializer, map)).apply()
    }

    private fun load(): Map<String, ReadingProgress> {
        val raw = prefs.getString(KEY, null) ?: return emptyMap()
        return runCatching { json.decodeFromString(MapSerializer, raw) }.getOrDefault(emptyMap())
    }

    companion object {
        private const val KEY = "entries"
        private val MapSerializer = KMapSerializer(String.serializer(), ReadingProgress.serializer())
    }
}
