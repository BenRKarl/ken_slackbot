def summate_purchases(purchase_list):
  if len(purchase_list) == 0:
    return 0
  elif len(purchase_list) == 1:
    return purchase_list[0]["amount"]
  else:
    totals = map(lambda a: a["amount"], purchase_list)
    return reduce(lambda a, b: a + b, totals)