import os

def main_menu():
    main_options = int(input("""
Welcome.
Exit: 0
Continue: 1
"""))
    while main_options !=0:
        sub_menu()
    exit()


def sub_menu():
    option = int(input("""
Welcome to the product and courier menu.
Main menu: 0
Print list: 1
Add to product/courier list: 2
Update product/courier list: 3
Delete product/courier: 4:
"""))

    while option != 0:
        if option ==1:
            print_menu()
        elif option == 2:
            create_item()
        elif option == 3:
            update_item()
        elif option == 4:
            delete_item()
        else:
            print("Please enter a number between 0 and 4.")
    return main_menu

def print_menu():
    which_file = int(input("""
Which menu would you like to access?
Product: 1
Courier: 2
"""))
    if which_file == 1:
        try:
            with open(r"data\products.txt", "r") as product:
                product_list = product.readlines()
                formatted_product_list = [i.strip("\n") for i in product_list]
                print(f"Products: {', '.join(formatted_product_list)}")
        except Exception as e:
            print(f"Error: {str(e)}.")
            
    elif which_file == 2:
        try:
            with open(r"data\couriers.txt", "r") as courier:
                courier_list = courier.readlines()
                formatted_courier_list = [i.strip("\n") for i in courier_list]
                print(f"Couriers: {formatted_courier_list}")
        except Exception as e:
            print(f"Error: {str(e)}.")
    elif which_file == 3:
        global orders_list
        print(orders_list)
    return sub_menu()

def create_item():
    which_file = int(input("""
Which menu would you like to access?
Product: 1
Courier: 2
Orders: 3
"""))
    if which_file == 1:
        new_item = input("Enter new product:\n").lower()
        try:
            with open(r"data\products.txt","a") as products:
                products.write("\n" + new_item)
        except Exception as e:
            print(f"Error: {str(e)}")
        return sub_menu()
    elif which_file == 2:
        new_item = input("Enter new courier:\n").lower()
        try:
            with open(r"data\couriers.txt","a") as courier:
                courier.write("\n" + new_item)
        except Exception as e:
            print(f"Error: {str(e)}")
        return sub_menu()
    # elif which_file == 3:
        #add_order()


def update_item():
    which_file =  int(input("""
Which menu would you like to access?
Product: 1
Courier: 2
"""))
    if which_file == 1:
        
        try:
            with(open(r"data\products.txt", "r")) as f:
                file_lines = f.readlines()
                formatted_product_list = [i.strip("\n") for i in file_lines]
            print(formatted_product_list)
            index_to_update =int(input(f"""
The product list items with their index items are : {list(enumerate(formatted_product_list))}.
Please enter the index of the item you would like to update.
"""))
            updated_product = input("Please enter the new product name.\n")
            for item in range(len(formatted_product_list)):
                if item == index_to_update:
                    formatted_product_list[index_to_update] = updated_product
        except Exception as e:
            print(f"Error: {str(e)}")

        try:
            with open(r"data\products.txt","w") as f:
                for i in formatted_product_list:
                    f.write(i+"\n")
        except Exception as e:
            print(f"Error: {str(e)}")

    elif which_file == 2:
        try:
            with(open(r"data\couriers.txt", "r")) as f:
                file_lines = f.readlines()
                formatted_courier_list = [i.strip("\n") for i in file_lines]
                index_to_update =int(input(f"""
The product list items with their index items are : {list(enumerate(formatted_courier_list))}.
Please enter the index of the item you would like to update.
"""))
                updated_courier = input("Please enter the new courier name.\n").title()
                for item in range(len(formatted_courier_list)):
                    if item == index_to_update:
                        formatted_courier_list[index_to_update] = updated_courier
        except Exception as e:
            print(f"Error: {str(e)}")

        try:
            with open(r"data\couriers.txt","w") as f:
                for i in formatted_courier_list:
                    f.write(i+"\n")
        except Exception as e:
            print(f"Error: {str(e)}")
    return sub_menu()

def delete_item():
    which_file =  int(input("""
Which menu would you like to access?
Product: 1
Courier: 2
"""))
    if which_file == 1:
        try:
            with open(r"data\products.txt", "r") as f:
                formatted_products = [i.strip("\n") for i in f.readlines()]
            print(formatted_products)
            index_to_delete =int(input(f"""
The product list items with their index items are : {list(enumerate(formatted_products))}.
Please enter the index of the item you would like to delete.
"""))
        except Exception as e:
            print(f"Error: {str(e)}")
        for index in range(len(formatted_products)):
            if index == index_to_delete:
                formatted_products.remove(formatted_products[index])
        print(formatted_products)
        try:
            with open(r"data\products.txt","w") as f:
                for i in formatted_products:
                    f.write(i+"\n")
        except Exception as e:
            print(f"Error: {str(e)}")
    elif which_file == 2:
        try:
            with open(r"data\couriers.txt", "r") as f:
                formatted_couriers = [i.strip("\n") for i in f.readlines()]
            print(formatted_couriers)
            index_to_delete =int(input(f"""
The product list items with their index items are : {list(enumerate(formatted_couriers))}.
Please enter the index of the item you would like to delete.
"""))
        except Exception as e:
            print(f"Error: {str(e)}")
        for index in range(len(formatted_couriers)):
            if index == index_to_delete:
                formatted_couriers.remove(formatted_couriers[index])
        print(formatted_couriers)
        try:
            with open(r"data\couriers.txt","w") as f:
                for i in formatted_couriers:
                    f.write(i+"\n")
        except Exception as e:
            print(f"Error: {str(e)}")
    return sub_menu()

    
        
    


if __name__ == "__main__":
    main_menu()