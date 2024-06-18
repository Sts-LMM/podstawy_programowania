import unittest

class SortedListTest(unittest.TestCase):

    def test_is_sorted(self):
        self.assertTrue(is_sorted([1, 2, 3, 4, 5]))
        self.assertTrue(is_sorted(['a', 'b', 'c', 'd', 'e']))

    def test_is_not_sorted(self):
        self.assertFalse(is_sorted([1, 3, 2, 4, 5]))
        self.assertFalse(is_sorted(['a', 'c', 'b', 'd', 'e']))

def is_sorted(list1):
    for i in range(1, len(list1)):
        if list1[i] < list1[i - 1]:
            return False

    return True


if __name__ == '__main__':
    unittest.main()
