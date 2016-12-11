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

def filter_by_month(purchase_list, month_number):
  filtered = []

  for purchase in purchase_list:
    if purchase["date"].month == month_number:
      filtered.append(purchase)

  return filtered

def get_biggest_spender(totals_list):
  biggest_spender = None
  highest_amount = 0

  for total in totals_list:
    spent = total[1]

    if spent > highest_amount:
      highest_amount = spent
      biggest_spender = total

  return biggest_spender

def get_debtor(totals_list):
  debtor = None
  lowest_amount = None

  for total in totals_list:
    spent = total[1]

    if lowest_amount == None:
      lowest_amount = spent

    if spent < lowest_amount:
      lowest_amount = spent
      debtor = total

  return debtor

def get_debt_summary(biggest_spender, debtor):
  biggest_spender_name = biggest_spender[0]
  debtor_name = debtor[0]
  difference = biggest_spender[1] - debtor[1]
  amount_owed = difference / 2
  return (debtor_name, biggest_spender_name, amount_owed)

def parse_purchase_amount(amount):
  cleaned = amount.replace("$", "")
  return float(cleaned)
