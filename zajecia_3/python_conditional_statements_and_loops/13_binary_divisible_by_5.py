def binary_divisible_by_5(sequence):
    numbers = sequence.split(',')
    result = []
    for number in numbers:
        decimal_number = int(number, 2)
        if decimal_number % 5 == 0:
            result.append(number)
    return ','.join(result)

# Test data
sample_data = "0100,0011,1010,1001,1100,1001"

print("Input Sequence:", sample_data)
output = binary_divisible_by_5(sample_data)
print("Numbers divisible by 5:", output)
