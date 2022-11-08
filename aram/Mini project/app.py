#A product should just be a string containing its name, 
# #i.e: "Coke Zero" A list of products should be a list of strings , i.e: ["Coke Zero"]

# add some product names
from re import U


products = ["Coke Zero", "Coke", "Crips", "Coffee"]

def show_products(products):
    print("\nProduct list")
    for product in products:
        print(product)
    

def product_in_list_checker(products, product):
    if product in products:
        return False
    else:
        return True


#IDEA: add a validator that takes a function and a list of valid inputs? Very imcomplete idea
def create_product(products):
    new_product = input("Enter the new product:\n")
    #because the recursive call was resulting in invalid values coming through, I decided
    #to create tuples to keep track of an input was really new so that I can use it later
    #to decide if the input goes in or not
    real_new_prod = (new_product, product_in_list_checker(products, new_product))
    if real_new_prod[1] == False:
        #weakness, this would accept same product if capitalisation different
        print("That product is already in our list")
        new_or_quit = input("Enter 1 to add a different product or 0 go back to product menu:\n")
        while new_or_quit != "1" and new_or_quit != "0":
            print("Not a valid option. Try again.")
            new_or_quit  = input("Enter 1 to add a different product or 0 go back to product menu:\n")
        if new_or_quit == "1":
            #This is the recursion that was causing trouble because the script would accept invalid inputs
            #and append them later on.
            create_product(products)
        else:
            product_menu(products)
    #if the product was actually new return the updated list
    if real_new_prod[1] == True:
        products.append(new_product)
        return(products)
    #we return the unchanged list if there was no new product, needed because of the 
    #recursive call (could code an if check for returned value in the product menu instead)
    else:
        return(products)

def update_product(products):
    print("")
    for product in products:
        print(products.index(product), product)
    print("")
    print("Enter the number for the product you want to replace: ")
    try:
        replacee = int(input())
    except ValueError:
        replacee = -1
        print("Only whole numbers are valid.Please, enter one from the list")
        update_product(products)
    while replacee not in range(len(products)) and str(replacee).lower() != "x":
        print("Not a valid option. Try again.\nChoose an option:")
        replacee = input("Enter the number for the product you want to replace or x to go back to product menu")
    if str(replacee).lower() == "x":
        product_menu(products)
    else:
        replacement = input(f"Enter the product you want to replace {products[replacee]} with: ")
        products[replacee] = replacement
        print(f"Product number {replacee} is now {replacement}.")
        product_menu(products)

def delete_product(products):
    print("")
    for product in products:
        print(products.index(product), product)
    print("")
    print("Enter the number for the product you want to delete: ")
    try:
        deletee = int(input())
    except ValueError:
        deletee = -1
        print("Only whole numbers are valid.Please, enter one from the list")
        update_product(products)
    while deletee not in range(len(products)) and str(deletee).lower() != "x":
        print("Not a valid option. Try again.\nChoose an option:")
        deletee = input("Enter the number for the product you want to replace or x to go back to product menu")
    if str(deletee).lower() == "x":
        product_menu(products)
    else:
        del products[deletee]
        print(f"Product number {deletee} is now deleted.")
        product_menu(products)

def menu(products):
    print("Choose an option:\n0 to exit\n1 for seeing the products menu")
    u_input = input()
    print("")
    while u_input != "1" and u_input != "0":
        print("Not a valid option. Try again.\nChoose an option:\n0 to exit\n1 for seeing the products menu")
        u_input = input()
        print("")
    if u_input == "0":
        exit()
    elif u_input == "1":
        print("")
        product_menu(products)
        
        

def product_menu(products):
    print("Choose an option:\n0 to go to main menu\n1 for seeing the list of products")
    print("2 to add a new product\n3 Update product list\n4 Delete product")
    u_input2 = input()
    while u_input2 != "1" and u_input2 != "0" and u_input2 != "2" and u_input2 != "3" and u_input2 != "4":
        print("Not a valid option. Try again.") 
        print("Choose an option:\n0 to go to main menu\n1 for seeing the list of products")
        print("2 to add a new product\n3 Update product list\n4 Delete product")
        u_input2 = input()
    if u_input2 == "0":
        menu(products)
    elif u_input2 == "1":
        show_products(products)
        print("")
        product_menu(products)
    elif u_input2 == "2":
        products = list(create_product(products))
        print("")
        product_menu(products)
    elif u_input2 == "3":
        update_product(products)
        print("")
        product_menu(products)
    elif u_input2 == "4":
        delete_product(products)
        print("")
        product_menu(products)


menu(products)