from helpers.constants import greetings

def parse_purchase_amount(amount):
  cleaned = amount.replace("$", "")
  return float(cleaned)

def clean_command(command):
  if (command.startswith(':')):
    return command[1:].strip()

  return command.strip()

def is_greeting(command):
  return command in greetings()
