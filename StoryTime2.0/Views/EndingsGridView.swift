import SwiftUI

// MARK: - Endings grid
//
// "3 of 7 endings discovered" plus a small wobbly-rect grid of the
// ending names. Discovered endings are inked; undiscovered show as
// "??" so the reader knows what's still out there without spoiling
// the path that gets there.

struct EndingsGridView: View {
    let story: CatalogStory
    let discovered: Set<String>

    private var endingNodes: [StoryNode] {
        story.nodes.filter { $0.isEnding }
    }

    var body: some View {
        if endingNodes.isEmpty {
            EmptyView()
        } else {
            VStack(alignment: .leading, spacing: 12) {
                header
                LazyVGrid(columns: [
                    GridItem(.flexible(), spacing: 10),
                    GridItem(.flexible(), spacing: 10),
                ], spacing: 10) {
                    ForEach(endingNodes, id: \.id) { node in
                        endingChip(for: node)
                    }
                }
            }
        }
    }

    private var header: some View {
        HStack(spacing: 8) {
            DoodleIcon(.starFill, size: 16, filled: true)
            Text("Endings")
                .font(Theme.Fonts.label())
                .tracking(1)
                .foregroundColor(Theme.Palette.inkSoft)
            Spacer()
            Text("\(discovered.count) of \(endingNodes.count) discovered")
                .font(Theme.Fonts.bodyItalic(13))
                .foregroundColor(Theme.Palette.inkSoft)
        }
    }

    @ViewBuilder
    private func endingChip(for node: StoryNode) -> some View {
        let isFound = discovered.contains(node.id)
        let label = node.endingTitle ?? "An ending"
        ZStack(alignment: .leading) {
            WobblyRect(jitter: 0.4, corner: 6, seed: CGFloat(node.id.stableSeed(60)))
                .fill(isFound ? Theme.Palette.butterDeep : Theme.Palette.mist)
            WobblyRect(jitter: 0.4, corner: 6, seed: CGFloat(node.id.stableSeed(60)))
                .stroke(Theme.Palette.ink, lineWidth: isFound ? Theme.Stroke.bold : Theme.Stroke.hair)
            HStack(spacing: 8) {
                DoodleIcon(isFound ? .starFill : .star,
                           size: 14, filled: isFound)
                    .opacity(isFound ? 1.0 : 0.45)
                Text(isFound ? label : "?? Undiscovered")
                    .font(Theme.Fonts.bodyItalic(13))
                    .foregroundColor(isFound ? Theme.Palette.ink : Theme.Palette.inkSoft)
                    .lineLimit(2)
                Spacer(minLength: 0)
            }
            .padding(.horizontal, 10)
            .padding(.vertical, 10)
        }
        .frame(minHeight: 52)
    }
}
