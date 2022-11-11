from os import system
from time import sleep

# OPEN TEXT FILE AND RETURN CONTENTS
def read_file(file_name):
    with open(file_name, "r+") as file:
        return file.read().splitlines()

# FUNCTION FOR SORTING LIST
def sort_list_and_view(which_list, item_type):
    if not which_list:
        return f"No {item_type}s found, please add to the list using the 'Add {item_type}' option." 
    # return the list with items listed inline, in alphabetical order, separated by a comma
    else: return f"""{item_type.upper()} LIST (in alphabetical order):
    {(", ".join(sorted(which_list))).title()}
"""

# DISPLAY NUMBERED ITEMS FOR USER TO SELECT FROM
def select_item(which_list, action_to_be_performed, item_type):
    # iterate over items in the list and print them with their index position
    print(f"{action_to_be_performed.title()} Entry")
    for i, item in enumerate(which_list):
        print(f"    [{i}] {item}")

    # prompt user to select item they want to select by its index position
    user_selection = int(input(f"Please input the number of the {item_type} you wish to {action_to_be_performed}: "))
    return user_selection

# ADD TO LIST FUNCTION
def add_item(list_name, item_type):
    # prompt user to state what they want to add
    print(f"Add {item_type.title()}")
    item_to_add = input(f"Enter new {item_type} name: ")

    #checks if item name is in list, if it isn't, returns the value, otherwise returns none value
    if item_to_add not in list_name:
        return item_to_add
    else: 
        print(f"{item_to_add.title()} already in list.")
        return 

# UPDATE LIST
def update_list_item(list_name, item_selection):
    print(f"You have selected {list_name[item_selection]}.")
    update_item_entry = input("Please enter your correction: ")
    if update_item_entry not in list_name:
        return update_item_entry
    else:
        print(f"{update_item_entry.title()} already in list, no changes have been made.")
        return

# DEFINE FUNCTION FOR ACCEPTING USER INPUT AND SEPARATE THIS FROM THE CHECK PERFORMED
#

# UPDATE DICTIONARY
def update_dictionary(which_dict, which_entry, which_key):
    print(f"Update Orders")
    print(f"You have selected {which_dict[which_entry][which_key]}")
    update_value = input(f"Please enter new {which_key}: ")
    if not update_value:
        return print("No changes made. Returning to menu.")
    else:
        print("Update successful. Returning to menu.")
        return update_value


# DELETING FROM LISTS
def delete_item(list_name, user_selection):
    print(f"You have deleted {list_name[user_selection]}. Returning to main menu.")
    return user_selection

# # WRITING TO A FILE
def write_file(file_name, which_list_to_write):
    with open(file_name, "w") as file:
        file.write("\n".join(which_list_to_write).lower())

# Test Dictionary
orders_dict = [{
        "customer_name": "John",
        "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
        "customer_phone": "0789887334",
        "courier": 0,
        "status": "preparing"
    },
    {
        "customer_name": "Sarah",
        "customer_address": "75 Dummy Address, LONDON, WH1 2ER",
        "customer_phone": "0758784657",
        "courier": 1,
        "status": "delivered"
    }]

# SUB-MENU FUNCTION
def sub_menu_function(item_type):
    return f"""{item_type.upper()} MENU
    [0] Return to main menu 
    [1] View all {item_type}s 
    [2] Add {item_type}  
    [3] Update existing {item_type}  
    [4] Delete existing {item_type} 

Please enter your selection: """

