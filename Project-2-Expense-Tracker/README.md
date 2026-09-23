
# Expense Tracker – Python Project 2

A simple command-line Expense Tracker built with Python.

This project allows users to enter their expenses continuously, keeps a running total, handles invalid input, and displays the final amount when the user chooses to quit.

## Features

- Add expenses through user input
- Continuously calculate total expenses
- Display the current total after each expense
- Stop the program using `quit`
- Handle invalid inputs using exception handling
- Prevent the program from crashing due to invalid input

## Concepts Practiced

This project helped me practice:

- Python functions
- `while` loops
- `if` statements
- `try-except`
- `ValueError` exception handling
- Type conversion using `int()`
- Accumulator pattern
- User input handling
- Basic defensive programming

## How It Works

1. The program starts with a total expense of `0`.
2. The user enters an expense.
3. The expense is converted into an integer.
4. The expense is added to the running total.
5. The current total is displayed.
6. The process continues until the user enters `quit`.
7. The final total is displayed before the program ends.

## Example

```text
Enter expense (or 'quit' to stop): 500
Current Total: $ 500

Enter expense (or 'quit' to stop): 1200
Current Total: $ 1700

Enter expense (or 'quit' to stop): 300
Current Total: $ 2000

Enter expense (or 'quit' to stop): quit
Final Total Spent: $ 2000








