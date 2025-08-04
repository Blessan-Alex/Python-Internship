#!/usr/bin/env python3
"""
To-Do List Application (Console-based)
A simple to-do list manager with file persistence
"""

import os
from datetime import datetime

class TodoList:
    def __init__(self, filename="tasks.txt"):
        """Initialize the todo list with file storage"""
        self.filename = filename
        self.tasks = []
        self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from file"""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r', encoding='utf-8') as file:
                    for line in file:
                        task = line.strip()
                        if task:  # Skip empty lines
                            self.tasks.append(task)
        except FileNotFoundError:
            print(f"Creating new task file: {self.filename}")
        except Exception as e:
            print(f"Error loading tasks: {e}")
    
    def save_tasks(self):
        """Save tasks to file"""
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                for task in self.tasks:
                    file.write(task + '\n')
        except Exception as e:
            print(f"Error saving tasks: {e}")
    
    def add_task(self, task_description):
        """Add a new task to the list"""
        if task_description.strip():
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
            task = f"[{timestamp}] {task_description.strip()}"
            self.tasks.append(task)
            self.save_tasks()
            print(f"✓ Task added: {task_description}")
        else:
            print("✗ Task description cannot be empty!")
    
    def view_tasks(self):
        """Display all tasks"""
        if not self.tasks:
            print("No tasks found. Add some tasks to get started!")
            return
        
        print("\n" + "="*50)
        print("                    YOUR TO-DO LIST")
        print("="*50)
        
        for index, task in enumerate(self.tasks, 1):
            print(f"{index:2d}. {task}")
        
        print("="*50)
        print(f"Total tasks: {len(self.tasks)}")
    
    def remove_task(self, task_index):
        """Remove a task by its index"""
        try:
            task_index = int(task_index)
            if 1 <= task_index <= len(self.tasks):
                removed_task = self.tasks.pop(task_index - 1)
                self.save_tasks()
                print(f"✓ Removed task: {removed_task}")
            else:
                print(f"✗ Invalid task number. Please enter a number between 1 and {len(self.tasks)}")
        except ValueError:
            print("✗ Please enter a valid number!")
    
    def clear_all_tasks(self):
        """Clear all tasks"""
        if self.tasks:
            confirm = input("Are you sure you want to clear all tasks? (y/N): ").strip().lower()
            if confirm == 'y':
                self.tasks.clear()
                self.save_tasks()
                print("✓ All tasks cleared!")
            else:
                print("Operation cancelled.")
        else:
            print("No tasks to clear!")

def display_menu():
    """Display the main menu"""
    print("\n" + "="*40)
    print("           TO-DO LIST MANAGER")
    print("="*40)
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Clear All Tasks")
    print("5. Exit")
    print("="*40)

def main():
    """Main function to run the todo list application"""
    print("Welcome to To-Do List Manager!")
    print("Your tasks will be saved automatically.")
    
    todo = TodoList()
    
    while True:
        display_menu()
        
        try:
            choice = input("Enter your choice (1-5): ").strip()
            
            if choice == '1':
                task = input("Enter task description: ")
                todo.add_task(task)
                
            elif choice == '2':
                todo.view_tasks()
                
            elif choice == '3':
                if todo.tasks:
                    todo.view_tasks()
                    task_num = input("Enter task number to remove: ")
                    todo.remove_task(task_num)
                else:
                    print("No tasks to remove!")
                    
            elif choice == '4':
                todo.clear_all_tasks()
                
            elif choice == '5':
                print("Thank you for using To-Do List Manager!")
                print("Your tasks have been saved.")
                break
                
            else:
                print("Invalid choice! Please enter a number between 1 and 5.")
                
        except KeyboardInterrupt:
            print("\n\nTo-Do List interrupted. Your tasks have been saved.")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main() 