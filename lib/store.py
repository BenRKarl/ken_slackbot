import os
import datetime
import parser
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

def get_all_purchases_by_name(name):
  return purchases.find({ "name": name })

def get_recent_purchases_by_name(name):
  current_month = datetime.datetime.utcnow().month
  all_purchases = get_all_purchases_by_name(name)
  purchase_list = parser.convert_to_list(all_purchases)
  recent_purchases = parser.filter_by_month(all_purchases, current_month)
  return recent_purchases

def get_this_months_total(name):
  purchases = get_recent_purchases_by_name(name)
  return parser.summate_purchases(purchases)
