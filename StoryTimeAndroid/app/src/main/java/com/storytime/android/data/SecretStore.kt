package com.storytime.android.data

import android.content.Context
import androidx.security.crypto.EncryptedSharedPreferences
import androidx.security.crypto.MasterKey

class SecretStore(context: Context) {
    private val master = MasterKey.Builder(context)
        .setKeyScheme(MasterKey.KeyScheme.AES256_GCM)
        .build()

    private val prefs = EncryptedSharedPreferences.create(
        context, "secrets.v1", master,
        EncryptedSharedPreferences.PrefKeyEncryptionScheme.AES256_SIV,
        EncryptedSharedPreferences.PrefValueEncryptionScheme.AES256_GCM,
    )

    fun get(key: String): String? = prefs.getString(key, null)?.takeIf { it.isNotEmpty() }

    fun set(key: String, value: String?) {
        if (value.isNullOrEmpty()) prefs.edit().remove(key).apply()
        else prefs.edit().putString(key, value).apply()
    }

    object Keys {
        const val ANTHROPIC = "anthropicAPIKey"
    }
}
