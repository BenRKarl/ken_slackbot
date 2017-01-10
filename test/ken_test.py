import unittest
from unittest.mock import MagicMock
from mocks import mock_store

from bot.ken import Ken
from helpers import constants

mock_user_id = 'U0F19CBU2'
mock_channel_id = 12345
mock_user_name = 'Test'

def new_ken(**args):
    return Ken({
        'chat': args['chat'],
        'store': args['store'],
        'dev': args['dev'] })

class KenTests(unittest.TestCase):
  def test_get_current_user_name(self):
    test_bot = new_ken(chat=MagicMock(), store=mock_store, dev=False)
    test_bot.set_current_user_id(mock_user_id)
    self.assertEqual(test_bot.get_current_user_name(), 'Ben')

  def test_set_current_user_id(self):
    test_bot = new_ken(chat=MagicMock(), store=mock_store, dev=False)
    test_bot.set_current_user_id(mock_user_name)
    self.assertEqual(test_bot.current_user_id, mock_user_name)

  def test_set_current_channel_id(self):
    test_bot = new_ken(chat=MagicMock(), store=mock_store, dev=False)
    test_bot.set_current_channel_id(mock_channel_id)
    self.assertEqual(test_bot.current_channel_id, mock_channel_id)

  def test_get_current_user_id(self):
    test_bot = new_ken(chat=MagicMock(), store=mock_store, dev=False)
    test_bot.current_user_id = mock_user_id
    returned = test_bot.get_current_user_id()
    self.assertEqual(returned, mock_user_id)

  def test_get_current_channel_id(self):
    test_bot = new_ken(chat=MagicMock(), store=mock_store, dev=False)
    test_channel = 12345
    test_bot.current_channel_id = test_channel
    returned = test_bot.get_current_channel_id()
    self.assertEqual(returned, test_channel)

  def test_debt_summary_message(self):
    test_bot = new_ken(chat=MagicMock(), store=mock_store, dev=False)
    test_bot.handle_command('who owes', 'U0F19CBU2', 'C0F19CV96')
    test_bot.chat.api_call.assert_called_with('chat.postMessage',
                                              as_user=True,
                                              channel='U0F19CBU2',
                                              text='<@C0F19CV96> <@U0F1FNUCQ> owes <@U0F19CBU2> $25.0')

  def test_last_month_summary_message(self):
    test_bot = new_ken(chat=MagicMock(), store=mock_store, dev=False)
    test_bot.handle_command('last month', 'U0F19CBU2', 'C0F19CV96')
    test_bot.chat.api_call.assert_called_with('chat.postMessage',
                                              as_user=True,
                                              channel='U0F19CBU2',
                                              text='<@C0F19CV96> last month <@U0F1FNUCQ> owed <@U0F19CBU2> $25.0')

  def test_get_help_message(self):
    test_bot = new_ken(chat=MagicMock(), store=mock_store, dev=False)
    actual = test_bot.get_help_message()
    expected = constants.get_help_message()
    self.assertEqual(expected, actual)

  def test_deletion_failed_message(self):
    test_bot = new_ken(chat=MagicMock(), store=mock_store, dev=False)
    actual = test_bot.deletion_failed_message()
    expected = constants.no_purchase_response()
    self.assertEqual(expected, actual)

  def test_default_message(self):
    test_bot = new_ken(chat=MagicMock(), store=mock_store, dev=False)
    actual = test_bot.default_response()
    expected = constants.default_response()
    self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main()