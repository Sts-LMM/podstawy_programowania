import unittest
import os

class FileExistenceTest(unittest.TestCase):

    def setUp(self):
        with open('test.txt', 'w'):
            pass

    def tearDown(self):
        os.remove('test.txt')

    def test_file_exists(self):
        self.assertTrue(os.path.isfile('test.txt'))

    def test_file_does_not_exist(self):
        self.assertFalse(os.path.isfile('non_existent_file.txt'))


if __name__ == '__main__':
    unittest.main()
