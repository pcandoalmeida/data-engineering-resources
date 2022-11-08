from os import system
from time import sleep

# WEEK ONE
# 0 -> exit
# 1 -> product menu
# view products (list)
# create new product
#only create new product if not already present in list.
# STRETCH delete product
    # search for product
    # remove product
# STRETCH update product
    # search for product
    # amend product

# WEEK TWO v1
# 2 -> order menu
# view orders (dict)
    # order details
        # customer name
        # customer address
        # customer phone
        # order status
            # default: PREPARING
# update order status
    # display order list
    # request update value
# STRETCH update order
    # display order list
    # update order, if nothing entered, do not update
# STRETCH delete order
    # display order list
    # delete order

# WEEK TWO v2
# persist (load and write) lists of products and couriers
# courier menu
# view couriers (list)
# create new courier
# STRETCH delete courier
    # search for courier
    # remove courier
# STRETCH update courier
    # search for courier
    # amend courier

# CREATE a products list


product_list = ["apple", "orange", "pineapple"]

courier_list = ["Wisp", "Saryn", "Oberon"]


# Test Dictionary
orders_dict = [{
        "customer_name": "John",
        "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
        "customer_phone": "0789887334",
        "status": "preparing"
    },
    {
        "customer_name": "Sarah",
        "customer_address": "75 Dummy Address, LONDON, WH1 2ER",
        "customer_phone": "0758784657",
        "status": "delivered"
    }]


# FUNC - ADD product to list
def add_product(to_add): 
    if to_add not in product_list:
        print(f"{to_add} added to list.")
        return product_list.append(to_add)
    else: print("Product already in list.")

# FUNC - ADD couriet to list
def add_courier(): 
    to_add = input("Please enter the name of the new courier")
    if to_add not in product_list:
        print(f"{to_add} added to list.")
        return courier_list.append(to_add)
    else: print("Product already in list.")


# UPDATE order status options
order_status_options = ["preparing", "dispatched", "delivered", "cancelled"]

# CREATE menus that accepts user input
main_menu_options = ("""NYL'S CAFE 

MAIN MENU
Welcome! What would you like to do? 
    [0] Exit app
    [1] View product menu
    [2] View couriers menu
    [3] View orders menu

Please enter your selection: """)


product_menu_options = ("""
PRODUCTS MENU 
    [0] Return to main menu 
    [1] View all products 
    [2] Add products 
    [3] Amend existing product 
    [4] Delete existing product

Please enter your selection: """)

courier_menu_options = ("""
COURIERS MENU 
    [0] Return to main menu 
    [1] View all couriers 
    [2] Add couriers 
    [3] Amend existing courier 
    [4] Delete existing courier

Please enter your selection: """)

orders_menu_options = ("""
ORDERS MENU
    [0] Return to main menu 
    [1] View all orders
    [2] Add order 
    [3] Update order status
    [4] Update order details
    [5] Delete existing order

Please enter your selection: """)

