#!/usr/bin/env python3
"""
Test suite for the rule-based chatbot
Tests all response functions and edge cases
"""

import unittest
from unittest.mock import patch
from io import StringIO
import sys
import os

# Add the current directory to the path so we can import chatbot
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from chatbot import (
    get_greeting_response,
    get_farewell_response,
    get_weather_response,
    get_time_response,
    get_help_response,
    get_name_response,
    get_feeling_response,
    get_default_response
)

class TestChatbot(unittest.TestCase):
    """Test cases for the chatbot functionality"""
    
    def test_greeting_responses(self):
        """Test greeting response function"""
        greetings = ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening']
        
        for greeting in greetings:
            with self.subTest(greeting=greeting):
                response = get_greeting_response(greeting)
                self.assertIsNotNone(response)
                self.assertIn("Hello", response)
        
        # Test case sensitivity
        response = get_greeting_response("HELLO")
        self.assertIsNotNone(response)
        
        # Test non-greeting
        response = get_greeting_response("what's the weather?")
        self.assertIsNone(response)
    
    def test_farewell_responses(self):
        """Test farewell response function"""
        farewells = ['bye', 'goodbye', 'see you', 'exit', 'quit']
        
        for farewell in farewells:
            with self.subTest(farewell=farewell):
                response = get_farewell_response(farewell)
                self.assertIsNotNone(response)
                self.assertIn("Goodbye", response)
        
        # Test non-farewell
        response = get_farewell_response("hello")
        self.assertIsNone(response)
    
    def test_weather_responses(self):
        """Test weather response function"""
        weather_queries = ['weather', 'temperature', 'rain', 'sunny', 'cold', 'hot']
        
        for query in weather_queries:
            with self.subTest(query=query):
                response = get_weather_response(f"what's the {query} like?")
                self.assertIsNotNone(response)
                self.assertIn("weather", response.lower())
        
        # Test non-weather
        response = get_weather_response("hello")
        self.assertIsNone(response)
    
    def test_time_responses(self):
        """Test time response function"""
        time_queries = ['time', 'clock', 'hour', 'date', 'day']
        
        for query in time_queries:
            with self.subTest(query=query):
                response = get_time_response(f"what {query} is it?")
                self.assertIsNotNone(response)
                self.assertIn("current date and time", response)
        
        # Test non-time
        response = get_time_response("hello")
        self.assertIsNone(response)
    
    def test_help_responses(self):
        """Test help response function"""
        help_queries = ['help', 'what can you do', 'commands', 'features']
        
        for query in help_queries:
            with self.subTest(query=query):
                response = get_help_response(query)
                self.assertIsNotNone(response)
                self.assertIn("help", response.lower())
        
        # Test non-help
        response = get_help_response("hello")
        self.assertIsNone(response)
    
    def test_name_responses(self):
        """Test name response function"""
        name_queries = ['name', 'who are you', 'what are you']
        
        for query in name_queries:
            with self.subTest(query=query):
                response = get_name_response(query)
                self.assertIsNotNone(response)
                self.assertIn("chatbot", response.lower())
        
        # Test non-name
        response = get_name_response("hello")
        self.assertIsNone(response)
    
    def test_feeling_responses(self):
        """Test feeling response function"""
        feeling_queries = ['how are you', 'feeling', 'mood']
        
        for query in feeling_queries:
            with self.subTest(query=query):
                response = get_feeling_response(query)
                self.assertIsNotNone(response)
                self.assertIn("well", response.lower())
        
        # Test non-feeling
        response = get_feeling_response("hello")
        self.assertIsNone(response)
    
    def test_default_response(self):
        """Test default response function"""
        random_inputs = ['xyz123', 'random gibberish', 'asdf', 'qwerty']
        
        for random_input in random_inputs:
            with self.subTest(random_input=random_input):
                response = get_default_response(random_input)
                self.assertIsNotNone(response)
                self.assertIn("not sure", response.lower())
    
    def test_case_insensitivity(self):
        """Test that responses work regardless of case"""
        # Test uppercase
        response = get_greeting_response("HELLO")
        self.assertIsNotNone(response)
        
        # Test mixed case
        response = get_weather_response("What's the WEATHER like?")
        self.assertIsNotNone(response)
        
        # Test title case
        response = get_name_response("What's Your Name?")
        self.assertIsNotNone(response)
    
    def test_empty_input(self):
        """Test handling of empty input"""
        response = get_greeting_response("")
        self.assertIsNone(response)
        
        response = get_default_response("")
        self.assertIsNotNone(response)
    
    def test_whitespace_handling(self):
        """Test handling of input with extra whitespace"""
        response = get_greeting_response("  hello  ")
        self.assertIsNotNone(response)
        
        response = get_weather_response("  weather  ")
        self.assertIsNotNone(response)

class TestChatbotIntegration(unittest.TestCase):
    """Integration tests for the chatbot"""
    
    @patch('builtins.input', side_effect=['hello', 'what time is it?', 'bye'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_chatbot_conversation(self, mock_stdout, mock_input):
        """Test a complete conversation flow"""
        from chatbot import chatbot
        
        # This would normally run the chatbot, but we're mocking input
        # For now, we'll test the individual functions
        response1 = get_greeting_response("hello")
        response2 = get_time_response("what time is it?")
        response3 = get_farewell_response("bye")
        
        self.assertIsNotNone(response1)
        self.assertIsNotNone(response2)
        self.assertIsNotNone(response3)

def run_tests():
    """Run all tests and display results"""
    print("🧪 Running Chatbot Tests...")
    print("=" * 50)
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestChatbot)
    suite.addTests(loader.loadTestsFromTestCase(TestChatbotIntegration))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print("\n" + "=" * 50)
    print("📊 Test Summary:")
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    
    if result.failures:
        print("\n❌ Failures:")
        for test, traceback in result.failures:
            print(f"  - {test}: {traceback}")
    
    if result.errors:
        print("\n❌ Errors:")
        for test, traceback in result.errors:
            print(f"  - {test}: {traceback}")
    
    if not result.failures and not result.errors:
        print("\n✅ All tests passed!")
    
    return result.wasSuccessful()

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
