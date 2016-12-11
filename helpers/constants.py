def get_name_by_id(user_id):
  names = {
    "U0F19CBU2": "Ben",
    "U0F1FNUCQ": "Katie"
  }

  return names[user_id]

def get_id_by_name(name):
  ids = {
    "Ben": "U0F19CBU2",
    "Katie": "U0F1FNUCQ"
  }

  return ids[name]

def get_help_message():
  return """Here are my commands:\n
            1. To save a purchase: *_@ken I spent 34.99 on tomatoes_*\n
            2. To check your monthly total: *_@ken how much_*\n
            3. To see who owes who: *_@ken who owes_*\n
            4. To get help: *_@ken help_*"""