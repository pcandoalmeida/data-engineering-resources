with open("products.txt", "r") as products:
    products_list = [lines.replace('\n', '') for lines in products.readlines()]

with open("couriers.txt", "r") as couriers:
    couriers_list = [lines.replace('\n', '') for lines in couriers.readlines()]

orders_list =[
    {"customer_name": "Carlton",
    "customer_address": "1 Vim Street, LONDON, SH1 2ER","customer_phone": "0789887334",
    "status": "preparing"},
    {"customer_name": "Sheikh",
    "customer_address": "34 League Lane, LONDON, EH1 2ER","customer_phone": "0789887334",
    "status": "preparing"},
    {"customer_name": "Faruuq",
    "customer_address": "Eastenders Street, LONDON, WH1 2ER","customer_phone": "0789887334",
    "status": "preparing"},
    {"customer_name": "Patrick",
    "customer_address": "ASMR Road, LONDON, WH1 2ER","customer_phone": "0789887334",
    "status": "preparing"}
]

def view_list(list_type, menu_type):
    if len(list_type) == 0:
        print(f'{menu_type.title()} list is empty.\n')
        sub_menu(list_type, menu_type)
    elif menu_type == 'order':
        for item in list_type:
            print(item)
        sub_menu(list_type, menu_type)
    else:
        print(list_type)
        sub_menu(list_type, menu_type)

def create(list_type, menu_type):
    if menu_type == 'order':
        customer_name = input('Input customer name\n')
        customer_address = input('Input customer address\n')
        customer_phone_number = input('Input customer phone number\n')
        orders_list.append({ "customer_name": f"{customer_name}", "customer_address": f"{customer_address}","customer_phone": f"{customer_phone_number}", "status": "preparing"})
        view_list(list_type, menu_type)
    else:
        item = input(f'Please input name of {menu_type}\n')
        list_type.append(item)
        view_list(list_type, menu_type)
        

def update(list_type, menu_type):
    if len(list_type) == 0:
        view_list(list_type, menu_type)
    else:
        print([(index, type) for index, type in enumerate(list_type)])
        try:
            index = int(input(f'Input index of {menu_type} to update from the {menu_type} list\n'))
            if index == 0 or index < len(list_type):
                new_type = input(f'Input a new {menu_type} to update from the {menu_type} list\n')
                list_type[index] = new_type
                print([(index, type) for index, type in enumerate(list_type)])
                view_list(list_type, menu_type)
            else:
                print(f'Index {index} isn\'t in {menu_type} list')
                view_list(list_type, menu_type)
        except ValueError:
            print('Invalid input')
            sub_menu(list_type, menu_type)

def update_order(list_type, menu_type):
    if len(list_type) == 0:
        view_list(list_type, menu_type)
    else:
        for index, order in enumerate(orders_list):
            print(index, order)
        try:
            order_number = int(input('Input order number to change status\n'))
            if order_number == 0 or order_number < len(list_type):
                print(orders_list[order_number])
                order_number_status = int(input('Input 1 to change or 2 to return to menu \n'))
                if order_number_status == 1:
                    if orders_list[order_number_status]['status'] == 'preparing':
                        orders_list[order_number_status]['status'] = 'dispatched'
                        view_list(list_type, menu_type)
                    else:
                        orders_list[order_number_status]['status'] = 'dispatched'
                        orders_list[order_number_status]['status'] = 'preparing'
                        view_list(list_type, menu_type)
                elif order_number_status == 2:
                    sub_menu(list_type, menu_type)
                else:
                    incorrect_input()
            else:
                print(f'Order {order_number} isn\'t in {menu_type} list')
                view_list(list_type, menu_type)
        except ValueError and KeyError:
            print('Invalid input')
            sub_menu(list_type, menu_type)

