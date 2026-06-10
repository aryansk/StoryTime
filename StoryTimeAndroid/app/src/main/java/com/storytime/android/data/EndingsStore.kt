package com.storytime.android.data

import android.content.Context
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.serialization.builtins.ListSerializer
import kotlinx.serialization.builtins.MapSerializer
import kotlinx.serialization.builtins.serializer
import kotlinx.serialization.json.Json

class EndingsStore(context: Context) {
    private val prefs = context.getSharedPreferences("endingsTracker.v1", Context.MODE_PRIVATE)
    private val json = Json { ignoreUnknownKeys = true }
    private val serializer = MapSerializer(String.serializer(), ListSerializer(String.serializer()))

    private val _discovered = MutableStateFlow(load())
    val discovered: StateFlow<Map<String, Set<String>>> = _discovered

    fun reached(storyKey: String): Set<String> = _discovered.value[storyKey].orEmpty()
    fun count(storyKey: String): Int = reached(storyKey).size

    fun record(storyKey: String, endingNodeId: String) {
        val cur = _discovered.value[storyKey].orEmpty()
        if (endingNodeId in cur) return
        val next = _discovered.value.toMutableMap()
        next[storyKey] = cur + endingNodeId
        commit(next)
    }

    fun reset() = commit(emptyMap())

    private fun commit(map: Map<String, Set<String>>) {
        _discovered.value = map
        val plain = map.mapValues { it.value.toList() }
        prefs.edit().putString(KEY, json.encodeToString(serializer, plain)).apply()
    }

    private fun load(): Map<String, Set<String>> {
        val raw = prefs.getString(KEY, null) ?: return emptyMap()
        return runCatching {
            json.decodeFromString(serializer, raw).mapValues { it.value.toSet() }
        }.getOrDefault(emptyMap())
    }

    companion object { private const val KEY = "data" }
}
