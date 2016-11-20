from helpers import parser

class Ken:
  def setup(self, options):
    self.chat = options["chat"]
    self.store = options["store"]

  def set_current_user(self, user_name):
    self.current_user = user_name

  def set_current_room(self, room_id):
    self.current_room = room_id

  def get_current_user(self):
    return self.current_user

  def get_current_room(self):
    return self.current_room

  def send_message(self, channel, message, user):
    user_name = "<@" + user + ">"
    personalized = user_name + ' ' + message
    self.chat.api_call("chat.postMessage", channel = channel, text = personalized, as_user = True)

  def get_user_name(self, user_id):
    names = {
      "U0F19CBU2": "Ben",
      "U0F1FNUCQ": "Katie"
    }

    return names[user_id]

  def handle_command(self, command, channel, user):
    response = "I don't get it... Try writing your command like this: \"I spent 10.00 on oatmeal\""

    if command.startswith('i spent'):
      self.add_purchase(command, user)
      response = 'Your purchase was added to the database!'
    elif command.startswith('how much'):
      name = self.get_user_name(user)
      purchases = self.store.get_recent_purchases_by_name(name)
      total = parser.summate_purchases(purchases)
      response = 'So far this month you\'ve spent: ' + str(total)

    self.send_message(channel, response, user)

  def add_purchase(self, purchase, user):
    user = self.get_user_name(user)
    parts = purchase.split()
    amount = float(parts[2])
    description = ' '.join(parts[4:])

    self.store.insert_purchase({
      "name": user,
      "description": description,
      "amount": amount })
