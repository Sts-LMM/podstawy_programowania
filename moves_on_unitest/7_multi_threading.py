import unittest

def add_floats(a: float, b: float, decimals: int = 2) -> float:
    return round(a + b, decimals)

class AddFloatsTest(unittest.TestCase):

    def test_add_floats(self):
        self.assertEqual(add_floats(0.1, 0.2), 0.3)
        self.assertEqual(add_floats(1.234, 5.678), 6.91)
        self.assertEqual(add_floats(-0.5, 0.75), 0.25)

if __name__ == '__main__':
    unittest.main()
