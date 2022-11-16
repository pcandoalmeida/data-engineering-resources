import csv

product_list = []
couriers_list = []
orders_list = []


order_status = ["PREPARING", "DISPATCHED", "DELIVERED"]
order_properties = ["customer_name", "customer_address", "customer_phone","courier", "status", "items"]

# Loading Products list
with open("products.csv", "r") as p:
    p_reader = csv.DictReader(p, delimiter= ",")
    for product in p_reader:
        product_list.append(product)


# Loading Couriers List
with open("couriers.csv", "r") as c:
    c_reader = csv.DictReader(c, delimiter=",")
    for courier in c_reader:
        couriers_list.append(courier)


# loading Orders list
with open("orders.csv", "r") as o:
    o_reader = csv.DictReader(o, delimiter = ".")
    for order in o_reader:
        orders_list.append(order)

# User Menu
def main_menu():
    answer = input("This is the main menu. Type 0 to exit, 1 for Products Menu, 2 for Couriers Menu, 3 for Orders Menu\n")
    if answer == "0":
        save_data()
        quit()

    elif answer == "1":
        products()

    elif answer == "2":
        couriers()

    elif answer == "3":
        orders()

    else:
        print("Please enter either 0 or 1")
        main_menu()
        
# Products menu
def products():
    ans = input("""This is the products menu. 
    Type 0 to return to main menu, or 1 for your product list, or 2 to create new product, 3 to update an existing product, 4 to delete a product\n""")

    if ans == "0":
        main_menu()

    elif ans == "1":
        print(product_list)
        main_menu()

    elif ans == "2":
        create_new_product()
    
    elif ans == "3":
        update_product()

    elif ans == "4":
        delete_product()

    else:
        print("Please enter either 0, 1, 2, 3 or 4")
        products()

# create new product
def create_new_product():
    new_product = input("What product would you like to add?\n")
    new_product_price = int(input("What price will it be?"))
    product_list.append({"name" : new_product, "price" : new_product_price})
    print(f"Product has been added. Your new product list: {product_list}")
    main_menu()

# update existing product
def update_product():
    print("Here are the products with their index value:")
    for index, value in enumerate(product_list):
        print(f"product index {index}:\n", value["name"])
    
    while True:
        try:
            product_change = int(input("Please type the index of the product you would like to update\n"))
            print(f"Here are the current properties of your selected product {product_list[product_change]}")
            break
        except:
            print("Please enter a valid index number from the given index values")

    for property in product_list[product_change]:
        new_property = input(f"Please type the new {property}, otherwise leave blank\n")
        if new_property != "":
            product_list[product_change][property] = new_property

    print(f"Your current product list: {product_list}")

    main_menu()

# delete product
def delete_product():
    print("Here are the products with their index value:")
    for index, value in enumerate(product_list):
        print(f"product index {index}:\n", value["name"])
    while True:
        try:
            product_del = int(input("Please type the index of the product you would like to delete\n"))
            del product_list[product_del]
            break
        except:
            print("Please enter a valid index number from the given index values")
    
    print(f"Your new product list: {product_list}")
    
    main_menu()

# Couriers menu
def couriers():
    ans = input("""This is the couriers menu.
    Type 0 to return to the main menu, 1 to view all couriers, 2 to create a new courier, 3 to update existing courier, 4 to delete a courier\n""")

    if ans == "0":
        main_menu()
    
    elif ans == "1":
        print(couriers_list)
        main_menu()

    elif ans == "2":
        create_courier()

    elif ans == "3":
        update_courier()

    elif ans == "4":
        delete_courier()

    else:
        print("Please enter either 0, 1, 2, 3, or 4")
        couriers()

# Create new courier
def create_courier():
    courier_name = input("Enter name of courier\n")
    courier_number = input("Enter phone number of courier\n")

    couriers_list.append({"name" : courier_name, "phone" : courier_number})
    print(f"New couriers list:\n {couriers_list}")

    main_menu()
    
# update existing courier
def update_courier():
    print("Here are the couriers with their index values:")
    for index, value in enumerate(couriers_list):
        print(f"courier index {index}:\n", value["name"])
    
    while True:
        try:
            courier_change_index = int(input("Please type the index of the product you would like to update\n"))
            print(f"Here are the current properties of your selected courier: {couriers_list[courier_change_index]}")
            break
        except:
            print("Please enter a valid index number from the given index values")

    for property in couriers_list[courier_change_index]:
        new_property = input(f"Please type the new {property}, otherwise leave blank\n")
        if new_property != "":
            couriers_list[courier_change_index][property] = new_property

    print(f"Your current couriers list: {couriers_list}")

    main_menu()

