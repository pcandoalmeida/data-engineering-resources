#A courier should just be a string containing its name, i.e: "John"
#A list of couriers should be a list of strings , i.e: ["John"]


# TODO Change data validation in functions into its own function
# TODO Replace long strigns with """ multiline strings
# TODO Make create, update, delete functions independent of courier or product
# 


#~~~~~~~~~~~~~~~~~~~~~~~~~~
# COURIER FUNCTIONS START HERE
#~~~~~~~~~~~~~~~~~~~~~~~~~~

couriers = ["John", "Pete", "Mary", "Rasheed"]

def show_couriers(couriers):
    print("\nCourier list")
    for courier in couriers:
        print(courier)


def courier_in_list_checker(couriers, courier):
    if courier in couriers:
        return False
    else:
        return True

def create_courier(products,couriers):
    new_courier = input("Enter the name of the new courier:\n")
    #because the recursive call was resulting in invalid values coming through, I decided
    #to create tuples to keep track of an input was really new so that I can use it later
    #to decide if the input goes in or not
    real_new_courier = (new_courier, courier_in_list_checker(couriers, new_courier))
    if real_new_courier[1] == False:
        #weakness, this would accept same courier if capitalisation different
        print("That courier is already in our list")
        new_or_quit = input("Enter 1 to add a different courier or 0 go back to courier menu:\n")
        while new_or_quit != "1" and new_or_quit != "0":
            print("Not a valid option. Try again.")
            new_or_quit  = input("Enter 1 to add a different courier or 0 go back to courier menu:\n")
        if new_or_quit == "1":
            #This is the recursion that was causing trouble because the script would accept invalid inputs
            #and append them later on.
            create_courier(products, couriers)
        else:
            courier_menu(products, couriers)
    #if the courier was actually new return the updated list
    if real_new_courier[1] == True:
        couriers.append(new_courier)
        return(couriers)
    #we return the unchanged list if there was no new courier, needed because of the 
    #recursive call (could code an if check for returned value in the c menu instead)
    else:
        return(couriers)


def update_courier(couriers):
    print("")
    for courier in couriers:
        print(couriers.index(courier), courier)
    print("")
    print("Enter the number for the courier you want to replace: ")
    try:
        replacee = int(input())
    except ValueError:
        replacee = -1
        print("""Only whole numbers are valid.
Please, enter one from the list""")
        update_courier(couriers)
    while replacee not in range(len(couriers)) and str(replacee).lower() != "x":
        print("""Not a valid option. Try again.
Choose an option:""")
        replacee = input("""Enter the number for the courier you want
to replace or x to go back to courier menu""")
    if str(replacee).lower() == "x":
        courier_menu(products, couriers)
    else:
        replacement = input(f"Enter the courier you want to replace {couriers[replacee]} with: ")
        couriers[replacee] = replacement
        print(f"courier number {replacee} is now {replacement}.")
        courier_menu(products, couriers)

def delete_courier(couriers):
    print("")
    for courier in couriers:
        print(couriers.index(courier), courier)
    print("")
    print("Enter the number for the courier you want to delete: ")
    try:
        deletee = int(input())
    except ValueError:
        deletee = -1
        print("Only whole numbers are valid.Please, enter one from the list")
        update_courier(couriers)
    while deletee not in range(len(couriers)) and str(deletee).lower() != "x":
        print("Not a valid option. Try again.\nChoose an option:")
        deletee = input("""Enter the number for the courier you want
to replace or x to go back to courier menu""")
    if str(deletee).lower() == "x":
        courier_menu(products, couriers)
    else:
        del couriers[deletee]
        print(f"courier number {deletee} is now deleted.")
        courier_menu(products, couriers)



#~~~~~~~~~~~~~~~~~~~~~~~~~~
# COURIER FUNCTIONS END HERE
#END END END
#~~~~~~~~~~~~~~~~~~~~~~~~~~

products = []
with open("data\products.txt", "r") as productf:
    for line in productf:
        #Each line had 
        products.append(line.strip("\n"))




def show_products(products):
    print("\nProduct list")
    with open("data\products.txt", "r") as productf:
        for line in productf:
            #Each line had 
            print(line.strip("\n"))

    

def product_in_list_checker(products, product):
    if product in products:
        return False
    else:
        return True


#IDEA: add a validator that takes a function and a list of valid inputs? Very imcomplete idea
def create_product(products):
    #
    #DEFENSIVE STUFF
    #
    new_product = input("Enter the new product:\n")
    #because the recursive call was resulting in invalid values coming through, I decided
    #to create tuples to keep track of an input was really new so that I can use it later
    #to decide if the input goes in or not
    real_new_prod = (new_product, product_in_list_checker(products, new_product))
    new_or_quit_string = """Enter 1 to add a different product or 0 go 
back to product menu:\n"""
    if real_new_prod[1] == False:
        #weakness, this would accept same product if capitalisation different
        print("That product is already in our list")
        new_or_quit = input(new_or_quit_string)
        while new_or_quit != "1" and new_or_quit != "0":
            print("Not a valid option. Try again.")
            new_or_quit  = input(new_or_quit_string)
        if new_or_quit == "1":
            #This is the recursion that was causing trouble because the script would accept invalid inputs
            #and append them later on.
            create_product(products)
        else:
            product_menu(products, couriers)
    #END OF DEFENSIVE STUFF
    if real_new_prod[1] == True:
        with open("data\products.txt", "a") as productsf:
            productsf.write(f"\n{new_product}")
        return(products)
    #we return the unchanged list if there was no new product
    #needed because of the 
    #recursive call (could code an if check for returned value in
    #the product menu instead)
    else:
        return(products)

