from pymongo import MongoClient
from datetime import datetime

client = MongoClient(host = "localhost", port = 27017)
my_db = client.store
item_collection = my_db.items

new_item =  {"name": "Arsenic", "sub-type": 52, "stock": 70, "cost": 1.50, "selling_price": 10.00,
    "sell_by": datetime(2030, 12, 31), "items_damaged": 0, "is_safe": False}


new_id = item_collection.insert_one(new_item)
