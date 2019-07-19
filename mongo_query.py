from pymongo import MongoClient

client = MongoClient(host = "localhost", port = 27017)
my_db = client.zipsDB
my_collection = my_db.zips

myquery = {"city": "CWMBRAN"}

doc = my_collection.find_one(myquery)

if doc is not None:
    print(doc)
else:
    print("City not found")