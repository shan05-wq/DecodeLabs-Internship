# Project 4
# General Knowledge Quiz

score = 0

# Question 1
answer = input("1. What is the capital of France? ").strip().lower()

if answer == "paris":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Question 2
answer = input("2. How many days are there in a week? ").strip().lower()

if answer == "7":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Question 3
answer = input("3. Which planet is known as the Red Planet? ").strip().lower()

if answer == "mars":
    print("Correct!")
    score += 1
else:
    print("Wrong!")

# Final score
print("\nFinal Score:", score, "/ 3")
