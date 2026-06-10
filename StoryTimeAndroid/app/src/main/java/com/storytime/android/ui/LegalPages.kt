package com.storytime.android.ui

import androidx.compose.foundation.layout.*
import androidx.compose.foundation.rememberScrollState
import androidx.compose.foundation.verticalScroll
import androidx.compose.material3.Text
import androidx.compose.material3.TextButton
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import com.storytime.android.ui.theme.LocalStPalette
import com.storytime.android.ui.theme.PageBackground

enum class LegalPage(val title: String) {
    Privacy("Privacy"),
    Terms("Terms"),
    About("About"),
}

@Composable
fun LegalPageScreen(page: LegalPage, onBack: () -> Unit) {
    val palette = LocalStPalette.current
    PageBackground(Modifier.fillMaxSize()) {
        Column(Modifier.fillMaxSize().padding(20.dp).verticalScroll(rememberScrollState())) {
            TextButton(onClick = onBack) { Text("← Back", color = palette.ink) }
            Text(page.title, fontSize = 32.sp, fontWeight = FontWeight.Black, color = palette.ink)
            Spacer(Modifier.height(16.dp))
            Body(page)
            Spacer(Modifier.height(48.dp))
        }
    }
}

@Composable
private fun Body(page: LegalPage) {
    val palette = LocalStPalette.current
    val text = when (page) {
        LegalPage.Privacy -> """
            StoryTime stores everything on your device.

            • Reading progress, favorites, endings, Choice DNA and stats all live in local SharedPreferences and app files. We don't sync them.
            • Your Anthropic API key is stored in EncryptedSharedPreferences on this device and is only ever sent to api.anthropic.com when you tap Generate.
            • The catalog ships bundled with the app — no network call is made to load a story.
            • We don't run analytics, ad SDKs or crash reporting. There is no account, no email, no user id.
            • Daily reminder notifications, when enabled, are scheduled by the OS via AlarmManager and only display locally.

            Resetting reading data in Settings wipes progress, endings, DNA, stats and favorites from this device. Personal stories you generated are kept in a file under the app's private storage — uninstalling the app removes them.
        """.trimIndent()
        LegalPage.Terms -> """
            StoryTime is provided as-is, for personal entertainment.

            • The bundled stories are short interactive scenes inspired by the listed films, shows and books. They are commentary / fan fiction and not endorsed by the original rights holders.
            • You're responsible for any Anthropic API usage you incur with your own key. The in-app daily cap is a soft safety net; it doesn't replace your own budget alerts.
            • Don't generate stories that violate Anthropic's usage policies or any applicable law. Generated content may be inaccurate or offensive — review before sharing.
            • The app is offered without warranty. The maintainers aren't liable for lost progress, missed reminders, or how a story makes you feel.
        """.trimIndent()
        LegalPage.About -> """
            StoryTime — interactive stories that remember your choices.

            • Android port of the iOS StoryTime 2.0 app.
            • Built with Kotlin and Jetpack Compose.
            • Story catalog: 175 hand-curated CYOA scenes from films, shows and books.
            • Optional Claude-powered generator for your own stories.

            Thank you for reading.
        """.trimIndent()
    }
    Text(text, fontSize = 15.sp, lineHeight = 22.sp, color = palette.ink)
}
