import SwiftUI

struct SignUpView: View {
    @ObservedObject var userModel: UserModel
    @Binding var isPresented: Bool
    @State private var username = ""
    @State private var showElements = false
    @State private var attempts = 0
    @State private var isButtonPressed = false
    
    var body: some View {
        ZStack {
            Color(.systemBackground)
                .ignoresSafeArea()
            
            VStack(spacing: 30) {
                // Title
                Text("Welcome to StoryTime")
                    .font(.largeTitle.bold())
                    .multilineTextAlignment(.center)
                    .transition(.asymmetric(
                        insertion: .move(edge: .top).combined(with: .opacity),
                        removal: .identity
                    ))
                    .offset(y: showElements ? 0 : -30)
                    .opacity(showElements ? 1 : 0)
                
                // Subtitle
                Text("Your journey begins here...")
                    .font(.title3)
                    .foregroundStyle(.secondary)
                    .transition(.opacity)
                    .opacity(showElements ? 1 : 0)
                    .offset(y: showElements ? 0 : -20)
                
                // Text Field with Shake Animation
                TextField("Enter your name", text: $username)
                    .textFieldStyle(.roundedBorder)
                    .font(.title3)
                    .padding(.horizontal, 40)
                    .padding(.top, 20)
                    .autocorrectionDisabled()
                    .textInputAutocapitalization(.words)
                    .modifier(ShakeEffect(animatableData: CGFloat(attempts)))
                    .transition(.move(edge: .leading))
                    .opacity(showElements ? 1 : 0)
                
                // Continue Button
                Button(action: {
                    if username.isEmpty {
                        withAnimation(.spring(response: 0.3, dampingFraction: 0.2)) {
                            attempts += 1
                        }
                    } else {
                        isButtonPressed = true
                        withAnimation(.easeInOut(duration: 0.4)) {
                            userModel.username = username
                            isPresented = false
                        }
                    }
                }) {
                    Text("Continue")
                        .font(.title3.bold())
                        .foregroundColor(.white)
                        .frame(maxWidth: .infinity)
                        .padding()
                        .background(
                            RoundedRectangle(cornerRadius: 12)
                                .fill(username.isEmpty ? .gray : .blue)
                                .animation(.easeInOut(duration: 0.3), value: username.isEmpty)
                        )
                        .padding(.horizontal, 40)
                        .scaleEffect(isButtonPressed ? 0.95 : 1)
                }
                .disabled(username.isEmpty)
                .transition(.opacity.combined(with: .scale))
                .opacity(showElements ? 1 : 0)
                .offset(y: showElements ? 0 : 20)
                
                Spacer()
            }
            .padding(.top, 60)
        }
        .onAppear {
            withAnimation(.spring(dampingFraction: 0.8).delay(0.2)) {
                showElements = true
            }
        }
    }
}

// Shake Effect Modifier
struct ShakeEffect: GeometryEffect {
    var animatableData: CGFloat
    
    func effectValue(size: CGSize) -> ProjectionTransform {
        let translation = sin(animatableData * .pi * 2) * 10
        return ProjectionTransform(CGAffineTransform(translationX: translation, y: 0))
    }
}
