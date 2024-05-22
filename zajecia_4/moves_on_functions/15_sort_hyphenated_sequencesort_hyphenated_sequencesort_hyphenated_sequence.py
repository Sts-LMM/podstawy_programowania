def sort_hyphenated_sequence(sequence):
    words = sequence.split('-')
    words.sort()
    return '-'.join(words)

# Example
input_sequence = "green-red-yellow-black-white"
print(sort_hyphenated_sequence(input_sequence))  # black-green-red-white-yellow
