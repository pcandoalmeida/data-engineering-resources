import re 
orders = [{
        "customer_name": "John", 
        "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
        "customer_phone": "0789887334",
        "status": "preparing"
}]

def load_products_from_file():
    with open("products.txt") as file:
        lines = file.readlines()
        products = [line.rstrip() for line in lines]
    return products 

def load_couriers_from_file():
    with open("couriers.txt") as file:
        lines = file.readlines()
        couriers = [line.rstrip() for line in lines]
    return couriers 



def main_menu(): 
    print("\n~~~~~~~~~~~~~~~~~~~ MAIN MENU ~~~~~~~~~~~~~~~~~~~~~~")
    while True: 
        selected_option = int(input("""
        0 --- Save any changes & Exit 
        1 ----- View the product menu 
        2 ----- View the courier menu 
        3 ---- -- View the order menu 
    \n"""))
        if selected_option not in [0, 1, 2, 3]:
            print("\nInvaid option. Select again! \n")
        else:
            return selected_option


def product_menu():
    print("\n~~~~~~~~~~~~~~~~ PRODUCT MENU ~~~~~~~~~~~~~~~~~~~")
    while True:
        selected_option = int(input("""
        0 ----- Return to the main menu 
        1 ------- View all the products
        2 ----------- Add a new product
        3 -- Update an existing product
        4 ------------ Delete a product
        \n"""))
        if selected_option not in [0, 1, 2, 3, 4]:
            print("Invaid option. Select again! ")
        else:
            return selected_option


def courier_menu():
    print("\n~~~~~~~~~~~~~~~~~~ COURIER MENU ~~~~~~~~~~~~~~~~~~~~~")
    while True:
        selected_option = int(input(
        """
        0 ----- Return to the main menu 
        1 ------- View all the couriers 
        2 --------------- Add a courier 
        3 -- Update an existing courier 
        4 ------------ Delete a courier 
    \n"""
    ))
        if selected_option not in [0, 1, 2, 3, 4, 5]:
            print("Invaid option. Select again! ")
        else:
            return selected_option

def order_menu():
    print("\n~~~~~~~~~~~~~~~~~~ ORDER MENU ~~~~~~~~~~~~~~~~~~~~~")
    selected_option = int(input(
        """
        0 ---- Return to the main menu 
        1 ------------ View all orders
        2 --------- Create a new order
        3 ---- Update the order status 
        4 --- Update an existing order 
        5 ------------ Delete an order 
        """
    ))
    if selected_option not in [0, 1, 2, 3, 4, 5]:
        print("Invaid option. Select again! ")
        return order_menu()
    else:
        return selected_option

def display_list_with_indexes(list):
    print("\nIndex |  Order\n")
    for index, order in enumerate(list):
        print(f"{index}       {order}")

# def validate_phone_num(phone_number):
#     pattern = "^0+[0-9]{10}$"
#     return re.search(pattern, phone_number)

def isValidIndex(index,list): 
    try: 
        list[index]
        return True
    except IndexError:
        print("Invalid index. Try again")
        return False
    except ValueError: 
        print("Invalid index. Cannot accept string. Try again")
        return False 



    
def confirm_updates_menu():
    while True:
        user_input = input("Confirm changes: (y) yes (n) no \n")
        if user_input =="y": 
            return True
        elif user_input == "n": 
            return False
        else:
            print("Invalid input! Try again!")


    

#product functions 

def display_products():
    products = load_products_from_file()
    print("-------------List Of Products--------------")
    print(f"\n{products}")


def add_product():
    products = load_products_from_file()
    print("-------------Adding a Product--------------\n")
    new_product = input("Product name: ").title()
    if new_product in products: 
        print("Product already added!\n")
        user_input = input("(y) Try again (n) Exit ")
        if user_input == "y": 
            return add_product()
        else: 
            print("\n-------------EXIT--------------\n")
    else:
        is_confirmed = confirm_updates_menu()
        if is_confirmed: 
            with open("products.txt","a") as file:
                file.write(new_product + "\n")
            print(f"{new_product} has been successflly added\n")
        else: 
            print("\n-------------EXIT--------------\n")

    
