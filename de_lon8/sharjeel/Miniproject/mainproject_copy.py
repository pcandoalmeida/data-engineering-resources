import time
import csv

def product_list():
    with open("products.csv", "r") as product_list:
        next(product_list, None)
        products_contents = csv.reader(product_list)
        for i,x in enumerate(products_contents):
            print(f"Number: {i}, Product: {x}")

def orders_list():
    with open("orders.csv", "r") as file:
        next(file, None)
        orders_contents = csv.reader(file)
        for i,x in enumerate(orders_contents):
            print(f"Number: {i}, Order: {x}")

def product_list_delete():
    with open("products.csv", "a+") as product_list:
        next(product_list, None)
        lines = csv.reader(product_list)
        numline = len(product_list.readlines())
        for i, x in enumerate(lines):
            print(f"Number: {i}, Product: {x}")
        choice = int(input("Choose the number of the product you'd like to delete: "))
        if (choice <= numline):
            drop(lines[choice])
            with open("products.csv", "r+") as product_list:
                for line in lines:
                    product_list.DictWrite(line)
        else:
            print("line:", choice, "is not in the products")
            print("The file has ", numline-1, "lines.")

def product_list_update():
    with open("products.csv", "a+") as product_list:
        next(product_list, None)
        products_contents = csv.reader(product_list)
        numline = len(product_list.readlines())
        for i,x in enumerate(products_contents):
            print(f"Number: {i}, Product: {x}")
        choice = int(input("Choose the courier you'd like to replace "))
        if (choice <= numline):
            lines[choice] = input("Please enter the name of the new products: ")
        else:
            print("line:", choice, "is not among the products")

# def updatefile(updatedlist):
#     with open("product.csv","w",newline="") as f:
#         Writer=csv.writer(f)
#         Writer.writerows(updatedlist)
#         print("File has been updated")

# def main():
#     #1. This code snippet asks the user for a username and deletes the user's record from file.
#     updatedlist=[]
#     with open("product.csv",newline="") as f:
#       reader = csv.reader(f)
#       product = input("Enter the name of the product ypu'd like to add: ")
#       for row in reader: 
#             if row[0]!= product: 
#                 updatedlist.append(row)
#       print(updatedlist)
#       updatefile(updatedlist)

def write_prod_file():
    with open("products.csv", "a") as products_list:
        fieldnames = ["Product", "Price"]
        writer = csv.DictWriter(products_list, fieldnames=fieldnames)
        prod_name = input("Whats the name of the new product? ")
        prod_price = float(input("Whats the price of the product?: "))
        writer.writerow({"Product": prod_name, "Price": prod_price})

def read_cour_file():
    with open("couriers.txt", "r") as couriers:
        couriers_contents = couriers.readlines()
        for i in couriers_contents:
            print(i)

def write_cour_file():
    with open("couriers.txt", "a") as couriers:
        couriers.write(input("Who would you like to add? "))

def replace_cour_file():
    with open("couriers.txt", "r") as couriers:
        lines = couriers.readlines()
        for i, x in enumerate(lines):
            print(f"Number: {i}, Courier: {x}")
        choice = int(input("Choose the courier you'd like to replace "))
        if (choice <= len(lines)):
            lines[choice] = input("Please enter the name of the new courier: ")
        else:
            print("line:", choice, "is not in the couriers")

def delete_courier_file():
    with open("couriers.txt", "r+") as couriers:
        lines = couriers.readlines()
        for i, x in enumerate(lines):
            print(f"Number: {i}, Courier: {x}")
        choice = int(input("Choose the inndex of the courier you'd like to delete: "))
        if (choice <= len(lines)):
            del lines[choice] 
            with open("couriers.txt", "w") as couriers:
                for line in lines:
                    couriers.write(line)
        else:
            print("line:", choice, "is not in the couriers")

def add_order():
    with open("orders.csv", "a") as orders:
        fieldnames = ["customer_name", "customer_address", "customer_phone_number", "courier", "Status"]
    writer = csv.DictWriter(orders, fieldnames=fieldnames)
    c_name = input("Please enter your name: ")
    c_address = input("Please enter your address: ")
    c_phone_number = input("Please enter your phone number: ")
    read_cour_file()
    courier = input("Please enter the name of a courier for the delivery: ")
    writer.writerow({
    "customer_name": c_name,
    "customer_address": c_address,
    "customer_phone_number": c_phone_number,
    "courier": courier,
    "Status": "Preparing..."
    })

orders = []


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

    while True:

        product_option = int(input("Please select an option: "))

        if product_option == 0:
            menu()

        elif product_option == 1:
            product_list()

        elif product_option == 2:
            write_prod_file()
            product_list()

        elif product_option == 3:
            product_list_delete()

        elif product_option == 4:
            product_list_update()

        else:
            print("""Uh-oh Invalid option
    Please try again!""")  
            product_menu()

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

    while True:

        order_option = int(input("Please select an option: "))
    
        if order_option == 0:
            menu()

        elif order_option == 1:
            orders_list()
            # print(orders)
            time.sleep(5)
            order_menu()

        elif order_option == 2:
            with open("orders.csv", "a") as orders:
                fieldnames = ["customer_name", "customer_address", "customer_phone_number", "courier", "Status"]
                writer = csv.DictWriter(orders, fieldnames=fieldnames)
                c_name = input("Please enter your name: ")
                c_address = input("Please enter your address: ")
                c_phone_number = input("Please enter your phone number: ")
                read_cour_file()
                courier = input("Please select a courier for the delivery: ")
                writer.writerow({
                "customer_name": c_name,
                "customer_address": c_address,
                "customer_phone_number": c_phone_number,
                "courier": courier,
                "Status": "Preparing..."
                })
            orders_list()
            time.sleep(2)
            order_menu()

        elif order_option == 3:
            for index, order in enumerate(orders):
                print(f"Index: {index}, Order: {order}")
            order_index = int(input("Please select the index of your order: "))
            orders[order_index]
            order_status = input("Order status: ")
            orders[order_index]["Status"] = order_status
            print("Orders:", orders)
            time.sleep(5)
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
            time.sleep(5)
            order_menu()

        elif order_option == 5:
            print(orders)
            for index, order in enumerate(orders):
                print(f"Index: {index}, Order: {orders}")
            order_index = int(input(f"Select the order you'd like to delete: "))
            del orders[order_index]
            print(orders)
            time.sleep(5)
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

    while True:

        courier_option = int(input("Please slect your option: "))

        if courier_option == 0:
            menu()

        if courier_option == 1:
            read_cour_file()
            time.sleep(5)
            courier_menu()
        
        if courier_option == 2:
            write_cour_file()
            time.sleep(5)
            courier_menu()

        if courier_option == 3:
            delete_courier_file()
            time.sleep(5)
            courier_menu()

        if courier_option == 4:
            replace_cour_file()
            time.sleep(5)
            courier_menu()


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
            print("""Uh oh, invalid option
            Please choose one of the following:""")
            menu()
    
    exit

menu()

print("Miss you already!")
