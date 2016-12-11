def parse_purchase_amount(amount):
  cleaned = amount.replace("$", "")
  return float(cleaned)