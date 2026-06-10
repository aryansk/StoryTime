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
 */
@Composable
fun DoodleIcon(name: String, modifier: Modifier = Modifier, tint: ColorFilter? = null) {
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
        else           -> R.drawable.doodle_sparkle
    }
    Image(painter = painterResource(res), contentDescription = name, modifier = modifier, colorFilter = tint)
}