# APP
system("cls")
while True:
    main_menu_selection = int(input(main_menu_options))
    system("cls")

    if main_menu_selection == 0:
        system("cls")
        print("Thanks for using Nyl's cafe app. Have a great day!")
        break

    # ENTER product menu
    elif main_menu_selection == 1:
        while True:
            prod_menu_selection = int(input(product_menu_options))
            system("cls")
        
        # BACK TO MAIN
            if prod_menu_selection == 0:
                print("Returning to main menu")
                sleep(1)
                system("cls")
                break
                
        # VIEW products
            if prod_menu_selection == 1:
                print("Viewing all products.")
                print("Product list: \n    ", " ".join(product_list))

        # ADD products        
            elif prod_menu_selection == 2:
                print("Adding New Product")
                to_add = input("Please enter the name of the product you wish to add: ")
                add_product(to_add)
                sleep(2)
                system("cls")

        # UPDATE product
            elif prod_menu_selection == 3:
                system("cls")
                print("Update Product")
                for i in range(len(product_list)):
                    print(f"[{i}] {product_list[i]}")
                to_amend = int(input("Please input the number of the product you wish to amend: "))
                print(f"You have selected {product_list[to_amend]}:")
                product_list[to_amend] = input("Please enter your correction: ")
                system("cls")

        # DELETE product
            elif prod_menu_selection == 4:
                system("cls")
                print("Remove Product")
                for i in range(len(product_list)):
                    print(f"[{i}] {product_list[i]}")
                to_delete = int(input("Please input the number of the product you wish to delete: "))
                print(f"{product_list[to_delete]} has been deleted. Returning to main menu.")
                product_list.pop(to_delete)
                sleep(2)
                system("cls")

    # ENTER courier menu
    elif main_menu_selection == 2:
        while True:
            courier_menu_selection = int(input(courier_menu_options))
            system("cls")
        
        # BACK TO MAIN
            if courier_menu_selection == 0:
                print("Returning to main menu")
                sleep(1)
                system("cls")
                break
                
        # VIEW couriers
            if courier_menu_selection == 1:
                print("Viewing all couriers.")
                print("courier list: \n    ", " ".join(courier_list))

        # ADD couriers        
            elif courier_menu_selection == 2:
                print("Adding New courier")
                add_courier()
                sleep(2)
                system("cls")

        # UPDATE courier
            elif courier_menu_selection == 3:
                system("cls")
                print("Update courier")
                for i in range(len(courier_list)):
                    print(f"[{i}] {courier_list[i]}")
                to_amend = int(input("Please input the number of the courier you wish to amend: "))
                print(f"You have selected {courier_list[to_amend]}:")
                courier_list[to_amend] = input("Please enter your correction: ")
                system("cls")

        # DELETE courier
            elif courier_menu_selection == 4:
                system("cls")
                print("Remove courier")
                for i in range(len(courier_list)):
                    print(f"[{i}] {courier_list[i]}")
                to_delete = int(input("Please input the number of the courier you wish to delete: "))
                print(f"You have deleted {courier_list[to_delete]}. Returning to main menu.")
                courier_list.pop(to_delete)
                sleep(2)
                system("cls")


    # ENTER order menu
    elif main_menu_selection == 3:
        while True:
            order_menu_selection = int(input(orders_menu_options))
            system("cls")

            # RETURN to main menu
            if order_menu_selection == 0:
                print("Returning to main menu.")
                sleep(2)
                system("cls")
                break

            # DISPLAY orders
            elif order_menu_selection == 1:
                system("cls")
                print("Display Orders")
                for order in orders_dict:
                    print(order)

            # CREATE new order
            elif order_menu_selection == 2:
                system("cls")
                print("Add new order")
                orders_dict.append(
                    {
                        "customer_name": input("Please enter customer name: "),
                        "customer_address": input("Please enter customer's address: "),
                        "customer_phone": input("Please enter customer's telephone number: "),
                        "status": "preparing"
                    }
                )
                print("Order placed. Returning to order menu.")
                sleep(2)
                system("cls")

            # UPDATE order status
            elif order_menu_selection == 3:
                system("cls")
                print("Update Order Status\n")
                for i, order in enumerate(orders_dict):
                    print(f"[{i}] {order}")
                to_update_status = int(input("Please select the order you wish to update: "))
                system("cls")
                print(f"""Update Order Status

Customer name: {orders_dict[to_update_status]["customer_name"]},
    Order status: {orders_dict[to_update_status]["status"]}
    """)
                for i, status in enumerate(order_status_options):
                    print(f"[{i}] {status}")
                try:
                    update_status = int(input("What would you like to update the status to?: "))
                except ValueError:
                        print("No value entered. No changes have been made. \n Returning to order menu.")
                        sleep(2)
                        system("cls")
                else: 
                    # update order status to new value
                    orders_dict[to_update_status]["status"] = order_status_options[update_status]
                    system("cls")
                    print("Order status updated. Returning to order menu.")
                    sleep(2)
                    system("cls")


            # update order details
            elif selection == 4:
                system("cls")
                print("Update Order Details\n")
                # displays each order for the user to select from
                for i, order in enumerate(orders_dict):
                    print(f"[{i}] {order}")
                order_selection = int(input("Please select an order: "))
                system("cls")
                print(f"""Update Order Details

                {orders_dict[order_selection]}""")
                # user selects which detail they will update
                for i, details in enumerate(orders_dict[order_selection]):
                    print(f"[{i}] {details}")
                selection = int(input("Please select which detail you would like to update: "))
                if selection == 0:
                    print(f"""You have selected {orders_dict[order_selection]["customer_name"]}""")
                    orders_dict[order_selection]["customer_name"] = input("Please enter new name: ")
                elif selection == 1:
                    print(f"""You have selected {orders_dict[order_selection]["customer_address"]}""")
                    orders_dict[order_selection]["customer_address"] = input("Please enter new address: ")
                elif selection == 2:
                    print(f"""You have selected {orders_dict[order_selection]["customer_phone"]}""")
                    orders_dict[order_selection]["customer_phone"] = input("Please enter new phone number: ")
                print("Order updated. Returning to order menu.")
                sleep(2)
                system("cls")

            # DELETE order
            elif order_menu_selection == 5:
                system("cls")
                print("Update Order Details")
                for i, order in enumerate(orders_dict):
                    print(f"[{i}] {order}")
                order_selection = int(input("Please select which order you wish to delete: "))
                del orders_dict[order_selection]
                print("Order removed. Returning to order menu.")
                sleep(2)
                system("cls")
