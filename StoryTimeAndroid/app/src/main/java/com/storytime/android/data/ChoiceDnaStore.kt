package com.storytime.android.data

import android.content.Context
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.serialization.Serializable
import kotlinx.serialization.json.Json

enum class ChoiceTrait(val display: String, val keywords: List<String>, val blurb: String) {
    BRAVE("Brave",   listOf("brave", "courage"),                                  "You step toward what scares you."),
    WISE("Wise",     listOf("wise", "wisdom", "patient", "patience", "discipline", "strategic", "smart"), "You read the room before you act."),
    HONOR("Honor",   listOf("honor", "vow", "honour"),                            "You keep the vows you make."),
    CUNNING("Cunning", listOf("cunning", "clever", "trick"),                      "You bend the rules cleverly."),
    HEART("Heart",   listOf("heart", "love", "friend", "care", "kind"),           "You lead with love and friendship."),
    HONEST("Honest", listOf("honest", "truth", "plain", "honesty"),               "You say the true thing aloud."),
    MERCY("Mercy",   listOf("mercy", "spare", "forgive"),                         "You spare what you don't have to."),
    SPIRIT("Spirit", listOf("spirit", "joy", "defiance", "defiant"),              "You refuse to be diminished."),
    QUIET("Quiet",   listOf("quiet", "still", "modest"),                          "You let the moment breathe."),
    COLD("Cold",     listOf("cold", "pride", "anger", "rage"),                    "You hold the line, even chilled."),
}

@Serializable
data class ChoiceDnaSnapshot(val tally: Map<String, Int> = emptyMap(), val totalChoices: Int = 0)

class ChoiceDnaStore(context: Context) {
    private val prefs = context.getSharedPreferences("choiceDNA.v1", Context.MODE_PRIVATE)
    private val json = Json { ignoreUnknownKeys = true }

    private val _state = MutableStateFlow(load())
    val state: StateFlow<ChoiceDnaSnapshot> = _state

    val tally: Map<ChoiceTrait, Int>
        get() = _state.value.tally.mapNotNull { (k, v) -> runCatching { ChoiceTrait.valueOf(k) }.getOrNull()?.let { it to v } }.toMap()

    val totalChoices: Int get() = _state.value.totalChoices

    val ranked: List<Pair<ChoiceTrait, Int>>
        get() = ChoiceTrait.entries
            .map { it to (tally[it] ?: 0) }
            .filter { it.second > 0 }
            .sortedByDescending { it.second }

    fun percent(trait: ChoiceTrait): Int {
        val total = tally.values.sum()
        if (total == 0) return 0
        val v = (tally[trait] ?: 0).toDouble() / total
        return (v * 100).toInt()
    }

    fun record(consequence: String, choiceText: String) {
        val combined = (consequence + " " + choiceText).lowercase()
        val current = _state.value.tally.toMutableMap()
        var matched = false
        for (trait in ChoiceTrait.entries) {
            if (trait.keywords.any { it in combined }) {
                current[trait.name] = (current[trait.name] ?: 0) + 1
                matched = true
            }
        }
        val next = ChoiceDnaSnapshot(current, _state.value.totalChoices + if (matched) 1 else 0)
        commit(next)
    }

    fun reset() = commit(ChoiceDnaSnapshot())

    private fun commit(s: ChoiceDnaSnapshot) {
        _state.value = s
        prefs.edit().putString(KEY, json.encodeToString(ChoiceDnaSnapshot.serializer(), s)).apply()
    }

    private fun load(): ChoiceDnaSnapshot {
        val raw = prefs.getString(KEY, null) ?: return ChoiceDnaSnapshot()
        return runCatching { json.decodeFromString(ChoiceDnaSnapshot.serializer(), raw) }.getOrDefault(ChoiceDnaSnapshot())
    }

    companion object { private const val KEY = "snap" }
}
