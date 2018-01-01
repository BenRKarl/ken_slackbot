from helpers import command_parser
from helpers import cursor_parser
from helpers import constants
from helpers import events

class Ken:
  def __init__(self, options):
    self.chat = options["chat"]
    self.store = options["store"]
    self.dev = options["dev"]
    self.last_purchase = None

  def set_current_user_id(self, user_id):
    self.current_user_id = user_id

  def set_current_channel_id(self, channel_id):
    self.current_channel_id = channel_id

  def get_current_user_id(self):
    return self.current_user_id

  def get_current_channel_id(self):
    return self.current_channel_id

  def update_time(self, date):
    if events.monthly_reminder(date):
      self.handle_debt_reminder()

    if events.is_christmas(date):
      self.handle_merry_christmas(True)

  def handle_debt_reminder(self):
    self.handle_last_month_summary(True, True)

  def get_current_user_name(self):
    user_id = self.get_current_user_id()
    user_name = constants.get_name_by_id(user_id)
    return user_name

  def debt_summary_message(self, debt_summary):
    if debt_summary == None:
      return constants.no_one_owes_message()

    debtor_id = constants.get_id_by_name(debt_summary[0])
    spender_id = constants.get_id_by_name(debt_summary[1])
    amount_owed = str(debt_summary[2])
    return '<@' + debtor_id + '> owes <@' + spender_id + '> $' + amount_owed

  def last_month_summary_message(self, debt_summary):
    if debt_summary == None:
      return constants.no_one_owes_message()

    debtor_id = constants.get_id_by_name(debt_summary[0])
    spender_id = constants.get_id_by_name(debt_summary[1])
    amount_owed = str(debt_summary[2])
    return 'last month <@' + debtor_id + '> owed <@' + spender_id + '> $' + amount_owed

  def get_help_message(self):
    return constants.get_help_message()

  def deletion_failed_message(self):
    return constants.no_purchase_response()

  def default_response(self):
    return constants.default_response()

  def handle_command(self, command, channel_id, user_id):
    self.set_current_user_id(user_id)
    self.set_current_channel_id(channel_id)
    cleaned = command_parser.clean_command(command)

    if cleaned.startswith('i spent'):
      self.handle_new_purchase(cleaned)
      self.handle_debt_request()
    elif cleaned.startswith('how much'):
      self.handle_get_total_request()
    elif cleaned.startswith('who owes'):
      self.handle_debt_request()
    elif cleaned.startswith('help'):
      self.handle_help_request()
    elif cleaned.startswith('delete'):
      self.handle_purchase_deletion()
    elif cleaned.startswith('list'):
      self.handle_purchase_list()
    elif cleaned.startswith('thank'):
      self.handle_thank_you()
    elif cleaned.startswith('last month'):
      self.handle_last_month_summary()
    elif cleaned.startswith('poo'):
      self.handle_poo_request()
    elif command_parser.is_greeting(cleaned):
      self.handle_greeting()
    elif cleaned.startswith('merry christmas'):
      self.handle_merry_christmas()
    else:
      self.send_message(self.default_response())

  def handle_new_purchase(self, command):
    self.add_purchase(command)
    self.send_message('Your purchase was added to the database!')

  def handle_poo_request(self):
    self.send_message(':poop:')

  def handle_greeting(self):
    random_greeting = constants.get_greeting()
    self.send_message(random_greeting)

  def handle_merry_christmas(self, generalize=False):
    self.send_message(constants.merry_christmas(), generalize)

  def add_purchase(self, command):
    user_name = self.get_current_user_name()
    parts = command.split()
    amount = command_parser.parse_purchase_amount(parts[2])
    description = ' '.join(parts[4:])

    self.last_purchase = self.store.insert_purchase({
      "name": user_name,
      "description": description,
      "amount": amount
    })

  def handle_purchase_deletion(self):
    message = self.deletion_failed_message()
    deleted = self.store.delete_purchase(self.last_purchase)

    if (deleted != False):
      message = cursor_parser.build_deletion_message(deleted)

    self.send_message(message)

  def handle_get_total_request(self):
    user_name = self.get_current_user_name()
    purchases = self.store.get_recent_purchases_by_name(user_name)
    total = cursor_parser.summate_purchases(purchases)
    self.send_message('So far this month you\'ve spent: ' + str(total))

  def handle_purchase_list(self):
    user_name = self.get_current_user_name()
    purchases = self.store.get_recent_purchases_by_name(user_name)
    list_message = cursor_parser.list_purchases_message(purchases)
    self.send_message(list_message)

  def handle_debt_request(self):
    recent_purchases = self.store.get_recent_purchase_totals()
    biggest_spender = cursor_parser.get_biggest_spender(recent_purchases)
    debtor = cursor_parser.get_debtor(recent_purchases)
    summary = cursor_parser.get_debt_summary(biggest_spender, debtor)
    message = self.debt_summary_message(summary)
    self.send_message(message)

  def handle_last_month_summary(self, generalize=False, present_tense=False):
    recent_purchases = self.store.get_last_months_totals()
    biggest_spender = cursor_parser.get_biggest_spender(recent_purchases)
    debtor = cursor_parser.get_debtor(recent_purchases)
    summary = cursor_parser.get_debt_summary(biggest_spender, debtor)

    if present_tense:
      message = self.debt_summary_message(summary)
    else:
      message = self.last_month_summary_message(summary)

    self.send_message(message, generalize)

  def handle_help_request(self):
    self.send_message(self.get_help_message())

  def handle_thank_you(self):
    self.send_message(constants.you_are_welcome())

  def personalized_prefix(self):
    user_id = self.get_current_user_id()
    return "<@" + user_id + ">"

  def send_message(self, message, generalize=False):
    if generalize:
      prefix = constants.default_user()
      channel_id = constants.default_channel()
    else:
      prefix = self.personalized_prefix()
      channel_id = self.get_current_channel_id()

    if (self.dev):
      assembled_message = '[DEV] ' + prefix + ' ' + message
    else:
      assembled_message = prefix + ' ' + message

    self.chat.api_call("chat.postMessage", channel = channel_id, text = assembled_message, as_user = True)
