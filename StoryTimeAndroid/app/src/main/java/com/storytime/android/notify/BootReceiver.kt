package com.storytime.android.notify

import android.content.BroadcastReceiver
import android.content.Context
import android.content.Intent
import com.storytime.android.app

class BootReceiver : BroadcastReceiver() {
    override fun onReceive(context: Context, intent: Intent) {
        val s = app.settings.state.value
        if (s.reminderEnabled) {
            ReminderScheduler(context).schedule(s.reminderHour, s.reminderMinute, s.dailyStoryEnabled)
        }
    }
}
