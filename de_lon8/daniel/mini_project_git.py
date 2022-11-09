import time
import os
import csv

logo = """________                .__       .__/\        
\______ \ _____    ____ |__| ____ |  )/  ______
 |    |  \\__  \  /    \|  |/ __ \|  |  /  ___/
 |    `   \/ __ \|   |  \  \  ___/|  |__\___ \ 
/_______  (____  /___|  /__|\___  >____/____  >
        \/     \/     \/        \/          \/ 
_________         _____                        
\_   ___ \_____ _/ ____\____                   
/    \  \/\__  \\   __\/ __ \                  
\     \____/ __ \|  | \  ___/                  
 \______  (____  /__|  \___  >                 
        \/     \/          \/                  
"""


def main_menu():
    product = MenuItem('product')

    courier = MenuItem('courier')

    order = MenuItem('order')

    os.system('clear')
    print(logo)
    command = input(f"Welcome to Daniel's cafe, please state your command!"
                    f"\n0. Exit"
                    f"\n1. Product Menu"
                    f"\n2. Order Menu."
                    f"\n3. Courier Menu."
                    f"\n4. TBC."
                    f"\n")

    if command == '1':
        time.sleep(0.5)
        product.print_menu()

    elif command == '2':
        time.sleep(0.5)
        order.order_menu()

    elif command == '3':
        time.sleep(0.5)
        print('TBC')
        courier.print_menu()

    elif command == '4':
        time.sleep(0.5)
        print('TBC')
        main_menu()

    elif command == '0':
        time.sleep(0.5)
        os.system('clear')

        print(logo)
        print("Goodbye!! See you next time.")

        global app_end
        app_end = True

    else:
        print("\nPlease only input number as command.\n")
        time.sleep(2)
        main_menu()


def get_last_item_id(some_list):
    if len(some_list) > 0:
        return len(some_list) - 1
    else:
        return 0


def generate_order_id():
    return time.strftime("%y%m%d%H%M%S", time.gmtime())


def processing_animation():
    text = 'Processing'
    for _ in range(5):
        os.system('clear')
        print(text)
        text += '..'
        time.sleep(0.3)


def get_courier_file():
    try:
        with open(f'courier.txt', 'r') as file:
            temp_list = [line.strip() for line in file]

    except FileNotFoundError:
        with open(f'courier.txt', 'w') as file:
            temp_list = ['Rick', 'Morty']
            for item in temp_list:
                file.write(f'{item}\n')

    return temp_list


