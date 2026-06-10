import Foundation

// MARK: - Anthropic client
//
// Minimal bring-your-own-API-key wrapper around the Anthropic Messages
// API. Used to generate a personal CYOA story by sending the model a
// strict instruction to return our CatalogStory JSON schema.
//
// No data leaves the device except to api.anthropic.com when the user
// taps "Generate."

enum AnthropicError: Error, LocalizedError {
    case missingKey
    case http(Int, String)
    case decode(String)
    case noContent
    case invalidGraph([StoryGraphValidator.Issue])

    var errorDescription: String? {
        switch self {
        case .missingKey:   return "Add an Anthropic API key in Settings first."
        case .http(let s, let body): return "API error (\(s)): \(body.prefix(200))"
        case .decode(let why): return "Couldn't read the response: \(why)"
        case .noContent:    return "The model returned no usable content."
        case .invalidGraph(let issues):
            return "The generated story had broken scenes (\(issues.map(\.description).joined(separator: "; ").prefix(200))). Please try again."
        }
    }
}

struct AnthropicClient {
    /// Default model. Latest Claude family that's good at structured generation.
    var model: String = "claude-sonnet-4-5"
    var apiKey: String

    /// Generate a story and validate its node graph. If the first attempt
    /// produces a broken graph (the most common model failure), retry once
    /// with the validation errors fed back; if that also fails, surface
    /// the issues to the caller.
    func generateStory(title: String, premise: String, kind: StoryKind, genre: StoryGenre) async throws -> CatalogStory {
        let first = try await generateStoryOnce(title: title, premise: premise,
                                                kind: kind, genre: genre)
        let issues = StoryGraphValidator.validate(first)
        if issues.isEmpty { return first }

        let feedback = "Your previous attempt had these structural errors: "
            + issues.map(\.description).joined(separator: "; ")
            + ". Regenerate the full JSON with all of them fixed."
        let second = try await generateStoryOnce(title: title, premise: premise,
                                                 kind: kind, genre: genre,
                                                 extraInstruction: feedback)
        let secondIssues = StoryGraphValidator.validate(second)
        guard secondIssues.isEmpty else {
            throw AnthropicError.invalidGraph(secondIssues)
        }
        return second
    }

    private func generateStoryOnce(title: String, premise: String, kind: StoryKind,
                                   genre: StoryGenre, extraInstruction: String? = nil) async throws -> CatalogStory {
        guard !apiKey.trimmingCharacters(in: .whitespaces).isEmpty else {
            throw AnthropicError.missingKey
        }

        let system = """
        You are a CYOA story author. Reply with ONE JSON object only, no \
        prose before or after. It must conform to this schema (Swift Codable):

        {
          "id": "user-<slug>-####",
          "title": "<the original work's title>",
          "sourceTitle": "<the original work's title>",
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
          "nodes": [ <see below> ]
        }

        Nodes form a directed graph. Use 12–14 decision nodes named s1..sN \
        and 3 ending nodes named end_a, end_b, end_c. For decision nodes, \
        "choices" is an array of 2 objects with text/consequence/nextNodeId \
        and "isEnding" is false. Endings: "choices": [], "isEnding": true, \
        "endingTitle" set. Make the prose vivid, second-person, with \
        "what would you have done in <Title>?" framing. Every nextNodeId \
        must exist. The last decision node's choices point to the endings.
        """

        var user = """
        Title: \(title)
        Kind: \(kind.rawValue)
        Genre: \(genre.rawValue)
        Premise / framing: \(premise.isEmpty ? "Place the reader in the world of the original." : premise)

        Generate the JSON now.
        """
        if let extraInstruction {
            user += "\n\n" + extraInstruction
        }

        let body: [String: Any] = [
            "model": model,
            "max_tokens": 8192,
            "system": system,
            "messages": [
                ["role": "user", "content": user]
            ]
        ]

        var request = URLRequest(url: URL(string: "https://api.anthropic.com/v1/messages")!)
        request.httpMethod = "POST"
        request.setValue(apiKey, forHTTPHeaderField: "x-api-key")
        request.setValue("2023-06-01", forHTTPHeaderField: "anthropic-version")
        request.setValue("application/json", forHTTPHeaderField: "content-type")
        request.httpBody = try JSONSerialization.data(withJSONObject: body)

        let (data, response) = try await URLSession.shared.data(for: request)
        if let http = response as? HTTPURLResponse, !(200..<300).contains(http.statusCode) {
            let s = String(data: data, encoding: .utf8) ?? ""
            throw AnthropicError.http(http.statusCode, s)
        }

        // Anthropic returns { content: [{ type: "text", text: "..." }] }
        guard let json = try JSONSerialization.jsonObject(with: data) as? [String: Any],
              let parts = json["content"] as? [[String: Any]] else {
            throw AnthropicError.decode("unexpected response shape")
        }
        let combined = parts.compactMap { $0["text"] as? String }.joined()
        guard !combined.isEmpty else { throw AnthropicError.noContent }

        // Carve out the first JSON object from the response.
        guard let storyJSONString = Self.extractFirstJSONObject(from: combined),
              let storyData = storyJSONString.data(using: .utf8) else {
            throw AnthropicError.decode("no JSON object found in response")
        }
        do {
            return try CatalogJSON.decoder.decode(CatalogStory.self, from: storyData)
        } catch {
            throw AnthropicError.decode(String(describing: error))
        }
    }

    /// Pull the first balanced `{...}` block out of a string. Tolerant of
    /// minor preamble or trailing prose around the JSON.
    static func extractFirstJSONObject(from text: String) -> String? {
        guard let start = text.firstIndex(of: "{") else { return nil }
        var depth = 0
        var inString = false
        var escape = false
        var i = start
        while i < text.endIndex {
            let c = text[i]
            if escape { escape = false; i = text.index(after: i); continue }
            if c == "\\" && inString { escape = true; i = text.index(after: i); continue }
            if c == "\"" { inString.toggle() }
            else if !inString {
                if c == "{" { depth += 1 }
                if c == "}" {
                    depth -= 1
                    if depth == 0 {
                        return String(text[start...i])
                    }
                }
            }
            i = text.index(after: i)
        }
        return nil
    }
}
