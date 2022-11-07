product_list = ["Water", "Fanta", "Croissant", "Apple"] # Decent

orders_list = []

# START OF OUTER LOOP <---------
while True:
    start = int(input("Welcome to Julio's Cafe: \n\
    Here are our Main Menu Options: \n\
    0. Exit \n\
    1. Product Menu Option \n\
    2. Orders Menu \n\
    >>"))

    if start == 0: # start(0) == 0 => TRUE, start(1) == 0 => FALSE
        break

    elif start == 1:
        print("Product Menu Options")
        
        product_menu_option = int(input("Please select one of the following options: To return to main menu press 0, to view the product list press 1, to add a new product to the list press 2, to update an exisiting product press 3 and to delete a product press 4: "))
        # START OF PMO INNER LOOP <---------
        while product_menu_option != 0: # while pmo is not 0, continue into the loop; if 0, break
           
           # product list
            if product_menu_option == 1:
                print("\nProduct list: ", product_list)
                product_menu_option = int(input("Please select one of the following options: To return to main menu press 0, to view the product list press 1, to add a new product to the list press 2, to update an exisiting product press 3 and to delete a product press 4: "))
            
            # adding item to product list
            elif product_menu_option == 2:
                product_name = input("What is the new product you would like to add?")
                print("\nProduct list: ", product_list.append(product_name))
                product_menu_option = int(input("Please select one of the following options: To return to main menu press 0, to view the product list press 1, to add a new product to the list press 2, to update an exisiting product press 3 and to delete a product press 4: "))            
            
            # update exisiting product
            elif product_menu_option == 3:
                print(list(enumerate(product_list)))
                product_index = int(input("Product Index: "))
                product_name = input("Product Name: ")
                product_list[product_index] = product_name
                print("\nProduct list: ", product_list)
                product_menu_option = int(input("Please select one of the following options: To return to main menu press 0, to view the product list press 1, to add a new product to the list press 2, to update an exisiting product press 3 and to delete a product press 4: "))
            
            # delete product
            elif product_menu_option == 4:
                print(list(enumerate(product_list)))
                product_index = int(input("Product Index: "))
                del product_list[product_index]
                print("\nProduct list: ", product_list)
                product_menu_option = int(input("Please select one of the following options: To return to main menu press 0, to view the product list press 1, to add a new product to the list press 2, to update an exisiting product press 3 and to delete a product press 4: "))
        # return to main menu
        print("Product menu option is zero")
    
    elif start == 2:
        print('Orders Menu')

        orders_menu_section = int(input("Please select one of the following options: To return to main menu press 0, to view the orders dictionary press 1, to Create a new order press 2, to update existing order status press 3, to update exisiting order press 4 and to delete order press 5: "))
        #Start of OM inner loop
        while orders_menu_section != 0: # while OM is not 0, continue into the loop; if 0, break

            # print orders dictionary
            if orders_menu_section == 1:
                print('\nOrders: ', orders_list)
                orders_menu_section = int(input("Please select one of the following options: To return to main menu press 0, to view the orders dictionary press 1, to Create a new order press 2, to update existing order status press 3, to update exisiting order press 4 and to delete order press 5: "))

            # create an order
            elif orders_menu_section == 2:
                customer_name = input('Input Name: ')
                customer_address = input('Input Address: ')
                customer_phone = input('Input number: ')
                set_order_status = 'PREPARING'
                new_order = {
                    'Customer Name: ': customer_name,
                    'Customer Address: ': customer_address,
                    'Customer Phone: ': customer_phone,
                    'Order Status: ': set_order_status
                }
                orders_list.append(new_order)
                orders_menu_section = int(input("Please select one of the following options: To return to main menu press 0, to view the orders dictionary press 1, to Create a new order press 2, to update existing order status press 3, to update exisiting order press 4 and to delete order press 5: "))

            # update exisiting order status
            elif orders_menu_section == 3:
                for dict in orders_list:
                    print('order #{} = {}'.format(index, dict))
                # for idx, x in enumerate(xs):
                # print(idx, x)
                orders_menu_section = int(input("Please select one of the following options: To return to main menu press 0, to view the orders dictionary press 1, to Create a new order press 2, to update existing order status press 3, to update exisiting order press 4 and to delete order press 5: "))

                

            # # update existiting order:
            # elif orders_menu_section == 4:

                


            # # delete order 
            elif orders_menu_section == 5:
                print(orders_list) # needs to be an index list
                user_input_for_order_index_value = int(input('Input the order index'))
                order_list.remove(user_input_for_order_index_value)
                orders_menu_section = int(input("Please select one of the following options: To return to main menu press 0, to view the orders dictionary press 1, to Create a new order press 2, to update existing order status press 3, to update exisiting order press 4 and to delete order press 5: "))

            #     user_to_input_index = int(input('Please input the index of order'))