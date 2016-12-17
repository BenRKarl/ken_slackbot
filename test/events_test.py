import unittest
import datetime
from helpers import events

class EventsTests(unittest.TestCase):
  def test_monthly_reminder(self):
    date = datetime.datetime(2016, 12, 1, 4, 0, 0, 0)
    actual = events.monthly_reminder(date)
    self.assertEqual(actual, True)

if __name__ == '__main__':
    unittest.main()
