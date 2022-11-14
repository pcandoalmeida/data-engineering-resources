product_list = ["Coke", "Pepsi", "Fanta"]
orders_list = [{'customer_name': 'd', 'customer address': 'ht', 'customer_phone': '535', 'status': 'PREPARING'},
{'customer_name': 'd', 'customer address': 'ht', 'customer_phone': '535', 'status': 'PREPARING'}]

# User Menu
def main_menu():
    answer = input("This is the main menu. Type 0 to exit, 1 for Products Menu, 2 for Orders Menu \n")
    if answer == "0":
        quit()

    elif answer == "1":
        products()

    elif answer == "2":
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
    product_list.append(new_product)
    print(f"Product has been added. Your new product list: {product_list}")
    main_menu()

# update existing product
def update_product():
    print("Here are the products with their index value:\n")
    for index, value in enumerate(product_list):
        print(index, value)
    
    while True:
        try:
            product_change = int(input("Please type the index of the product you would like to update\n"))
            product_list[product_change]
            break
        except:
            print("Please enter a valid index number from the given index values")

    new_product = input("Please type the new product name\n")
    product_list[product_change] = new_product
    print(f"Your product list has now been updated: {product_list}")

    main_menu()

# delete product
def delete_product():
    print("Here are the products with their index value:\n")
    for index, value in enumerate(product_list):
        print(index, value)
    while True:
        try:
            product_del = int(input("Please type the index of the product you would like to delete\n"))
            del product_list[product_del]
            break
        except:
            print("Please enter a valid index number from the given index values")
    
    print(f"Your new product list: {product_list}")
    
    main_menu()

# Orders menu
def orders():
    ans = input("""This is the orders menu.
    Type 0 to return to the main menu, 1 to view all orders, 2 to add a new order, 3 to update status of existing order, 4 to update an existing order, 5 to delete an order""")

    if ans == "0":
        main_menu()
    
    elif ans == "1":
        print(orders_list)

    elif ans == "2":
        create_order()

    elif ans == "3":
        update_status()


def create_order():
    customer_name = input("Type your name\n")
    customer_address = input("Type your address\n")
    customer_phone = input("Type your phone number\n")
    status = "PREPARING"
    order_dict = {"customer_name" : customer_name, "customer address" : customer_address, "customer_phone" : customer_phone, "status" : status}
    orders_list.append(order_dict)
    print(orders_list)

    main_menu()         

def update_status():
    for i, v in enumerate(orders_list):
        print (f"order number {i}:\n {v}")

    index = input("please type the order number")
    
    main_menu()

main_menu()