class StringProcessor:
    def __init__(self):
        self.string = ""

    def get_string(self):
        self.string = input("Enter a string: ")

    def print_string(self):
        print(self.string.upper())

processor = StringProcessor()
processor.get_string()
processor.print_string()
