# Project 3 — Random Password Generator

## 📌 Overview

This is a simple Python-based Random Password Generator developed as part of my Decode Labs Python Internship.

The program asks the user for a desired password length and generates a random password using letters and numbers.

## 🛠️ Technologies Used

* Python
* Random Module
* String Module
* Loops
* User Input
* Strings

## ⚙️ How It Works

1. The program asks the user to enter the desired password length.
2. It uses `string.ascii_letters` to create a combination of uppercase and lowercase letters.
3. It uses `string.digits` to include numbers.
4. The characters are combined into one character set.
5. The program randomly selects characters using `random.choice()`.
6. The selected characters are combined to create the password.
7. The generated password is displayed to the user.

## ▶️ How to Run

Make sure Python is installed on your computer.

Run the following command:

```bash
python random_password_generator.py
```

Then enter the desired password length when prompted.

### Example

```text
Enter password length: 10
Generated Password: aB7xP2mQ9z
```

## 📚 Learning Outcomes

Through this project, I practiced:

* Importing Python modules
* Using the `random` module
* Using the `string` module
* Working with strings
* Using `for` loops
* Taking user input
* Generating random values

## 🚀 Future Improvements

Future versions could include:

* Special characters
* Stronger password generation
* Password strength checking
* Option to generate multiple passwords
* A graphical user interface

## 👨‍💻 Internship

Developed during my Python Internship at Decode Labs.
