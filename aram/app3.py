import json
import ast
def update_item(selected_list, name_of_selected_list):
    print("")
# #TODO add the order
#     if name_of_selected_list == "orders":
#         order = create_order(selected_list, name_of_selected_list)
#         with open(f"data\{name_of_selected_list}.txt", "a") as itemsf:
#             itemsf.write(f"\n{order}")
#             return(f"New order has been added to {name_of_selected_list[:-1]} list")
# # END OF THE TODO BIT
    valid_input = show_items_and_gen_valid_inputs(selected_list, name_of_selected_list)
    print(f"Enter the number for the {name_of_selected_list[:-1]} you want to replace: ")
    replacee = input()
    while replacee not in valid_input:
        print(f"Not a valid option. Try again.\nChoose an option:")
        replacee = input(f"""Enter the number for the {name_of_selected_list[:-1]} you want
to replace or x to go back to main menu: """)        
    if str(replacee).lower() == "x":
        menu()
    else:
        replacement = input(f"Enter the {name_of_selected_list[:-1]} you want to replace your choice with: ")#
        while replacement.strip().capitalize() in selected_list and replacement.capitalize() != "X":
            print(f"That {name_of_selected_list[:-1]} is already registered")
            replacement = input(f"""Enter a new {name_of_selected_list[:-1]} or enter x
to go back to go back to {name_of_selected_list[:-1]} menu: """).strip()
        if replacement.lower() == "x":
            menu()
        else:
            with open(f"data\{name_of_selected_list}.txt", "r") as itemsf:
                lines = itemsf.readlines()
            if int(replacee) == len(lines)-1:
                lines[int(replacee)] = f"{replacement}"
            else:
                lines[int(replacee)] = f"{replacement}\n"
            print(f"{replacement} has replaced {lines[int(replacee)]}")
            with open(f"data\{name_of_selected_list}.txt", "w") as itemsf:
                itemsf.writelines(lines)
            
# def update_order
def delete_item(selected_list, name_of_selected_list):
    print("")
    valid_input = show_items_and_gen_valid_inputs(selected_list, name_of_selected_list)
    print("")
    print("Enter the number for the item you want to delete: ")
    deletee = input()
    while deletee not in valid_input:
        print("Not a valid option. Try again.\nChoose an option:")
        deletee = input("""Enter the number for the item you want
to replace or x to go back to main menu""")        
    if str(deletee).lower() == "x":
        menu()
    else:
        with open(f"data\{name_of_selected_list}.txt", "r") as itemsf:
            lines = itemsf.readlines()
            del lines[int(deletee)]
        with open(f"data\{name_of_selected_list}.txt", "w") as itemsf:
            for pos, line in enumerate(lines):
                #needed because otherwise deleting the last item would add a blank like
                if pos == len(lines)-1:
                    itemsf.write(line.strip())
                else:
                    itemsf.write(line)
        print(f"{name_of_selected_list[:-1]} number {deletee} is now deleted.")
        menu()

#TODO create variant for nicely formatted order output and reuse index code
def show_items_and_gen_valid_inputs(selected_list, name_of_selected_list):
    with open(f"data\{name_of_selected_list}.txt", "r") as itemsf:
        valid_input = []
        for num, line in enumerate(itemsf):
            if name_of_selected_list == "orders":
                print(f"Order n.{num}")
                line_as_dict = ast.literal_eval(line)
                for key, value in line_as_dict.items():
                    
                    key = key.replace("_", " ").title()
                    print(f"{key}: {value}")
                print("")
            else:           
                print(num, line.strip("\n"))
            valid_input.append(str(num))
        valid_input.append("x")
    return valid_input
    print("")

def create_order(selected_list, name_of_selected_list):
    order = {}
    order["customer_name"] = input("Enter the customer name: ")
    order["customer_address"] = input("Enter the customer address: ")
    order["customer_phone"] = input("Enter the customer phone: ")
    order["status"] = "PREPARING"
    return order

    
def create_new_item(selected_list, name_of_selected_list):
    print(f"selected add {name_of_selected_list[:-1]}")
    if name_of_selected_list == "orders":
        order = create_order(selected_list, name_of_selected_list)
        with open(f"data\{name_of_selected_list}.txt", "a") as itemsf:
            itemsf.write(f"\n{order}")
            return(f"New order has been added to {name_of_selected_list[:-1]} list")
    else:
        new_item = input(f"Enter a new {name_of_selected_list[:-1]}: ").strip()
        while new_item.strip().capitalize() in selected_list and new_item.capitalize() != "X":
            print(f"That {name_of_selected_list[:-1]} is already registered")
            new_item = input(f"""Enter a new {name_of_selected_list[:-1]} or enter x
    to go back to go back to {name_of_selected_list[:-1]} menu: """).strip()
        if new_item.capitalize() == "X":
            print("you chose X")
            menu()
        else:
            with open(f"data\{name_of_selected_list}.txt", "a") as itemsf:
                itemsf.write(f"\n{new_item.strip()}")
            return(f"{new_item} has been added to {name_of_selected_list[:-1]} list")

