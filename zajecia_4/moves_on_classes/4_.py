import builtins

abs_function = builtins.abs

print("Documentation of the abs function:")
print(abs_function.__doc__)

number = -155
absolute_value = abs_function(number)
print("\nThe absolute value of -155 is:", absolute_value)