def update_product():
    print("\n-------------Updating An Existing Product--------------\n")
    products = load_products_from_file()
    display_list_with_indexes(products)
    while True: 
        index = int(input("Index of the order: \n"))
        if isValidIndex(index, products):
            old_product= products[index]
            print(f"You want to modify the product: {products[index]}")
            updated_product = input("\n New product: ").title()
            print(f"You want to update {old_product} to {updated_product}")
            is_confirmed = confirm_updates_menu()
            if is_confirmed: 
                with open("products.txt",'w') as f:
                    for i,line in enumerate(products):        
                        if i == index:                             
                            f.writelines(updated_product + "\n")
                        else:
                            f.writelines(line + "\n")
                print(f"{products[index]} successfully updated to {updated_product}\n")
                print("\n ------------------SUCCESSFULLY UPDATED -------------------\n")
                break
        
            else: 
                print("\n-------------EXIT--------------\n")

    
def delete_product():
    print("-------------Deleting a Product--------------")
    products = load_products_from_file()
    display_list_with_indexes(products)  
    while True:
        index = int(input("Index of the order \n"))
        if isValidIndex(index, products):
            print(f"You want to delete: {products[index]}")
            is_confirmed = confirm_updates_menu()
            if is_confirmed: 
                with open("products.txt",'w') as f:
                    for i,line in enumerate(products):        
                        if i == index:                             
                            continue
                        else:
                            f.writelines(line + "\n")
                print("-------------SUCCESSFULLY DELETED--------------\n")
                break
            else:
                user_input = input("(y)Delete another product (n) Exit")
                if user_input == "y":
                    return delete_product()
                else:
                    print("\n-------------EXIT--------------\n")
                    break



def display_couriers():
    print("-------------List Of Couriers--------------\n")
    couriers = load_couriers_from_file()
    print(f"\n{couriers}")


 
def add_courier():
    couriers = load_couriers_from_file()
    print("-------------Adding a Courier--------------\n")
    new_courier = input("Courier: ").title()
    if new_courier in couriers: 
        print("Courier already added!\n")
        user_input = input("(y)Try again (n) exit \n")
        if user_input == "y": 
            return add_courier()
        else: 
            print("\n-------------EXIT--------------\n")
    else:
        is_confirmed = confirm_updates_menu()
        if is_confirmed:
            with open("couriers.txt","a") as file:
                file.write(new_courier + "\n")
            print(f"You have added {new_courier} to the list\n")
            print("-------------SUCCESSFULLY ADDED--------------\n")
        else:
            print("\n-------------EXIT--------------\n")
            
  
def update_product():
    print("\n-------------Updating An Existing Product--------------\n")
    products = load_products_from_file()
    display_list_with_indexes(products)
    while True: 
        index = int(input("Index of the order: \n"))
        if isValidIndex(index, products):
            old_product= products[index]
            print(f"You want to modify the product: {old_product}")
            updated_product = input("\n New product: ").title()
            print(f"You want to update {old_product} to {updated_product}")
            is_confirmed = confirm_updates_menu()
            if is_confirmed: 
                with open("products.txt",'w') as f:
                    for i,line in enumerate(products):        
                        if i == index:                             
                            f.writelines(updated_product + "\n")
                        else:
                            f.writelines(line + "\n")
                print(f"{products[index]} successfully updated to {updated_product}\n")
                print("\n ------------------SUCCESSFULLY UPDATED -------------------\n")
                break
        
            else: 
                print("\n-------------EXIT--------------\n")

