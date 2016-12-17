def monthly_reminder(date):
  first_day = date.day == 1
  eight_am_ET = date.hour == 3
  zero_min = date.minute == 0
  zero_sec = date.second == 0

  return first_day & eight_am_ET & zero_min & zero_sec
