# Week 1 - Project 1: To-Do List

A simple command-line To-Do List application built using Python.

## 📌 Project Overview

This is my first project during Week 1 of my internship at Decode Labs.

The program allows the user to enter multiple tasks and displays all the tasks in a To-Do List when the user types `done`.

## 🛠️ Technologies Used

- Python
- Lists
- While Loop
- For Loop
- Conditional Statements
- User Input

## ⚙️ How It Works

1. The program starts with an empty list.
2. The user enters a task.
3. Each task is stored in the list.
4. The user can continue adding tasks.
5. When the user types `done`, the program stops taking input.
6. Finally, all entered tasks are displayed as a To-Do List.
   
## 🎯 Learning Outcomes

Through this project, I learned and practiced:

- Creating and working with Python lists
- Taking user input using `input()`
- Using `while` and `for` loops
- Using conditional statements with `if`
- Using `break` to stop a loop
- Using `.lower()` to handle user input
- Storing and displaying multiple tasks

## 🚀 Future Improvements

In future versions, I would like to add:

- Delete tasks
- Edit existing tasks
- Mark tasks as completed
- Save tasks to a file
- Use Object-Oriented Programming (OOP)
- Add a graphical user interface (GUI)

## 💻 Code

```python
tasks = []

while True:
    task = input("\nEnter a task (or type 'done' to finish): ")

    if task.lower() == "done":
        break

    tasks.append(task)

print("\nYour To-Do List:")

for task in tasks:
    print("-", task)
