# Python Developer Internship Projects

This repository contains two Python CLI applications developed as part of a Python Developer Internship.

## Project Overview

This project demonstrates fundamental Python programming concepts through two practical applications:

1. **Calculator CLI App** - Basic arithmetic operations with user input
2. **To-Do List Application** - File-based task management with persistence

## Project Structure

```
broskies internship/
├── task1/
│   ├── calculator.py      # Calculator CLI application
│   ├── README.md         # Calculator documentation
│   └── task.txt          # Task requirements
├── task2/
│   ├── todo.py           # To-Do list application
│   ├── README.md         # To-Do list documentation
│   ├── task2.txt         # Task requirements
│   └── tasks.txt         # Persistent task storage (auto-generated)
└── README.md             # This file - project overview
```

## Task 1: Calculator CLI App

### Overview
A command-line calculator supporting basic arithmetic operations (+, -, *, /) with robust error handling and user-friendly interface.

### Key Features
- **Four Operations**: Addition, Subtraction, Multiplication, Division
- **Error Handling**: Division by zero protection and input validation
- **User Interface**: Clear menu system with numbered options
- **Input Validation**: Robust handling of invalid inputs
- **Clean Exit**: Proper application termination

### Key Concepts Demonstrated
- **Functions**: Separate functions for each operation
- **Loops**: Main while loop for continuous operation
- **Conditionals**: if-elif-else statements for menu choices
- **CLI Interaction**: User input and output handling
- **Error Handling**: Try-catch blocks for robust operation

### How to Run
```bash
cd task1
python calculator.py
```

## Task 2: To-Do List Application

### Overview
A console-based to-do list manager with file persistence, allowing users to add, view, remove, and clear tasks.

### Key Features
- **Task Management**: Add, view, remove, and clear tasks
- **File Persistence**: Automatic saving to `tasks.txt`
- **Timestamps**: Each task includes creation timestamp
- **User Interface**: Numbered menu system
- **Data Validation**: Input validation and error handling

### Key Concepts Demonstrated
- **File Handling**: Reading and writing files with context managers
- **Lists**: Dynamic data storage and manipulation
- **String Manipulation**: Using `strip()` and string formatting
- **Object-Oriented Design**: TodoList class for organization
- **Data Persistence**: Automatic file-based storage

### How to Run
```bash
cd task2
python todo.py
```

## Technical Requirements

### Prerequisites
- Python 3.x
- No additional dependencies required

### File Structure
- **task1/calculator.py**: Complete calculator implementation
- **task2/todo.py**: Complete to-do list implementation
- **task2/tasks.txt**: Auto-generated file for task persistence

## Learning Objectives

### Task 1 Learning Outcomes
- Understanding of basic Python functions and control structures
- Implementation of user input handling with `input()`
- Error handling with try-catch blocks
- Menu-driven CLI application design
- Basic arithmetic operations and validation

### Task 2 Learning Outcomes
- File I/O operations using `open()` and context managers
- List data structure manipulation (`append()`, `pop()`, `clear()`)
- String manipulation with `strip()` and formatting
- Object-oriented programming with classes
- Data persistence and file management
- Error handling for file operations

## Interview Preparation

Both tasks address common Python interview questions:

### Task 1 Questions
- How do you handle user input in Python?
- What are the basic control structures in Python?
- How do you implement error handling?
- What are functions and how do you use them?

### Task 2 Questions
- How do you open and write to a file in Python?
- What are common file modes?
- What's the use of `.strip()`?
- How do lists work in Python?
- What is the difference between `append()` and `insert()`?
- How can you remove elements from a list?
- What are context managers (with statement)?
- How do you loop through a file line by line?
- What is a data structure?
- What happens if the file doesn't exist?

## Code Quality Features

### Both Applications Include
- **Comprehensive Documentation**: Detailed docstrings and comments
- **Error Handling**: Robust exception handling
- **User-Friendly Interface**: Clear menus and helpful messages
- **Input Validation**: Proper validation of user inputs
- **Clean Code Structure**: Well-organized and readable code
- **Modular Design**: Separate functions for different operations

### Best Practices Implemented
- **PEP 8 Compliance**: Proper Python coding standards
- **Type Hints**: Clear function signatures
- **Exception Handling**: Graceful error recovery
- **Resource Management**: Proper file handling with context managers
- **User Experience**: Intuitive interface design

## Testing

Both applications have been tested and verified to work correctly:

### Calculator Testing
- ✅ All four arithmetic operations work correctly
- ✅ Division by zero protection
- ✅ Invalid input handling
- ✅ Menu navigation
- ✅ Clean exit functionality

### To-Do List Testing
- ✅ Task addition with timestamps
- ✅ Task viewing with numbering
- ✅ Task removal by index
- ✅ Clear all tasks with confirmation
- ✅ File persistence (tasks.txt)
- ✅ Error handling for invalid inputs

## Future Enhancements

### Calculator Potential Improvements
- Add more mathematical operations (power, square root, etc.)
- Implement calculation history
- Add support for complex numbers
- Include unit conversion features

### To-Do List Potential Improvements
- Add task categories/tags
- Implement task priority levels
- Add due dates and reminders
- Include task completion status
- Add search and filter functionality
- Implement task editing capability

## Conclusion

This project successfully demonstrates fundamental Python programming concepts through practical, working applications. Both tasks showcase different aspects of Python development:

- **Task 1** focuses on basic programming constructs and user interaction
- **Task 2** emphasizes file handling, data structures, and persistence

The code is production-ready with proper error handling, documentation, and user experience considerations. These applications serve as excellent examples of Python CLI development and can be used as portfolio pieces or learning resources. 