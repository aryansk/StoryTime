import Foundation

// MARK: - DefaultsWriter
//
// Coalesces frequent "encode this snapshot → write to UserDefaults" requests
// into a single debounced background write. A single reader action (visiting a
// scene, making a choice) used to trigger several *synchronous, main-thread*
// JSON encodes per second across the stat / DNA stores. This mirrors the
// pattern already used by ReadingProgressStore, extracted so every store can
// share it.

final class DefaultsWriter<Value: Encodable> {
    private let key: String
    private let interval: TimeInterval
    private var pending: DispatchWorkItem?
    private let queue = DispatchQueue(label: "storytime.defaultswriter", qos: .utility)

    init(key: String, interval: TimeInterval = 0.6) {
        self.key = key
        self.interval = interval
    }

    /// Schedule a coalesced write ~`interval` out, replacing any pending one.
    func schedule(_ value: Value) {
        pending?.cancel()
        let key = self.key
        let work = DispatchWorkItem {
            if let data = try? JSONEncoder().encode(value) {
                UserDefaults.standard.set(data, forKey: key)
            }
        }
        pending = work
        queue.asyncAfter(deadline: .now() + interval, execute: work)
    }

    /// Flush immediately (used for destructive changes that must not be lost,
    /// e.g. a reset the user just tapped).
    func flushNow(_ value: Value) {
        pending?.cancel()
        pending = nil
        let key = self.key
        queue.async {
            if let data = try? JSONEncoder().encode(value) {
                UserDefaults.standard.set(data, forKey: key)
            }
        }
    }
}
