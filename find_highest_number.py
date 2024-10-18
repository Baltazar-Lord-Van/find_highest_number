highest_number = None

for i in range(5):
    user_input = input(f"Enter number{i + 1}: ")
    number = float(user_input)

    if highest_number is None:
        highest_number = number
    if number > highest_number:
        highest_number = number

print("The highest number is:", highest_number)