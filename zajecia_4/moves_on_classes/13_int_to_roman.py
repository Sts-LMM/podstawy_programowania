class RomanConverter:
    def __init__(self):
        self.roman_numerals = {
            1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X',
            40: 'XL', 50: 'L', 90: 'XC', 100: 'C',
            400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'
        }

    def int_to_roman(self, num):
        if num <= 0:
            return "Invalid number"
        
        result = ""
        for value, numeral in sorted(self.roman_numerals.items(), reverse=True):
            while num >= value:
                result += numeral
                num -= value
        return result

converter = RomanConverter()
number = 354
print(f"The Roman numeral representation of {number} is: {converter.int_to_roman(number)}")
