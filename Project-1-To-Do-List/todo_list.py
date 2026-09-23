# Week 1 - Project 1
# To-Do List

tasks = []

while True:
    task = input("\nEnter a task (or type 'done' to finish): ")

    if task.lower() == "done":
        break

    tasks.append(task)

print("\nYour To-Do List:")

for task in tasks:
    print("-", task)
