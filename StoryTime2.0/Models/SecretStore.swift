import Foundation
import Security

// MARK: - Secret store
//
// Tiny Keychain wrapper for items like the Anthropic API key. Stored as
// generic password items, account = key name, service = bundle id.

enum SecretStore {
    private static var service: String {
        Bundle.main.bundleIdentifier ?? "com.storytime.app"
    }

    static func set(_ value: String?, for account: String) {
        // Always delete any existing item first; simpler than SecItemUpdate.
        let baseQuery: [String: Any] = [
            kSecClass as String: kSecClassGenericPassword,
            kSecAttrService as String: service,
            kSecAttrAccount as String: account,
        ]
        SecItemDelete(baseQuery as CFDictionary)

        guard let value, !value.isEmpty,
              let data = value.data(using: .utf8) else { return }
        var attrs = baseQuery
        attrs[kSecValueData as String] = data
        attrs[kSecAttrAccessible as String] = kSecAttrAccessibleAfterFirstUnlock
        SecItemAdd(attrs as CFDictionary, nil)
    }

    static func get(_ account: String) -> String? {
        let query: [String: Any] = [
            kSecClass as String: kSecClassGenericPassword,
            kSecAttrService as String: service,
            kSecAttrAccount as String: account,
            kSecReturnData as String: true,
            kSecMatchLimit as String: kSecMatchLimitOne,
        ]
        var item: AnyObject?
        guard SecItemCopyMatching(query as CFDictionary, &item) == errSecSuccess,
              let data = item as? Data,
              let s = String(data: data, encoding: .utf8) else {
            return nil
        }
        return s
    }
}

// MARK: - Keys

enum SecretKey {
    static let anthropicAPIKey = "anthropicAPIKey"
}
