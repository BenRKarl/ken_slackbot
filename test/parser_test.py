import unittest
import datetime
from lib import parser

class ParserTests(unittest.TestCase):
    def test_summate_purchases(self):
        mock_purchases = [{ "date": datetime.datetime(2016, 11, 17, 2, 11, 45, 356000),
            "amount": 10.0,
            "_id": "582d11e117942bdbb5f10dc8",
            "name": "Ben",
            "description": "toast" },
          { "date": datetime.datetime(2016, 11, 17, 2, 11, 45, 356000),
            "amount": 25.0,
            "_id": "582d22e117942gfds5f10dc8",
            "name": "Ben",
            "description": "window cleaner" }
        ]

        total = parser.summate_purchases(mock_purchases)
        expected = 35.0
        self.assertEqual(total, expected)

if __name__ == '__main__':
    unittest.main()