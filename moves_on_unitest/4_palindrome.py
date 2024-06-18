import unittest

class PalindromeTest(unittest.TestCase):

    def test_is_palindrome(self):
        self.assertTrue(is_palindrome("racecar"))
        self.assertTrue(is_palindrome("madam"))
        self.assertTrue(is_palindrome("121"))

    def test_is_not_palindrome(self):
        self.assertFalse(is_palindrome("racecarx"))
        self.assertFalse(is_palindrome("madamx"))
        self.assertFalse(is_palindrome("123"))

def is_palindrome(string):
    return string == string[::-1]


if __name__ == '__main__':
    unittest.main()