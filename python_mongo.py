from pymongo import MongoClient

client = MongoClient(host = "localhost", port = 27017)
my_db = client.zipsDB
my_collection = my_db.zips

zips_data = my_collection.find()
for document in zips_data:
    print(document)

