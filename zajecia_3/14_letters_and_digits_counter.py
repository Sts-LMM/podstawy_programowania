def count_letters_digits(input_string):
    num_letters = 0
    num_digits = 0

    for char in input_string:
        if char.isalpha():
            num_letters += 1
        elif char.isdigit():
            num_digits += 1

    return num_letters, num_digits

sample_data = "Python 3.2"
letters, digits = count_letters_digits(sample_data)
print("Letters:", letters)
print("Digits:", digits)
