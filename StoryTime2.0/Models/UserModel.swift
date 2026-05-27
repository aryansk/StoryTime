import Foundation

class UserModel: ObservableObject {
    @Published var username: String {
        didSet {
            UserDefaults.standard.set(username, forKey: "username")
        }
    }
    
    @Published var goal: String {
        didSet {
            UserDefaults.standard.set(goal, forKey: "user_goal")
        }
    }
    
    @Published var experienceLevel: String {
        didSet {
            UserDefaults.standard.set(experienceLevel, forKey: "user_experience_level")
        }
    }
    
    @Published var onboardingCompleted: Bool {
        didSet {
            UserDefaults.standard.set(onboardingCompleted, forKey: "onboarding_completed")
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
        self.goal = UserDefaults.standard.string(forKey: "user_goal") ?? ""
        self.experienceLevel = UserDefaults.standard.string(forKey: "user_experience_level") ?? ""
        self.onboardingCompleted = UserDefaults.standard.bool(forKey: "onboarding_completed")
    }
    
    var isFirstLaunch: Bool {
        !onboardingCompleted
    }
} 
