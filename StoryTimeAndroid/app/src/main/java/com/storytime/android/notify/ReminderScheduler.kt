package com.storytime.android.notify

import android.app.AlarmManager
import android.app.PendingIntent
import android.content.Context
import android.content.Intent
import com.storytime.android.app
import com.storytime.android.data.CatalogRepository
import kotlinx.coroutines.CoroutineScope
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.launch
import java.util.Calendar

class ReminderScheduler(private val context: Context) {

    fun cancel() {
        val mgr = context.getSystemService(Context.ALARM_SERVICE) as AlarmManager
        mgr.cancel(buildPendingIntent("Time to read", "Your story is waiting."))
    }

    fun schedule(hour: Int, minute: Int, useDailyStory: Boolean) {
        CoroutineScope(Dispatchers.IO).launch {
            val (title, body) = if (useDailyStory) pickDailyStory() else "Time to read" to "Your story is waiting — keep your streak going."
            val mgr = context.getSystemService(Context.ALARM_SERVICE) as AlarmManager
            val pi = buildPendingIntent(title, body)
            val trigger = nextTrigger(hour, minute)
            if (canScheduleExactAlarms(context)) {
                mgr.setExactAndAllowWhileIdle(AlarmManager.RTC_WAKEUP, trigger, pi)
            } else {
                mgr.set(AlarmManager.RTC_WAKEUP, trigger, pi)
            }
        }
    }

    fun rescheduleAfterFire() {
        val s = app.settings.state.value
        if (s.reminderEnabled) schedule(s.reminderHour, s.reminderMinute, s.dailyStoryEnabled)
    }

    private suspend fun pickDailyStory(): Pair<String, String> {
        return runCatching {
            val index = CatalogRepository.loadIndex(context)
            val started = app.progress.entries.value.keys
            val pool = index.filterNot { it.id in started }.ifEmpty { index }
            val pick = pool.random()
            "Tonight's story: ${pick.title}" to pick.synopsis
        }.getOrDefault("Time to read" to "Your story is waiting.")
    }

    private fun buildPendingIntent(title: String, body: String): PendingIntent {
        val intent = Intent(context, ReminderReceiver::class.java).apply {
            putExtra(ReminderReceiver.EXTRA_TITLE, title)
            putExtra(ReminderReceiver.EXTRA_BODY, body)
        }
        return PendingIntent.getBroadcast(
            context, ReminderReceiver.REQUEST_CODE, intent,
            PendingIntent.FLAG_IMMUTABLE or PendingIntent.FLAG_UPDATE_CURRENT,
        )
    }

    private fun nextTrigger(hour: Int, minute: Int): Long {
        val c = Calendar.getInstance().apply {
            set(Calendar.HOUR_OF_DAY, hour)
            set(Calendar.MINUTE, minute)
            set(Calendar.SECOND, 0)
            set(Calendar.MILLISECOND, 0)
        }
        if (c.timeInMillis <= System.currentTimeMillis()) c.add(Calendar.DAY_OF_YEAR, 1)
        return c.timeInMillis
    }
}