def update_product(products):
    print("")
    print("\nProduct list")
    with open("data\products.txt", "r") as productf:
        for num, line in enumerate(productf):
            #Each line had 
            print(num, line.strip("\n"))
    print("")
    print("Enter the number for the product you want to replace: ")#
    #### BUNCH OF DEFENSIVE STUFF HERE
    try:
        replacee = int(input())
    except ValueError:
        replacee = -1
        print("Only whole numbers are valid.Please, enter one from the list")
        update_product(products)
    while replacee not in range(len(products)) and str(replacee).lower() != "x":
        print("Not a valid option. Try again.\nChoose an option:")
        replacee = input("""Enter the number for the product you want
to replace or x to go back to product menu""")
    if str(replacee).lower() == "x":
        product_menu(products, couriers)
    #END OF DEFENSIVE STUFF
    else:
        replacement = input(f"Enter the product you want to replace {products[replacee]} with: ")#
        with open("data\products.txt", "r") as productsf:
            data = productsf.readlines()
        data[replacee] = f"{replacement}\n"
        with open("data\products.txt", "w") as productsf:
            productsf.writelines(data)
        return(products)
        products[replacee] = replacement
        print(f"Product number {replacee} is now {replacement}.")
        product_menu(products, couriers)

def delete_product(products):
    print("")
    with open("data\products.txt", "r") as productf:
        for num, line in enumerate(productf):            
            print(num, line.strip("\n"))
    print("")
    print("Enter the number for the product you want to delete: ")
    # DEFENSIVE STUFF HERE
    try:
        deletee = int(input())
    except ValueError:
        deletee = -1
        print("Only whole numbers are valid.Please, enter one from the list")
        update_product(products)
    while deletee not in range(len(products)) and str(deletee).lower() != "x":
        print("Not a valid option. Try again.\nChoose an option:")
        deletee = input("""Enter the number for the product you want
to replace or x to go back to product menu""")
    if str(deletee).lower() == "x":
        product_menu(products, couriers)
    ##END OF DEFENSIVE STUFF
    else:
        with open("data\products.txt", "r") as productf:
                lines = productf.readlines()
        with open("data\products.txt", "w") as productf:
            for line in lines:
                if lines.index(line) != deletee:
                    productf.write(line)
        print(f"Product number {deletee} is now deleted.")
        product_menu(products, couriers)


def courier_menu(products, couriers):
    courier_menu_string = """Choose an option:
0 to go to main menu
1 for seeing the list of couriers
2 to add a new courier
3 to update/replace a courier
4 to delete a courier"""
    print(courier_menu_string)
    u_input2 = input()
    while u_input2 != "1" and u_input2 != "0"\
        and u_input2 != "2" and u_input2 != "3"\
        and u_input2 != "4":
        print("Not a valid option. Try again.") 
        print(courier_menu_string)
        u_input2 = input()
    if u_input2 == "0":
        menu(products, couriers)
    elif u_input2 == "1":
        show_couriers(couriers)
        print("")
        courier_menu(products,couriers)
    elif u_input2 == "2":
        couriers = list(create_courier(products, couriers))
        print("")
        courier_menu(products, couriers)
    elif u_input2 == "3":
        update_courier(couriers)
        print("")
        courier_menu(products, couriers)
    elif u_input2 == "4":
        delete_courier(couriers)
        print("")
        courier_menu(products, couriers)   

def product_menu(products, couriers):
    product_menu_string = """Choose an option:
0 to go to main menu
1 for seeing the list of products
2 to add a new product
3 Update product list
4 Delete product\n"""
    print(product_menu_string)
    u_input2 = input()
    while u_input2 != "1" and u_input2 != "0" \
        and u_input2 != "2" and u_input2 != "3"\
        and u_input2 != "4":
        print("Not a valid option. Try again.") 
        print(product_menu_string)        
        u_input2 = input()
    if u_input2 == "0":
        menu(products, couriers)
    elif u_input2 == "1":
        show_products(products)
        print("")
        product_menu(products, couriers)
    elif u_input2 == "2":
        products = list(create_product(products))
        print("")
        product_menu(products, couriers)
    elif u_input2 == "3":
        update_product(products)
        print("")
        product_menu(products, couriers)
    elif u_input2 == "4":
        delete_product(products)
        print("")
        product_menu(products, couriers)

def menu(products, couriers):
    main_menu_string = """Choose an option:
0 to exit
1 for seeing the products menu
2 for seeing the courier menu"""
    print(main_menu_string)
    u_input = input()
    print("")
    while u_input != "1" and u_input != "0" and u_input != "2":
        print("Not a valid option. Try again.")
        print(main_menu_string)
        u_input = input()
        print("")
    if u_input == "0":
        exit("Program ended")
    elif u_input == "1":
        print("")
        product_menu(products, couriers)
    elif u_input == "2":
        print("")
        courier_menu(products, couriers)

menu(products, couriers)