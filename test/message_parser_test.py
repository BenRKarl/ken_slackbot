import unittest
from helpers import message_parser

class MessageParserTests(unittest.TestCase):
  def test_parse_purchase_amount(self):
    mock_amount = '$40.9'
    expected = 40.90
    actual = message_parser.parse_purchase_amount(mock_amount)
    self.assertEqual(expected, actual)

if __name__ == '__main__':
  unittest.main()