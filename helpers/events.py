def monthly_reminder(date):
  first_day = date.day == 1
  nine_am = date.hour == 4
  zero_min = date.minute == 0
  zero_sec = date.second == 0
  zero_ms = date.microsecond == 0

  return first_day & nine_am & zero_min & zero_sec & zero_ms
