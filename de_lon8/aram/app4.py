import os.path
import csv

class Item():
    # def __init__(self) -> None: 
    
    def delete_item(self):
        self.show_items()
        valid_input = self.gen_valid_inputs()
        if len(valid_input) == 1:
            print("The are no items to delete") 
            self.item_menu() 
        else:
            print(f"Enter the number for the {self.type[:-1]} you want to delete: ")
            deletee = input()
            deletee = self.check_valid_input(deletee,valid_input)
            if deletee == "":
                self.menu()
            else:
                with open(f"data\{self.type}.csv", "r") as itemsf:
                    lines = itemsf.readlines()
                    del lines[int(deletee)]
                with open(f"data\{self.type}.csv", "w") as itemsf:
                    for pos, line in enumerate(lines):
                        itemsf.write(line)
                print(f"{self.type[:-1]} number {deletee} is now deleted.")
                self.item_menu()
    


    def gen_valid_inputs(self) -> list:
        list_of_dict = self.get_csv_and_return_as_list_of_dict()
        valid_input = [str(num+1) for num, line in enumerate(list_of_dict)] 
        #TODO there must be a way to do with without the unused line variable
        valid_input.append("x")
        return valid_input

    

    def check_valid_input(self, user_input : str, valid_inputs : list) -> str: 
        while user_input not in valid_inputs and user_input.capitalize() != "X" :
            print("Your choice was not valid or x to go back to the main menu.")
            print(valid_inputs)
            print(user_input)
            user_input = input(f"Please, choose a {self.type[:-1]} by entering the corresponding number above: ")
        if user_input.lower() == "x":
            return ""
        else:
            return user_input



    def get_headers(self) -> list:
        file_exists = os.path.isfile(f"data\{self.type}.csv")
        if not file_exists and self.type == "orders":
            field_names = ['customer_name', 'customer_address', 'customer_phone', 'courier', 'status', 'items']
        elif not file_exists and self.type == "couriers":
            field_names = ['name', 'phone']
        elif not file_exists and self.type == "products":
            field_names = ['name', 'price']
        else:
            with open(f"data\{self.type}.csv", "r") as csv_file:
                records = csv.DictReader(csv_file, skipinitialspace=True)
                field_names = records.fieldnames
                print(len(list(records)))
                print(field_names)
        return field_names
    


    def get_csv_and_return_as_list_of_dict(self) -> list:
        list_of_dict = []
        with open(f"data\{self.type}.csv", "r") as csv_file:
            records = csv.DictReader(csv_file, skipinitialspace=True)
            for row in records:
                list_of_dict.append(row)
        return list_of_dict



    def show_items(self) -> None:
        list_of_dict = self.get_csv_and_return_as_list_of_dict()
        if list_of_dict == []:
            print(f"There are no {self.type}s currently in the system")
        for num, line in enumerate(list_of_dict):      
            print(f"{self.type[:-1].capitalize()} n.{num+1}")
            for key, value in line.items():
                key_4_string = key.replace("_", " ").title()
                print(f"\t{key_4_string}: {value}")
            print("")

        
    def asdict(self):
        pass

#TODO: validate input for numeric data types, will probably need class specific implementation
    def update_attributes(self) -> dict:
        updatee_as_dict = self.asdict()
        for key, value in updatee_as_dict.items():
            key_4_string = key.replace("_", " ").title()
            newValue = input(f"Enter the {key_4_string} ")
            while newValue == "":
                newValue = input("Not a valid value. Enter another: ")    
            updatee_as_dict[key] = newValue
        return  updatee_as_dict


    def add_item_to_file(self): 
