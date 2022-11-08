import time
import os
from urllib.parse import parse_qsl
#TODO Create a courier menu

os.system("cls")

new_order = {
"customer_name":"",
"customer_address":"",
"customer_phone":"",
"status":""}




order_list = []

Products = ["apple","banana"]
'''
try:
    file = open("Cafe1.txt","r")
    for line in file:
        Products.append(line.strip())
    file.close()
except FileNotFoundError:
    pass
'''

def Exit():
    print("End of Program \n Thanks for visiting")
    return

print("Welcome to my program")


def StartScreen():
    os.system("cls")
    User_Option = input(" Enter a Value \n 0 : Exit \n 1: Menu \n 2 : Order Menu \n")
    while User_Option != 0:
        try:
            User_Option = int(User_Option)
        except ValueError:
            print("please enter a number")
            time.sleep(1)
            StartScreen()
        if User_Option == 0:
            Exit()
        elif User_Option == 1:
            Menu()
        elif User_Option == 2:
            Order_Menu()
        else:
            print("Invalid option")
            time.sleep(2)
            StartScreen()
        return

def Menu():
    #os.system('cls')
    print(f"The current list has {len(Products)} Items, {Products}")
    User_input = input("""Product menu option
     \n 0: Return to main menu 
     \n 1: View Product List 
     \n 2: Replace Product 
     \n 3: Update list 
     \n 4: Delete product \n""")
    try: 
        User_input = int(User_input)
    except ValueError:
        print("Please enter a number: ")
    if User_input == 0:
        StartScreen()
    elif User_input == 1:
        View_List()
    elif User_input == 2:
        Replace_Product()
    elif User_input == 3:
        Update_List()
    elif User_input == 4:
        Delete_Item()
    else:
        print("Invalid Input")
        time.sleep(2)
        os.system("cls")
        Menu()

def View_List():
    os.system('cls')
    if not Products:
        print("Empty List: ")
        time.sleep(1)
        Menu()
    else:
        print(Products)
        # replace below lines within a function
        UserChoice2 = input("Would you like to \n (0): View Product List \n (1) : replace Product \n (2): Update list \n (3): Delete product")
        try:
            UserChoice2 = int(UserChoice2)
        except ValueError:
            print("Please enter a number: ")
        if UserChoice2 == 0:
            View_List()
        elif UserChoice2 == 1:
            Replace_Product()
        elif UserChoice2 == 2:
            Update_List()
        elif UserChoice2== 3:
            pass

def Replace_Product():
    os.system('cls')
    print(f"The current list is {Products}")
    Old_item = input("Enter the index value of the Item you would like to replace: ")
    try:
        Old_item = int(Old_item)
    except ValueError:
        print("ENTER A NUMBER: ")
    New_item = input("Enter name of new item: ").title()
    try:
        Products[Old_item] = New_item
    except IndexError:
        print(f"Please enter an index value that is between 1 and {len(Products -1)} ")

def Update_List():
    choice = input("Would you like to add a new item ? \n  (0) :No \n (1):Yes ")
    os.system('cls')
    try:
        choice = int(choice)
    except ValueError:
        print("PlEASE ENTER A NUMBER Would you like to add a new item? \n \n \n 0:No \n 1:Yes ")
    while choice != 0:
        new_product = input("Enter name of new product ").title()
        Products.append(new_product)
        print(Products)
        Update_List()
    Menu()
 #TODO Option 4 delete item
def Delete_Item():
    os.system('cls')
    Delete_Menu = input("Would you like to delete an item \n Y \n N ").title()
    if Delete_Menu[0].upper() == "N":
        Menu()
    else:
        count = 0
        for item in Products:
            print(count, " - ", item)
            count +=1 
        Delete_option = input("Enter the value of item you would like to delete: ")
        try:
            Delete_option = int(Delete_option)
            del Products[Delete_option]
            print(f"The list looks like{Products}")
            time.sleep(1)
            Delete_Item()
        except:
            print("hi")
            Delete_Item() 


def Create_Order():
    os.system("cls")
    New_Costumer_Name = input("Enter Customer name: ").title()
    try:
        New_Costumer_Name = str(New_Costumer_Name)
    except ValueError:
        print("Enter a string ")
        Create_Order()
    new_order["customer_name"] = New_Costumer_Name
    New_Costumer_Address = input("Enter customer address: ")
    new_order["customer_address"] = New_Costumer_Address
    New_Costumer_Phone = input("Enter customer phone number: ")
    try:
        New_Costumer_Phone = int(New_Costumer_Phone)
    except ValueError:
        print("Please enter only numbers")
        Create_Order()
    new_order["customer_phone"] = New_Costumer_Phone
    new_order["New_Costumer_Status"] = "Preparing"
    print("Loading ... ")
    time.sleep(2)
    print(new_order)
    time.sleep(3)




def Order_Menu():
    os.system("cls")
    order_option = input("""
    Orders menu:\n
    0) Exit to main menu.\n
    1) View list of orders.\n
    2) Create a new order.\n
    3) Update order status.\n
    4) Update existing order.\n
    5) Remove existing order.\n""")
    while order_option !=0:
        try:
            order_option = int(order_option)
        except ValueError:
            print("Please enter an integer value")
            Order_Menu()
        if order_option == 0:
            Menu()
        elif order_option == 1:
            if not order_list:
                print("List empty")
                time.sleep(1)
                Order_Menu()
            print(*order_list, sep = "\n\n")
            time.sleep(1)
        elif order_option == 2:
            Create_Order()

        elif order_option == 3:
            pass
        elif order_option == 4:
            pass

        elif order_option == 5:
            pass
        else:
            print("Invalid Number input")
            time.sleep(2)
            Order_Menu()




def Save():
    file = open("Cafe1.txt","w")

StartScreen()