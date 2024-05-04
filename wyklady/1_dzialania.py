import math

def add(a,b):
    c = a + b
    return c

def subtract(a,b):
    c = a - b
    return c

def multiply(a,b):
    c = a * b
    return c

def devide(a,b):
    c = a / b
    return c

def power(a,b):
    c = math.pow(a,b)
    return c

def sqrt(a):
    c = math.sqrt(a)
    return c

a = 5
b = 3
print(add(a,b))  
print(subtract(a,b))           
print(multiply(a,b))           
print(devide(a,b))           
print(power(a,b))           
print(sqrt(a))           