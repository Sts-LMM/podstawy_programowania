import unittest
import sqlite3

class DatabaseTest(unittest.TestCase):

    def test_query(self):
        conn = sqlite3.connect(':memory:')
        c = conn.cursor()
        c.execute('CREATE TABLE test (id INTEGER PRIMARY KEY, name TEXT)')
        c.execute('INSERT INTO test (name) VALUES (?)', ('John',))
        c.execute('INSERT INTO test (name) VALUES (?)', ('Mary',))
        c.execute('SELECT * FROM test')
        results = c.fetchall()
        self.assertEqual(results, [(1, 'John'), (2, 'Mary')])

if __name__ == '__main__':
    unittest.main()
