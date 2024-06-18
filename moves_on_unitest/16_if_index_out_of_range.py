numbers = [1, 2, 3, 4, 5]

index = int(input("Enter the index of the element to access: "))

try:
    element = numbers[index]
    print("The element at index", index, "is", element)
except IndexError:
    print("Error: The index", index, "is out of range.")