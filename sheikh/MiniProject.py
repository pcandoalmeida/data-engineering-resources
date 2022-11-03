from ProjectFunctions import products,orders,couriers
from ProjectFunctions import new_product,updating_product,delete_product
from ProjectFunctions import customer_inputs,update_status,update_order,delete_order
from ProjectFunctions import read_file,write_file,new_courier,updating_courier,delete_courier

def main_menu():
    global main_menu_input
    main_menu_input = int(input("""
Main Menu

0: Exit
1: Product Menu Options
2: Order Menu
3: Courier Menu
>>>"""))

def products_menu():
    global products_menu_input
    products_menu_input = int(input("""
Products Menu

0: Return To Main Menu
1: Display Products
2: Add New Product
3: Change Product
4: Remove Product
>>>"""))

def order_menu():
    global order_menu_input
    order_menu_input = int(input("""
Order Menu

0: Return To Main Menu
1: Display Orders
2: New Order
3: Order Status
4: Update Order
5: Remove Order 
>>>"""))

def courier_menu():
    global courier_menu_input
    courier_menu_input = int(input("""
Courier Menu

0: Return To Main Menu
1: Display Couriers
2: Add New Courier
3: Update Courier
4: Remove Courier 
>>>"""))

read_file()
main_menu()

while True:
    if main_menu_input == 1:
        products_menu()
    
        if products_menu_input == 0:
            print("Returning to Main Menu")
            main_menu()

        elif products_menu_input == 1:
            print(products)

        elif products_menu_input == 2:
            new_product()

        elif products_menu_input == 3:
            updating_product()

        elif products_menu_input == 4:
            delete_product()
      

    elif main_menu_input == 2:
        order_menu()

        if order_menu_input == 0:
            print("Returning to Main Menu")
            main_menu()

        elif order_menu_input == 1:
            for i in orders:
                print(i)
        # print(orders)
    
        elif order_menu_input == 2:
            customer_inputs()

        elif order_menu_input == 3:
            update_status()

        elif order_menu_input == 4:
            update_order()

        elif order_menu_input == 5:
            delete_order()
    
    elif main_menu_input == 3:
        courier_menu()
        
        if courier_menu_input == 0:
            print("Returning to Main Menu")
            main_menu()
        
        elif courier_menu_input == 1:
            print(couriers)
        
        elif courier_menu_input == 2:
            new_courier()
        
        elif courier_menu_input == 3:
            updating_courier()
        
        elif courier_menu_input == 4:
            delete_courier()

    elif main_menu_input == 0:
        write_file()
        print("bye")
        exit()

    else:
        print("Not a vaild input")
        break