package com.storytime.android.ui.theme

import androidx.compose.foundation.Image
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.ColorFilter
import androidx.compose.ui.res.painterResource
import com.storytime.android.R

/**
 * Render the named doodle vector. Names come from [com.storytime.android.data.StoryCollection.doodle];
 * unknown names fall back to the sparkle.
 *
 * Doodles are decorative — they sit beside real text labels or inside labeled
 * buttons — so by default we expose no [contentDescription]. TalkBack was
 * otherwise announcing raw tokens like "starFill" and "xmark" on every icon.
 * Pass an explicit [contentDescription] for the rare icon-only control.
 */
@Composable
fun DoodleIcon(
    name: String,
    modifier: Modifier = Modifier,
    tint: ColorFilter? = null,
    contentDescription: String? = null,
) {
    val res = when (name) {
        "clock"        -> R.drawable.doodle_clock
        "starFill"     -> R.drawable.doodle_starfill
        "tv"           -> R.drawable.doodle_tv
        "sparkle"      -> R.drawable.doodle_sparkle
        "popcorn"      -> R.drawable.doodle_popcorn
        "clapperboard" -> R.drawable.doodle_clapperboard
        "heart"        -> R.drawable.doodle_heart
        "flame"        -> R.drawable.doodle_flame
        "branch"       -> R.drawable.doodle_branch
        "bookmark"     -> R.drawable.doodle_bookmark
        "plus"         -> R.drawable.doodle_plus
        "person"       -> R.drawable.doodle_person
        "gear"         -> R.drawable.doodle_gear
        "xmark"        -> R.drawable.doodle_xmark
        "chevronLeft"  -> R.drawable.doodle_chevron_left
        "speaker"      -> R.drawable.doodle_speaker
        "speakerPlaying" -> R.drawable.doodle_speaker_playing
        else           -> R.drawable.doodle_sparkle
    }
    Image(painter = painterResource(res), contentDescription = contentDescription, modifier = modifier, colorFilter = tint)
}
