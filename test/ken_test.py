import unittest

from bot.ken import Ken

class KenTests(unittest.TestCase):

  def test_get_ben_user_name(self):
    test_bot = Ken()
    user_id = 'U0F19CBU2'
    user_name = 'Ben'
    self.assertEqual(test_bot.get_user_name(user_id), user_name)

  def test_get_katie_user_name(self):
    test_bot = Ken()
    user_id = 'U0F1FNUCQ'
    user_name = 'Katie'
    self.assertEqual(test_bot.get_user_name(user_id), user_name)

  def test_set_current_user(self):
    test_bot = Ken()
    test_name = 'Test'
    test_bot.set_current_user(test_name)
    self.assertEqual(test_bot.current_user, test_name)

  def test_set_current_channel(self):
    test_bot = Ken()
    test_channel = 12345
    test_bot.set_current_channel(test_channel)
    self.assertEqual(test_bot.current_channel, test_channel)

  def test_get_current_user(self):
    test_bot = Ken()
    test_user = 'Test'
    test_bot.current_user = test_user
    returned = test_bot.get_current_user()
    self.assertEqual(returned, test_user)

  def test_get_current_channel(self):
    test_bot = Ken()
    test_channel = 12345
    test_bot.current_channel = test_channel
    returned = test_bot.get_current_channel()
    self.assertEqual(returned, test_channel)

if __name__ == '__main__':
    unittest.main()