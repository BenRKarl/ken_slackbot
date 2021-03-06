def convert_to_list(cursor_object):
  purchase_list = list(cursor_object)
  cursor_object.close()
  return purchase_list

def summate_purchases(purchase_list):
  if len(purchase_list) == 0:
    return 0
  elif len(purchase_list) == 1:
    return purchase_list[0]["amount"]
  else:
    totals = map(lambda a: a["amount"], purchase_list)
    return reduce(lambda a, b: a + b, totals)

def filter_by_current_month(purchase_list, month_number, year_number):
  filtered = []

  for purchase in purchase_list:
    if purchase["date"].month == month_number and purchase["date"].year == year_number:
      filtered.append(purchase)

  return filtered

def check_equal(totals_list):
  total_values = map(lambda summary: summary[1], totals_list)
  total_sum = reduce(lambda acc, total: acc + total, total_values)
  average = total_sum / len(totals_list)
  return average == totals_list[0][1]

def get_biggest_spender(totals_list):
  biggest_spender = None
  highest_amount = 0

  if check_equal(totals_list):
    return None

  for total in totals_list:
    spent = total[1]

    if spent > highest_amount:
      highest_amount = spent
      biggest_spender = total

  return biggest_spender

def get_debtor(totals_list):
  debtor = None
  lowest_amount = None

  if check_equal(totals_list):
    return None

  for total in totals_list:
    spent = total[1]

    if lowest_amount == None:
      lowest_amount = spent

    if spent <= lowest_amount:
      lowest_amount = spent
      debtor = total

  return debtor

def get_debt_summary(biggest_spender, debtor):
  if biggest_spender == None or debtor == None:
    return None

  biggest_spender_name = biggest_spender[0]
  debtor_name = debtor[0]
  difference = biggest_spender[1] - debtor[1]
  amount_owed = difference / 2

  return (debtor_name, biggest_spender_name, amount_owed)

def build_deletion_message(purchase):
  amount = purchase["amount"]
  description = purchase["description"]
  return "your purchase of $" + str(amount) + " on " + description + " was deleted from the database."

def list_purchases_message(purchase_list):
  message = "this month you spent:\n"

  for purchase in purchase_list:
    amount = purchase["amount"]
    description = purchase["description"]
    item = "$" + str(amount) + " on " + description + "\n"
    message += item

  return message
