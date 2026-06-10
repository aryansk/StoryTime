package com.storytime.android

import android.app.Application
import android.app.NotificationChannel
import android.app.NotificationManager
import com.storytime.android.audio.AmbienceService
import com.storytime.android.audio.SpeechService
import com.storytime.android.data.ChoiceDnaStore
import com.storytime.android.data.CollectionsCatalog
import com.storytime.android.data.EndingsStore
import com.storytime.android.data.FavoritesStore
import com.storytime.android.data.PersonalStoriesStore
import com.storytime.android.data.ProgressStore
import com.storytime.android.data.SecretStore
import com.storytime.android.data.SettingsStore
import com.storytime.android.data.StatsStore
import com.storytime.android.data.UserStore
import com.storytime.android.notify.ReminderScheduler

class StoryTimeApp : Application() {

    lateinit var progress: ProgressStore
    lateinit var endings: EndingsStore
    lateinit var favorites: FavoritesStore
    lateinit var dna: ChoiceDnaStore
    lateinit var stats: StatsStore
    lateinit var personal: PersonalStoriesStore
    lateinit var settings: SettingsStore
    lateinit var user: UserStore
    lateinit var secrets: SecretStore
    lateinit var ambience: AmbienceService
    lateinit var speech: SpeechService
    lateinit var reminders: ReminderScheduler

    override fun onCreate() {
        super.onCreate()
        instance = this

        progress = ProgressStore(this)
        endings = EndingsStore(this)
        favorites = FavoritesStore(this)
        dna = ChoiceDnaStore(this)
        stats = StatsStore(this)
        personal = PersonalStoriesStore(this)
        settings = SettingsStore(this)
        user = UserStore(this)
        secrets = SecretStore(this)
        ambience = AmbienceService(this)
        speech = SpeechService(this).also { it.setRate(settings.state.value.narrationRate) }
        reminders = ReminderScheduler(this)

        ensureChannel()
    }

    private fun ensureChannel() {
        val mgr = getSystemService(NOTIFICATION_SERVICE) as NotificationManager
        val channel = NotificationChannel(
            REMINDER_CHANNEL,
            "Daily Story",
            NotificationManager.IMPORTANCE_DEFAULT,
        ).apply { description = "Tonight's pick from your catalog" }
        mgr.createNotificationChannel(channel)
    }

    companion object {
        const val REMINDER_CHANNEL = "storytime.reminder"
        lateinit var instance: StoryTimeApp
            private set
    }
}

// Convenience accessor for Compose code.
val app: StoryTimeApp get() = StoryTimeApp.instance
