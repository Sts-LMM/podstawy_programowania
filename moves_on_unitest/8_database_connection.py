import unittest
import sqlite3

class DatabaseTest(unittest.TestCase):

    def test_connection(self):
        conn = sqlite3.connect(':memory:')
        self.assertIsNotNone(conn)

if __name__ == '__main__':
    unittest.main()
