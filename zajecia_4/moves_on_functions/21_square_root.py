import time

def square_root(x):
    return x ** 0.5

def invoke_after_delay(func, arg, delay):
    time.sleep(delay / 1000)
    return func(arg)

print("Square root after specific milliseconds:")
print(invoke_after_delay(square_root, 16, 1000))  
print(invoke_after_delay(square_root, 100, 2000))
print(invoke_after_delay(square_root, 25000, 3000))  
