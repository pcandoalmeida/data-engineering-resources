print(" |Cafe Generation| " )
shopping_basket = {}
order_status = 'preparing'
orders_list = []
main_menu = int(input(" '0' To Exit App \n '1' To View Menu \n '2' To Create New Product \n '3' To Update Product \n '4' To Delete Product \n '5' To Access Product "))

drink_list = ["coffee","tea","hot chocolate"]

product_list = ["breakfast", "wraps", "chips", "pastries", ]

while main_menu != 0:
    if main_menu == 1:

        menu2 = int(input("1 for drinks, 2 for food: "))
        if menu2 == 1:
            print(drink_list)
        else:
            print(product_list)

    elif main_menu == 2:
        menu2 = int(input("1 to create new drink, 2 for new food: "))
        if menu2 == 1:
            new_drink = input("Add New Drink: ")
            drink_list.append(new_drink)
            print(drink_list)
        else:
            new_product = input("add new product: ")
            product_list.append(new_product)
            print(product_list)

    elif main_menu == 3:
        for i in enumerate(product_list):
            print(i)
        idx_product = int(input("Product index that needs to be changed: "))
        upd_product = input("Put in updated product")
        product_list[idx_product] = upd_product
        print(product_list)
    elif main_menu == 4:
        for i in enumerate(product_list):
            print(i)
        index_p = int(input( " choose index that needs to be deleted: "))
        del product_list[index_p]
        print(product_list)
    elif main_menu == 5: #TODO: make a while loop to keep asking to add things to basket
        order_menu = int(input(""" 0 To Return to Main Menu
        1 To View Orders
        2 Add customer information
        3 to update existing order status
        4 to update order
        5 to delete order
        """))
        while order_menu != 0:
            if order_menu == 1:
                print(orders_list)
            elif order_menu == 2:
                customer_name = input("What is your name?: ")
                customer_address = input('what is your address?: ')
                customer_number = input('what is your number?:')
                shopping_basket['Customer Name: '] = customer_name
                shopping_basket['Customer Address: '] = customer_address
                shopping_basket['Customer Number'] = customer_number
                shopping_basket['order_status'] = order_status
                print(shopping_basket)
                orders_list.append(shopping_basket)
            elif order_menu == 3:
                update_status = input('what would you like to change Order Status too?')
                shopping_basket['order_status'] = update_status
                print(shopping_basket)
            elif order_menu == 4:
                for i in enumerate(orders_list):
                    print(i)
                Change_o = int(input("which order would you like to change"))
                print(orders_list[Change_o])
                new_name = input("What is your name?: ")
                new_address = input('what is your address?: ')
                new_number = input('what is your number?:')
                new_status = input('what is the status')
                Dictionary2 = {'Customer Name:': new_name,'Customer Address:': new_address,'Customer Number:': new_number,'Order Status': new_status,}
                orders_list[Change_o] = Dictionary2
                print(orders_list)
            elif order_menu == 5:
                shopping_basket.clear()
                print(shopping_basket)
            order_menu = int(input(""" 0 To Return to Main Menu
            1 To print Order 
            2 Customer information
            3 to update existing order status
            4 to update order
            5 to delete order
            """))     
    ans = input("would you like to continue or exit: ")
    if ans == "exit":
        exit()
    else:
        main_menu = int(input(" '0' To Exit App \n '1' To Access Menu \n '2' To Create New Product \n '3' To Update Product \n '4' To Delete Product: "))
    
            

