from pymongo import MongoClient
from datetime import datetime

client = MongoClient(host = "localhost", port = 27017)
my_db = client.store
item_collection = my_db.items

#insert some items
new_items = [
    {"name": "Apple", "sub-type": 1, "stock": 500, "cost": 0.20, "selling_price": 0.50,
    "sell_by": datetime(2019, 9, 1), "items_damaged": 0, "is_safe": True},
    {"name": "Banana", "sub-type": 1, "stock": 200, "cost": 0.10, "selling_price": 0.40,
    "sell_by": datetime(2019, 7, 31), "items_damaged": 10, "is_safe": True},
]

new_ids = item_collection.insert_many(new_items)

print("Inserted IDs and types")
for id in new_ids.inserted_ids:
    print(id)