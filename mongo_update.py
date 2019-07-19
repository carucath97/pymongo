from pymongo import MongoClient

client = MongoClient(host = "localhost", port = 27017)
my_db = client.zipsDB
my_collection = my_db.zips

myquery = {"city": "CWMBRAN"}
newvalue = {"$set": {"name": "ST. DIALS"}}

result = my_collection.update_one(myquery, newvalue)
print("%d documents mathced, %d documents updated" %(result.matched_count, result.modified_count))

