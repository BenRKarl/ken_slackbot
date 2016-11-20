import unittest
import datetime
import mocks

from lib import parser

class ParserTests(unittest.TestCase):
    def test_summate_empty_list(self):
        total = parser.summate_purchases([])
        self.assertEqual(total, 0)

    def test_summate_single_purchase(self):
        purchase = mocks.single_purchase()
        total = parser.summate_purchases(purchase)
        self.assertEqual(total, 10.0)

    def test_summate_multiple_purchases(self):
        purchases = mocks.multiple_purchases()
        total = parser.summate_purchases(purchases)
        self.assertEqual(total, 35.0)

if __name__ == '__main__':
    unittest.main()