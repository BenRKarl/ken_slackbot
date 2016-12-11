import unittest
import datetime
from mocks import mock
from helpers import parser
mock_totals_list = [('Ben', 230), ('Katie', 190)]

class ParserTests(unittest.TestCase):
  def test_summate_empty_list(self):
    total = parser.summate_purchases([])
    self.assertEqual(total, 0)

  def test_summate_single_purchase(self):
    purchase = mock.single_purchase_in_list()
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

  def test_get_biggest_spender(self):
    expected = mock_totals_list[0]
    actual = parser.get_biggest_spender(mock_totals_list)
    self.assertEqual(expected, actual)

  def test_get_debtor(self):
    expected = mock_totals_list[1]
    actual = parser.get_debtor(mock_totals_list)
    self.assertEqual(expected, actual)

  def test_get_amount_owed(self):
    biggest_spender = mock_totals_list[0]
    debtor = mock_totals_list[1]
    expected = ('Katie', 'Ben', 20)
    actual = parser.get_debt_summary(biggest_spender, debtor)
    self.assertEqual(expected, actual)

  def test(self):
    purchase = mock.single_purchase()
    expected = "Ben\'s purchase of $10.0 on toast was deleted from the database."
    actual = parser.build_deletion_message(purchase)
    self.assertEqual(expected, actual)

if __name__ == '__main__':
  unittest.main()