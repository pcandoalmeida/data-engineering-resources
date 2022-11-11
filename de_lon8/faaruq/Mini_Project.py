product_list = ["Water", "Fanta", "Croissant", "Apple"] # Decent

orders_list = []

# START OF OUTER LOOP <---------
while True:
    start = int(input("Welcome to Julio's Cafe: \n\
    Here are our Main Menu Options: \n\
    0. Exit \n\
    1. Product Menu Option \n\
    2. Orders Menu \n\
    >> "))

    if start == 0: # start(0) == 0 => TRUE, start(1) == 0 => FALSE
        break

    elif start == 1:
        print()
        print("Product Menu Options")
        print()
        product_menu_option = int(input("Please select one of the following options: \n\
        0. Return to Main Menu \n\
        1. View the product list \n\
        2. Add a new product to the list \n\
        3. Update an exisiting product \n\
        4. Delete a product \n\
        >> "))

        # START of Prodcut Menu Option INNER LOOP <---------
        while product_menu_option != 0: # while pmo is not 0, continue into the loop; if 0, break
           
           # product list
            if product_menu_option == 1:
                print("\nProduct list: ", product_list)
                print()
                product_menu_option = int(input("Please select one of the following options: \n\
        0. Return to Main Menu \n\
        1. View the product list \n\
        2. Add a new product to the list \n\
        3. Update an exisiting product \n\
        4. Delete a product \n\
        >> "))
            
            # adding item to product list
            elif product_menu_option == 2:
                print()
                product_name = input("What is the new product you would like to add? ")
                product_list.append(product_name)
                print("\nProduct list: ", product_list)
                print()
                product_menu_option = int(input("Please select one of the following options: \n\
        0. Return to Main Menu \n\
        1. View the product list \n\
        2. Add a new product to the list \n\
        3. Update an exisiting product \n\
        4. Delete a product \n\
        >> "))            
            
            # update exisiting product
            elif product_menu_option == 3:
                print()
                print(list(enumerate(product_list)))
                print()
                product_index = int(input("Product Index: "))
                product_name = input("Product Name: ")
                product_list[product_index] = product_name
                print("\nProduct list: ", product_list)
                print()
                product_menu_option = int(input("Please select one of the following options: \n\
        0. Return to Main Menu \n\
        1. View the product list \n\
        2. Add a new product to the list \n\
        3. Update an exisiting product \n\
        4. Delete a product \n\
        >> "))

            # delete product
            elif product_menu_option == 4:
                print()
                print(list(enumerate(product_list)))
                product_index = int(input("Product Index: "))
                del product_list[product_index]
                print("\nProduct list: ", product_list)
                print()
                product_menu_option = int(input("Please select one of the following options: \n\
        0. Return to Main Menu \n\
        1. View the product list \n\
        2. Add a new product to the list \n\
        3. Update an exisiting product \n\
        4. Delete a product \n\
        >> "))

        # END of Prodcut Menu Option INNER LOOP <---------


    elif start == 2:
        print()
        print('Orders Menu')
        print()
        orders_menu_section = int(input("Please select one of the following options: \n\
        0. Return to main menu \n\
        1. View the orders dictionary \n\
        2. Create a new order \n\
        3. Update existing order status \n\
        4. Update exisiting order \n\
        5. Delete order \n\
        >> "))

        #START of ORDER MENU INNER loop <---------
        while orders_menu_section != 0: # while OM is not 0, continue into the loop; if 0, break

            # print orders list
            if orders_menu_section == 1:
                print('\nOrders: ', orders_list)
                print()
                orders_menu_section = int(input("Please select one of the following options: \n\
        0. Return to main menu \n\
        1. View the orders dictionary \n\
        2. Create a new order \n\
        3. Update existing order status \n\
        4. Update exisiting order \n\
        5. Delete order \n\
        >> "))

            # create an order
            elif orders_menu_section == 2:
                print()
                customer_name = input('Input Name: ')
                customer_address = input('Input Address: ')
                customer_phone = input('Input number: ')
                order_status = 'PREPARING'
                new_order = {
                    'Customer Name': customer_name,
                    'Customer Address': customer_address,
                    'Customer Phone': customer_phone,
                    'Order Status': order_status
                }
                orders_list.append(new_order)
                print()
                orders_menu_section = int(input("Please select one of the following options: \n\
        0. Return to main menu \n\
        1. View the orders dictionary \n\
        2. Create a new order \n\
        3. Update existing order status \n\
        4. Update exisiting order \n\
        5. Delete order press \n\
        >> "))

            # update exisiting order status
            elif orders_menu_section == 3:
                for (count, item) in enumerate(orders_list):
                    print(count + 1, item, sep = ' ')
                print()
                orders_list_index_input = int((input("Please enter the order index value: ")))
                order_to_update = orders_list[orders_list_index_input]
                print()
                print(f"You have selected {order_to_update} to update")
                print()
                order_status_list = ['PREPARED', 'OUT FOR DELIVERY', 'DELIVERED']
                for (count, item) in enumerate(order_status_list):
                    print(count+1, item, sep = ' ')
                print()
                new_order_status_index = int(input('Please select an index from the Order Status List: '))
                new_order_status = order_status_list[new_order_status_index]
                order_to_update['Order Status'] = new_order_status
                print('\nUpdated Order: ', order_to_update)
                print()
                orders_menu_section = int(input("Please select one of the following options: \n\
        0. Return to main menu \n\
        1. View the orders dictionary \n\
        2. Create a new order \n\
        3. Update existing order status \n\
        4. Update exisiting order \n\
        5. Delete order \n\
        >> "))
                
            # update existiting order:
            elif orders_menu_section == 4:
                for (count, item) in enumerate(orders_list):
                    print(count + 1, item, sep = ' ')
                print()
                orders_list_index_input = int((input("Please enter the order index value: ")))
                order_to_update = orders_list[orders_list_index_input]
                print()
                print(f"You have selected {order_to_update} to update")
                print()
                updated_customer_name = input('Please input updated customer name, otherwise click Enter: ')
                print()
                updated_customer_address = input('Please input updated customer address, otherwise click Enter: ')
                print()
                updated_customer_phone = input('Please input updated customer phone, otherwise click Enter: ')
                for key, value in order_to_update.items():
                    if key == 'Customer Name':
                        if not updated_customer_name:
                            continue
                        else:
                            order_to_update[key] = updated_customer_name
                    if key == 'Customer Address':
                        if not updated_customer_address:
                            continue
                        else:
                            order_to_update[key] = updated_customer_address
                    if key == 'Customer Phone':
                        if not updated_customer_phone:
                            continue
                        else:
                            order_to_update[key] = updated_customer_phone
                print(order_to_update)
                print()
                orders_menu_section = int(input("Please select one of the following options: \n\
        0. Return to main menu \n\
        1. View the orders dictionary \n\
        2. Create a new order \n\
        3. Update existing order status \n\
        4. Update exisiting order \n\
        5. Delete order \n\
        >> ")) 

            # delete order 
            elif orders_menu_section == 5:
                for (count, item) in enumerate(orders_list):
                    print(count + 1, item, sep = " ")
                    print()
                orders_list_index_input = int((input("Please enter the order index value: ")))
                del orders_list[orders_list_index_input]
                print()
                print('Orders: ', orders_list)
                print()
                orders_menu_section = int(input("Please select one of the following options: \n\
        0. Return to main menu \n\
        1. View the orders dictionary \n\
        2. Create a new order \n\
        3. Update existing order status \n\
        4. Update exisiting order \n\
        5. Delete order \n\
        >> "))

        #END of ORDER MENU INNER loop <---------