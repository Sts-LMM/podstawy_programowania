def are_all_digits_even(number):
    return all(int(digit) % 2 == 0 for digit in str(number))

even_digit_numbers = [str(number) for number in range(100, 401) if are_all_digits_even(number)]
print(",".join(even_digit_numbers))
