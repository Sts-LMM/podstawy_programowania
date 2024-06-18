def divide(a, b):
    try:
        result = a / b
        print("The result of dividing", a, "by", b, "is", result)
    except ArithmeticError:
        print("Error: Arithmetic error occurred.")

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

divide(a, b)
