import os
import datetime
from helpers import cursor_parser
from pymongo import MongoClient

mongodb_uri = os.environ.get("MONGODB_URI")

if mongodb_uri:
  client = MongoClient(mongodb_uri)
else:
  client = MongoClient()

db = client.get_default_database()
purchases = db.purchases

def insert_purchase(body):
  purchase = { "name": body["name"],
               "description": body["description"],
               "amount": body["amount"],
               "date": datetime.datetime.utcnow() }

  purchase_id = purchases.insert_one(purchase).inserted_id
  return purchase_id

def delete_purchase(purchase_id):
  if (purchase_id == None): return False
  cursor = purchases.find({ "_id": purchase_id})
  purchase_list = cursor_parser.convert_to_list(cursor)

  if (len(purchase_list) == 0): return False

  purchases.delete_one({"_id": purchase_id})
  return purchase_list[0]

def get_all_purchases_by_name(name):
  cursor = purchases.find({ "name": name })
  purchase_list = cursor_parser.convert_to_list(cursor)
  return purchase_list

def get_recent_purchases_by_name(name):
  current_month = datetime.datetime.utcnow().month
  all_purchases = get_all_purchases_by_name(name)
  recent_purchases = cursor_parser.filter_by_month(all_purchases, current_month)
  return recent_purchases

def get_last_months_purchases_by_name(name):
  last_month = get_last_month_num(datetime.datetime.utcnow().month)
  all_purchases = get_all_purchases_by_name(name)
  last_months_purchases = cursor_parser.filter_by_month(all_purchases, last_month)
  return last_months_purchases

def get_last_month_num(num):
  if (num == 1):
    return 12
  else:
    return num - 1

def get_recent_purchase_totals():
  bens_purchases = get_recent_purchases_by_name('Ben')
  katies_purchases = get_recent_purchases_by_name('Katie')
  bens_total = cursor_parser.summate_purchases(bens_purchases)
  katies_total = cursor_parser.summate_purchases(katies_purchases)
  return [('Ben', bens_total), ('Katie', katies_total)]

def get_last_months_totals():
  bens_purchases = get_last_months_purchases_by_name('Ben')
  katies_purchases = get_last_months_purchases_by_name('Katie')
  bens_total = cursor_parser.summate_purchases(bens_purchases)
  katies_total = cursor_parser.summate_purchases(katies_purchases)
  return [('Ben', bens_total), ('Katie', katies_total)]