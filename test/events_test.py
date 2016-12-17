from helpers import events
import datetime

class EventsTests(unittest.TestCase):
  def monthly_reminder_test(self):
    date = datetime.datetime(2016, 12, 1, 9, 0)
    actual = events.monthly_reminder(data)
    self.assertEqual(actual, True)

if __name__ == '__main__':
    unittest.main()
