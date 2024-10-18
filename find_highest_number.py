def find_highest_number():
    highest_number = None

    # Loops to collect 5 numbers from the user
    for i in range(5):
        while True:  # Loops until valid input is received
            user_input = input(f"Enter a number {i + 1}: ")
            try:
                number = float(user_input)
                break  # Exit the loop if the input is valid
            except ValueError:
                print("Invalid input! Please enter a number.")

        # Checks and update the highest number
        if highest_number is None:
            highest_number = number
        if number > highest_number:
            highest_number = number
        # Only uses "if statement"

    # Displays the highest number
    print("The highest number is:", highest_number)

# Calls the function
find_highest_number()
