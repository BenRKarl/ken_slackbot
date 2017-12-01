import unittest
import datetime
from helpers import events

class EventsTests(unittest.TestCase):
  def test_monthly_reminder(self):
    date = datetime.datetime(2016, 12, 1, 5, 0, 0, 0)
    actual = events.monthly_reminder(date)
    self.assertEqual(actual, True)

  def test_monthly_reminder_false(self):
    date = datetime.datetime(2016, 12, 2, 5, 0, 0, 0)
    actual = events.monthly_reminder(date)
    self.assertEqual(actual, False)

  def test_is_christmas(self):
    date = datetime.datetime(2017, 12, 25, 12, 0, 0, 0)
    actual = events.is_christmas(date)
    self.assertEqual(actual, True)

if __name__ == '__main__':
    unittest.main()
