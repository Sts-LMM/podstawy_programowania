class ParenthesesValidator:
    def is_valid(self, s):
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping.values():
                stack.append(char)
            elif char in mapping.keys():
                if not stack or mapping[char] != stack.pop():
                    return False
            else:
                return False
        
        return not stack

validator = ParenthesesValidator()
print(validator.is_valid("()"))        # Output: True
print(validator.is_valid("()[]{}"))    # Output: True
print(validator.is_valid("[)"))        # Output: False
print(validator.is_valid("({[)]"))     # Output: False
print(validator.is_valid("{{{"))       # Output: False