def courier_menu():
    couriers = []
    with open("data\couriers.txt", "r+") as courierf:
        for line in courierf:
            couriers.append(line.strip("\n"))
    courier_menu_string = """Choose an option:
0 to go to main menu
1 for seeing the list of couriers
2 to add a new courier
3 to update/replace a courier
4 to delete a courier"""
    print(courier_menu_string)
    u_input2 = int(input())
    while u_input2 not in ("0","1","2","3","4"):
        print("Not a valid option. Try again.") 
        print(courier_menu_string)        
        u_input2 = input()
    if u_input2 == "0":
        menu()
    elif u_input2 == "1":
        show_items_and_gen_valid_inputs(couriers, "couriers")
        print("")
        courier_menu()
    elif u_input2 == "2":
        print(create_new_item(couriers, "couriers"))
        print("")
        courier_menu()
    elif u_input2 == "3":
        update_item(couriers, "couriers")
        print("")
        courier_menu()
    elif u_input2 == "4":
        delete_item(couriers, "couriers")
        print("")
        courier_menu(couriers, "couriers")

def product_menu():
    products = []
    with open("data\products.txt", "r") as productf:
        for line in productf:
            products.append(line.strip("\n"))
    product_menu_string = """Choose an option:
0 to go to main menu
1 for seeing the list of products
2 to add a new product
3 Update product list
4 Delete product\n"""
    print(product_menu_string)
    u_input2 = input()
    while u_input2 not in ("0","1","2","3","4"):
        print("Not a valid option. Try again.") 
        print(product_menu_string)        
        u_input2 = input()
    if u_input2 == "0":
        menu()
    elif u_input2 == "1":
        show_items_and_gen_valid_inputs(products, "products")
        print("")
        product_menu()
    elif u_input2 == "2":
        print(create_new_item(products, "products"))
        print("")
        product_menu()
    elif u_input2 == "3":
        update_item(products, "products")
        print("")
        product_menu()
    elif u_input2 == "4":
        delete_item(products, "products")
        print("")
        product_menu(products, "products")


def order_menu():
    orders = []
    with open("data\orders.txt", "r+") as orderf:
        for line in orderf:
            orders.append(line.strip("\n"))
    order_menu_string = """Choose an option:
0 to go to main menu
1 for seeing the list of orders
2 to add a new order
3 to update order status
4 to to change an order
5 to delete an order"""
    print(order_menu_string)
    u_input2 = input()
    while u_input2 not in ("0","1","2","3","4","5"):
        print("Not a valid option. Try again.") 
        print(order_menu_string)        
        u_input2 = input()
    if u_input2 == "0":
        menu()
    elif u_input2 == "1":
        show_items_and_gen_valid_inputs(orders, "orders")
        print("")
        order_menu()
    elif u_input2 == "2":
        print(create_new_item(orders, "orders"))
        print("")
        order_menu()
    elif u_input2 == "3":
        update_order(orders, "orders", True)
        print("")
        order_menu()
    elif u_input2 == "4":
        update_order(orders, "orders")
        print("")
        order_menu()
    elif u_input2 == "5":
        delete_item(orders, "orders")
        print("")
        order_menu(orders, "orders")

def menu():
    main_menu_string = """Choose an option:
0 to exit
1 for seeing the products menu
2 for seeing the courier menu
3 for seeing the order menu"""
    print(main_menu_string)
    u_input = input()
    print("")
    while u_input not in ("0", "1", "2", "3"):
        print("Not a valid option. Try again.")
        print(main_menu_string)
        u_input = input()
        print("")
    if u_input == "0":
        exit("Program ended")
    elif u_input == "1":
        print("")
        product_menu()
    elif u_input == "2":
        print("")
        courier_menu()
    elif u_input == "3":
        print("")
        order_menu()


def update_order(selected_list, name_of_selected_list, status = False):
    valid_input = show_items_and_gen_valid_inputs(selected_list, name_of_selected_list)
    print(f"""Enter the number for the {name_of_selected_list[:-1]} you want
to update or x to go to main menu: """)
    updatee = input()
    while updatee not in valid_input:
        print(f"Not a valid option. Try again.\nChoose an option:")
        updatee = input(f"""Enter the number for the {name_of_selected_list[:-1]} you want
to update or x to go back to main menu: """)        
    if str(updatee).lower() == "x":
        menu()
    else:
        updatee_str = selected_list[int(updatee)].replace("'", "\"")
        updatee_as_dict = json.loads(updatee_str)
        #print(updatee)
    if status:
        new_status = input(f"Enter the new status: ")
        if new_status.strip() != "":
            updatee_as_dict["status"] = new_status
    else:
        name = input("Enter the customer name: ")
        if name.strip() != "":
            updatee_as_dict["customer_name"] = name
        address = input("Enter the customer address: ")
        if address.strip() != "":
            updatee_as_dict["customer_address"] = address
        phone = input("Enter the customer phone: ")
        if phone.strip() != "":
            updatee_as_dict["customer_phone"] = phone
    with open(f"data\{name_of_selected_list}.txt", "r") as itemsf:
            lines = itemsf.readlines()
    if int(updatee) == len(lines)-1:
        lines[int(updatee)] = str(updatee_as_dict)
    else:
        lines[int(updatee)] = f"{str(updatee_as_dict)}\n"
    with open(f"data\{name_of_selected_list}.txt", "w") as itemsf:
            itemsf.writelines(lines)
    print(f"Order {lines[int(updatee)]} has been updated")
    

menu()


def test_always_passes():
    assert True

def test_always_fails():
    assert False