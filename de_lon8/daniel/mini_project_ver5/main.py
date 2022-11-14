import os

from menu_classes import ProductMenu, CourierMenu, OrderMenu

product_menu = ProductMenu()
courier_menu = CourierMenu()
order_menu = OrderMenu()
app_end = False


while app_end is not True:
    os.system('clear')
    command = input(f"Welcome to Daniel's cafe, please state your command!"
                    f"\n0. Exit"
                    f"\n1. Product Menu"
                    f"\n2. Courier Menu."
                    f"\n3. Order Menu."
                    f"\n")

    if command == '1':

        product_menu.show_product_menu()

    elif command == '2':

        courier_menu.show_courier_menu()

    elif command == '3':

        order_menu.show_order_menu()

    elif command == '0':

        os.system('clear')

        product_menu.save_list_to_csv()
        courier_menu.save_list_to_csv()
        order_menu.save_list_to_csv()

        print("Goodbye!! See you next time.")

        app_end = True

    else:
        print("\nPlease only input number as command.\n")


