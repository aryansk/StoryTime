import Foundation

class UserModel: ObservableObject {
    @Published var username: String {
        didSet {
            UserDefaults.standard.set(username, forKey: "username")
        }
    }
    
    var greeting: String {
        let hour = Calendar.current.component(.hour, from: Date())
        switch hour {
        case 0..<12:
            return "Good Morning 🌤️"
        case 12..<17:
            return "Good Afternoon ☀️"
        case 17..<21:
            return "Good Evening 🌳"
        default:
            return "Good Night 🌖"
        }
    }
    
    init() {
        self.username = UserDefaults.standard.string(forKey: "username") ?? ""
    }
    
    var isFirstLaunch: Bool {
        username.isEmpty
    }
} 
