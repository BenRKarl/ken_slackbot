from helpers import parser
from helpers import constants

class Ken:

  def setup(self, options):
    self.chat = options["chat"]
    self.store = options["store"]

  def set_current_user_id(self, user_id):
    self.current_user_id = user_id

  def set_current_channel_id(self, channel_id):
    self.current_channel_id = channel_id

  def get_current_user_id(self):
    return self.current_user_id

  def get_current_channel_id(self):
    return self.current_channel_id

  def get_current_user_name(self):
    user_id = self.get_current_user_id()
    user_name = constants.get_name_by_id(user_id)
    return user_name

  def handle_command(self, command, channel_id, user_id):
    self.set_current_user_id(user_id)
    self.set_current_channel_id(channel_id)

    if command.startswith('i spent'):
      self.handle_new_purchase(command)
    elif command.startswith('how much'):
      self.handle_get_total_request()
    else:
      self.send_message("I don't get it... Try writing your command like this: \"I spent 10.00 on oatmeal\"")

  def handle_new_purchase(self, command):
    self.add_purchase(command)
    self.send_message('Your purchase was added to the database!')

  def add_purchase(self, command):
    user_name = self.get_current_user_name()
    parts = command.split()
    amount = float(parts[2])
    description = ' '.join(parts[4:])

    self.store.insert_purchase({
      "name": user_name,
      "description": description,
      "amount": amount
    })

  def handle_get_total_request(self):
    user_name = self.get_current_user_name()
    purchases = self.store.get_recent_purchases_by_name(user_name)
    total = parser.summate_purchases(purchases)
    self.send_message('So far this month you\'ve spent: ' + str(total))

  def send_message(self, message):
    user_id = self.get_current_user_id()
    channel_id = self.get_current_channel_id()
    user_callout = "<@" + user_id + ">"
    personalized = user_callout + ' ' + message
    self.chat.api_call("chat.postMessage", channel = channel_id, text = personalized, as_user = True)
