# To-Do List Application

A console-based to-do list manager built in Python with file persistence for storing tasks.

## Features

- **Add Tasks**: Add new tasks with timestamps
- **View Tasks**: Display all tasks with numbering
- **Remove Tasks**: Remove specific tasks by index
- **Clear All**: Clear all tasks with confirmation
- **File Persistence**: Tasks are automatically saved to `tasks.txt`
- **Error Handling**: Robust input validation and error messages
- **User-friendly Interface**: Clear menu system with numbered options

## Requirements

- Python 3.x
- No additional dependencies required

## How to Run

1. Navigate to the task2 directory
2. Run the to-do list application:

```bash
python todo.py
```

## Usage

1. The application will display a menu with available operations
2. Enter your choice (1-5):
   - 1: Add Task
   - 2: View Tasks
   - 3: Remove Task
   - 4: Clear All Tasks
   - 5: Exit
3. Tasks are automatically saved to `tasks.txt` file
4. Each task includes a timestamp when it was created

## Example Output

```
Welcome to To-Do List Manager!
Your tasks will be saved automatically.

========================================
           TO-DO LIST MANAGER
========================================
1. Add Task
2. View Tasks
3. Remove Task
4. Clear All Tasks
5. Exit
========================================
Enter your choice (1-5): 1
Enter task description: Complete Python assignment
✓ Task added: Complete Python assignment

==================================================
                    YOUR TO-DO LIST
==================================================
 1. [2024-01-15 14:30] Complete Python assignment
 2. [2024-01-15 14:35] Review database concepts
==================================================
Total tasks: 2
```

## File Structure

The application creates and manages:
- `todo.py`: Main application file
- `tasks.txt`: File storing all tasks (created automatically)

## Code Structure

The application follows object-oriented design with:

- **TodoList Class**: Main class handling all operations
- **File Handling**: Using `open()` with context managers (`with` statement)
- **List Operations**: Using `append()`, `pop()`, `clear()` methods
- **String Manipulation**: Using `strip()` for input cleaning
- **Error Handling**: Try-catch blocks for robust operation

## Key Concepts Implemented

### File Handling
- **Opening files**: Using `open()` function with different modes
- **File modes**: 'r' for reading, 'w' for writing
- **Context managers**: Using `with` statement for automatic file closing
- **Encoding**: UTF-8 encoding for proper character handling

### Lists
- **Storing tasks**: Using Python lists to store task data
- **List methods**: `append()`, `pop()`, `clear()`, `enumerate()`
- **Indexing**: 1-based indexing for user-friendly task numbers

### String Manipulation
- **strip()**: Removing whitespace from user input
- **String formatting**: Using f-strings for dynamic output
- **String concatenation**: Building task descriptions with timestamps

### Data Persistence
- **Automatic saving**: Tasks saved after each operation
- **File existence check**: Using `os.path.exists()`
- **Error handling**: Graceful handling of file operations

## Interview Questions Addressed

1. **How do you open and write to a file in Python?**
   - Using `open()` function with 'w' mode and `write()` method

2. **What are common file modes?**
   - 'r': Read mode, 'w': Write mode, 'a': Append mode

3. **What's the use of .strip()?**
   - Removes leading and trailing whitespace from strings

4. **How do lists work in Python?**
   - Dynamic arrays that can store multiple items of different types

5. **What is the difference between append() and insert()?**
   - `append()` adds to end, `insert()` adds at specific position

6. **How can you remove elements from a list?**
   - Using `pop()` by index or `remove()` by value

7. **What are context managers (with statement)?**
   - Automatic resource management, ensures files are properly closed

8. **How do you loop through a file line by line?**
   - Using `for line in file:` with `strip()` to clean lines

9. **What is a data structure?**
   - A way to organize and store data efficiently (lists, dictionaries, etc.)

10. **What happens if the file doesn't exist?**
    - Using try-catch blocks to handle FileNotFoundError gracefully 