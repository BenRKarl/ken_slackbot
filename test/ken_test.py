import unittest

from bot.ken import Ken

class KenTests(unittest.TestCase):

  def test_get_user_name(self):
    test_bot = Ken()
    user_id = 'U0F19CBU2'
    user_name = 'Ben'
    self.assertEqual(test_bot.get_user_name(user_id), user_name)

if __name__ == '__main__':
    unittest.main()