# Calculator CLI App

A command-line calculator application built in Python that supports basic arithmetic operations.

## Features

- **Addition (+)**: Add two numbers
- **Subtraction (-)**: Subtract second number from first number
- **Multiplication (*)**: Multiply two numbers
- **Division (/)**: Divide first number by second number (with zero division protection)
- **User-friendly interface**: Clear menu system with numbered options
- **Error handling**: Robust input validation and error messages
- **Exit option**: Clean way to exit the application

## Requirements

- Python 3.x
- No additional dependencies required

## How to Run

1. Navigate to the task1 directory
2. Run the calculator using Python:

```bash
python calculator.py
```

## Usage

1. The application will display a menu with available operations
2. Enter your choice (1-5):
   - 1: Addition
   - 2: Subtraction
   - 3: Multiplication
   - 4: Division
   - 5: Exit
3. For operations 1-4, you'll be prompted to enter two numbers
4. The result will be displayed
5. The menu will appear again for the next calculation
6. Choose option 5 to exit

## Example Output

```
Welcome to Calculator CLI App!

========================================
           CALCULATOR CLI APP
========================================
Available Operations:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Exit
========================================
Enter your choice (1-5): 1
Enter first number: 10
Enter second number: 5

Addition: 10 + 5 = 15.0
```

## Code Structure

The application follows a well-structured schema with:

- **Separate functions** for each operation (add, subtract, multiply, divide)
- **Input validation** with try-catch blocks
- **User input handling** using input() function
- **Main loop** that continues until user chooses to exit
- **Error handling** for division by zero and invalid inputs
- **Clean exit** with proper goodbye message

## Key Concepts Implemented

- **Functions**: Each operation is a separate function
- **Loops**: Main while loop for continuous operation
- **Conditionals**: if-elif-else statements for menu choices
- **CLI Interaction**: User input and output handling
- **Error Handling**: Try-catch blocks for robust operation 