#TODO this function does not add a line the previous line does not have a break line character
        file_exists = os.path.isfile(f"data\{self.type}.csv")
        #field_names = self.get_headers()
        an_item = self.update_attributes()
        #print("data file empty is", data_file.empty)                
        if file_exists and os.stat(f"data\{self.type}.csv").st_size != 0: #file exists and it is not empty
            with open(f"data\{self.type}.csv", "a", newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames= self.field_names)
                writer.writerow(an_item)
        else: #file either does not exist or is emtpy
            with open(f"data\{self.type}.csv", "w", newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames= self.field_names)
                writer.writeheader()
                writer.writerow(an_item)

    def choose_courier_for_order(self) -> int:
        an_item = Courier()
        an_item.show_items()
        valid_inputs = an_item.gen_valid_inputs()
        valid_inputs.append("")
        chosen_item = input("Enter the number for your courier of choice: ")
        valid_inputs = an_item.check_valid_input(chosen_item,valid_inputs)
        if chosen_item != "":
            return int(chosen_item) 
        
    def choose_items_for_order(self) -> str:
        an_item = Product()
        an_item.show_items()
        valid_inputs = an_item.gen_valid_inputs()
        valid_inputs.append("d")
        chosen_item = input("Enter the number for a product of your choice: ")
        item_list_as_str = ""
        while chosen_item != "d":
            chosen_item = input("Enter the number for another product you want or d if you are done: ")
            print("These are the valid inputs:", valid_inputs)
            chosen_item = an_item.check_valid_input(chosen_item,valid_inputs)
            if chosen_item != "d":
                item_list_as_str += chosen_item + ","
            else:
                break
        if chosen_item != "":
            return item_list_as_str[:-1] 


    def check_if_input_already_exists(self, user_input : str, selected_list : list) -> str: 
        while user_input in selected_list and user_input.capitalize() != "X" :
            print(f"That {self.type} already exists.")
            user_input = input(f"Please, enter a new {self.type} or x to return to the main menu: ")
        if user_input.lower() == "x":
            return ""
        else:
            return user_input


#TODO: This function is crazy long. Refactor please.Make the whole courier thing its own function
#TODO also make update status its own function 
    def update_item(self):
            selected_list = self.get_csv_and_return_as_list_of_dict()
            valid_inputs = self.gen_valid_inputs()
            self.show_items()
            print(f"""Enter the number for the {self.type[:-1]} you want
        to update or x to go to main menu: """)
            updatee = input()
            self.check_valid_input(updatee, valid_inputs)
            updatee = int(updatee)
            updatee_as_dict = selected_list[updatee-1]
            for key, value in updatee_as_dict.items():
                key_4_string = key.replace("_", " ")
                if key == 'courier':
                    updatee_as_dict["courier"] = self.choose_courier_for_order()
                elif key == "status":
                    pass
                elif key == "items":
                    updatee_as_dict["items"] = self.choose_items_for_order()
                else:
                    newValue = input(f"Enter the {key_4_string} ")
                    if newValue == "":
                        pass
                    else:
                        updatee_as_dict[key] = newValue
#TODO this code screams function, look into it
            with open(f"data\{self.type}.csv", "r") as csv_file:
                records = csv.DictReader(csv_file, skipinitialspace=True)
                list_of_records = (list(records))
            list_of_records[int(updatee)-1] = updatee_as_dict

            with open(f"data\{self.type}.csv", "w", newline='') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames= self.field_names)
                writer.writeheader()
                for dictio in list_of_records:
                    writer.writerow(dictio)
            print(f"{self.type[:-1]} {updatee} has been updated")
                  


    
    def item_menu(self):
        if self.type == "orders":
            menu_string = f"""Choose an option:
                0 to go to main menu
                1 for seeing the list of {self.type}
                2 to add new {self.type}
                3 to update/replace {self.type}
                4 to update the status of {self.type}
                5 to delete {self.type}"""
            valid_inputs = ("0","1","2","3","4", "5")
        else:
            menu_string = f"""Choose an option:
                0 to go to main menu
                1 for seeing the list of {self.type}
                2 to add a new {self.type}
                3 to update/replace {self.type}
                4 to delete {self.type}"""
            valid_inputs = ("0","1","2","3","4")
        print(menu_string)
        u_input2 = input()
        while u_input2 not in valid_inputs:
            print("Not a valid option. Try again.") 
            print(menu_string)        
            u_input2 = input()
        if u_input2 == "0":
            aMenu = Menu()
            aMenu.menu()
        elif u_input2 == "1":
            self.show_items()
            print("")
            self.item_menu()
        elif u_input2 == "2":
            self.add_item_to_file()
            print("")
            self.item_menu()
        elif u_input2 == "3":
            self.update_item()
            print("")
            self.item_menu()
        elif u_input2 == "4" and self.type != "orders":
            self.delete_item()
            print("")
            self.item_menu()
        elif u_input2 == "4" and self.type == "orders":
            self.update_status()
            print("")
            self.item_menu()
        elif u_input2 == "5" and self.type == "orders":
            self.delete_item()
            print("")
            self.item_menu()


