def factorial_iterative(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def factorial_recursive(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


number = 12
print(f"Iterative: Factorial of {number} is {factorial_iterative(number)}")
print(f"Recursive: Factorial of {number} is {factorial_recursive(number)}")
