package com.storytime.android.data

import android.content.Context
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import java.util.Calendar

class UserStore(context: Context) {
    private val prefs = context.getSharedPreferences("user.v1", Context.MODE_PRIVATE)

    data class Profile(
        val username: String = "",
        val goal: String = "",
        val experienceLevel: String = "",
        val onboardingCompleted: Boolean = false,
    )

    private val _profile = MutableStateFlow(load())
    val profile: StateFlow<Profile> = _profile

    fun update(block: (Profile) -> Profile) {
        val p = block(_profile.value)
        _profile.value = p
        prefs.edit()
            .putString("name", p.username)
            .putString("goal", p.goal)
            .putString("xp", p.experienceLevel)
            .putBoolean("done", p.onboardingCompleted)
            .apply()
    }

    val isFirstLaunch: Boolean get() = !_profile.value.onboardingCompleted

    val greeting: String
        get() {
            val hour = Calendar.getInstance().get(Calendar.HOUR_OF_DAY)
            return when {
                hour < 12 -> "Good Morning"
                hour < 17 -> "Good Afternoon"
                hour < 21 -> "Good Evening"
                else -> "Good Night"
            }
        }

    private fun load() = Profile(
        username = prefs.getString("name", "") ?: "",
        goal = prefs.getString("goal", "") ?: "",
        experienceLevel = prefs.getString("xp", "") ?: "",
        onboardingCompleted = prefs.getBoolean("done", false),
    )
}
