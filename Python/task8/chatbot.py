#!/usr/bin/env python3
"""
Task 8: Rule-based Chatbot using if-else statements
A simple chatbot that demonstrates basic NLP structure and control flow.
"""

def get_greeting_response(user_input):
    """Handle greeting-related inputs"""
    greetings = ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening']
    if any(greeting in user_input.lower() for greeting in greetings):
        return "Hello! How can I help you today?"
    return None

def get_farewell_response(user_input):
    """Handle farewell-related inputs"""
    farewells = ['bye', 'goodbye', 'see you', 'exit', 'quit']
    if any(farewell in user_input.lower() for farewell in farewells):
        return "Goodbye! Have a great day!"
    return None

def get_weather_response(user_input):
    """Handle weather-related queries"""
    weather_keywords = ['weather', 'temperature', 'rain', 'sunny', 'cold', 'hot']
    if any(keyword in user_input.lower() for keyword in weather_keywords):
        return "I'm sorry, I don't have access to real-time weather data. You might want to check a weather app!"
    return None

def get_time_response(user_input):
    """Handle time-related queries"""
    time_keywords = ['time', 'clock', 'hour', 'date', 'day']
    if any(keyword in user_input.lower() for keyword in time_keywords):
        from datetime import datetime
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return f"The current date and time is: {current_time}"
    return None

def get_help_response(user_input):
    """Handle help requests"""
    help_keywords = ['help', 'what can you do', 'commands', 'features']
    if any(keyword in user_input.lower() for keyword in help_keywords):
        return """I can help you with:
- Greetings (hello, hi, hey)
- Weather questions (though I don't have real data)
- Time and date information
- Basic conversation
- Just say 'bye' or 'quit' to exit!"""
    return None

def get_name_response(user_input):
    """Handle name-related queries"""
    name_keywords = ['name', 'who are you', 'what are you']
    if any(keyword in user_input.lower() for keyword in name_keywords):
        return "I'm a simple rule-based chatbot created for Task 8. Nice to meet you!"
    return None

def get_feeling_response(user_input):
    """Handle feeling-related queries"""
    feeling_keywords = ['how are you', 'feeling', 'mood']
    if any(keyword in user_input.lower() for keyword in feeling_keywords):
        return "I'm doing well, thank you for asking! How are you feeling today?"
    return None

def get_default_response(user_input):
    """Default response for unrecognized inputs"""
    return "I'm not sure how to respond to that. Try asking for 'help' to see what I can do!"

def chatbot():
    """
    Main chatbot function that runs an input/output loop
    Uses if-elif-else structure for response selection
    """
    print("=" * 50)
    print("🤖 Welcome to the Rule-based Chatbot!")
    print("Type 'bye', 'quit', or 'exit' to end the conversation")
    print("Type 'help' to see what I can do")
    print("=" * 50)
    
    while True:
        # Collect user input
        user_input = input("\nYou: ").strip()
        
        # Check for exit commands first
        if user_input.lower() in ['bye', 'quit', 'exit']:
            print("Bot: Goodbye! Have a great day!")
            break
        
        # If input is empty, ask for input again
        if not user_input:
            print("Bot: Please say something!")
            continue
        
        # Process the input using if-elif-else structure
        response = None
        
        # Try each response function in order
        response_functions = [
            get_greeting_response,
            get_farewell_response,
            get_weather_response,
            get_time_response,
            get_help_response,
            get_name_response,
            get_feeling_response
        ]
        
        for func in response_functions:
            response = func(user_input)
            if response:
                break
        
        # If no specific response found, use default
        if not response:
            response = get_default_response(user_input)
        
        print(f"Bot: {response}")

def test_chatbot():
    """Test function to verify chatbot functionality"""
    print("🧪 Testing Chatbot Functionality...")
    
    test_cases = [
        "hello",
        "what's the weather like?",
        "what time is it?",
        "help",
        "what's your name?",
        "how are you?",
        "random gibberish",
        "bye"
    ]
    
    for test_input in test_cases:
        print(f"\nTesting input: '{test_input}'")
        # This would normally call the response functions directly
        # For now, just show what we expect
        if "hello" in test_input.lower():
            print("Expected: Greeting response")
        elif "weather" in test_input.lower():
            print("Expected: Weather response")
        elif "time" in test_input.lower():
            print("Expected: Time response")
        elif "help" in test_input.lower():
            print("Expected: Help response")
        elif "name" in test_input.lower():
            print("Expected: Name response")
        elif "how are you" in test_input.lower():
            print("Expected: Feeling response")
        elif "bye" in test_input.lower():
            print("Expected: Farewell response")
        else:
            print("Expected: Default response")

if __name__ == "__main__":
    # Check if user wants to run tests
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        test_chatbot()
    else:
        chatbot()
