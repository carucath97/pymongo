from pymongo import MongoClient

client = MongoClient(host = "localhost", port = 27017)
my_db = client["store"]
type_collection = my_db["types"]

new_types = [
    {"_id": 1, "name": "Food"}, {"_id": 2, "name": "Drinks"}, {"_id": 3, "name": "Health & Beauty"},
    {"_id": 4, "name": "Clothes"}, {"_id": 5, "name": "Baby & Toddler"}, 
    {"_id": 6, "name": "Household"}, {"_id": 7, "name": "Pets"}, 
    {"_id": 8, "name": "Homeware & Garden"}
]
new_ids = type_collection.insert_many(new_types)

print("Inserted IDs and types")
for id in new_ids.inserted_ids:
    print(id)