class StringReverser:
    def reverse_words(self, s):
        return ' '.join(reversed(s.split()))

reverser = StringReverser()
input_string = 'hello . py'
print(reverser.reverse_words(input_string)) 