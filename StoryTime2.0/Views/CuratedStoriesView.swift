//
//  CuratedStoriesView.swift
//  StoryTime2.0
//
//  Created by Aryan Signh on 28/01/25.
//
import SwiftUI

struct CuratedStoriesView: View {
    @ObservedObject var userModel: UserModel
    @ObservedObject var settings: SettingsModel
    @State private var selectedCategory: StoryCategory = .all
    @Environment(\.colorScheme) var colorScheme
    
    var filteredStories: [Story] {
        if selectedCategory == .all {
            return Story.samples
        }
        return Story.samples.filter { $0.category == selectedCategory }
    }
    
    var body: some View {
        NavigationStack {
            ScrollView(showsIndicators: false) {
                VStack(alignment: .leading, spacing: 16) {
                    // Featured Story
                    NavigationLink(destination: StoryStartView(story: Story.featured, settings: settings)) {
                        FeaturedStoryCard(settings: settings)
                            .padding(.horizontal)
                    }
                    .buttonStyle(ScaledButtonStyle())
                    
                    // Categories
                    VStack(alignment: .leading, spacing: 15) {
                        Text("Categories")
                            .font(.title2.bold())
                            .foregroundColor(.primary)
                            .padding(.horizontal)
                            .padding(.bottom, 4)
                        
                        ScrollView(.horizontal, showsIndicators: false) {
                            HStack(spacing: 8) {
                                ForEach(StoryCategory.allCases, id: \.self) { category in
                                    CategoryButton(
                                        title: category.rawValue,
                                        icon: category.icon,
                                        isSelected: selectedCategory == category,
                                        action: {
                                            withAnimation(.spring(response: 0.3)) {
                                                selectedCategory = category
                                            }
                                        }
                                    )
                                }
                            }
                            .padding(.horizontal)
                        }
                    }
                    
                    // Popular Stories
                    VStack(alignment: .leading, spacing: 16) {
                        Text(selectedCategory == .all ? "Popular Stories" : "\(selectedCategory.rawValue) Stories")
                            .font(.title2.bold())
                            .foregroundColor(.primary)
                            .padding(.horizontal)
                        
                        if filteredStories.isEmpty {
                            EmptyStateView(
                                showingNewStorySheet: .constant(false), category: selectedCategory
                            )
                            .padding(.top, 32)
                        } else {
                            LazyVStack(spacing: 16) {
                                ForEach(Array(filteredStories.enumerated()), id: \.element.id) { index, story in
                                    NavigationLink(destination: StoryStartView(story: story, settings: settings)) {
                                        PopularStoryRow(story: story, index: index)
                                    }
                                    .buttonStyle(ScaledButtonStyle())
                                }
                            }
                            .padding(.horizontal)
                        }
                    }
                }
                .padding(.vertical)
            }
            .navigationTitle("\(userModel.greeting), \(userModel.username)")
            .navigationBarTitleDisplayMode(.large)
            .background(Color(UIColor.systemGroupedBackground))
        }
        .tint(.orange)
    }
}
