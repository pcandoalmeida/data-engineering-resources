# # # # # #
# # Mini Project Week 1
# # In this week we'll be building out the foundation of your app, in particular, the UI aspect. This will make use of your ability to print to the screen, clear the screen,
# # accept user input, and create a basic list data structure.
# # Try to make good use of functions for repetitive tasks.

# # Goals
# # As a user I want to:
# # create a product and add it to a list
# # view all products
# # STRETCH update or delete a product

# # Spec
# # A product should just be a string containing its name, i.e: "Coke Zero" A list of products should be a list of strings , i.e: ["Coke Zero"]
# # # # # #

# products_list = ['Coke Zero', '7Up', 'Pepsi', 'Fanta', 'Dr Pepper', 'Mountain Dew']
# couriers_list = ['DPD', 'UPS', 'FedEx', 'DHL', 'EVRI' ]


def product_menu(menu_name,some_list):
    product_menu_input = int(input(f'\n--- {menu_name} Menu ---\n\
0. Return\n\
1. View {menu_name}\'s menu\n\
2. Add a {menu_name}\n\
3. Rename a {menu_name}\n\
4. Remove a {menu_name}\n\
>> ')) 

    # # 0. Return
    if product_menu_input == 0:
        return

    # # 1. View
    if product_menu_input == 1:
        print(f'\n{menu_name}:')
        for item in some_list:
            print(item)
        return product_menu(f'{menu_name}', some_list) 

    # # 2. Add
    if product_menu_input == 2:
        new_product = input('\nWhat would you like to add?\n>> ')
        some_list.append(new_product.title())
        print(f'\n{new_product} has been added.')
        return product_menu(f'{menu_name}', some_list) 

    # # 3. Rename
    if product_menu_input == 3:
        print('')
        for num in enumerate(some_list):
            print(str(num[0]) + '. ' + str(num[1]))
        rename_index = int(input(f'\nSelect which {menu_name} you would like to rename.\n>> '))
        rename_product = input(f'\n\nWhat would you like to rename this {menu_name} to?\n>> ')
        print(f'{some_list[rename_index]} has been renamed to {rename_product}')
        some_list[rename_index]=rename_product.title()
        return product_menu(f'{menu_name}',some_list)

    # # 4. Remove
    if product_menu_input == 4:
        print('')
        for num in enumerate(some_list):
            print(str(num[0]) + '. ' + str(num[1]))
        delete = int(input(f'\nSelect which {menu_name} you would like to remove.\n>>:'))
        print(f'\n{some_list[delete]} has been removed.')
        some_list.remove(some_list[delete])
        return product_menu(f'{menu_name}', some_list)
    else:
        print('\nInvalid option.')
        return product_menu(f'{menu_name}', some_list)

def orders_menu(orders):
    orders_menu_input = int(input(f'\n--- Orders Menu ---\n\
0. Return\n\
1. View Orders\n\
2. New Order\n\
3. Update Order Status\n\
4. Update Existing Order\n\
5. Cancel Order\n\
>> ')) 
    # 0. Return
    if orders_menu_input == 0:
        return
    # 1. View

    # 2. New order

    # 3. Update status

    # 4. Update Order

    # 5. Cancel
    

def main_menu():
    main_menu_input = int(input('\n--- Main Menu ---\n\
0. Exit\n\
1. Product Menu\n\
2. Courier Menu\n\
3. Orders Menu \n\
>> '))
    return main_menu_input

products_list = []
couriers_list = []
order_dict = {'customer name':'John', 
        'customer_address': 'Unit 2, 12 Main Street, LONDON, WH1 2ER',
        'customer_phone': '0789887334',
        'status': 'preparing'}

with open('product.txt','r') as f:
    for line in f:
        products_list.append(line.strip())


with open('courier.txt','r') as f:
    for line in f:
        couriers_list.append(line.strip())


while True:
    main_input = main_menu()
    if main_input == 0:
        with open('product.txt', 'w') as f:
            for item in products_list:
                f.write(f'{item}\n')

        with open('courier.txt', 'w') as f:
            for entry in couriers_list:
                f.write(f'{entry}\n')         

        print('\nGoodbye!')
        break
    elif main_input == 1:
        product_menu('Product',products_list)
    elif main_input == 2:
        product_menu('Courier',couriers_list)
    elif main_input == 3:
        orders_menu(order_dict)
        break
    elif main_input > 3:
        print('\nInvalid input. Please try again.')


