import store
EXAMPLE_COMMAND = "i spent"

class Ken:
  def setup(self, chat):
    self.chat = chat

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

    if command.startswith(EXAMPLE_COMMAND):
      self.add_purchase(command, user)

      response = 'Your purchase was added to the database!'
      self.send_message(channel, response, user)
    else:
      self.send_message(channel, response, user)

  def add_purchase(self, purchase, user):
    user = self.get_user_name(user)
    parts = purchase.split()
    amount = float(parts[2])
    description = ' '.join(parts[4:])

    store.insert_purchase({
      "name": user,
      "description": description,
      "amount": amount })
