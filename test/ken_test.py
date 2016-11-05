import unittest
import ken

class MyTest(unittest.TestCase):
  def test(self):
    self.assertEqual(ken.test(), true)