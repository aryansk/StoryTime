package com.storytime.android.model

import kotlinx.serialization.SerialName
import kotlinx.serialization.Serializable

@Serializable
enum class StoryKind {
    @SerialName("movie") MOVIE,
    @SerialName("show")  SHOW,
    @SerialName("book")  BOOK;

    val displayName: String
        get() = when (this) {
            MOVIE -> "Movie"; SHOW -> "Show"; BOOK -> "Book"
        }
}

@Serializable
data class StoryChoice(
    val text: String,
    val consequence: String,
    val nextNodeId: String? = null,
)

@Serializable
data class StoryNode(
    val id: String,
    val text: String,
    val sceneTitle: String? = null,
    val choices: List<StoryChoice> = emptyList(),
    val isEnding: Boolean = false,
    val endingTitle: String? = null,
)

@Serializable
data class CatalogIndexEntry(
    val id: String,
    val title: String,
    val sourceTitle: String,
    val kind: StoryKind,
    val synopsis: String,
    val releaseYear: Int? = null,
    val addedAt: String,
    val genre: String,
    val tags: List<String> = emptyList(),
    val rating: Int? = null,
    val loved: Boolean? = null,
    val nextStoryId: String? = null,
    val storyURL: String? = null,
)

@Serializable
data class CatalogIndex(
    val version: Int,
    val updatedAt: String,
    val stories: List<CatalogIndexEntry>,
)

@Serializable
data class CatalogStory(
    val id: String,
    val title: String,
    val sourceTitle: String,
    val kind: StoryKind,
    val synopsis: String,
    val releaseYear: Int? = null,
    val addedAt: String,
    val genre: String,
    val tags: List<String> = emptyList(),
    val rating: Int? = null,
    val loved: Boolean? = null,
    val nextStoryId: String? = null,
    val startNodeId: String,
    val nodes: List<StoryNode>,
) {
    fun node(id: String): StoryNode? = nodes.firstOrNull { it.id == id }
    val stars: Int? get() = rating?.coerceIn(0, 5)
    val isLoved: Boolean get() = loved == true
}
