from pymongo import MongoClient

client = MongoClient(host = "localhost", port = 27017)
my_db = client.store
sub_type_collection = my_db["subtypes"]

food_sub_types = [
    {"_id": 1, "type_id": 1, "name": "Fruit & Veg"}, {"_id": 2, "type_id": 1, "name": "Meat & Fish"},
    {"_id": 3, "type_id": 1, "name": "Eggs & Dairy"}, {"_id": 4, "type_id": 1, "name": "Bakery"},
    {"_id": 5, "type_id": 1, "name": "Frozen"}, {"_id": 6, "type_id": 1, "name": "Tinned Food"},
    {"_id": 7, "type_id": 1, "name": "Confectionary"}, {"_id": 8, "type_id": 1, "name": "Seasonal"},
    {"_id": 9, "type_id": 1, "name": "Cereals & Grains"}, 
    {"_id": 10, "type_id": 1, "name": "Herbs & Spices"}, {"_id": 11, "type_id": 1, "name": "Jams, Honey & Spreads"},
    {"_id": 12, "type_id": 1, "name": "Dry Food"}, {"_id": 13, "type_id": 1, "name": "Sauces & Condiments"},
    {"_id": 14, "type_id": 1, "name": "Sugar & Home Baking"}, {"_id": 15, "type_id": 1, "name": "Freefrom"}
]

drink_sub_types = [
    {"_id": 16, "type_id": 2, "name": "Tea, Coffee & Hot Drinks"}, {"_id": 17, "type_id": 2, "name": "Water"},
    {"_id": 18, "type_id": 2, "name": "Juice & Squash"}, {"_id": 19, "type_id": 2, "name": "Milk"},
    {"_id": 20, "type_id": 2, "name": "Milkshakes & Smoothies"}, {"_id": 21, "type_id": 2, "name": "Fizzy Drinks"},
    {"_id": 22, "type_id": 2, "name": "Fizzy Drinks"}, {"_id": 23, "type_id": 2, "name": "Alcohol"}
]

hb_sub_types = [
    {"_id": 24, "type_id": 3, "name": "Soap, shower & bath"}, {"_id": 25, "type_id": 3, "name": "Medicines & Healthcare"},
    {"_id": 26, "type_id": 3, "name": "Oral care & toothpaste"}, {"_id": 27, "type_id": 3, "name": "Skincare"},
    {"_id": 28, "type_id": 3, "name": "Haircare"}, {"_id": 29, "type_id": 3, "name": "Deodorants & Perfumes"},
    {"_id": 30, "type_id": 3, "name": "Make up"}, {"_id": 31, "type_id": 3, "name": "Feminine Care"},
    {"_id": 32, "type_id": 3, "name": "Shaving & Hair Removal"}, {"_id": 33, "type_id": 3, "name": "Vitamins"}
]

clothes_sub_types = [
    {"_id": 34, "type_id": 4, "name": "Seasonal"}, {"_id": 35, "type_id": 4, "name": "T-Shirts"}, 
    {"_id": 36, "type_id": 4, "name": "Dresses & Skirts"},  {"_id": 37, "type_id": 4, "name": "Shirts & Blouses"},
    {"_id": 38, "type_id": 4, "name": "Jeans, Shorts & Trousers"}, {"_id": 39, "type_id": 4, "name": "Underwear"},
    {"_id": 40, "type_id": 4, "name": "Gloves and Socks"},  {"_id": 41, "type_id": 4, "name": "Shoes"},
    {"_id": 42, "type_id": 4, "name": "Coats and Jackets"}  
]

baby_sub_types = [
    {"_id": 43, "type_id": 5, "name": "Nappies"}, {"_id": 44, "type_id": 5, "name": "Wipes"},
    {"_id": 45, "type_id": 5, "name": "Mum & mum to be"}, {"_id": 46, "type_id": 5, "name": "Bottles"},
    {"_id": 47, "type_id": 5, "name": "Baby milk"}, {"_id": 48, "type_id": 5, "name": "Baby food"},
    {"_id": 49, "type_id": 5, "name": "Toys"}
]

household_sub_types = [
    {"_id": 50, "type_id": 6, "name": "Laundry"}, {"_id": 51, "type_id": 6, "name": "Toilet roll, kitchen roll & tissues"},
    {"_id": 52, "type_id": 6, "name": "Cleaning Products"}, {"_id": 53, "type_id": 6, "name": "Dishwasher & Washing up"},
    {"_id": 54, "type_id": 6, "name": "Foil, food bags & storage"}, {"_id": 55, "type_id": 6, "name": "Air fresheners"},
    {"_id": 56, "type_id": 6, "name": "Newspapers & Magazines"}, {"_id": 57, "type_id": 6, "name": "Cutlery & Plates"}
]

pet_sub_types = [
    {"_id": 58, "type_id": 7, "name": "Cat & Kitten"}, {"_id": 59, "type_id": 7, "name": "Dog & Puppy"},
    {"_id": 60, "type_id": 7, "name": "Other Animals"}, {"_id": 61, "type_id": 7, "name": "Litter"},
    {"_id": 62, "type_id": 7, "name": "Animal Toys"}
]

garden_sub_types = [
    {"_id": 63, "type_id": 8, "name": "Gardening"}, {"_id": 64, "type_id": 8, "name": "Barbecue"},
    {"_id": 65, "type_id": 8, "name": "Picnic & Outdoor Dining"}, {"_id": 66, "type_id": 8, "name": "Home & Office"},
    {"_id": 67, "type_id": 8, "name": "Party Tableware"}, {"_id": 68, "type_id": 8, "name": "Technology & Electrical"},
    {"_id": 69, "type_id": 8, "name": "Batteries"}, {"_id": 70, "type_id": 8, "name": "Sports & Leisure"},
    {"_id": 71, "type_id": 8, "name": "Flowers & Plants"}, {"_id": 72, "type_id": 8, "name": "Toys"}        
]

new_ids = sub_type_collection.insert_many(food_sub_types)
new_ids2 = sub_type_collection.insert_many(drink_sub_types)
new_ids3 = sub_type_collection.insert_many(hb_sub_types)
new_ids4 = sub_type_collection.insert_many(clothes_sub_types)
new_ids5 = sub_type_collection.insert_many(baby_sub_types)
new_ids6 = sub_type_collection.insert_many(household_sub_types)
new_ids7 = sub_type_collection.insert_many(pet_sub_types)
new_ids8 = sub_type_collection.insert_many(garden_sub_types)

print("Inserted IDs and types")
for id in new_ids.inserted_ids:
    print(id)

for id in new_ids2.inserted_ids:
    print(id)

for id in new_ids3.inserted_ids:
    print(id)

for id in new_ids4.inserted_ids:
    print(id)

for id in new_ids5.inserted_ids:
    print(id)

for id in new_ids6.inserted_ids:
    print(id)

for id in new_ids7.inserted_ids:
    print(id)

for id in new_ids8.inserted_ids:
    print(id)