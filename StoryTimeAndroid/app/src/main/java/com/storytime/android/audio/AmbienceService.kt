package com.storytime.android.audio

import android.content.Context
import android.media.MediaPlayer
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow

class AmbienceService(private val context: Context) {
    private var player: MediaPlayer? = null
    private val _isPlaying = MutableStateFlow(false)
    val isPlaying: StateFlow<Boolean> = _isPlaying

    fun play(genre: String, volume: Float = 0.25f) {
        val name = assetName(genre)
        val resId = context.resources.getIdentifier(name, "raw", context.packageName)
        if (resId == 0) {
            // No bundled track for this genre — silent success.
            stop()
            return
        }
        runCatching {
            player?.release()
            val p = MediaPlayer.create(context, resId)
            p.isLooping = true
            p.setVolume(volume, volume)
            p.start()
            player = p
            _isPlaying.value = true
        }.onFailure { _isPlaying.value = false }
    }

    fun stop() {
        runCatching { player?.stop(); player?.release() }
        player = null
        _isPlaying.value = false
    }

    fun setVolume(v: Float) {
        val c = v.coerceIn(0f, 1f)
        player?.setVolume(c, c)
    }

    private fun assetName(genre: String): String = "ambience_" + when (genre.lowercase()) {
        "sci-fi", "scifi" -> "scifi"
        else -> genre.lowercase().replace("[^a-z]".toRegex(), "")
    }
}
