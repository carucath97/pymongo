from pymongo import MongoClient
from datetime import datetime
from datetime import date

client = MongoClient(host = "localhost", port = 27017)
my_db = client.store
staff_collection = my_db.staff

staff = staff_collection.delete_many({})
print("Deleted %d staff" %(staff.deleted_count))