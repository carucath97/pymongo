from pymongo import MongoClient
from datetime import datetime
from datetime import date

client = MongoClient(host = "localhost", port = 27017)
my_db = client.store
item_collection = my_db.items
staff_collection = my_db.staff

# Till Operator searching for items and their ids
def search_all_items():
    items = item_collection.find({}, {"_id": 1, "name": 1})
    print("All items")

    for item in items:   
        print(item)

# Till Operator searching for a specific item
def find_specific_item(i_type, i_name):
    myquery = {i_type: i_name}
    specific_item = item_collection.find(myquery, {"_id" : 1, "name": 1})

    for s_item in specific_item:
        print("")
        print("Item selected:")
        print(s_item)

#Store Manager adding different items
def add_new_product(name, sub_type, stock, cost, price, items_damaged, is_safe):
    product = {"name" : name, "sub_type": sub_type, "stock": stock, "cost": cost, "selling_price": price,
    "items_damaged": items_damaged, "is_safe": is_safe}
    new_id = item_collection.insert_one(product)
    print("Inserted item with id %s" % new_id.inserted_id)

#Stock controller managing stock
def update_stock(name, items_damaged):
    myquery = {"name": name}
    new_values = {"$inc": {"stock": -items_damaged, "items_damaged": items_damaged}}

    result = item_collection.update_one(myquery, new_values)
    print("%d documents matched, %d documents updated" %(result.matched_count, result.modified_count))

#Financial Consultant updating selling price
def update_price(name, value):
    myquery = {"name": name}
    new_value = {"$set" : {"selling_price": value}}

    result = item_collection.update_one(myquery, new_value)
    print("%d documents matched, %d documents updated" %(result.matched_count, result.modified_count))

#Store manager removing items from shop
def remove_item():
    results = item_collection.delete_many({"is_safe": False})
    print("Deleted %d items" %(results.deleted_count))

#Store manager adding a member of staff
def add_staff(id, first_name, middle_name, surname, role, salary, store):
    staff_member = {"_id": id, "first_name": first_name, "middle_name(s)": middle_name,
    "role": role, "salary": salary, "store": store}
    new_staff = staff_collection.insert_one(staff_member)
    print("Inserted staff member with id %d" %new_staff.inserted_id)

#Store manager deleting staff member
def remove_staff(staff_id):
    result = staff_collection.delete_many({"_id": staff_id})
    print("Deleted %d staff member" %(result.deleted_count))

#Staff member updating their surname
def update_staff_name(staff_id, surname):
    myquery = {"_id": staff_id}
    new_value = {"$set" : {"surname": surname}}

    result = staff_collection.update_one(myquery, new_value)
    print("%d documents matched, %d documents updated" %(result.matched_count, result.modified_count))

#Store manager seeing all staff in specific store
def find_staff_in_store(store):
    storequery = {"store": store}
    staff_in_store = staff_collection.find(storequery)

    for staff in staff_in_store:
        print(staff)

#Store manager updating staff roles
def update_role(staff_id, role):
    myquery = {"_id": staff_id}
    new_value = {"$set" : {"role": role}}

    result = staff_collection.update_one(myquery, new_value)
    print("%d documents matched, %d documents updated" %(result.matched_count, result.modified_count))

#Store manager updating staff salary
def update_salary(staff_id, salary):
    myquery = {"_id": staff_id}
    new_value = {"$set" : {"salary": salary}}

    result = staff_collection.update_one(myquery, new_value)
    print("%d documents matched, %d documents updated" %(result.matched_count, result.modified_count))


do_task = True
task = int(input("""Hello! Welcome to TesGo! What do you want to do today?
        1. Find all items and ids
        2. Find a specific item
        3. Add a new item
        4. Update the stock as item has been damaged
        5. Update price of item
        6. Remove dangerous items
        7. Add staff to the system
        8. Delete staff records
        9. Update staff surname
        10. Check staff in a store
        11. Update staff role
        12. Update staff salary
        
        """))

while (do_task == True):

    if (task == 1):
        search_all_items()

    elif (task == 2):
        item_type = "name"
        item_name = input("What is the name of the item? ")
        find_specific_item(item_type, item_name)

    elif (task == 3):
        name = input("Item name: ")
        sub_type = input("Sub-type: ")
        stock = int(input("Stock: "))
        cost = float(input("Cost per item: "))
        selling_price = float(input("Selling price: "))
       # sell_by = input("Sell by date (yyyy-mm-dd): ") -- commented out due to erroring, will amend
       # year, month, day = map(int, sell_by.split('-'))
       # sell_date = datetime.datetime(year, month, day)
        items_damaged = int(input("Items damaged: "))
        is_safe = input("Is item safe? True or False? ")
        safe = True
        if is_safe.upper() == "TRUE" or is_safe.upper() == "T":
            safe = True
        elif is_safe.upper() == "FALSE" or is_safe.upper() == "F":
            safe = False
        add_new_product(name, sub_type, stock, cost, selling_price, items_damaged, safe)

    elif (task == 4):
        name = input("Which item's stock do you wish to update? ")
        newly_damaged = int(input("How many items have been damaged? "))
        update_stock(name, newly_damaged)

    elif (task == 5):
        name = input("Which item's price do you wish to update? ")
        value = float(input("What does the price need updating to? "))
        update_price(name, value)

    elif (task == 6):
        remove_item()

    elif (task == 7):
        staff_id = int(input("Id: "))
        first_name = input("First Name: ")
        middle_name = input("Middle Name(s): ")
        surname = input("Surname: ")
        role = input("Role: ")
        salary = int(input("Salary: "))
        store = input("Store: ")

        add_staff(staff_id, first_name, middle_name, surname, role, salary, store)
    
    elif (task == 8):
        staff_id = int(input("What is the id of the member of staff? "))
        remove_staff(staff_id)

    elif (task == 9):
        staff_id = int(input("What is your staff id? "))
        surname = input("What is your new surname? ")
        update_staff_name(staff_id, surname)

    elif (task == 10):
        store = input("Which store do you wish to see the staff of? ")
        find_staff_in_store(store)

    elif (task == 11):
        staff_id = int(input("What is their staff id? "))
        role = input("What is their new role? ")
        update_role(staff_id, role)

    elif (task == 12):
        staff_id = int(input("What is their staff id? "))
        salary = int(input("What is their new salary? "))
        update_salary(staff_id, salary) 

    else:
        print("Invalid entry")

    task = int(input("""Do you want to do another task? Here's a reminder:
        1. Find all items and ids
        2. Find a specific item
        3. Add a new item
        4. Update the stock as item has been damaged
        5. Update price of item
        6. Remove dangerous items
        7. Add staff to the system
        8. Delete staff records
        9. Update staff surname
        10. Check staff in a store
        11. Update staff role
        12. Update staff salary

        0. Quit

        """))
    if (task == 0):
        print("You are leaving the interface, bye!")
        do_task = False


