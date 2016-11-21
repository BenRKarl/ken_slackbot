import unittest
import datetime
from mocks import mock
from helpers import parser

class ParserTests(unittest.TestCase):
  def test_summate_empty_list(self):
    total = parser.summate_purchases([])
    self.assertEqual(total, 0)

  def test_summate_single_purchase(self):
    purchase = mock.single_purchase()
    total = parser.summate_purchases(purchase)
    self.assertEqual(total, 10.0)

  def test_summate_multiple_purchases(self):
    purchases = mock.multiple_purchases()
    total = parser.summate_purchases(purchases)
    self.assertEqual(total, 35.0)

  def test_filter_by_month(self):
    purchases = mock.purchases_in_different_months()
    month = 11
    filtered = parser.filter_by_month(purchases, month)
    self.assertEqual(len(filtered), 1)

  def test_determine_amount_owed(self):
    totals_list = [('Ben', 234), ('Katie', 120)]
    user_name = 'Ben'
    expected = ('Katie', 114)
    actual = parser.determine_amount_owed(user_name, totals_list)
    self.assertEqual(actual, expected)

if __name__ == '__main__':
  unittest.main()