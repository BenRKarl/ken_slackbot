import unittest
from bot.ken import Ken
mock_user_id = 'U0F19CBU2'
mock_channel_id = 12345
mock_user_name = 'Test'

class KenTests(unittest.TestCase):

  def test_get_current_user_name(self):
    test_bot = Ken()
    test_bot.set_current_user_id(mock_user_id)
    self.assertEqual(test_bot.get_current_user_name(), 'Ben')

  def test_set_current_user_id(self):
    test_bot = Ken()
    test_bot.set_current_user_id(mock_user_name)
    self.assertEqual(test_bot.current_user_id, mock_user_name)

  def test_set_current_channel_id(self):
    test_bot = Ken()
    test_bot.set_current_channel_id(mock_channel_id)
    self.assertEqual(test_bot.current_channel_id, mock_channel_id)

  def test_get_current_user_id(self):
    test_bot = Ken()
    test_bot.current_user_id = mock_user_id
    returned = test_bot.get_current_user_id()
    self.assertEqual(returned, mock_user_id)

  def test_get_current_channel_id(self):
    test_bot = Ken()
    test_channel = 12345
    test_bot.current_channel_id = test_channel
    returned = test_bot.get_current_channel_id()
    self.assertEqual(returned, test_channel)

if __name__ == '__main__':
    unittest.main()