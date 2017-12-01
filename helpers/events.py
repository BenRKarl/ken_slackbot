def monthly_reminder(date):
  first_day = date.day == 1
  eight_am_ET = date.hour == 5
  zero_min = date.minute == 0
  zero_sec = date.second == 0

  return first_day & eight_am_ET & zero_min & zero_sec

def is_christmas(date):
  is_december = date.month == 12
  is_twentyfifth = date.day == 25
  eight_am_ET = date.hour == 12
  zero_min = date.minute == 0
  zero_sec = date.second == 0

  return is_december & is_twentyfifth & eight_am_ET & zero_min & zero_sec
