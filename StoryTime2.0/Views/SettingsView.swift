import SwiftUI

struct SettingsView: View {
    @ObservedObject var settings: SettingsModel
    @Environment(\.dismiss) var dismiss
    @State private var showingColorPicker = false
    @State private var selectedColor = Color.white
    @Environment(\.colorScheme) var colorScheme
    
    var body: some View {
        List {
            // Reading Experience
            Section {
                NavigationLink(destination: FontSettingsView(settings: settings)) {
                    SettingRow(
                        icon: "textformat.size",
                        title: "Typography",
                        subtitle: "\(settings.selectedFontName), Size \(Int(settings.textSize))"
                    )
                }
                
                NavigationLink(destination: ThemeSettingsView(settings: settings, showingColorPicker: $showingColorPicker, selectedColor: $selectedColor)) {
                    SettingRow(
                        icon: "paintpalette",
                        title: "Theme",
                        subtitle: themeDescription
                    )
                }
            } header: {
                Text("Reading Experience")
                    .padding(.bottom, 8)
            }
            
            // Display
            Section {
                Toggle(isOn: $settings.isDarkMode) {
                    SettingRow(
                        icon: "moon.circle.fill",
                        title: "Dark Mode",
                        subtitle: "Adjust app appearance"
                    )
                }
            } header: {
                Text("Display")
                    .padding(.bottom, 8)
            }
            
            // Preview
            Section {
                VStack(alignment: .leading, spacing: 12) {
                    Text("Preview")
                        .font(.headline)
                        .foregroundColor(.primary)
                    
                    VStack(alignment: .leading, spacing: 12) {
                        Text("Story Preview")
                            .font(.custom(settings.selectedFontName, size: settings.textSize))
                            .foregroundColor(.primary)
                        
                        Text("This is how your story will appear while reading. The text size, font, and colors reflect your current settings.")
                            .font(.custom(settings.selectedFontName, size: max(settings.textSize - 2, settings.minTextSize)))
                            .foregroundColor(.secondary)
                    }
                    .padding()
                    .frame(maxWidth: .infinity, alignment: .leading)
                    .background(settings.themeColor)
                    .cornerRadius(12)
                    .shadow(color: Color.black.opacity(0.05), radius: 2, y: 1)
                }
                .listRowInsets(EdgeInsets(top: 12, leading: 16, bottom: 12, trailing: 16))
            } header: {
                Text("Live Preview")
                    .padding(.bottom, 8)
            }
        }
        .navigationTitle("Settings")
        .navigationBarTitleDisplayMode(.large)
        .listStyle(InsetGroupedListStyle())
        .background(Color(UIColor.systemGroupedBackground))
        .scrollContentBackground(.hidden)
        .sheet(isPresented: $showingColorPicker) {
            ColorPickerView(selectedColor: $selectedColor, settings: settings)
        }
    }
    
    private var themeDescription: String {
        switch settings.selectedTheme {
        case 0: return "Light Yellow"
        case 1: return "Light Grey"
        case 2: return "Custom Color"
        default: return "Light Yellow"
        }
    }
}

struct SettingRow: View {
    let icon: String
    let title: String
    let subtitle: String
    
    var body: some View {
        HStack(spacing: 12) {
            Image(systemName: icon)
                .font(.system(size: 22, weight: .semibold))
                .frame(width: 32, height: 32)
                .foregroundColor(.blue)
            
            VStack(alignment: .leading, spacing: 2) {
                Text(title)
                    .font(.body)
                    .foregroundColor(.primary)
                Text(subtitle)
                    .font(.subheadline)
                    .foregroundColor(.secondary)
            }
        }
        .padding(.vertical, 4)
    }
}

struct FontSettingsView: View {
    @ObservedObject var settings: SettingsModel
    
