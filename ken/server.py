import time
import os
import store
from slackclient import SlackClient
from ken import Ken

BOT_ID = os.environ.get("BOT_ID")
AT_BOT = "<@" + BOT_ID + ">"
slack_client = SlackClient(os.environ.get("SLACK_BOT_TOKEN"))

def parse_slack_output(slack_rtm_output):
  output_list = slack_rtm_output

  if output_list and len(output_list) > 0:
    for output in output_list:
      if output and 'text' in output and AT_BOT in output['text']:
        return output['text'].split(AT_BOT)[1].strip().lower(), \
               output['channel'], \
               output['user']

  return None, None, None

if __name__ == "__main__":
  READ_WEBSOCKET_DELAY = 1

  if slack_client.rtm_connect():
    ken = Ken()
    ken.setup({
      "chat": slack_client,
      "store": store })

    print("Ken is listening!")

    while True:
      command, channel, user = parse_slack_output(slack_client.rtm_read())

      if command and channel:
        ken.handle_command(command, channel, user)

      time.sleep(READ_WEBSOCKET_DELAY)

  else:
    print("Connection failed. Invalid Slack token or Bot ID.")
