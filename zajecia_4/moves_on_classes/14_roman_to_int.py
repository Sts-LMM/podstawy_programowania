class RomanToIntConverter:
    def __init__(self):
        self.roman_numerals = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }

    def roman_to_int(self, s):
        if not s:
            return 0

        total = 0
        prev_value = 0
        for char in reversed(s):
            value = self.roman_numerals[char]
            if value < prev_value:
                total -= value
            else:
                total += value
            prev_value = value
        return total

# Example usage:
converter = RomanToIntConverter()
roman_numeral = "CCXLVI"
print(f"The integer representation of {roman_numeral} is: {converter.roman_to_int(roman_numeral)}")