# MENUS
main_menu_options = ("""NYL'S CAFE 

MAIN MENU
Welcome! What would you like to do? 
    [0] Exit app
    [1] View product menu
    [2] View couriers menu
    [3] View orders menu

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

# UPDATE order status options
order_status_options = ["preparing", "dispatched", "delivered", "cancelled"]


product_list = read_file("products.txt")
courier_list = read_file("couriers.txt")

# # APP
system("cls")
while True:
    main_menu_selection = int(input(main_menu_options))
    
    if main_menu_selection == 0:        
        print("Thanks for using Nyl's cafe app. Have a great day!")
        write_file("products.txt", product_list)
        write_file("couriers.txt", courier_list)
        break

    # ENTER product menu
    elif main_menu_selection == 1:
        while True:
            product_menu_selection = int(input(sub_menu_function("product")))            
        
        # BACK TO MAIN
            if product_menu_selection == 0:                
                break
                
        # VIEW products
            if product_menu_selection == 1:
                print(sort_list_and_view(product_list, "product"))

        # ADD products        
            elif product_menu_selection == 2:
                product_to_add = add_item(product_list, "product")
                # if the return value is none, no action is performed
                if not product_to_add: 
                    pass
                else:
                    product_list.append(product_to_add)
                    write_file("products.txt", product_list)
        
        # UPDATE product
            elif product_menu_selection == 3:
                # user selects an item from an enumerated list
                product_index_val = select_item(product_list, "update", "product")
                # assigns new product name to a variable if it does not already exist in list, else, none value returned by function
                updated_product_name = update_list_item(product_list, product_index_val)
                # if a none value was returned, do nothing, else update the product
                if not updated_product_name: 
                    pass
                else:
                    product_list[product_index_val] = updated_product_name
                    write_file("products.txt", product_list)

        # DELETE product
            elif product_menu_selection == 4:
                # User selects item from enumerated product list
                product_delete_index = select_item(product_list, "delete", "product")
                # User shown item that has been deleted
                print(f"{product_list[product_delete_index]} has been deleted. Returning to main menu.")
                # item is deleted from list
                product_list.pop(product_delete_index)
                sleep(1)
                write_file("products.txt", product_list)
                

    # ENTER courier menu
    elif main_menu_selection == 2:
        while True:
            courier_menu_selection = int(input(sub_menu_function("courier")))
        
            # BACK TO MAIN
            if courier_menu_selection == 0:
                print("Returning to main menu")
                break
                
            # VIEW couriers
            if courier_menu_selection == 1:
                print(sort_list_and_view(courier_list, "courier"))

            # ADD couriers        
            elif courier_menu_selection == 2:
                courier_to_add = add_item(courier_list, "courier")
                # if the return value is none, no action is performed
                if not courier_to_add: 
                    pass
                else:
                    courier_list.append(courier_to_add)
                    write_file("couriers.txt", courier_list)

            # UPDATE courier
            elif courier_menu_selection == 3:
                courier_index_val = select_item(courier_list, "update", "courier")
                # assigns new courier name to a variable if it does not already exist in list, else, none value returned by function
                updated_courier_name = update_list_item(courier_list, courier_index_val)
                # if a none value was returned, do nothing, else update the courier
                if not updated_courier_name: 
                    pass
                else:
                    courier_list[courier_index_val] = updated_courier_name
                    write_file("couriers.txt", courier_list)

            # DELETE courier
            elif courier_menu_selection == 4:
                # User selects item from enumerated courier list
                courier_delete_index = select_item(courier_list, "delete", "courier")
                # User shown item that has been deleted
                print(f"{courier_list[courier_delete_index]} has been deleted. Returning to main menu.")
                # item is deleted from list
                courier_list.pop(courier_delete_index)
                sleep(1)
                write_file("couriers.txt", courier_list)
                
                

    # ENTER order menu
    elif main_menu_selection == 3:
        while True:
            order_menu_selection = int(input(orders_menu_options))

            # RETURN to main menu
            if order_menu_selection == 0:
                print("Returning to main menu.")
                break

            # DISPLAY orders
            elif order_menu_selection == 1:
                for order in orders_dict:
                    print(order)

            # CREATE new order
            elif order_menu_selection == 2:
                print("Add new order")
                orders_dict.append(
                    {
                        "customer_name": input("Please enter customer name: "),
                        "customer_address": input("Please enter customer's address: "),
                        "customer_phone": input("Please enter customer's telephone number: "),
                        "courier": (select_item(courier_list, "assign", "courier")),
                        "status": "preparing"
                    }
                )
                print("Order placed. Returning to order menu.")
                sleep(1)
                

            # UPDATE order status
            elif order_menu_selection == 3:
                print("Update Order Status\n")
                to_update_status_of = select_item(orders_dict, "update", "order")
                print(f"""Update Order Status

Customer name: {orders_dict[to_update_status_of]["customer_name"]},
    Order status: {orders_dict[to_update_status_of]["status"]}
    """)
                try:
                    new_status = select_item(order_status_options, "update", "order status")
                except ValueError:
                        print("Incorrect value entered. No changes have been made.")
                        sleep(1)
                        
                else: 
                    # update order status to new value
                    orders_dict[to_update_status_of]["status"] = order_status_options[new_status]
                    print("Order status updated.")


            # update order details
            elif order_menu_selection == 4:
                print("Update Order Details\n")
                # displays each order for the user to select from
                order_selection = select_item(orders_dict, "update", "order")
                print(f"""Update Order Details
                {orders_dict[order_selection]}""")
                # user selects which detail they will update
                order_detail_selection = select_item(orders_dict[order_selection], "update", "order detail")
                
                # FIND A WAY TO SIMPLIFY THIS SO THAT IT IS MORE READABLE
                if order_detail_selection == 0:
                    orders_dict[order_selection]["customer_name"] = update_dictionary(orders_dict, order_selection, "customer_name")
                elif order_detail_selection == 1:
                    orders_dict[order_selection]["customer_address"] = update_dictionary(orders_dict, order_selection, "customer_address")
                elif order_detail_selection == 2:
                    orders_dict[order_selection]["customer_phone"] = update_dictionary(orders_dict, order_selection, "customer_phone")
                elif order_detail_selection == 3:
                    orders_dict[order_selection]["courier"] = (select_item(courier_list, "assign", "courier"))
                elif order_detail_selection == 4:
                    orders_dict[order_selection]["order_status"] = update_dictionary(orders_dict, order_selection, "order_status")
                

            # DELETE order
            elif order_menu_selection == 5:
                print("Delete an Order")
                order_selection = select_item(orders_dict, "delete", "order")
                del orders_dict[order_selection]
                print("Order removed. Returning to order menu.")
