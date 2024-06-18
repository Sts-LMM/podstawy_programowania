def get_numerical_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Error: Invalid numerical input. Please try again.")

num1 = get_numerical_input("Enter the first number: ")
num2 = get_numerical_input("Enter the second number: ")

