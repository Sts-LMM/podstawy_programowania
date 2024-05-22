def outer_function():
    def inner_function():
        return "This is the inner function."
    
    return inner_function()

result = outer_function()
print(result)
