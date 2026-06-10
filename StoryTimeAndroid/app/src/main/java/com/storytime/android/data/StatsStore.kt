package com.storytime.android.data

import android.content.Context
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.Json
import java.util.Calendar
import java.util.concurrent.TimeUnit

@Serializable
data class StatsSnapshot(
    val scenesRead: Int = 0,
    val choicesMade: Int = 0,
    val storiesStarted: Set<String> = emptySet(),
    val lastReadDateMillis: Long? = null,
    val currentStreak: Int = 0,
)

class StatsStore(context: Context) {
    private val prefs = context.getSharedPreferences("readingStats.v1", Context.MODE_PRIVATE)
    private val json = Json { ignoreUnknownKeys = true }

    private val _state = MutableStateFlow(load())
    val state: StateFlow<StatsSnapshot> = _state

    fun recordStoryStarted(title: String) {
        val cur = _state.value
        val started = if (title in cur.storiesStarted) cur.storiesStarted else cur.storiesStarted + title
        commit(bumpStreak(cur.copy(storiesStarted = started)))
    }

    fun recordSceneVisit() = commit(bumpStreak(_state.value.copy(scenesRead = _state.value.scenesRead + 1)))
    fun recordChoice() = commit(_state.value.copy(choicesMade = _state.value.choicesMade + 1))
    fun reset() = commit(StatsSnapshot())

    private fun bumpStreak(s: StatsSnapshot): StatsSnapshot {
        val today = Calendar.getInstance().let {
            it.set(Calendar.HOUR_OF_DAY, 0); it.set(Calendar.MINUTE, 0)
            it.set(Calendar.SECOND, 0); it.set(Calendar.MILLISECOND, 0)
            it.timeInMillis
        }
        val last = s.lastReadDateMillis
        if (last == null) return s.copy(currentStreak = 1, lastReadDateMillis = today)
        val days = TimeUnit.MILLISECONDS.toDays(today - last)
        val streak = when (days) {
            0L -> s.currentStreak
            1L -> s.currentStreak + 1
            else -> 1
        }
        return s.copy(currentStreak = streak, lastReadDateMillis = today)
    }

    private fun commit(s: StatsSnapshot) {
        _state.value = s
        prefs.edit().putString(KEY, json.encodeToString(StatsSnapshot.serializer(), s)).apply()
    }

    private fun load(): StatsSnapshot {
        val raw = prefs.getString(KEY, null) ?: return StatsSnapshot()
        return runCatching { json.decodeFromString(StatsSnapshot.serializer(), raw) }.getOrDefault(StatsSnapshot())
    }

    companion object { private const val KEY = "snap" }
}