def update_courier():
    print("\n-------------Updating An Existing Courier--------------\n")
    couriers = load_couriers_from_file()
    display_list_with_indexes(couriers)
    while True:
        index = int(input("Index of the order: \n"))
        if isValidIndex(index, couriers):
            courier = couriers[index]
            print(f"You want to modify the product: {courier}")
            updated_courier = input("New courier: ").title()
            print(f"You want to update {courier} to {updated_courier}")
            is_confirmed = confirm_updates_menu()
            if is_confirmed: 
                with open("couriers.txt",'w') as f:
                    for i,line in enumerate(couriers):         
                        if i == index:                              
                            f.writelines(updated_courier + "\n")
                        else:
                            f.writelines(line + "\n")

                    print(f"{courier} successfully updated to {updated_courier}\n")
                    print("\n ------------------SUCCESSFULLY UPDATED -------------------\n")
                    break
        
            else: 
                print("\n-------------EXIT--------------\n")
                break

    
def delete_courier():
    print("\n-------------Deleting a Courier--------------\n")
    couriers = load_couriers_from_file()
    display_list_with_indexes(couriers)
    while True:
        index = int(input("Index of the order:  "))
        if isValidIndex(index, couriers):
            print(f"You want to delete: {couriers[index]}")
            is_confirmed = confirm_updates_menu()
            if is_confirmed: 
                with open("couriers.txt",'w') as f:
                    for i,line in enumerate(couriers):        
                        if i == index:                             
                            continue
                        else:
                            f.writelines(line + "\n")
                print("-------------SUCCESSFULLY DELETED--------------\n")
                break
            else: 
                user_input = input("(y)Delete another courier (n) Exit \n")
                if user_input == "y":
                    return delete_courier()
                else: 
                    print("\n-------------EXIT--------------\n")
                    break

def display_orders(): 
   print("-------------List Of Orders--------------")
   print(f"\n{orders}")


def get_valid_address_from_user():
   while True:
        address_line1= input("Address Line 1: ")
        address_line2= input("Address Line 2:(Optional)")
        city = input("City: ")
        country = input("Country: ")
        postcode = input("Postcode: ")
        customer_address = ""
        if address_line1 != "" and city != "" and country!= "" and postcode != "": 
            customer_address = address_line1 + ", " +  address_line2 + ", " + city+ ", "+ country + ", " + postcode
            if address_line2=="":
                customer_address = address_line1 + ", "  + city+ ", "+ country + ", " + postcode
            return customer_address
        else: 
            print("Invalid address - try again")


def get_valid_phone_num_from_user():
    while True:
        customer_number = input("Customer phone number in this formatt (0xxxxxxx):  ")
        pattern = "^0+[0-9]{10}$"
        if re.search(pattern, customer_number):
            return customer_number
        else: 
            print("Invalid format - Try again!")



def get_valid_address_from_user():
    while True: 
        address_line1= input("Address Line 1: ")
        address_line2= input("Address Line 2:(Optional): ")
        city = input("City: ")
        country = input("Country: ")
        postcode = input("Postcode: ")
        customer_address = ""
        if address_line1 != "" and city != "" and country!= "" and postcode != "": 
            customer_address = address_line1 + ", " +  address_line2 + ", " + city+ ", "+ country + ", " + postcode
            if address_line2=="":
                customer_address = address_line1 + ", "  + city+ ", "+ country + ", " + postcode
            return customer_address
        else: 
            print("Invalid address - try again")


def add_order():
    print("-------------CREATING AN ORDER--------------\n")
    customer_name = input("Customer name: ")
    customer_address = get_valid_address_from_user()
    customer_phone = get_valid_phone_num_from_user()
    is_confirmed = confirm_updates_menu()
    if is_confirmed:
        orders.append({
                "customer_name": customer_name, 
                "customer_address": customer_address,
                "customer_phone": customer_phone,
                "status": "Preparing"
                        })
        print("-------------SUCCESSFULLY UPDATED----------------")
    else: 
        print("\n-------------EXIT--------------\n")
        

def update_order_status():
    print("-------------Updating An Existing Product--------------\n")
    display_list_with_indexes(orders)
    while True: 
        index = int(input("Index of the order: "))
        if isValidIndex(index, orders):
            print("This is the order you want to update: ", orders[index])
            order_status = input("New order status: ")
            is_confirmed = confirm_updates_menu()
            if is_confirmed:
                orders[index]["status"]=order_status
                print("Order status successfully updated")
                break
            else: 
                print("\n-------------EXIT--------------\n")
                break

    


