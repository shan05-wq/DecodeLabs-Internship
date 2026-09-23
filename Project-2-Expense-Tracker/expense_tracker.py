def expense_tracker():
    total = 0   # Initialization outside loop

    while True:  # Continuous audit loop
        try:
            expense = input("Enter expense (or 'quit' to stop): ")

            # Kill switch
            if expense.lower() == "quit":
                print("Final Total Spent: $", total)
                break

            # type conversion
            expense = int(expense)

            # Accumulator pattern
            total += expense
            print("Current Total: $", total)

        except ValueError:
           
            print("Invalid input, please enter a number.")


# Run the tracker
expense_tracker()
