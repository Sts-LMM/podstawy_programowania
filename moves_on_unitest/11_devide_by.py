try:
    number = int(input("Enter a number: "))
    result = 100 / number
    print(result)
except ZeroDivisionError:
    print("Error: division by zero is not allowed.")