#NEW CLASS HERE


class Courier(Item):
    def __init__(self) -> None:
        self.type = "couriers"
        self.name = ""
        self.phone = ""
        self.field_names = ['name', 'phone']

    
    def asdict(self):
        return {'name': self.name, 'phone': self.phone}


#NEW CLASS HERE

class Product(Item):   
    def __init__(self) -> None:
        self.type = "products"
        self.name = ""
        self.price = 0
        self.field_names = ['name', 'price']

    
    def asdict(self):
        return {'name': self.name, 'price': self.price}
        

#NEW CLASS HERE

class Order(Item):
#TODO add method to add products to an order when creating a new order
    def __init__(self) -> None:

        self.type = "orders"
        self.customer_name = ""
        self.customer_address = ""
        self.customer_phone = ""
        self.courier = ""
        self.status = ""
        self.items = ""
        self.field_names = ['customer_name', 'customer_address', 'customer_phone', 'courier', 'status', 'items' ]

    def asdict(self):
        return {'customer_name': self.customer_name, 'customer_address': self.customer_address,
            'customer_phone' : self.customer_phone, 'courier' : self.courier, 'status' : self.status,
            'items' : self.items}
        
    def update_status(self):
            selected_list = self.get_csv_and_return_as_list_of_dict()
            valid_inputs = self.gen_valid_inputs()
            self.show_items()
            print(f"""Enter the number for the {self.type[:-1]} you want
        to update or x to go to main menu: """)
            updatee = input()
            self.check_valid_input(updatee, valid_inputs)
            updatee = int(updatee)
            updatee_as_dict = selected_list[updatee-1]
            new_status = input(f"Enter the new status: ")
            if new_status.strip() != "":
                updatee_as_dict["status"] = new_status

 

#NEW CLASS STARTS BELOW

class Menu():

    def menu(self):
        main_menu_string = """Choose an option:
    0 to exit
    1 for seeing the products menu
    2 for seeing the courier menu
    3 for seeing the order menu"""
        print(main_menu_string)
        u_input = input()
        print("")
        while u_input not in ("0", "1", "2", "3"):
            print("Not a valid option. Try again.")
            print(main_menu_string)
            u_input = input()
            print("")
        if u_input == "0":
            exit("Program ended")
        elif u_input == "1":
            print("")
            a_product = Product()
            a_product.item_menu()
        elif u_input == "2":
            print("")
            a_courier = Courier()
            a_courier.item_menu()
        elif u_input == "3":
            print("")
            an_order = Order()
            an_order.item_menu()

    # def get_couriers():
    #     couriers = []
    #     with open("data\couriers.txt", "r+") as courierf:
    #         for line in courierf:
    #             couriers.append(line.strip("\n"))
    #     return couriers


        


#anOrder = Order()
#anOrder.add_item_to_file()
#anOrder.show_items()
#anOrder.update_item()

# aProduct = Product()
# aProduct.add_item_to_file()
# # aProduct.show_items()
# aProduct.delete_item()

# aCourier = Courier()
# aCourier.add_item_to_file()


aMenu = Menu()
aMenu.menu()