highest_number = None

for i in range(5):
    user_input = input(f"Enter number{i + 1}: ")
    try:
        number = float(user_input)
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue    
    
    if highest_number is None:
        highest_number = number
    if number > highest_number:
        highest_number = number

print("The highest number is:", highest_number)
