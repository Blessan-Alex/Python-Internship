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

## Interview Questions & Answers

### Database Concepts

**1. What is normalization?**
Normalization is a database design technique that organizes data to reduce redundancy and dependency by dividing large tables into smaller ones and defining relationships between them. It follows specific rules (1NF, 2NF, 3NF, BCNF, etc.) to ensure data integrity and eliminate anomalies.

**2. Explain primary vs foreign key.**
- **Primary Key**: A unique identifier for each record in a table. It cannot be NULL and must be unique. Only one primary key per table.
- **Foreign Key**: A field that creates a link between two tables by referencing the primary key of another table. It maintains referential integrity.

**3. What are constraints?**
Constraints are rules applied to database columns to ensure data integrity:
- **NOT NULL**: Column cannot have NULL values
- **UNIQUE**: All values must be unique
- **PRIMARY KEY**: Unique identifier for each row
- **FOREIGN KEY**: References primary key of another table
- **CHECK**: Ensures values meet specific conditions
- **DEFAULT**: Sets default value for column

**4. What is a surrogate key?**
A surrogate key is an artificial primary key (usually auto-incrementing integer) that has no business meaning but serves as a unique identifier. It's independent of the data it identifies and is often used when natural keys are complex or change frequently.

**5. How do you avoid data redundancy?**
- **Normalization**: Follow database normalization rules
- **Use foreign keys**: Instead of duplicating data, reference it
- **Create lookup tables**: For repeated values
- **Use computed columns**: Instead of storing derived data
- **Proper indexing**: To avoid storing redundant indexes

**6. What is ER diagram?**
Entity-Relationship (ER) diagram is a visual representation of database structure showing:
- **Entities**: Tables/objects (represented as rectangles)
- **Attributes**: Properties of entities (represented as ovals)
- **Relationships**: Connections between entities (represented as diamonds)
- **Cardinality**: One-to-one, one-to-many, many-to-many relationships

**7. What are the types of relationships in DBMS?**
- **One-to-One (1:1)**: One record in first table relates to exactly one record in second table
- **One-to-Many (1:N)**: One record in first table relates to multiple records in second table
- **Many-to-One (N:1)**: Multiple records in first table relate to one record in second table
- **Many-to-Many (M:N)**: Multiple records in both tables relate to each other (requires junction table)

**8. Explain the purpose of AUTO_INCREMENT.**
AUTO_INCREMENT automatically generates a unique, sequential number for each new record inserted into a table. It's commonly used for primary keys to ensure each record has a unique identifier without manual input.

**9. What is the default storage engine in MySQL?**
**InnoDB** is the default storage engine in MySQL (since MySQL 5.5). It provides ACID compliance, foreign key support, and crash recovery capabilities.

**10. What is a composite key?**
A composite key is a primary key that consists of two or more columns combined to create a unique identifier. It's used when no single column can uniquely identify a record, but the combination of multiple columns can. 