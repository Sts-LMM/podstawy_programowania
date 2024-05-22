def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Examples
print(is_palindrome("madam"))         # True
print(is_palindrome("nurses run"))    # True