class MenuItem:
    def __init__(self, name):
        self.name = name

    def get_file(self):
        try:
            with open(f'{self.name}.txt', 'r') as file:
                temp_list = [line.strip() for line in file]
        except FileNotFoundError:
            with open(f'{self.name}.txt', 'w') as file:
                temp_list = []
                for item in temp_list:
                    file.write(f'{item}\n')

        return temp_list

    def print_menu(self, *some_list):
        self.get_file()
        temp_list = self.get_file()

        os.system('clear')

        print(*some_list, '\n')

        command = input(f"Please enter your command.\n"
                        f"0. Go back to main menu.\n"
                        f"1. Print {self.name} list.\n"
                        f"2. Create new {self.name}\n"
                        f"3. Update {self.name}\n"
                        f"4. Delete {self.name}\n")
        if command == '1':
            time.sleep(0.5)
            self.print_menu(temp_list)
        elif command == '2':
            time.sleep(0.5)
            self.create_stuff()
        elif command == '3':
            time.sleep(0.5)
            self.update_stuff()
        elif command == '4':
            time.sleep(0.5)
            self.delete_stuff()

        elif command == '0':
            time.sleep(0.5)
            main_menu()

        else:
            time.sleep(0.5)
            print("\nPlease only input number as command.\n")
            time.sleep(3)
            self.print_menu()

    def create_stuff(self):
        os.system('clear')
        temp_list = self.get_file()
        new_stuff = input('Please create a new product: ')
        temp_list.append(new_stuff)
        with open(f'{self.name}.txt', 'w') as file:
            file.write('\n'.join(temp_list))
        print(f'\n{new_stuff} is added to the {self.name} list.')

        time.sleep(1.5)
        self.print_menu()

    def update_stuff(self):
        os.system('clear')
        temp_list = self.get_file()
        for count, value in enumerate(temp_list):
            print(count + 1, value)
        try:
            thing_to_update = int(input(f'Please pick a {self.name} to update: '))
            new_thing_name = input(f'What is the new {self.name}? ')
            old_thing = temp_list[thing_to_update - 1]
            temp_list[thing_to_update - 1] = new_thing_name
            print(f"\n'{old_thing}' is updated to '{new_thing_name}'\n")
            with open(f'{self.name}.txt', 'w') as file:
                file.write('\n'.join(temp_list))
            self.print_menu()
        except (ValueError, IndexError):
            print('\nInvalid input.\n')
            self.update_stuff()

    def delete_stuff(self):
        os.system('clear')
        temp_list = self.get_file()
        for count, value in enumerate(temp_list):
            print(count + 1, value)
        try:
            thing_to_update = int(input(f'Please pick a {self.name} to delete: '))
            confirmation = input(f"Are you sure to delete {temp_list[thing_to_update - 1]}?\n"
                                 f"'y' for yes and 'n' for no.\n")
            if confirmation == 'y':
                print(f"{temp_list[thing_to_update - 1]} is deleted.")
                temp_list.remove(temp_list[thing_to_update - 1])
                print("here", temp_list)
                with open('product.txt', 'w') as file:
                    file.write('\n'.join(temp_list))
                main_menu()
            elif confirmation == 'n':
                self.print_menu()
            else:
                print('\nInvalid input.\n')
                time.sleep(1.5)
                self.print_menu()
        except (ValueError, IndexError):
            print('\nInvalid input.\n')
            time.sleep(1.5)
            self.print_menu()

    def order_menu(self):

        os.system('clear')

        command = input(f"Please enter your command.\n"
                        f"0. Go back to main menu.\n"
                        f"1. Print {self.name} list.\n"
                        f"2. Create new {self.name}\n"
                        f"3. Update {self.name} status.\n"
                        f"4. Update {self.name} details.\n"
                        f"5. Delete {self.name} order.\n")
        if command == '1':
            time.sleep(0.5)
            self.print_order_list()
        elif command == '2':
            time.sleep(0.5)
            self.create_order()
        elif command == '3':
            time.sleep(0.5)
            self.update_order_status()
        elif command == '4':
            time.sleep(0.5)
            self.update_order_item()

        elif command == '5':
            time.sleep(0.5)
            self.delete_order()

        elif command == '0':
            time.sleep(0.5)
            main_menu()
        else:
            time.sleep(0.5)
            print("\nPlease only input number as command.\n")
            time.sleep(3)
            self.order_menu()

    def create_order(self):
        os.system('clear')
        temp_dict = {}

        c_name = input('Please input the name of customer: ')
        c_address = input('Please input the address: ')
        c_phone = input('Please input the phone number: ')
        courier = self.choose_courier()
        status = 'PREPARING'

        temp_dict['order_number'] = generate_order_id()
        temp_dict['customer_name'] = c_name
        temp_dict['customer_address'] = c_address
        temp_dict['customer_phone'] = c_phone
        temp_dict['courier'] = courier
        temp_dict['status'] = status

        processing_animation()

        self.append_csv_file(temp_dict)
        print(f'\nNew order is made.')

        time.sleep(1.5)
        self.order_menu()

    def print_order_list(self):
        if os.path.exists(f'{self.name}.csv'):
            os.system('clear')
            time.sleep(1)
            with open(f'{self.name}.csv', 'r') as file:
                dict_reader = csv.DictReader(file)
                for item in dict_reader:
                    # if item['order_number'] != 'order_number':
                    print(item)
            command = input('Please type "1" to order menu or "0" for main menu.')
            if command == "1":
                self.order_menu()
            elif command == "0":
                main_menu()
            else:
                print('Invalid input.')
                time.sleep(1.5)
                main_menu()
        else:
            print('There is no order list at the moment.')
            time.sleep(1.5)
            self.order_menu()

    def append_csv_file(self, some_dict):

        fields = ['order_number', 'customer_name',
                  'customer_address', 'customer_phone', 'courier', 'status']

        if os.path.exists(f'{self.name}.csv'):
            with open(f'{self.name}.csv', 'a') as file:
                writer = csv.DictWriter(file, fieldnames=fields)
                writer.writerow(some_dict)

        else:
            with open(f'{self.name}.csv', 'a') as file:
                fields = ['order_number', 'customer_name',
                          'customer_address', 'customer_phone', 'courier', 'status']

                writer = csv.DictWriter(file, fieldnames=fields)
                writer.writeheader()
                writer.writerow(some_dict)

    def get_csv_file(self):
        """To return a DictReader object for further process"""
        # seems some bug inside
        if os.path.exists(f'{self.name}.csv'):
            os.system('clear')
            time.sleep(1)
            with open(f'{self.name}.csv', 'r') as file:
                dict_reader = csv.DictReader(file)
                return dict_reader
        else:
            with open(f'{self.name}.csv', 'w+') as file:
                fields = ['order_number', 'customer_name',
                          'customer_address', 'customer_phone', 'courier', 'status']

                writer = csv.DictWriter(file, fieldnames=fields)
                writer.writeheader()
                dict_reader = csv.DictReader(file)
                return dict_reader

    def check_valid_order_no(self, order_no):
        answer = False
        try:
            with open(f'{self.name}.csv', 'r') as file:
                dict_reader = csv.DictReader(file)

                for item in dict_reader:
                    if order_no in item.values():
                        answer = True
                return answer
        except FileNotFoundError:
            return answer

    def update_order_item(self):
        os.system('clear')
        order_no = input('Please enter the order number: ')
        temp_list = []
        if self.check_valid_order_no(order_no):
            with open(f'{self.name}.csv', 'r') as file:
                reader = csv.DictReader(file)
                for item in reader:
                    if item['order_number'] == order_no:
                        item['customer_name'] = input('Please input the name of customer: ')
                        item['customer_address'] = input('Please input the address: ')
                        item['customer_phone'] = input('Please input the phone number: ')
                        temp_list.append(item)
                    else:
                        temp_list.append(item)
            with open(f'{self.name}.csv', 'w') as file:
                fields = ['order_number', 'customer_name',
                          'customer_address', 'customer_phone', 'courier', 'status']
                writer = csv.DictWriter(file, fieldnames=fields)
                writer.writeheader()
                writer.writerows(temp_list)
                processing_animation()
                print('The order is updated.')
                time.sleep(1)
            self.order_menu()
        else:
            print('There is no such order number.')
            time.sleep(1.5)
            self.order_menu()

    def update_order_status(self):
        os.system('clear')
        order_no = input('Please enter the order number: ')
        temp_list = []
        status = ''
        if self.check_valid_order_no(order_no):
            command = input('Please update the status: \n'
                            '1. Preparing\n'
                            '2. Delivering\n'
                            '3. Delivered\n'
                            '4. Cancelled\n')
            if command == '1':
                status = 'Preparing'
            elif command == '2':
                status = 'Delivering'
            elif command == '3':
                status = 'Delivered'
            elif command == '4':
                status = 'Cancelled'
            else:
                print('This is invalid input.')
                time.sleep(1.5)
                self.update_order_status()
            with open(f'{self.name}.csv', 'r') as file:
                reader = csv.DictReader(file)
                for item in reader:
                    if item['order_number'] == order_no:
                        item['status'] = status
                        temp_list.append(item)
                    else:
                        temp_list.append(item)
            with open(f'{self.name}.csv', 'w') as file:
                fields = ['order_number', 'customer_name',
                          'customer_address', 'customer_phone', 'courier', 'status']
                writer = csv.DictWriter(file, fieldnames=fields)
                writer.writeheader()
                writer.writerows(temp_list)
                processing_animation()
                print('The order is updated.')
                time.sleep(1)
            self.order_menu()
        else:
            print('There is no such order number.')
            time.sleep(1.5)
            self.order_menu()

    def delete_order(self):
        os.system('clear')
        order_no = input('Please enter the order number: ')
        temp_list = []

        if self.check_valid_order_no(order_no):

            with open(f'{self.name}.csv', 'r') as file:
                reader = csv.DictReader(file)
                for item in reader:
                    if item['order_number'] == order_no:
                        pass
                    else:
                        temp_list.append(item)
            with open(f'{self.name}.csv', 'w') as file:
                fields = ['order_number', 'customer_name',
                          'customer_address', 'customer_phone', 'courier', 'status']
                writer = csv.DictWriter(file, fieldnames=fields)
                writer.writeheader()
                writer.writerows(temp_list)
                processing_animation()
                print('The order is deleted.')
                time.sleep(1)
            self.order_menu()
        else:
            print('There is no such order number.')
            time.sleep(1.5)
            self.order_menu()

    def choose_courier(self):
        temp_list = get_courier_file()
        chosen_courier_name = ''
        for count, value in enumerate(temp_list):
            print(count + 1, value)
        try:
            chosen_courier_num = int(input(f'Please pick a courier: '))
            chosen_courier_name = temp_list[chosen_courier_num - 1]

        except (ValueError, IndexError):
            print('\nInvalid input.\n')
            self.choose_courier()

        return chosen_courier_name


app_end = False

while app_end is not True:
    main_menu()