    var body: some View {
        List {
            Section {
                VStack(alignment: .leading, spacing: 8) {
                    Text("Text Size: \(Int(settings.textSize))")
                        .font(.headline)
                    
                    HStack {
                        Text("A")
                            .font(.system(size: settings.minTextSize))
                        Slider(
                            value: $settings.textSize,
                            in: settings.minTextSize...settings.maxTextSize,
                            step: 1
                        )
                        Text("A")
                            .font(.system(size: settings.maxTextSize))
                    }
                }
                .padding(.vertical, 8)
            }
            
            Section {
                ForEach(settings.availableFonts, id: \.self) { font in
                    Button(action: { settings.selectedFontName = font }) {
                        HStack {
                            Text(font)
                                .font(.custom(font, size: 17))
                            Spacer()
                            if settings.selectedFontName == font {
                                Image(systemName: "checkmark")
                                    .foregroundColor(.blue)
                            }
                        }
                    }
                    .foregroundColor(.primary)
                }
            } header: {
                Text("Font Style")
            }
        }
        .navigationTitle("Typography")
    }
}

struct ThemeSettingsView: View {
    @ObservedObject var settings: SettingsModel
    @Binding var showingColorPicker: Bool
    @Binding var selectedColor: Color
    @State private var selectedThemeTag: Int
    
    init(settings: SettingsModel, showingColorPicker: Binding<Bool>, selectedColor: Binding<Color>) {
        self.settings = settings
        self._showingColorPicker = showingColorPicker
        self._selectedColor = selectedColor
        self._selectedThemeTag = State(initialValue: settings.selectedTheme)
    }
    
    var body: some View {
        List {
            Section {
                themeButton("Light Yellow", color: Color(hex: "FFFBE6"), tag: 0)
                themeButton("Light Grey", color: Color(hex: "F5F5F5"), tag: 1)
                
                Button(action: { showingColorPicker = true }) {
                    HStack {
                        Text("Custom Color")
                        Spacer()
                        if settings.selectedTheme == 2 {
                            Circle()
                                .fill(Color(hex: settings.customThemeColor))
                                .frame(width: 24, height: 24)
                                .overlay(
                                    Circle()
                                        .stroke(Color.gray, lineWidth: 1)
                                )
                                .transition(.scale.combined(with: .opacity))
                        }
                        if settings.selectedTheme == 2 {
                            Image(systemName: "checkmark")
                                .foregroundColor(.blue)
                                .transition(.scale.combined(with: .opacity))
                        }
                    }
                }
            } header: {
                Text("Background Theme")
            }
        }
        .navigationTitle("Theme")
        .onChange(of: selectedThemeTag) { oldValue, newValue in
            settings.transitionToTheme(newValue)
        }
        .sheet(isPresented: $showingColorPicker) {
            ColorPickerView(selectedColor: $selectedColor, settings: settings)
        }
    }
    
    private func themeButton(_ title: String, color: Color, tag: Int) -> some View {
        Button(action: { selectedThemeTag = tag }) {
            HStack {
                Text(title)
                Spacer()
                Circle()
                    .fill(color)
                    .frame(width: 24, height: 24)
                    .overlay(
                        Circle()
                            .stroke(Color.gray, lineWidth: 1)
                    )
                if settings.selectedTheme == tag {
                    Image(systemName: "checkmark")
                        .foregroundColor(.blue)
                        .transition(.scale.combined(with: .opacity))
                }
            }
        }
        .contentTransition(.opacity)
    }
}

struct ColorPickerView: View {
    @Binding var selectedColor: Color
    @ObservedObject var settings: SettingsModel
    @Environment(\.dismiss) var dismiss
    
    var body: some View {
        NavigationView {
            VStack {
                ColorPicker("Choose a color", selection: $selectedColor, supportsOpacity: false)
                    .padding()
                
                RoundedRectangle(cornerRadius: 12)
                    .fill(selectedColor)
                    .frame(height: 100)
                    .padding()
                    .overlay(
                        RoundedRectangle(cornerRadius: 12)
                            .stroke(Color.gray.opacity(0.3), lineWidth: 1)
                    )
                
                Spacer()
            }
            .navigationTitle("Custom Color")
            .navigationBarTitleDisplayMode(.inline)
            .toolbar {
                ToolbarItem(placement: .cancellationAction) {
                    Button("Cancel") {
                        dismiss()
                    }
                }
                ToolbarItem(placement: .confirmationAction) {
                    Button("Done") {
                        settings.customThemeColor = selectedColor.toHex()
                        settings.selectedTheme = 2
                        dismiss()
                    }
                }
            }
        }
    }
} 
