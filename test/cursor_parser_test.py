import unittest
import datetime
from mocks import mock
from helpers import cursor_parser
mock_totals_list = [('Ben', 230), ('Katie', 190)]

class CursorTests(unittest.TestCase):
  def test_summate_empty_list(self):
    total = cursor_parser.summate_purchases([])
    self.assertEqual(total, 0)

  def test_summate_single_purchase(self):
    purchase = mock.single_purchase_in_list()
    total = cursor_parser.summate_purchases(purchase)
    self.assertEqual(total, 10.0)

  def test_summate_multiple_purchases(self):
    purchases = mock.multiple_purchases()
    total = cursor_parser.summate_purchases(purchases)
    self.assertEqual(total, 35.0)

  def test_filter_by_month(self):
    purchases = mock.purchases_in_different_months()
    month = 11
    year = 2016
    filtered = cursor_parser.filter_by_current_month(purchases, month, year)
    self.assertEqual(len(filtered), 1)

  def test_get_biggest_spender(self):
    expected = mock_totals_list[0]
    actual = cursor_parser.get_biggest_spender(mock_totals_list)
    self.assertEqual(expected, actual)

  def test_check_equal(self):
    mock_totals_list = [('Katie', 0), ('Ben', 0)]
    expected = True
    actual = cursor_parser.check_equal(mock_totals_list)
    self.assertEqual(expected, actual)

  def test_check_equal_false(self):
    mock_totals_list = [('Katie', 2), ('Ben', 0)]
    expected = False
    actual = cursor_parser.check_equal(mock_totals_list)
    self.assertEqual(expected, actual)

  def test_get_debtor(self):
    expected = mock_totals_list[1]
    actual = cursor_parser.get_debtor(mock_totals_list)
    self.assertEqual(expected, actual)

  def test_get_debtor_no_totals(self):
    mock_totals_list = [('Katie', 0), ('Ben', 0)]
    actual = cursor_parser.get_debtor(mock_totals_list)
    self.assertEqual(None, actual)

  def test_get_debtor_order(self):
    mock_totals_list = [('Katie', 190), ('Ben', 230)]
    expected = mock_totals_list[0]
    actual = cursor_parser.get_debtor(mock_totals_list)
    self.assertEqual(expected, actual)

  def test_get_amount_owed(self):
    biggest_spender = mock_totals_list[0]
    debtor = mock_totals_list[1]
    expected = ('Katie', 'Ben', 20)
    actual = cursor_parser.get_debt_summary(biggest_spender, debtor)
    self.assertEqual(expected, actual)

  def test_get_amount_owed_none(self):
    biggest_spender = None
    debtor = None
    expected = None
    actual = cursor_parser.get_debt_summary(biggest_spender, debtor)
    self.assertEqual(expected, actual)

  def test_build_deletion_message(self):
    purchase = mock.single_purchase()
    expected = "your purchase of $10.0 on toast was deleted from the database."
    actual = cursor_parser.build_deletion_message(purchase)
    self.assertEqual(expected, actual)

  def test_list_purchases_message(self):
    purchases = mock.multiple_purchases()
    expected = "this month you spent:\n$10.0 on toast\n$25.0 on window cleaner\n"
    actual = cursor_parser.list_purchases_message(purchases)
    self.assertEqual(expected, actual)

if __name__ == '__main__':
  unittest.main()