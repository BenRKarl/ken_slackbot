import unittest
from helpers import command_parser

class CommandParserTests(unittest.TestCase):
  def test_parse_purchase_amount(self):
    mock_amount = '$40.9'
    expected = 40.90
    actual = command_parser.parse_purchase_amount(mock_amount)
    self.assertEqual(expected, actual)

  def test_clean_command(self):
    mock_command = ': test something : colon'
    expected = 'test something : colon'
    actual = command_parser.clean_command(mock_command)
    self.assertEqual(expected, actual)

  def test_clean_command(self):
    mock_command = 'test something : colon'
    expected = 'test something : colon'
    actual = command_parser.clean_command(mock_command)
    self.assertEqual(expected, actual)

  def test_is_greeting(self):
    mock_command = 'hello'
    actual = command_parser.is_greeting(mock_command)
    self.assertEqual(actual, True)

if __name__ == '__main__':
  unittest.main()