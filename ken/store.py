import datetime
from pymongo import MongoClient
client = MongoClient()
db = client.purchase_collection
purchases = db.purchases

def insert_purchase(body):
  purchase = { "name": body["buyer"],
               "description": body["description"],
               "amount": body["amount"],
               "date": datetime.datetime.utcnow() }

  purchase_id = purchases.insert_one(purchase).inserted_id
  return purchase_id

def get_purchase_by_name(name):
  return purchases.find_one({ "name": name })
