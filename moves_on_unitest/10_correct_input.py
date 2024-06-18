import unittest
import json

def parse_input(data):

  try:
    parsed_data = json.loads(data)

    if not isinstance(parsed_data, dict):
      raise ValueError("Input data must be a dictionary.")
    if "name" not in parsed_data:
      raise ValueError("Input data must contain a 'name' field.")
    if "age" not in parsed_data:
      raise ValueError("Input data must contain an 'age' field.")

    return parsed_data

  except ValueError as e:
    raise e


class ParseInputTest(unittest.TestCase):

  def test_valid_input(self):
    """Tests that the parse_input() function correctly parses and validates valid input data."""

    input_data = '{"name": "John", "age": 30}'
    parsed_data = parse_input(input_data)

    self.assertEqual(parsed_data, {"name": "John", "age": 30})

  def test_invalid_input(self):
    """Tests that the parse_input() function raises a ValueError when given invalid input data."""

    input_data = '{"name": "John"}'

    with self.assertRaises(ValueError):
      parse_input(input_data)


if __name__ == '__main__':
  unittest.main()
