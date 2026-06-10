package com.storytime.android.ui.theme

import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.Box
import androidx.compose.foundation.layout.PaddingValues
import androidx.compose.foundation.layout.padding
import androidx.compose.foundation.layout.size
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.material3.Text
import androidx.compose.runtime.Composable
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.text.font.FontWeight
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp

@Composable
fun PageBackground(modifier: Modifier = Modifier, content: @Composable () -> Unit) {
    val p = LocalStPalette.current
    Box(modifier.background(p.paper)) { content() }
}

@Composable
fun SketchCard(
    modifier: Modifier = Modifier,
    onClick: (() -> Unit)? = null,
    padding: PaddingValues = PaddingValues(14.dp),
    content: @Composable () -> Unit,
) {
    val p = LocalStPalette.current
    val shape = RoundedCornerShape(14.dp)
    val base = modifier
        .clip(shape)
        .background(p.butter, shape)
        .border(1.5.dp, p.ink, shape)
        .let { if (onClick != null) it.clickable(onClick = onClick) else it }
        .padding(padding)
    Box(base) { content() }
}

@Composable
fun SketchChip(
    label: String,
    selected: Boolean,
    onClick: () -> Unit,
    modifier: Modifier = Modifier,
    doodle: String? = null,
) {
    val p = LocalStPalette.current
    val shape = RoundedCornerShape(99.dp)
    val bg = if (selected) p.ink else Color.Transparent
    val fg = if (selected) p.paper else p.ink
    Box(
        modifier
            .clip(shape)
            .background(bg, shape)
            .border(1.5.dp, p.ink, shape)
            .clickable(onClick = onClick)
            .padding(horizontal = 14.dp, vertical = 6.dp),
        contentAlignment = Alignment.Center,
    ) {
        androidx.compose.foundation.layout.Row(
            verticalAlignment = Alignment.CenterVertically,
            horizontalArrangement = androidx.compose.foundation.layout.Arrangement.spacedBy(6.dp),
        ) {
            if (doodle != null) {
                DoodleIcon(
                    name = doodle,
                    modifier = Modifier.size(14.dp),
                    tint = androidx.compose.ui.graphics.ColorFilter.tint(fg),
                )
            }
            Text(label, color = fg, fontSize = 13.sp, fontWeight = FontWeight.SemiBold)
        }
    }
}

@Composable
fun SketchPrimaryButton(
    text: String,
    onClick: () -> Unit,
    modifier: Modifier = Modifier,
    enabled: Boolean = true,
) {
    val p = LocalStPalette.current
    val shape = RoundedCornerShape(14.dp)
    Box(
        modifier
            .clip(shape)
            .background(if (enabled) p.ink else p.inkHair, shape)
            .border(1.5.dp, p.ink, shape)
            .clickable(enabled = enabled, onClick = onClick)
            .padding(horizontal = 22.dp, vertical = 14.dp),
        contentAlignment = Alignment.Center,
    ) {
        Text(text, color = p.paper, fontSize = 16.sp, fontWeight = FontWeight.SemiBold)
    }
}

@Composable
fun SketchSecondaryButton(
    text: String,
    onClick: () -> Unit,
    modifier: Modifier = Modifier,
) {
    val p = LocalStPalette.current
    val shape = RoundedCornerShape(14.dp)
    Box(
        modifier
            .clip(shape)
            .background(Color.Transparent, shape)
            .border(1.5.dp, p.ink, shape)
            .clickable(onClick = onClick)
            .padding(horizontal = 18.dp, vertical = 12.dp),
        contentAlignment = Alignment.Center,
    ) {
        Text(text, color = p.ink, fontSize = 15.sp, fontWeight = FontWeight.Medium)
    }
}
