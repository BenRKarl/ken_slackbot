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

non_november_purchase = {
    "date": datetime.datetime(2016, 5, 17, 2, 11, 45, 356000),
    "amount": 22.0,
    "_id": "582d32r117942gfds5f10dc8",
    "name": "Ben",
    "description": "may stuff" }

def single_purchase():
    return first_mock_purchase

def single_purchase_in_list():
    return [ first_mock_purchase ]

def multiple_purchases():
    return [ first_mock_purchase, second_mock_purchase ]

def purchases_in_different_months():
    return [ first_mock_purchase, non_november_purchase ]