import datetime

first_mock_purchase = {
    "date": datetime.datetime(2016, 11, 17, 2, 11, 45, 356000),
    "amount": 10.0,
    "_id": "582d11e117942bdbb5f10dc8",
    "name": "Ben",
    "description": "toast" }


second_mock_purchase = {
    "date": datetime.datetime(2016, 11, 17, 2, 11, 45, 356000),
    "amount": 25.0,
    "_id": "582d22e117942gfds5f10dc8",
    "name": "Ben",
    "description": "window cleaner" }

def single_purchase():
    return [ first_mock_purchase ]

def multiple_purchases():
    return [ first_mock_purchase, second_mock_purchase ]