from helpers import message_parser
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

  def debt_summary_message(self, debt_summary):
    debtor_id = constants.get_id_by_name(debt_summary[0])
    spender_id = constants.get_id_by_name(debt_summary[1])
    amount_owed = str(debt_summary[2])
    return '<@' + debtor_id + '> owes <@' + spender_id + '> $' + amount_owed

  def get_help_message(self):
    return constants.get_help_message()

  def handle_command(self, command, channel_id, user_id):
    self.set_current_user_id(user_id)
    self.set_current_channel_id(channel_id)
    cleaned = message_parser.clean_command(command)

    if cleaned.startswith('i spent'):
      self.handle_new_purchase(cleaned)
    elif cleaned.startswith('how much'):
      self.handle_get_total_request()
    elif cleaned.startswith('who owes'):
      self.handle_debt_request()
    elif cleaned.startswith('help'):
      self.handle_help_request()
    else:
      self.send_message("I don't get it... Try writing your command like this: \"I spent 10.00 on oatmeal\"")

  def handle_new_purchase(self, command):
    self.add_purchase(command)
    self.send_message('Your purchase was added to the database!')

  def add_purchase(self, command):
    user_name = self.get_current_user_name()
    parts = command.split()
    amount = message_parser.parse_purchase_amount(parts[2])
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

  def handle_debt_request(self):
    recent_purchases = self.store.get_recent_purchase_totals()
    biggest_spender = parser.get_biggest_spender(recent_purchases)
    debtor = parser.get_debtor(recent_purchases)
    summary = parser.get_debt_summary(biggest_spender, debtor)
    message = self.debt_summary_message(summary)
    self.send_message(message)

  def handle_help_request(self):
    self.send_message(self.get_help_message())

  def send_message(self, message):
    user_id = self.get_current_user_id()
    channel_id = self.get_current_channel_id()
    user_callout = "<@" + user_id + ">"
    personalized = user_callout + ' ' + message
    self.chat.api_call("chat.postMessage", channel = channel_id, text = personalized, as_user = True)
