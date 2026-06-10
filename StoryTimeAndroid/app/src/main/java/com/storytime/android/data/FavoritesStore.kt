package com.storytime.android.data

import android.content.Context
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow

class FavoritesStore(context: Context) {
    private val prefs = context.getSharedPreferences("favoriteStoryTitles.v1", Context.MODE_PRIVATE)
    private val _titles = MutableStateFlow(prefs.getStringSet(KEY, emptySet())!!.toSet())
    val titles: StateFlow<Set<String>> = _titles

    fun isFavorite(title: String) = title in _titles.value

    fun toggle(title: String) {
        val next = _titles.value.toMutableSet()
        if (!next.add(title)) next.remove(title)
        _titles.value = next
        prefs.edit().putStringSet(KEY, next).apply()
    }

    companion object { private const val KEY = "titles" }
}
