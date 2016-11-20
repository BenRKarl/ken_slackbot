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