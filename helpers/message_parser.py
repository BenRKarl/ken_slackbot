def parse_purchase_amount(amount):
  cleaned = amount.replace("$", "")
  return float(cleaned)

def clean_command(command):
  if (command.startswith(':')):
    return command[1:].strip()

  return command.strip()