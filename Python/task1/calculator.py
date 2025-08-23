#!/usr/bin/env python3
"""
Calculator CLI App
A command-line calculator supporting basic operations (+, -, *, /)
"""

def add(num1, num2):
    """Add two numbers"""
    return num1 + num2

def subtract(num1, num2):
    """Subtract second number from first number"""
    return num1 - num2

def multiply(num1, num2):
    """Multiply two numbers"""
    return num1 * num2

def divide(num1, num2):
    """Divide first number by second number"""
    if num2 == 0:
        return "Error: Cannot divide by zero!"
    return num1 / num2

def display_menu():
    """Display the calculator menu"""
    print("\n" + "="*40)
    print("           CALCULATOR CLI APP")
    print("="*40)
    print("Available Operations:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("="*40)

def get_numbers():
    """Get two numbers from user input"""
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        return num1, num2
    except ValueError:
        print("Error: Please enter valid numbers!")
        return None, None

def main():
    """Main function to run the calculator"""
    print("Welcome to Calculator CLI App!")
    
    while True:
        display_menu()
        
        try:
            choice = input("Enter your choice (1-5): ").strip()
            
            if choice == '5':
                print("Thank you for using Calculator CLI App!")
                break
            elif choice in ['1', '2', '3', '4']:
                num1, num2 = get_numbers()
                
                if num1 is None or num2 is None:
                    continue
                
                if choice == '1':
                    result = add(num1, num2)
                    operation = "Addition"
                    symbol = "+"
                elif choice == '2':
                    result = subtract(num1, num2)
                    operation = "Subtraction"
                    symbol = "-"
                elif choice == '3':
                    result = multiply(num1, num2)
                    operation = "Multiplication"
                    symbol = "*"
                elif choice == '4':
                    result = divide(num1, num2)
                    operation = "Division"
                    symbol = "/"
                
                print(f"\n{operation}: {num1} {symbol} {num2} = {result}")
                
            else:
                print("Invalid choice! Please enter a number between 1 and 5.")
                
        except KeyboardInterrupt:
            print("\n\nCalculator interrupted. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main() 