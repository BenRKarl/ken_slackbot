import random

def default_channel():
  return 'C0F19CV96'

def default_user():
  return '<!here>'

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

def no_one_owes_message():
  return "No one owes anyone anything!"

def default_response():
  return "I don't understand... Enter *_@ken help_* for a list of commands."

def no_purchase_response():
  return "That purchase was not found or has already been deleted."

def get_help_message():
  return """Here are my commands:\n
  1. To save a purchase: *_@ken I spent 34.99 on tomatoes_*\n
  2. To check your monthly total: *_@ken how much_*\n
  3. To see who owes who: *_@ken who owes_*\n
  4. To delete the most recently added purchase: *_@ken delete_*\n
  5. To list all purchases made this month: *_@ken list_*\n
  6. To get a summary of last month: *_@ken last month_*"""

def you_are_welcome():
  responses = [
    "you're welcome!",
    "no problem!",
    "you got it!",
    "fo sho!",
    "any time!",
    "my pleasure!"
  ]

  return random.choice(responses)

def get_greeting():
  return random.choice(greetings())

def greetings():
  return [
    'hey',
    'hello',
    'whats up',
    'what up',
    'what\'s up',
    'what it is',
    'sup',
    'heyo',
    'howdy',
    'hi'
  ]

def merry_christmas():
  base = ''
  emojis = [
    ':christmas_tree:',
    ':santa:',
    ':santa::skin-tone-2:',
    ':santa::skin-tone-3:',
    ':santa::skin-tone-4:',
    ':santa::skin-tone-5:',
    ':santa::skin-tone-6:',
    ':gift:',
    ':ribbon:',
    ':snowflake:',
    ':snowman:'
  ]

  for i in xrange(100):
    base += random.choice(emojis) + ' '

  return base

