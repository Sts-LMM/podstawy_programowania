while True:
    try:
        number = int(input("Enter an integer: "))
    except ValueError:
        print("Invalid integer. Please try again.")
    else:
        print("You entered the integer:", number)
        break
