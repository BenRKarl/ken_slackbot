class Ken:
  def setup(self, options):
    self.chat = options["chat"]
    self.store = options["store"]

  def send_message(self, channel, message, user):
    user_name = "<@" + user + ">"
    personalized = user_name + ' ' + message
    self.chat.api_call("chat.postMessage", channel = channel, text = personalized, as_user = True)

  def get_user_name(self, user_id):
    names = {
      "U0F19CBU2": "Ben"
    }

    return names[user_id]

  def handle_command(self, command, channel, user):
    response = "I don't get it... Try writing your command like this: \"I spent 10.00 on oatmeal\""

    if command.startswith('i spent'):
      self.add_purchase(command, user)
      response = 'Your purchase was added to the database!'
    elif command.startswith('how much'):
      name = self.get_user_name(user)
      total = self.store.get_this_months_total(name)
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
