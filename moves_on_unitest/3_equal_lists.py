import unittest

class ListEqualityTest(unittest.TestCase):

    def test_equal_lists(self):
        self.assertEqual([1, 2, 3], [1, 2, 3])
        self.assertEqual(['a', 'b', 'c'], ['a', 'b', 'c'])

    def test_unequal_lists(self):
        self.assertNotEqual([1, 2, 3], [1, 2, 4])
        self.assertNotEqual(['a', 'b', 'c'], ['a', 'b', 'd'])


if __name__ == '__main__':
    unittest.main()
