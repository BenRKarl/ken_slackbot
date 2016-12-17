import unittest
import datetime
from helpers import events

class EventsTests(unittest.TestCase):
  def test_monthly_reminder(self):
    date = datetime.datetime(2016, 12, 1, 3, 0, 0, 0)
    actual = events.monthly_reminder(date)
    self.assertEqual(actual, True)

  def test_monthly_reminder_false(self):
    date = datetime.datetime(2016, 12, 2, 3, 0, 0, 0)
    actual = events.monthly_reminder(date)
    self.assertEqual(actual, False)

if __name__ == '__main__':
    unittest.main()
