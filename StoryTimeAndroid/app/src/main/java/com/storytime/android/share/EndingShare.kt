package com.storytime.android.share

import android.content.Context
import android.content.Intent
import android.graphics.Bitmap
import android.graphics.Canvas
import android.graphics.Color
import android.graphics.Paint
import android.graphics.RectF
import android.graphics.Typeface
import androidx.core.content.FileProvider
import java.io.File
import java.io.FileOutputStream

object EndingShare {

    fun share(context: Context, storyTitle: String, endingTitle: String) {
        val bitmap = render(storyTitle, endingTitle)
        val dir = File(context.cacheDir, "shared").apply { mkdirs() }
        val file = File(dir, "ending-${System.currentTimeMillis()}.png")
        FileOutputStream(file).use { bitmap.compress(Bitmap.CompressFormat.PNG, 100, it) }

        val uri = FileProvider.getUriForFile(context, "${context.packageName}.fileprovider", file)
        val intent = Intent(Intent.ACTION_SEND).apply {
            type = "image/png"
            putExtra(Intent.EXTRA_STREAM, uri)
            putExtra(Intent.EXTRA_TEXT, "Reached \"$endingTitle\" in $storyTitle on StoryTime.")
            addFlags(Intent.FLAG_GRANT_READ_URI_PERMISSION)
        }
        context.startActivity(Intent.createChooser(intent, "Share ending").apply {
            addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
        })
    }

    private fun render(storyTitle: String, endingTitle: String): Bitmap {
        val w = 1080; val h = 1350
        val bm = Bitmap.createBitmap(w, h, Bitmap.Config.ARGB_8888)
        val c = Canvas(bm)
        val paper = Color.rgb(254, 248, 217)
        val ink = Color.rgb(26, 39, 68)
        val accent = Color.rgb(201, 162, 39)
        c.drawColor(paper)

        val border = Paint().apply { color = ink; style = Paint.Style.STROKE; strokeWidth = 8f; isAntiAlias = true }
        c.drawRoundRect(RectF(48f, 48f, w - 48f, h - 48f), 36f, 36f, border)

        val brand = Paint().apply {
            color = accent; isAntiAlias = true
            typeface = Typeface.create(Typeface.SANS_SERIF, Typeface.BOLD)
            textSize = 36f
        }
        c.drawText("STORYTIME", 96f, 140f, brand)

        val label = Paint().apply {
            color = ink; isAntiAlias = true; typeface = Typeface.SANS_SERIF
            textSize = 32f
        }
        c.drawText("ENDING REACHED", 96f, h / 2f - 200f, label)

        val title = Paint().apply {
            color = ink; isAntiAlias = true
            typeface = Typeface.create(Typeface.SERIF, Typeface.BOLD)
            textSize = 96f
        }
        drawWrapped(c, endingTitle, 96f, h / 2f - 120f, w - 192f, title, lineHeight = 110f)

        val sub = Paint().apply {
            color = ink; isAntiAlias = true
            typeface = Typeface.create(Typeface.SERIF, Typeface.NORMAL)
            textSize = 44f
        }
        drawWrapped(c, "in $storyTitle", 96f, h - 220f, w - 192f, sub, lineHeight = 56f)
        return bm
    }

    private fun drawWrapped(c: Canvas, text: String, x: Float, y: Float, maxWidth: Float, paint: Paint, lineHeight: Float) {
        val words = text.split(' ')
        var line = StringBuilder()
        var dy = y
        for (w in words) {
            val tentative = if (line.isEmpty()) w else "$line $w"
            if (paint.measureText(tentative) > maxWidth) {
                c.drawText(line.toString(), x, dy, paint)
                dy += lineHeight
                line = StringBuilder(w)
            } else {
                line = StringBuilder(tentative)
            }
        }
        if (line.isNotEmpty()) c.drawText(line.toString(), x, dy, paint)
    }
}
