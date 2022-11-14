import os
import csv
import copy
import time
import re


def get_product_list_from_csv():
    temp_list = []
    if os.path.exists('product.csv'):
        with open('product.csv', 'r') as file:
            reader = csv.DictReader(file)
            for item in reader:
                temp_list.append(item)
        return temp_list
    else:
        with open('product.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'price'])
            writer.writerow(['latte', '4.0'])
            writer.writerow(['espresso', '3.0'])
            writer.writerow(['cappuccino', '5.0'])
        with open('product.csv', 'r') as file:
            reader = csv.DictReader(file)
            for item in reader:
                temp_list.append(item)
        return temp_list


def get_courier_list_from_csv():
    temp_list = []
    if os.path.exists('courier.csv'):
        with open('courier.csv', 'r') as file:
            reader = csv.DictReader(file)
            for item in reader:
                temp_list.append(item)
        return temp_list
    else:
        with open('courier.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['name', 'phone'])
            writer.writerow(['JustEat', '189047221984'])
            writer.writerow(['UberEat', '235791935235'])
            writer.writerow(['Deliveroo', '423781235352'])
        with open('courier.csv', 'r') as file:
            reader = csv.DictReader(file)
            for item in reader:
                temp_list.append(item)
        return temp_list


def get_order_list_from_csv():
    temp_list = []
    if os.path.exists('order.csv'):
        with open('order.csv', 'r') as file:
            reader = csv.DictReader(file)
            for item in reader:
                temp_list.append(item)
        return temp_list
    else:
        with open('order.csv', 'w') as file:
            writer = csv.writer(file)
            writer.writerow(['customer_name',
                             'customer_address', 'customer_phone',
                             'courier', 'status', 'items'])
        with open('order.csv', 'r') as file:
            reader = csv.DictReader(file)
            for item in reader:
                temp_list.append(item)
        return temp_list


class Product(dict):
    def __init__(self, name: str, price: float):
        super().__init__()
        self.name = name
        self.price = price
        self.dict = {name: price}

    # def __repr__(self):
    #     return self.dict


class Courier(dict):
    def __init__(self, name: str, cou_phone: str):
        super().__init__()
        self.name = name
        self.phone = cou_phone
        self.dict = {'courier name': name, 'phone': cou_phone}


class ProductMenu:
    def __init__(self):
        self.product_list = get_product_list_from_csv()

    def show_product_menu(self):

        os.system('clear')
        self.product_list = get_product_list_from_csv()

        command = input(f"Please enter your command.\n"
                        f"0. Go back to main menu.\n"
                        f"1. Print product list.\n"
                        f"2. Create new product\n"
                        f"3. Update product\n"
                        f"4. Delete product\n")
        if command == '1':
            self.print_product_list()
        elif command == '2':
            self.create_product()
        elif command == '3':
            self.update_product()
        elif command == '4':
            self.delete_product()
        elif command == '0':
            pass

    def save_list_to_csv(self):
        header = ['name', 'price']

        with open('product.csv', 'w') as file:
            writer = csv.DictWriter(file, header)
            writer.writeheader()
            writer.writerows(self.product_list)

    def print_product_list(self):
        temp_list = get_product_list_from_csv()
        for item in temp_list:
            print(item)

    def create_product(self):
        try:
            new_product_name = input("Please input the name of the new product? ")
            new_product_price = float(input("Please input the price of the new product? "))
            new_item = {'name': new_product_name, 'price': new_product_price}
            # new_item = Product(new_product_name, new_product_price)
            self.product_list.append(new_item)
            print("The product is created!!")
            self.save_list_to_csv()
        except (ValueError, IndexError):
            print('Invalid input.')
            self.create_product()

    def update_product(self):
        temp_list = self.product_list
        for count, value in enumerate(self.product_list):
            print(count + 1, value)
        try:
            thing_to_update = int(input(f'Please pick a product to update: '))

            old_thing = copy.deepcopy(temp_list[thing_to_update - 1])
            new_thing = temp_list[thing_to_update - 1]
            for key in new_thing:
                new_key = input(f'What is the new {key}? ')
                if new_key == '':
                    pass
                else:
                    new_thing[key] = new_key

            temp_list[thing_to_update - 1] = new_thing

            print(f"\n'{old_thing}' is updated to '{new_thing}'\n")
            self.product_list = temp_list
            self.save_list_to_csv()

        except (ValueError, IndexError):
            print('\nInvalid input.\n')
            self.update_product()

    def delete_product(self):
        temp_list = self.product_list
        for count, value in enumerate(self.product_list):
            print(count + 1, value)
        try:
            thing_to_delete = int(input(f"Please pick a product to delete or enter 'b' to return: "))
            if thing_to_delete == 'b':
                self.show_product_menu()
            else:
                del temp_list[thing_to_delete - 1]
                self.save_list_to_csv()

        except (ValueError, IndexError):
            print('\nInvalid input.\n')
            self.delete_product()


class CourierMenu:
    def __init__(self):
        self.courier_list = get_courier_list_from_csv()

    def show_courier_menu(self):

        os.system('clear')

        self.courier_list = get_courier_list_from_csv()

        command = input(f"Please enter your command.\n"
                        f"0. Go back to main menu.\n"
                        f"1. Print courier list.\n"
                        f"2. Create new courier\n"
                        f"3. Update courier\n"
                        f"4. Delete courier\n")
        if command == '1':
            self.print_courier_list()
        elif command == '2':
            self.create_courier()
        elif command == '3':
            self.update_courier()
        elif command == '4':
            self.delete_courier()
        elif command == '0':
            pass

    def save_list_to_csv(self):
        header = ['name', 'phone']

        with open('courier.csv', 'w') as file:
            writer = csv.DictWriter(file, header)
            writer.writeheader()
            writer.writerows(self.courier_list)

    def print_courier_list(self):
        temp_list = get_courier_list_from_csv()
        for item in temp_list:
            print(item)

    def create_courier(self):
        try:
            new_courier_name = input("Please input the name of the new courier? ")
            new_courier_phone = input("Please input the number of the new courier? ")
            new_item = {'name': new_courier_name, 'phone': new_courier_phone}
            # new_item = Courier(new_courier_name, new_courier_phone)
            self.courier_list.append(new_item)
            print("The courier is created!!")
            print(self.courier_list)
            self.save_list_to_csv()
        except (ValueError, IndexError) as e:
            print('Invalid input.')
            print(e)
            self.create_courier()

    def update_courier(self):
        temp_list = self.courier_list
        for count, value in enumerate(self.courier_list):
            print(count + 1, value)
        try:
            thing_to_update = int(input(f'Please pick a product to update: '))

            old_thing = copy.deepcopy(temp_list[thing_to_update - 1])
            new_thing = temp_list[thing_to_update - 1]
            for key in new_thing:
                new_key = input(f'What is the new {key}? ')
                if new_key == '':
                    pass
                else:
                    new_thing[key] = new_key

            temp_list[thing_to_update - 1] = new_thing

            print(f"\n'{old_thing}' is updated to '{new_thing}'\n")
            self.courier_list = temp_list
            self.save_list_to_csv()

        except (ValueError, IndexError):
            print('\nInvalid input.\n')
            self.update_courier()

    def delete_courier(self):
        temp_list = self.courier_list
        for count, value in enumerate(self.courier_list):
            print(count + 1, value)
        try:
            thing_to_delete = int(input(f"Please pick a product to delete or enter 'b' to return: "))
            if thing_to_delete == 'b':
                self.show_courier_menu()
            else:
                del temp_list[thing_to_delete - 1]
                self.save_list_to_csv()

        except (ValueError, IndexError):
            print('\nInvalid input.\n')
            self.delete_courier()


class OrderMenu:
    def __init__(self):
        self.order_list = get_order_list_from_csv()

    def show_order_menu(self):

        os.system('clear')

        self.order_list = get_order_list_from_csv()

        command = input(f"Please enter your command.\n"
                        f"0. Go back to main menu.\n"
                        f"1. Print order list.\n"
                        f"2. Create new order\n"
                        f"3. Update order\n"
                        f"4. Delete order\n")
        if command == '1':
            self.print_order_list()
        elif command == '2':
            self.create_order()
        elif command == '3':
            self.update_order()
        elif command == '4':
            self.delete_order()
        elif command == '0':
            pass

    # def generate_order_id(self):
    #     return time.strftime("%y%m%d%H%M%S", time.gmtime())

    def save_list_to_csv(self):
        header = ['customer_name',
                  'customer_address', 'customer_phone',
                  'courier', 'status', 'items']

        with open('order.csv', 'w') as file:
            writer = csv.DictWriter(file, header)
            writer.writeheader()
            writer.writerows(self.order_list)

    def print_order_list(self):
        temp_list = get_order_list_from_csv()
        for item in temp_list:
            print(item)

    def create_order(self):
        try:
            status = 'PREPARING'

            # order_id = self.generate_order_id()
            cus_name = input('Please input the name of customer: ')
            cus_address = input('Please input the address: ')
            cus_phone = input('Please input the phone number: ')
            choice_courier = self.choose_courier()
            choice_product = self.choose_product()
            new_item = {'customer_name': cus_name,
                        'customer_address': cus_address,
                        'customer_phone': cus_phone,
                        'courier': choice_courier,
                        'status': status,
                        'items': choice_product}
            self.order_list.append(new_item)
            print('The order is created!!')
            self.save_list_to_csv()
        except (ValueError, IndexError):
            print('Invalid input.')
            self.create_order()

    def update_order(self):
        temp_list = self.order_list
        for count, value in enumerate(self.order_list):
            print(count + 1, value)
        try:
            thing_to_update = int(input(f'Please pick an order to update: '))

            old_thing = copy.deepcopy(temp_list[thing_to_update - 1])
            new_thing = temp_list[thing_to_update - 1]
            for key in new_thing:
                new_key = input(f'What is the new {key}? ')
                if new_key == '':
                    pass
                else:
                    new_thing[key] = new_key

            temp_list[thing_to_update - 1] = new_thing

            print(f"\n'{old_thing}' is updated to '{new_thing}'\n")
            self.order_list = temp_list
            self.save_list_to_csv()

        except (ValueError, IndexError):
            print('\nInvalid input.\n')
            self.update_order()

    def delete_order(self):
        temp_list = self.order_list
        for count, value in enumerate(self.order_list):
            print(count + 1, value)
        try:
            thing_to_delete = int(input(f"Please pick a product to delete order: "))
            if thing_to_delete == 'b':
                self.show_order_menu()
            else:
                del temp_list[thing_to_delete - 1]
                print("Order is deleted!!")
                self.save_list_to_csv()

        except (ValueError, IndexError):
            print('\nInvalid input.\n')
            self.delete_order()

    def choose_courier(self):
        temp_list = get_courier_list_from_csv()
        for count, value in enumerate(temp_list):
            print(count + 1, value)
        choice = input("Please choose a courier from above list: ")
        if re.match("^[0-9,]*$", choice):
            return choice
        else:
            print('Invalid input.')
            self.choose_courier()

    def choose_product(self):
        temp_list = get_product_list_from_csv()
        for count, value in enumerate(temp_list):
            print(count + 1, value)
        loop_end = False
        while loop_end is not True:
            choice = input('Please input the indexes of the products with comma only:')
            if re.match("^[0-9,]*$", choice):
                loop_end = True
            else:
                continue
        return choice


