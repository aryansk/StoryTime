import Foundation

class GeminiService {
    private let apiKey = "AIzaSyDyJhbMVyHXwkhQycdDQ4Ka0WJKRrEgSnI"
    private let baseURL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent"
    
    func generateStoryContent(prompt: String) async throws -> StoryResponse {
        let url = URL(string: "\(baseURL)?key=\(apiKey)")!
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        
        let requestBody = GeminiRequest(contents: [
            Content(parts: [
                Part(text: """
                    Generate a short interactive story segment based on this prompt: \(prompt)
                    Format the response exactly like this:
                    {
                        "story_text": "The story segment text here...",
                        "choices": [
                            {
                                "text": "First choice text",
                                "prompt": "Continuation prompt for this choice"
                            },
                            {
                                "text": "Second choice text",
                                "prompt": "Continuation prompt for this choice"
                            }
                        ]
                    }
                    Make the story engaging and the choices meaningful. Each choice should lead to a different direction.
                    """)
            ])
        ])
        
        let encoder = JSONEncoder()
        request.httpBody = try encoder.encode(requestBody)
        
        let (data, _) = try await URLSession.shared.data(for: request)
        let response = try JSONDecoder().decode(GeminiResponse.self, from: data)
        
        // Extract the JSON string from the response
        guard let jsonString = response.candidates.first?.content.parts.first?.text,
              let jsonData = jsonString.data(using: .utf8) else {
            throw GeminiError.invalidResponse
        }
        
        // Parse the story response
        return try JSONDecoder().decode(StoryResponse.self, from: jsonData)
    }
}

// Request Models
struct GeminiRequest: Codable {
    let contents: [Content]
}

struct Content: Codable {
    let parts: [Part]
}

struct Part: Codable {
    let text: String
}

// Response Models
struct GeminiResponse: Codable {
    let candidates: [Candidate]
}

struct Candidate: Codable {
    let content: Content
}

// Story Response Model
struct StoryResponse: Codable {
    let story_text: String
    let choices: [StoryChoice]
}

struct StoryChoice: Codable {
    let text: String
    let prompt: String
}

enum GeminiError: Error {
    case invalidResponse
} 