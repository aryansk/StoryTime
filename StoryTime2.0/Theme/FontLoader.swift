import SwiftUI
import CoreText

// MARK: - FontLoader
//
// Registers any .ttf / .otf files found in the app bundle at runtime, so
// custom fonts (Space Grotesk, Source Serif 4) work without editing the
// generated Info.plist. Call FontLoader.registerAll() once at launch.

enum FontLoader {
    private static var didRegister = false

    static func registerAll() {
        guard !didRegister else { return }
        didRegister = true

        let extensions = ["ttf", "otf"]
        var urls: [URL] = []
        for ext in extensions {
            // Top-level + common subdirectories.
            urls.append(contentsOf: Bundle.main.urls(forResourcesWithExtension: ext,
                                                     subdirectory: nil) ?? [])
            urls.append(contentsOf: Bundle.main.urls(forResourcesWithExtension: ext,
                                                     subdirectory: "Fonts") ?? [])
            urls.append(contentsOf: Bundle.main.urls(forResourcesWithExtension: ext,
                                                     subdirectory: "Resources/Fonts") ?? [])
        }
        let unique = Array(Set(urls))
        for url in unique {
            var err: Unmanaged<CFError>?
            if !CTFontManagerRegisterFontsForURL(url as CFURL, .process, &err) {
                // Already registered or invalid — fine, the system fallback
                // will keep the UI rendering. Log lightly.
                #if DEBUG
                if let e = err?.takeRetainedValue() {
                    print("FontLoader: \(url.lastPathComponent) → \(e.localizedDescription)")
                }
                #endif
            }
        }
    }
}
