from typing import MutableSequence
import hashlib
import sys

def read_prod_file():
    with open("products.txt", "r") as products:
        products_contents = products.readlines()
        for i in products_contents:
            print(i)

def read_cour_file():
    with open("couriers.txt", "r") as couriers:
        couriers_contents = couriers.readlines()
        for i in couriers_contents:
            print(i)

def write_prod_file():
    with open("products.txt", "a+") as products:
        for line in products:
            products.write(line)
            products.write("\n")

def write_cour_file():
    with open("couriers.txt", "a+") as couriers:
        couriers.writelines(input("Who would you like to add? "))
        couriers.close()

#Not sure which one to use ^
# def write_cour_file():
#     choice = input()
#     with open("couriers.txt", "a+") as couriers:
#         couriers.write(f"{choice}")


orders = []

product_list = ["Snickers", "Kit Kat", "Mars", "Bueno", "Ritter"]

def product_menu():
    print( """
    Product menu
    -0- Back to Main Menu
    -1- Show Products
    -2- Add products
    -3- Delete products
    -4- Change products

    What would you like to do?
    
    """ )
    product_option = int(input("Please select an option: "))

    while True:
        if product_option == 0:
            menu()

        elif product_option == 1:
            global product_list
            print(product_list)
            product_option = int(input("Would you like to do anything else: "))

        elif product_option == 2:
            print('What is the name of the new product? ')
            item = input()
            product_list.append(item)
            print(product_list)
            product_option = int(input("Would you like to do anything else: "))

        elif product_option == 3:
            print(product_list)
            for product in range(len(product_list)):
                print(f'-{product}- {product_list[product]}')
            try:
                to_delete = int(input("Please choose the number of the product you'd like to delete: "))
                print(f"You have selected {product_list[to_delete]}")
            
            except ValueError:
                print("\nYou can only input integers (whole numbers) Please try again\n")

            else:
                product_list.pop(to_delete)
                print(product_list)
                product_option = int(input("Would you like to do anything else: "))

        elif product_option == 4:
            for i in range(len(product_list)):
                print(f'-{i}- {product_list[i]}')

            while True:

                try:
                    to_change = int(input('Please choose the product from the available options. '))
                    print(f'You have selected {product_list[to_change]}: ')

                except IndexError:
                    print("Oh no, this product doesn't exit, please try again!")

                except ValueError:
                    print("\nYou can only input integers (whole numbers) Please try again\n")

                else:
                    product_list[to_change] = input('Enter the new product name: ')
                    print(product_list)
                    product_option = int(input("Would you like to do anything else: "))

        else:
            print("""Uh-oh Invalid option
    Please try again!""")  
            print(product_menu())
            product_option = int(input("Would you like to do anything else: "))   

def order_menu():
    print( """
    Order menu
    -0- Back to Main Menu
    -1- Show orders
    -2- Add new order
    -3- Change order
    -4- Delete order

    What would you like to do?
    
    """ )

    order_option = int(input("Please select an option: "))

    while True:
    
        if order_option == 0:
            menu()

        elif order_option == 1:
            print(orders)
            order_menu

        elif order_option == 2:
            c_name = input("Please enter your name: ")
            c_address = input("Please enter your address: ")
            c_phone_number = input("Please enter your phone number: ")
            orders.append({
                "customer_name": c_name,
                "customer_address": c_address,
                "customer_phone_number": c_phone_number,
                "Status": "Preparing..."
            })
            print(orders)
            order_menu()
            

        elif order_option == 3:
            for index, order in enumerate(orders):
                print(f"Index: {index}, Order: {order}")
            order_index = int(input("Please select the index of your order: "))
            orders[order_index]
            order_status = input("Order status: ")
            orders[order_index]["Status"] = order_status
            print("Orders:", orders)
            order_menu()

        elif order_option == 4:
            for index, order in enumerate(orders):
                print(f"Index: {index}, Order: {orders}")
            order_index = int(input("Please select your order from the index: "))
            for key, value in orders[order_index].items():
                if key == "Status":
                    continue 
                order_update_input = (f"Update number - {key}: ")
                if order_update_input:
                    orders[order_index][key] = order_update_input
            print(orders)
            order_menu()

        elif order_option == 5:
            print(orders)
            for index, order in enumerate(orders):
                print(f"Index: {index}, Order: {orders}")
            order_index = int(input(f"Select the order you'd like to delete: "))
            del orders[order_index]
            print(orders)
            order_menu()

        else:
            print("""Uh-oh Invalid option
    Please try again!""")  
            order_menu()


def courier_menu():
    print( """
    Order menu
    -0- Back to Main Menu
    -1- Show couriers
    -2- Add couriers
    -3- Delete couriers
    -4- Change couriers

    What would you like to do?
    
    """ )
    courier_option = int(input("Please slect your option: "))

    while True:

        if courier_option == 0:
            menu()

        if courier_option == 1:
            choice = input("Please add the nname of your driver: ")
            read_cour_file()
            exit
        
        if courier_option == 2:
            write_cour_file()
            read_cour_file




def menu():
    print( """
    Welcome to Sajid's Delivery Service!
    
    Please choose one of the following options:
    -0- Exit the delivery service
    -1- Product menu
    -2- Order menu
    -3- Courier menu
    
    """ )
    main_option = int(input("Choice: "))

    while main_option != 0:
        if main_option == 1:
            product_menu()
    
        elif main_option == 2:
            order_menu()

        elif main_option == 3:
            courier_menu()

        else:
            print("""Oh oh, invalid option
            Please choose one of the following:""")
            menu()
    
    exit


menu()

print("Miss you already!")
