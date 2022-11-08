import project_functions as pf

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

pf.read_file()
main_menu()

while True:
    if main_menu_input == 1:
        products_menu()
    
        if products_menu_input == 0:
            print("Returning to Main Menu")
            main_menu()

        elif products_menu_input == 1:
            print(pf.products)

        elif products_menu_input == 2:
            pf.new_product()

        elif products_menu_input == 3:
            pf.updating_product()

        elif products_menu_input == 4:
            pf.delete_product()
      

    elif main_menu_input == 2:
        order_menu()

        if order_menu_input == 0:
            print("Returning to Main Menu")
            main_menu()

        elif order_menu_input == 1:
            for i in pf.orders:
                print(i)
        # print(orders)
    
        elif order_menu_input == 2:
            pf.customer_inputs()

        elif order_menu_input == 3:
            pf.update_status()

        elif order_menu_input == 4:
            pf.update_order()

        elif order_menu_input == 5:
            pf.delete_order()
    
    elif main_menu_input == 3:
        courier_menu()
        
        if courier_menu_input == 0:
            print("Returning to Main Menu")
            main_menu()
        
        elif courier_menu_input == 1:
            print(pf.couriers)
        
        elif courier_menu_input == 2:
            pf.new_courier()
        
        elif courier_menu_input == 3:
            pf.updating_courier()
        
        elif courier_menu_input == 4:
            pf.delete_courier()

    elif main_menu_input == 0:
        pf.write_file()
        print("bye")
        exit()

    else:
        print("Not a vaild input")
        break