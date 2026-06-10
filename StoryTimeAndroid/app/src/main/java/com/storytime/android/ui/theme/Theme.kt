package com.storytime.android.ui.theme

import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.ColorScheme
import androidx.compose.material3.MaterialTheme
import androidx.compose.material3.darkColorScheme
import androidx.compose.material3.lightColorScheme
import androidx.compose.runtime.Composable
import androidx.compose.runtime.CompositionLocalProvider
import androidx.compose.runtime.staticCompositionLocalOf
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontFamily
import androidx.compose.ui.unit.dp
import com.storytime.android.data.SettingsStore

data class StPalette(
    val paper: Color,
    val ink: Color,
    val inkSoft: Color,
    val inkHair: Color,
    val mist: Color,
    val butter: Color,
    val accent: Color,
)

val LocalStPalette = staticCompositionLocalOf {
    StPalette(
        paper = Color(0xFFFEF8D9),
        ink = Color(0xFF1A2744),
        inkSoft = Color(0xAA1A2744),
        inkHair = Color(0x381A2744),
        mist = Color(0xFFD8DEE8),
        butter = Color(0xFFFEF8D9),
        accent = Color(0xFFC9A227),
    )
}

private fun paperFor(theme: Int, hex: String, dark: Boolean): Color {
    if (dark) return Color(0xFF161A26)
    return when (theme) {
        1 -> Color(0xFFF5F5F5)
        2 -> runCatching {
            val s = hex.trim().removePrefix("#").padEnd(6, '0').take(6)
            Color(("FF$s").toLong(16))
        }.getOrDefault(Color(0xFFFEF8D9))
        else -> Color(0xFFFEF8D9)
    }
}

@Composable
fun StoryTimeTheme(settings: SettingsStore.Settings, content: @Composable () -> Unit) {
    val dark = settings.darkMode
    val paper = paperFor(settings.paperTheme, settings.customPaperHex, dark)
    val palette = if (dark) {
        StPalette(
            paper = paper,
            ink = Color(0xFFECE7D6),
            inkSoft = Color(0xBBECE7D6),
            inkHair = Color(0x42ECE7D6),
            mist = Color(0xFF2B3247),
            butter = Color(0xFF1F2433),
            accent = Color(0xFFE7D6B7),
        )
    } else {
        StPalette(
            paper = paper,
            ink = Color(0xFF1A2744),
            inkSoft = Color(0xAA1A2744),
            inkHair = Color(0x381A2744),
            mist = Color(0xFFD8DEE8),
            butter = paper,
            accent = Color(0xFFC9A227),
        )
    }

    val cs: ColorScheme = if (dark) {
        darkColorScheme(
            primary = palette.accent, secondary = palette.ink,
            background = palette.paper, surface = palette.mist,
            onBackground = palette.ink, onSurface = palette.ink, onPrimary = palette.paper,
        )
    } else {
        lightColorScheme(
            primary = palette.ink, secondary = palette.accent,
            background = palette.paper, surface = palette.butter,
            onBackground = palette.ink, onSurface = palette.ink, onPrimary = palette.paper,
        )
    }

    CompositionLocalProvider(LocalStPalette provides palette) {
        MaterialTheme(
            colorScheme = cs,
            shapes = MaterialTheme.shapes.copy(
                small = RoundedCornerShape(10.dp),
                medium = RoundedCornerShape(14.dp),
                large = RoundedCornerShape(20.dp),
            ),
            content = content,
        )
    }
}

fun readerFontFamily(name: String): FontFamily = when (name) {
    "Sans" -> FontFamily.SansSerif
    "Monospace" -> FontFamily.Monospace
    else -> FontFamily.Serif
}
