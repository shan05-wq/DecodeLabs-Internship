# Project 3
# Random Password Generator

import random
import string

# Ask the user for password length
length = int(input("Enter password length: "))

# Create a combination of letters and numbers
characters = string.ascii_letters + string.digits

# Generate the password
password = ""

for i in range(length):
    password += random.choice(characters)

# Display the generated password
print("Generated Password:", password)
