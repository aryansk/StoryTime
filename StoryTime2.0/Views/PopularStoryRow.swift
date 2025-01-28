//
//  PopularStoryRow.swift
//  StoryTime2.0
//
//  Created by Aryan Signh on 28/01/25.
//

import SwiftUI

struct PopularStoryRow: View {
    let story: Story
    let index: Int
    @State private var isShown = false
    @State private var isHovered = false
    
    var body: some View {
        HStack(spacing: 16) {
            // Story Image
            ZStack(alignment: .topLeading) {
                RoundedRectangle(cornerRadius: 20)
                    .fill(Color.orange.opacity(0.15))
                    .frame(width: 100, height: 100)
                    .overlay(
                        Image(systemName: "book.fill")
                            .font(.system(size: 32))
                            .foregroundColor(.orange)
                    )
                
                // Rank Badge
                Text("#\(index + 1)")
                    .font(.system(size: 14, weight: .bold))
                    .foregroundColor(.white)
                    .frame(width: 32, height: 32)
                    .background(
                        Circle()
                            .fill(
                                LinearGradient(
                                    colors: [.orange, .orange.opacity(0.8)],
                                    startPoint: .topLeading,
                                    endPoint: .bottomTrailing
                                )
                            )
                            .shadow(color: .black.opacity(0.15), radius: 4, y: 2)
                    )
                    .offset(x: -8, y: -8)
            }
            
            // Story Details
            VStack(alignment: .leading, spacing: 8) {
                Text(story.title)
                    .font(.system(size: 17, weight: .semibold))
                    .foregroundColor(.primary)
                
                Text(story.description)
                    .font(.system(size: 15))
                    .foregroundColor(.secondary)
                    .lineLimit(2)
                    .lineSpacing(4)
                
                HStack(spacing: 16) {
                    Label("4.8", systemImage: "star.fill")
                        .foregroundColor(.orange)
                    
                    Label("10 min", systemImage: "clock")
                        .foregroundColor(.secondary)
                }
                .font(.system(size: 13, weight: .medium))
            }
            
            Spacer()
            
            Image(systemName: "chevron.right")
                .font(.system(size: 14, weight: .semibold))
                .foregroundColor(.secondary)
                .opacity(isHovered ? 1 : 0.5)
                .offset(x: isHovered ? 4 : 0)
        }
        .padding(16)
        .background(
            RoundedRectangle(cornerRadius: 20)
                .fill(Color(UIColor.secondarySystemGroupedBackground))
                .shadow(
                    color: Color.black.opacity(isHovered ? 0.1 : 0.05),
                    radius: isHovered ? 10 : 8,
                    y: isHovered ? 5 : 4
                )
        )
        .scaleEffect(isHovered ? 0.98 : 1)
        .opacity(isShown ? 1 : 0)
        .offset(x: isShown ? 0 : 50)
        .onAppear {
            withAnimation(.spring(response: 0.6, dampingFraction: 0.8).delay(Double(index) * 0.1)) {
                isShown = true
            }
        }
        .onHover { hovering in
            withAnimation(.spring(response: 0.3)) {
                isHovered = hovering
            }
        }
    }
}

enum StoryCategory: String, CaseIterable {
    case all = "All"
    case adventure = "Adventure"
    case mystery = "Mystery"
    case fantasy = "Fantasy"
    case sciFi = "Sci-Fi"
    
    var icon: String {
        switch self {
        case .all: return "square.stack.3d.up"
        case .adventure: return "map"
        case .mystery: return "magnifyingglass"
        case .fantasy: return "wand.and.stars"
        case .sciFi: return "star"
        }
    }
}
