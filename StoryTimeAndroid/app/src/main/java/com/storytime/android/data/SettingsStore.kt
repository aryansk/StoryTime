package com.storytime.android.data

import android.content.Context
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import java.util.Calendar

class SettingsStore(context: Context) {
    private val prefs = context.getSharedPreferences("settings.v1", Context.MODE_PRIVATE)

    private val _state = MutableStateFlow(load())
    val state: StateFlow<Settings> = _state

    data class Settings(
        val textSize: Float = 17f,
        val typingSpeed: Float = 0.05f,
        val darkMode: Boolean = false,
        val fontName: String = "Serif",
        val paperTheme: Int = 0,
        val customPaperHex: String = "FFFFFF",
        val typewriterEnabled: Boolean = false,
        val reminderEnabled: Boolean = false,
        val reminderHour: Int = 19,
        val reminderMinute: Int = 0,
        val dailyStoryEnabled: Boolean = false,
        val ambienceEnabled: Boolean = false,
        val companionEnabled: Boolean = false,
        val companionA: String = "Player 1",
        val companionB: String = "Player 2",
        val aiGenerationsToday: Int = 0,
        val aiResetEpochDay: Long = 0,
        val narrationRate: Float = 1.0f,
    ) {
        companion object {
            const val AI_DAILY_CAP = 20
            val FONTS = listOf("Serif", "Sans", "Monospace")
            val TEXT_SIZE_RANGE = 12f..24f
        }
    }

    fun update(block: (Settings) -> Settings) {
        val next = block(_state.value)
        _state.value = next
        prefs.edit()
            .putFloat("textSize", next.textSize)
            .putFloat("typingSpeed", next.typingSpeed)
            .putBoolean("dark", next.darkMode)
            .putString("font", next.fontName)
            .putInt("paperTheme", next.paperTheme)
            .putString("paperHex", next.customPaperHex)
            .putBoolean("typewriter", next.typewriterEnabled)
            .putBoolean("reminder", next.reminderEnabled)
            .putInt("reminderHour", next.reminderHour)
            .putInt("reminderMinute", next.reminderMinute)
            .putBoolean("dailyStory", next.dailyStoryEnabled)
            .putBoolean("ambience", next.ambienceEnabled)
            .putBoolean("companion", next.companionEnabled)
            .putString("companionA", next.companionA)
            .putString("companionB", next.companionB)
            .putInt("aiToday", next.aiGenerationsToday)
            .putLong("aiResetDay", next.aiResetEpochDay)
            .putFloat("narrationRate", next.narrationRate)
            .apply()
    }

    fun recordAiGeneration(): Boolean {
        rolloverIfNeeded()
        val s = _state.value
        if (s.aiGenerationsToday >= Settings.AI_DAILY_CAP) return false
        update { it.copy(aiGenerationsToday = it.aiGenerationsToday + 1) }
        return true
    }

    val aiGenerationsRemaining: Int
        get() {
            rolloverIfNeeded()
            return (Settings.AI_DAILY_CAP - _state.value.aiGenerationsToday).coerceAtLeast(0)
        }

    private fun rolloverIfNeeded() {
        val today = Calendar.getInstance().run {
            set(Calendar.HOUR_OF_DAY, 0); set(Calendar.MINUTE, 0)
            set(Calendar.SECOND, 0); set(Calendar.MILLISECOND, 0)
            timeInMillis / (24L * 60 * 60 * 1000)
        }
        if (_state.value.aiResetEpochDay != today) {
            update { it.copy(aiResetEpochDay = today, aiGenerationsToday = 0) }
        }
    }

    private fun load(): Settings {
        val d = Settings()
        return Settings(
            textSize = prefs.getFloat("textSize", d.textSize),
            typingSpeed = prefs.getFloat("typingSpeed", d.typingSpeed),
            darkMode = prefs.getBoolean("dark", d.darkMode),
            fontName = prefs.getString("font", d.fontName) ?: d.fontName,
            paperTheme = prefs.getInt("paperTheme", d.paperTheme),
            customPaperHex = prefs.getString("paperHex", d.customPaperHex) ?: d.customPaperHex,
            typewriterEnabled = prefs.getBoolean("typewriter", d.typewriterEnabled),
            reminderEnabled = prefs.getBoolean("reminder", d.reminderEnabled),
            reminderHour = prefs.getInt("reminderHour", d.reminderHour),
            reminderMinute = prefs.getInt("reminderMinute", d.reminderMinute),
            dailyStoryEnabled = prefs.getBoolean("dailyStory", d.dailyStoryEnabled),
            ambienceEnabled = prefs.getBoolean("ambience", d.ambienceEnabled),
            companionEnabled = prefs.getBoolean("companion", d.companionEnabled),
            companionA = prefs.getString("companionA", d.companionA) ?: d.companionA,
            companionB = prefs.getString("companionB", d.companionB) ?: d.companionB,
            aiGenerationsToday = prefs.getInt("aiToday", d.aiGenerationsToday),
            aiResetEpochDay = prefs.getLong("aiResetDay", d.aiResetEpochDay),
            narrationRate = prefs.getFloat("narrationRate", d.narrationRate),
        )
    }
}