def updating_exitsting_order(list_type, menu_type):
    for index, order in enumerate(orders_list):
            print(index, order)
    order_number = int(input('Input number of order you would like to update\n'))
    print(orders_list[order_number])
    order_select = input('Input 1 to change customer name\nInput 2 to change customer address\nInput 3 to change customer phone number\nInput 4 to change all of above\n')
    if order_select == '1':
        customer_name = input('Input customer name\n')
        orders_list[order_number]['customer_name'] = customer_name
        view_list(list_type, menu_type)
    elif order_select == '2':
        customer_address = input('Input customer address\n')
        orders_list[order_number]['customer_address'] = customer_address
        view_list(list_type, menu_type)
    elif order_select == '3':
        customer_phone_number = input('Input customer phone number\n')
        orders_list[order_number]['customer_phone'] = customer_phone_number
        view_list(list_type, menu_type)
    elif order_select == '4':
        customer_name = input('Input customer name\n')
        customer_address = input('Input customer address\n')
        customer_phone_number = input('Input customer phone number\n')
        orders_list[order_number]['customer_name'] = customer_name
        orders_list[order_number]['customer_address'] = customer_address
        orders_list[order_number]['customer_phone'] = customer_phone_number
        view_list(list_type, menu_type)
    else:
        incorrect_input()

def delete(list_type, menu_type):
    if list_type == orders_list:
        if len(list_type) == 0:
            print(f'{menu_type.title()} list is empty.\n')
            sub_menu(list_type, menu_type)
        else:
            for index, order in enumerate(orders_list):
                print(index, order)
            order_number = int(input('Input number of order you would like to delete\n'))
            del orders_list[order_number]
            view_list(list_type, menu_type)    
    else:
        if len(list_type) == 0:
            print(f'{menu_type.title()} list is empty.\n')
            sub_menu(list_type, menu_type)
        else:
            print([type for type in list_type])
            type = input(f'Input {menu_type} to delete from the {menu_type} list\n')
            if type in list_type:
                list_type.remove(type)
                view_list(list_type, menu_type)
            else:
                print(f'{type} isn\'t in {menu_type} list')
                view_list(list_type, menu_type)

def incorrect_input():
    print('Incorrect input')
    main_menu()
        
def sub_menu(list_type, menu_type):
    if menu_type == 'order':
        cmd = input(f"""Menu {menu_type.title()} Options: 
0 to return to main menu
1 to view 
2 to add
3 to update order status
4 to update existing order
5 to delete
>>> """)
    else:
        cmd = input(f"""Menu {menu_type.title()} Options: 
0 to return to main menu
1 to view 
2 to add
3 to update 
4 to delete
>>> """)
    if cmd == '0':
        main_menu()
    elif cmd == '1':
        view_list(list_type, menu_type)
    elif cmd == '2':
        create(list_type, menu_type)
    elif cmd == '3':
        if list_type == orders_list:
            update_order(list_type, menu_type)
        else:
            update(list_type, menu_type)
    elif cmd == '4':
        if list_type == orders_list:
            updating_exitsting_order(list_type, menu_type)
        else:
            delete(list_type, menu_type)
    elif cmd == '5':
        if list_type == orders_list:
            delete(list_type, menu_type)
        else:
            incorrect_input()
    else:
        incorrect_input()

def main_menu():
    cmd = input(f"""Main Menu:
0 to save and exit
1 for product menu options
2 for courier menu options
3 for order menu options
>>> """)
    if cmd == '0':
        couriers_list_newline = [f'{courier}\n' for courier in couriers_list]
        with open('couriers.txt', 'w') as couriers:
            couriers.writelines(couriers_list_newline)
        products_list_newline = [f'{product}\n' for product in products_list]
        with open('products.txt', 'w') as products:
            products.writelines(products_list_newline)
        return
    elif cmd == '1':
        menu_type = 'product'
        list_type = products_list
        sub_menu(list_type, menu_type)
    elif cmd == '2':
        menu_type = 'courier'
        list_type = couriers_list
        sub_menu(list_type, menu_type)
    elif cmd == '3':
        menu_type = 'order'
        list_type = orders_list
        sub_menu(list_type, menu_type)
    else:
        incorrect_input()

main_menu()
print('Have a nice day!')
