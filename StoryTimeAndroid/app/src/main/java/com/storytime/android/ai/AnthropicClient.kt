package com.storytime.android.ai

import com.storytime.android.model.CatalogStory
import com.storytime.android.model.StoryKind
import kotlinx.coroutines.Dispatchers
import kotlinx.coroutines.withContext
import kotlinx.serialization.json.Json
import kotlinx.serialization.json.JsonArray
import kotlinx.serialization.json.JsonObject
import kotlinx.serialization.json.buildJsonArray
import kotlinx.serialization.json.buildJsonObject
import kotlinx.serialization.json.contentOrNull
import kotlinx.serialization.json.jsonArray
import kotlinx.serialization.json.jsonObject
import kotlinx.serialization.json.jsonPrimitive
import kotlinx.serialization.json.put
import okhttp3.MediaType.Companion.toMediaType
import okhttp3.OkHttpClient
import okhttp3.Request
import okhttp3.RequestBody.Companion.toRequestBody
import java.util.concurrent.TimeUnit

class AnthropicError(message: String) : Exception(message)

class AnthropicClient(
    private val apiKey: String,
    private val model: String = "claude-sonnet-4-5",
) {
    private val client = OkHttpClient.Builder()
        .callTimeout(60, TimeUnit.SECONDS)
        .readTimeout(60, TimeUnit.SECONDS)
        .build()

    private val json = Json { ignoreUnknownKeys = true; coerceInputValues = true }

    suspend fun generateStory(title: String, premise: String, kind: StoryKind, genre: String): CatalogStory =
        withContext(Dispatchers.IO) {
            if (apiKey.isBlank()) throw AnthropicError("Add an Anthropic API key in Settings first.")

            val system = SYSTEM_PROMPT
            val user = "Title: $title\nKind: ${kind.name.lowercase()}\nGenre: $genre\n" +
                "Premise / framing: ${premise.ifEmpty { "Place the reader in the world of the original." }}\n\nGenerate the JSON now."

            val body = buildJsonObject {
                put("model", model)
                put("max_tokens", 8192)
                put("system", system)
                put("messages", buildJsonArray {
                    add(buildJsonObject {
                        put("role", "user")
                        put("content", user)
                    })
                })
            }

            val req = Request.Builder()
                .url("https://api.anthropic.com/v1/messages")
                .addHeader("x-api-key", apiKey)
                .addHeader("anthropic-version", "2023-06-01")
                .addHeader("content-type", "application/json")
                .post(body.toString().toRequestBody("application/json".toMediaType()))
                .build()

            client.newCall(req).execute().use { resp ->
                val raw = resp.body?.string().orEmpty()
                if (!resp.isSuccessful) throw AnthropicError("API error (${resp.code}): ${raw.take(200)}")
                val parsed = json.parseToJsonElement(raw).jsonObject
                val combined = (parsed["content"] as? JsonArray)
                    ?.mapNotNull { (it as? JsonObject)?.get("text")?.jsonPrimitive?.contentOrNull }
                    ?.joinToString("")
                    .orEmpty()
                if (combined.isBlank()) throw AnthropicError("The model returned no usable content.")
                val storyJson = extractFirstJsonObject(combined)
                    ?: throw AnthropicError("No JSON object found in response.")
                runCatching { json.decodeFromString(CatalogStory.serializer(), storyJson) }
                    .getOrElse { throw AnthropicError("Couldn't decode story: ${it.message}") }
            }
        }

    companion object {
        private val SYSTEM_PROMPT = """
            You are a CYOA story author. Reply with ONE JSON object only, no prose before or after.
            Schema:
            {
              "id": "user-<slug>-####",
              "title": "<the original work's title>",
              "sourceTitle": "<same>",
              "kind": "movie" | "show" | "book",
              "synopsis": "<one to two sentences, second-person>",
              "releaseYear": <int or null>,
              "addedAt": "<ISO 8601 timestamp>",
              "genre": "Drama" | "Comedy" | "Thriller" | "Sci-Fi" | "Horror" | "Fantasy" | "Action",
              "tags": [<short strings>],
              "rating": null,
              "loved": false,
              "nextStoryId": null,
              "startNodeId": "s1",
              "nodes": [ ... ]
            }
            Nodes form a directed graph: 12–14 decision nodes named s1..sN and 3 endings end_a/end_b/end_c.
            Decision nodes: "isEnding": false, "choices": [2 objects with text/consequence/nextNodeId].
            Endings: "isEnding": true, "choices": [], "endingTitle" set. Every nextNodeId must exist.
            Vivid second-person prose, "what would you have done in <Title>?" framing.
        """.trimIndent()

        fun extractFirstJsonObject(text: String): String? {
            val start = text.indexOf('{')
            if (start < 0) return null
            var depth = 0
            var inString = false
            var escape = false
            for (i in start until text.length) {
                val c = text[i]
                if (escape) { escape = false; continue }
                if (c == '\\' && inString) { escape = true; continue }
                if (c == '"') { inString = !inString; continue }
                if (inString) continue
                if (c == '{') depth++
                if (c == '}') {
                    depth--
                    if (depth == 0) return text.substring(start, i + 1)
                }
            }
            return null
        }
    }
}
