import inspect

def student(name, age, grade):
    return f"Student: {name}, Age: {age}, Grade: {grade}"

def display_argument_names(func):
    sig = inspect.signature(func)
    param_names = [param.name for param in sig.parameters.values()]
    return param_names

argument_names = display_argument_names(student)

print("Names of all arguments in the student function:")
print(argument_names)
