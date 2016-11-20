import unittest

from bot.ken import Ken

class KenTests(unittest.TestCase):

  def test_get_current_user_name(self):
    test_bot = Ken()
    user_id = 'U0F19CBU2'
    test_bot.set_current_user_id(user_id)
    self.assertEqual(test_bot.get_current_user_name(), 'Ben')

  def test_set_current_user(self):
    test_bot = Ken()
    test_name = 'Test'
    test_bot.set_current_user_id(test_name)
    self.assertEqual(test_bot.current_user_id, test_name)

  def test_set_current_channel(self):
    test_bot = Ken()
    test_channel = 12345
    test_bot.set_current_channel_id(test_channel)
    self.assertEqual(test_bot.current_channel_id, test_channel)

  def test_get_current_user(self):
    test_bot = Ken()
    test_user = 'Test'
    test_bot.current_user_id = test_user
    returned = test_bot.get_current_user_id()
    self.assertEqual(returned, test_user)

  def test_get_current_channel(self):
    test_bot = Ken()
    test_channel = 12345
    test_bot.current_channel_id = test_channel
    returned = test_bot.get_current_channel_id()
    self.assertEqual(returned, test_channel)

if __name__ == '__main__':
    unittest.main()