def update_order():
    print("-------------Updating An Existing Product--------------")
    for index, order in enumerate(orders):
        print(index, "    : ", order)
    while True:
        order_index = int(input("Index of the order:  "))
        if isValidIndex(order_index, orders):
            customer_name=input("Name: ")
            change_address= input("Do you want to change address: (y) yes (n) no  ")
            customer_address=""
            if change_address=="y":
                customer_address = get_valid_address_from_user()
            print(customer_address)
            customer_phone=""
            change_phone= input("Do you want to change phone number: (y) yes (n) no  ")
            if change_phone=="y":
                customer_phone = get_valid_phone_num_from_user()
            
            customer_order_status = input("Customer order status:  ")

            if customer_name != "": 
                prev_name= orders[order_index]["customer_name"]
                print(f"You want to change your name from {prev_name} to {customer_name}")
            if customer_address!= "": 
                prev_address= orders[order_index]["customer_address"]
                print(f"You want to change your address from {prev_address} to {customer_address}")
            if customer_phone!= "": 
                prev_phone= orders[order_index]["customer_phone"]
                print(f"You want to change your phone number from {prev_phone} to {customer_phone}")
            if customer_order_status!= "": 
                prev_status= orders[order_index]["status"]
                print(f"You want to change your order status from {prev_status} to {customer_order_status}")
            is_confirmed = confirm_updates_menu()
    
            if is_confirmed:
                if customer_name!= "": 
                    orders[order_index]["customer_name"] = customer_name
                if customer_address!= "": 
                    orders[order_index]["customer_address"] = customer_address
                if customer_phone!="": 
                    orders[order_index]["customer_phone"] = customer_phone
                if customer_order_status!="":
                    orders[order_index]["status"] = customer_order_status
                print("-------------SUCCESSFULLY UPDATED----------------")
                break

            else: 
                print("\n-------------EXIT--------------\n")
                break
    
    

def delete_order():
    print("---------------Deleting a Product----------------")
    for index, order in enumerate(orders):
        print(index, "    : ", order)
    # order_index = isValidIndex(orders)
    while True:
        order_index = int(input("Index of the order:  "))
        if isValidIndex(order_index, orders):
            print(f"you want to delete order {orders[order_index]}")
            is_confirmed = confirm_updates_menu()
            if is_confirmed: 
                orders.pop(order_index)
                print("-------------SUCCESSFULLY DELETED--------------")
                break 
            else:
                print("\n-------------EXIT--------------\n")
                break

    
        

    

    




def main(selected_main_option):
    while selected_main_option!=0:
        if selected_main_option==0:
            print("Saving product list")
            print("Saving courier list")
            print("exit")
            break #Exit app 
        elif selected_main_option==1: 
            selected_product_option=product_menu()
            if selected_product_option==0: 
                selected_main_option= main_menu()
            elif selected_product_option ==1: 
                display_products()
            elif selected_product_option==2: 
                add_product()
            elif selected_product_option==3: 
                update_product()
            elif selected_product_option==4: 
                delete_product()
        elif selected_main_option==2: 
            selected_courier_option = courier_menu()
            if selected_courier_option==0: 
                selected_main_option= main_menu()
            elif selected_courier_option ==1: 
                display_couriers()
            elif selected_courier_option==2: 
                add_courier()
            elif selected_courier_option==3: 
                update_courier()
            elif selected_courier_option==4: 
                delete_courier()
        elif selected_main_option==3: 
            selected_courier_option = order_menu()
            if selected_courier_option==0: 
                selected_main_option= main_menu()
            elif selected_courier_option ==1: 
                display_orders()
            elif selected_courier_option==2: 
                add_order()
            elif selected_courier_option==3: 
                update_order_status()
            elif selected_courier_option==4: 
                update_order()
            elif selected_courier_option==5: 
                delete_order()

main(selected_main_option:=main_menu())    


