package com.storytime.android.audio

import android.content.Context
import android.speech.tts.TextToSpeech
import android.speech.tts.UtteranceProgressListener
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import java.util.Locale
import java.util.UUID

class SpeechService(context: Context) {
    private val _isSpeaking = MutableStateFlow(false)
    val isSpeaking: StateFlow<Boolean> = _isSpeaking

    private var rate: Float = 1.0f
    private var ready = false
    private val tts = TextToSpeech(context.applicationContext) { status ->
        ready = status == TextToSpeech.SUCCESS
        if (ready) {
            tts?.language = Locale.getDefault()
            tts?.setOnUtteranceProgressListener(object : UtteranceProgressListener() {
                override fun onStart(utteranceId: String?) { _isSpeaking.value = true }
                override fun onDone(utteranceId: String?) { _isSpeaking.value = false }
                @Deprecated("Deprecated in Java")
                override fun onError(utteranceId: String?) { _isSpeaking.value = false }
            })
        }
    }

    fun setRate(value: Float) {
        rate = value.coerceIn(0.5f, 2.0f)
        if (ready) tts.setSpeechRate(rate)
    }

    fun speak(text: String) {
        if (!ready) return
        tts.setSpeechRate(rate)
        tts.speak(text, TextToSpeech.QUEUE_FLUSH, null, UUID.randomUUID().toString())
    }

    fun stop() {
        if (ready) tts.stop()
        _isSpeaking.value = false
    }

    fun shutdown() {
        runCatching { tts.shutdown() }
    }
}
