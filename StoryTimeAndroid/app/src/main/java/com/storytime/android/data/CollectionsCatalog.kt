package com.storytime.android.data

import com.storytime.android.model.CatalogIndexEntry
import com.storytime.android.model.StoryKind

data class StoryCollection(
    val id: String,
    val title: String,
    val subtitle: String,
    val doodle: String,
    val matches: (CatalogIndexEntry) -> Boolean,
)

object CollectionsCatalog {
    private val cozyIds = setOf(
        "abbott-supply-day", "superstore-closing-shift",
        "young-sheldon-science-fair", "the-intern-day-one",
        "fm-forrest-gump", "fm-lion-king", "fm-wizard-of-oz",
        "fb-pride-prejudice", "fb-hobbit", "more-the-merrier-thanksgiving",
    )
    private val weepy = setOf(
        "the-lost-bus-evacuation", "shrinking-the-honest-week",
        "wuthering-heights-the-moor", "pursuit-happiness-the-internship",
        "fm-forrest-gump", "fm-titanic", "fm-schindlers-list",
        "fm-saving-private-ryan", "fm-et", "fm-lion-king",
        "fb-beloved", "fb-tale-two-cities",
    )
    private val clever = setOf(
        "fb-sherlock-holmes", "fb-and-then-none",
        "wayward-tall-pines", "bodkin-the-podcast",
        "him-and-hers-the-recording", "cabin-10-the-luxury-cruise",
        "the-boys-the-leak", "loot-the-giveaway",
        "fm-pulp-fiction", "fm-the-matrix", "fm-inception",
    )
    private val adapted = setOf(
        "wuthering-heights-the-moor", "fb-hobbit", "fb-lotr",
        "fm-lotr-fotr", "fb-pride-prejudice",
        "fb-1984", "fb-frankenstein", "fb-dracula",
        "fb-jane-eyre", "fb-mockingbird",
        "fb-harry-potter-1", "fb-don-quixote", "fb-and-then-none",
    )

    val all: List<StoryCollection> = listOf(
        StoryCollection("quick",    "Quick Reads", "Five-minute stories", "clock") { "mini" in it.tags },
        StoryCollection("loved",    "Loved",       "Curator favorites",   "starFill") { it.loved == true },
        StoryCollection("books",    "Books",       "Step inside a classic novel", "tv") { it.kind == StoryKind.BOOK },
        StoryCollection("classics", "Classics",    "25 famous movies & 25 famous books", "sparkle") {
            it.id.startsWith("fm-") || it.id.startsWith("fb-")
        },
        StoryCollection("cozy",     "Cozy",        "Warm, gentle, low-stakes", "popcorn") {
            it.id in cozyIds || it.genre.equals("Comedy", true)
        },
        StoryCollection("tense",    "Tense",       "Hold-your-breath stories", "clapperboard") {
            it.genre.equals("Thriller", true) || it.genre.equals("Horror", true)
        },
        StoryCollection("tearjerkers", "Tear-jerkers", "Bring tissues", "heart") { it.id in weepy },
        StoryCollection("epic",     "Epic",        "Big worlds, big stakes", "flame") {
            val g = it.genre
            g.equals("Fantasy", true) || g.equals("Sci-Fi", true) || g.equals("Action", true)
        },
        StoryCollection("clever",   "Clever",      "Twists, deductions, schemes", "branch") { it.id in clever },
        StoryCollection("adapted",  "Book → Screen", "Stories that lived twice", "bookmark") { it.id in adapted },
    )
}
