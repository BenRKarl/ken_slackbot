import unittest
from helpers import message_parser

class MessageParserTests(unittest.TestCase):
  def test_parse_purchase_amount(self):
    mock_amount = '$40.9'
    expected = 40.90
    actual = message_parser.parse_purchase_amount(mock_amount)
    self.assertEqual(expected, actual)

  def test_clean_command(self):
    mock_command = ': test something : colon'
    expected = 'test something : colon'
    actual = message_parser.clean_command(mock_command)
    self.assertEqual(expected, actual)

if __name__ == '__main__':
  unittest.main()