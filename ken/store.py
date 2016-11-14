import os
import datetime
from pymongo import MongoClient

mongodb_uri = os.environ.get("MONGODB_URI")

if mongodb_uri:
  client = MongoClient(mongodb_uri)
else:
  client = MongoClient()

db = client.purchase_collection
purchases = db.purchases

def insert_purchase(body):
  purchase = { "name": body["name"],
               "description": body["description"],
               "amount": body["amount"],
               "date": datetime.datetime.utcnow() }

  purchase_id = purchases.insert_one(purchase).inserted_id
  return purchase_id

def get_this_months_purchases(name):
  recent_purchases = []
  current_month = datetime.datetime.utcnow().month
  all_purchases = purchases.find({ "name": name })

  for purchase in all_purchases:
    if purchase["date"].month == current_month:
      recent_purchases.append(purchase)

  all_purchases.close()
  return recent_purchases

def get_this_months_total(name):
  purchases = get_this_months_purchases(name)
  return reduce(lambda a,b: a["amount"] + b["amount"], purchases)

