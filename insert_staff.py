from pymongo import MongoClient
from datetime import datetime
from datetime import date

client = MongoClient(host = "localhost", port = 27017)
my_db = client.store
item_collection = my_db["staff"]

#insert staff details
new_staff = [
    {"_id": 1, "first_name": "Annie", "middle name(s)": "Penny", "surname": "Price", 
    "role": "Customer Assisstant", "salary": 21000, "store": "Newport"},
    {"_id": 2, "first_name": "Simon", "middle name(s)": "Oliver", "surname": "Davies", 
    "role": "Cleaner", "salary": 16000, "store": "Newport"},
    {"_id": 3, "first_name": "Laura", "middle name(s)": "Olivia", "surname": "Lewis", 
    "role": "Cleaner", "salary": 17000, "store": "Newport"},
    {"_id": 4, "first_name": "Carol", "middle name(s)": "Rachel Ashleigh", "surname": "Perkins", 
    "role": "Cashier", "salary": 18000, "store": "Cardiff"},
    {"_id": 5, "first_name": "Peter", "middle name(s)": "Edward Steven", "surname": "Thomas", 
    "role": "Site Manager", "salary": 40000, "store": "Bristol"},
]

new_ids = item_collection.insert_many(new_staff)

print("Inserted IDs and types")
for id in new_ids.inserted_ids:
    print(id)