# delete courier
def delete_courier():
    print("Here are the couriers with their index values:")
    for index, value in enumerate(couriers_list):
        print(f"courier index {index}:\n", value["name"])
    while True:
        try:
            courier_del_index = int(input("Please type the index of the courier you would like to delete\n"))
            del couriers_list[courier_del_index]
            break
        except:
            print("Please enter a valid index number from the given index values")
    
    print(f"Your new courier list: {couriers_list}")
    
    main_menu()

# Orders menu
def orders():
    ans = input("""This is the orders menu.
    Type 0 to return to the main menu, 1 to view all orders, 2 to add a new order, 3 to update status of existing order, 4 to update an existing order, 5 to delete an order\n""")

    if ans == "0":
        main_menu()
    
    elif ans == "1":
        print(orders_list)
        main_menu()

    elif ans == "2":
        create_order()

    elif ans == "3":
        update_status()
    
    elif ans == "4":
        update_order()

    elif ans == "5":
        delete_order()

#create order
def create_order():
    customer_name = input("Type your name\n")
    customer_address = input("Type your address\n")
    customer_phone = input("Type your phone number\n")

    # Choosing Product
    product_choices = []
    print("Here are the products with their index values:")
    for index, value in enumerate(product_list):
        print(f"product index {index}:\n", value["name"])
    while True:
        try:
            choice1 = input("Type index value of your chosen product, otherwise if you are done type -1, or if you wish to cancel, type -2 \n")
            if choice1 == "-1":
                break
            elif choice1 == "-2":
                main_menu()
            elif int(choice1) > len(product_list) or int(choice1) < -2:
                print("An error occured. Please type an index value")
                continue
        except:
            print("An error occured. Please type an index value")
            continue
        product_choices.append(choice1)
    product_choices = ",".join(product_choices)

    # Choosing courier
    print("Here are the couriers with their index values:")
    for index, value in enumerate(couriers_list):
        print(f"courier index {index}:\n", value["name"])

    courier_choice_index = input("Please enter the index of the courier\n")

    status = "PREPARING"
    order_dict = {"customer_name" : customer_name, "customer_address" : customer_address, "customer_phone" : customer_phone,"courier" : courier_choice_index, 
    "status" : status, "items" : product_choices}

    orders_list.append(order_dict)
    print(orders_list)

    main_menu()         

#update status of order
def update_status():
    print("Here are the orders with their index values")
    for i, v in enumerate(orders_list):
        print (f"order index {i}:\n {v}")

    order_index = int(input("please type the order index you wish to update the status of\n"))
    
    for i, v in enumerate(order_status):
        print(f"Order Status Index {i}: {v}")

    status_index = int(input("Please type the appropriate index which you want to update the status with\n"))
    orders_list[order_index]["status"] = order_status[status_index]
    print(f"Your updated orders list:\n{orders_list}")

    main_menu()

#update properties of an order
def update_order():
    for i, v in enumerate(orders_list):
        print (f"order index {i}:\n {v}")

    while True:
        try:
            order_change_index = int(input("Please type the index of the product you would like to update\n"))
            print(f"Here are the current properties of your selected product {orders_list[order_change_index]}")
            break
        except:
            print("Please enter a valid index number from the given index values")

    for property in orders_list[order_change_index]:
        new_property = input(f"Please type the new {property}, otherwise leave blank\n")
        if new_property != "":
            orders_list[order_change_index][property] = new_property

    print(f"Your current order list: {orders_list}")

    main_menu()

# delete an order
def delete_order():
    print("Here are the orders with their index values:")
    for index, value in enumerate(orders_list):
        print(f"order index {index}:\n {value}")
    while True:
        try:
            order_del_index = int(input("Please type the index of the order you would like to delete\n"))
            del orders_list[order_del_index]
            break
        except:
            print("Please enter a valid index number from the given index values")
    
    print(f"Your new order list: {orders_list}")
    
    main_menu()

# saves all products, couriers, and orders data to csv files
def save_data():
    with open("products.csv", "w", newline = "") as p:
        headers_product = ["name", "price"]
        p_reader = csv.DictWriter(p, fieldnames = headers_product)
        p_reader.writeheader()
        p_reader.writerows(product_list)
    
    with open("couriers.csv", "w", newline = "") as c:
        headers_courier = ["name", "phone"]
        c_reader = csv.DictWriter(c, fieldnames = headers_courier)
        c_reader.writeheader()
        c_reader.writerows(couriers_list)

    with open("orders.csv", "w", newline = "") as o:
        o_reader = csv.DictWriter(o, fieldnames = order_properties, delimiter = ".")
        o_reader.writeheader()
        o_reader.writerows(orders_list)

main_menu()
