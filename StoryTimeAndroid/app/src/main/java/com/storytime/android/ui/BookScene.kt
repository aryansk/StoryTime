package com.storytime.android.ui

import android.graphics.Color as AndroidColor
import android.webkit.WebView
import android.webkit.WebViewClient
import androidx.compose.foundation.background
import androidx.compose.foundation.border
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.RoundedCornerShape
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.clip
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.graphics.graphicsLayer
import androidx.compose.ui.unit.dp
import androidx.compose.ui.unit.sp
import androidx.compose.ui.viewinterop.AndroidView
import com.storytime.android.model.CatalogStory
import com.storytime.android.ui.theme.LocalStPalette
import org.json.JSONArray
import org.json.JSONObject

@Composable
fun BookSceneView(story: CatalogStory, modifier: Modifier = Modifier) {
    val payload = remember(story.id) {
        val minutes = maxOf(2, story.nodes.size)
        val endings = story.nodes.count { it.isEnding }
        val books = JSONArray()
        listOf(
            if (story.sourceTitle == story.title) "A different path" else story.sourceTitle,
            story.title,
            "The next chapter",
        ).forEach { title ->
            books.put(
                JSONObject()
                    .put("title", title)
                    .put("genre", story.genre)
                    .put("minutes", minutes)
                    .put("endings", endings),
            )
        }
        JSONObject().put("books", books).toString()
    }
    var ready by remember { mutableStateOf(false) }

    AndroidView(
        modifier = modifier,
        factory = { context ->
            WebView(context).apply {
                setBackgroundColor(AndroidColor.TRANSPARENT)
                settings.javaScriptEnabled = true
                settings.domStorageEnabled = true
                settings.allowFileAccess = true
                settings.allowContentAccess = true
                isVerticalScrollBarEnabled = false
                isHorizontalScrollBarEnabled = false
                webViewClient = object : WebViewClient() {
                    override fun onPageFinished(view: WebView, url: String) {
                        ready = true
                        view.evaluateJavascript("window.setBookData($payload);", null)
                    }
                }
                loadUrl("file:///android_asset/bookscene.html")
            }
        },
        update = { webView ->
            if (ready) webView.evaluateJavascript("window.setBookData($payload);", null)
        },
    )
}

@Composable
fun BookCoverThumbnail(
    title: String,
    genre: String,
    modifier: Modifier = Modifier,
) {
    val palette = LocalStPalette.current
    val cover = when (genre.lowercase()) {
        "horror" -> Color(0xFF753952)
        "thriller" -> Color(0xFFB34C45)
        "comedy" -> Color(0xFFE99D47)
        "drama" -> Color(0xFF5E7CA7)
        "fantasy" -> Color(0xFF7A66A8)
        "action" -> Color(0xFFC26955)
        "sci-fi" -> Color(0xFF3B93A0)
        else -> palette.ink
    }
    val shape = RoundedCornerShape(7.dp)
    Box(modifier.graphicsLayer(rotationY = -7f)) {
        Box(
            Modifier
                .matchParentSize()
                .offset(x = 5.dp)
                .clip(shape)
                .background(Color(0xFFF6EFDF)),
        )
        Row(
            Modifier
                .fillMaxSize()
                .clip(shape)
                .background(cover)
                .border(1.5.dp, palette.ink, shape),
        ) {
            Box(Modifier.width(8.dp).fillMaxHeight().background(cover.copy(alpha = .78f)))
            Column(Modifier.fillMaxSize().padding(10.dp), verticalArrangement = Arrangement.SpaceBetween) {
                androidx.compose.material3.Text("STORYTIME", color = palette.paper, fontSize = 9.sp)
                androidx.compose.material3.Text(
                    title,
                    color = palette.paper,
                    fontSize = 14.sp,
                    lineHeight = 16.sp,
                    maxLines = 4,
                )
                androidx.compose.material3.Text(genre.uppercase(), color = palette.paper.copy(alpha = .82f), fontSize = 9.sp)
            }
        }
    }
}
