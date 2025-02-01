import SwiftUI

struct TypewriterText: View {
    let text: String
    
    var body: some View {
        Text(text)
            .font(.body)
            .lineSpacing(8)
    }
} 
