import os
import products
import couriers
import orders

# main menue
def main_menu():
    first_input = 1
    while first_input != 0:
        os.system("cls")
        print("******* Welcome to POP-UP CAFE *******\n")
        first_input = int(input("0 To Exit \n1 Product Menue \n2 Couriers Menue \n3 Order Menue: "))
        try:
            if first_input <4:
                if first_input == 1:
                    os.system("cls")
                    product_menue()

                elif first_input == 2:
                    os.system("cls")
                    courioure_menue()

                elif first_input == 3:
                    os.system("cls")
                    order_menue()
        except ValueError as r:
            print(r)
    print("Thank you very much")

# product menue
def product_menue():
    prod_data = products.Products()
    second_input = 1
    while second_input != 0:
        print("\n******* PRODUCT MENUE *******\n")
        second_input = int(input("0 Main Menue \n1 All products \n2 Add new product \n3 update an Existing product \n4 Delete a product: "))
       
        #List of all products
        if second_input == 1:
            os.system('cls')
            print("\n******* All products *******\n")
            prod_data.display_products()

        #adding new products
        elif second_input == 2:
            os.system('cls')
            print("\n******* Adding New Product *******\n")
            new_product = input("\nEnter the name of new product: ")
            prod_data.add_product(new_product)
            print("\nNew Product Added...")

        # Updating existing product
        elif second_input == 3:
            temp = 'y'
            while not temp == 'n':
                os.system('cls')
                print("\n******* Updating Existing Product *******\n")
                prod_name = input("\nEnter the name of product:  ")
                prod_check = prod_data.is_product_exist(prod_name)
                if prod_check != "none":
                    new_prod_name = input("\nEnter new product Name:  ")
                    prod_data.update_product(prod_check,new_prod_name)
                    print("\nProduct Updated...")
                    break
                else:
                     temp = input("\nProduct not exist try again y/n: ")
       
        #Deleting a product
        elif second_input == 4:
            temp = 'y'
            while not temp == 'n':
                os.system('cls')
                print("\n******* Delete a Product *******\n")
                prod_name = input("\nEnter the name of product: ")
                if prod_name in prod_data.get_products():
                    prod_data.del_product(prod_name)
                    print("\nProduct Deleted...")
                    break
                else:
                    temp = input("\nProduct not exist try again y/n")
    prod_data.write_into_file()

# couriour menue
def courioure_menue():
    cour_data = couriers.Couriers()
    second_input = 1
    while second_input != 0:
        print("\n******* PRODUCT MENUE *******\n")
        second_input = int(input("0 Main Menue \n1 All Couriers \n2 Add new Couriers \n3 update an Existing Couriers \n4 Delete a Couriers: "))
        # All couriers
        if second_input == 1:
            os.system('cls')
            print("******* All Couriers *******\n")
            cour_data.display_products()
        # Addidng new Courier
        elif second_input == 2:
            os.system('cls')
            print("\n******* Adding New Courier *******\n")
            new_courier = input("Enter the name of new Courier: ")
            cour_data.add_product(new_courier)
            print("\nNew Courier Added")
        #Update an Existing courier
        elif second_input == 3:
            temp = 'y'
            while not temp == 'n':
                os.system('cls')
                print("\n******* Updating Existing Courier *******\n")
                name = input("\nEnter the name of Courier:  ")
                check = cour_data.is_product_exist(name)
                if check != "none":
                    new_prod_name = input("\nEnter new Courier Name:  ")
                    cour_data.update_product(check,new_prod_name)
                    print("\Courier Updated...")
                    break
                else:
                     temp = input("\nCourier not exist try again y/n: ")

        elif second_input == 4:
            temp = 'y'
            while not temp == 'n':
                os.system('cls')
                print("\n******* Delete a Courier *******\n")
                name = input("\nEnter the name of Courier: ")
                if name in cour_data.get_products():
                    cour_data.del_product(name)
                    print("\nCourier Deleted...")
                    break
                else:
                    temp = input("\Courier not exist try again y/n")
    cour_data.write_into_file()

# Order Menue
def order_menue():

    second_input = 1
    order_data = orders.Orders()
    while second_input != 0:
        print("\n******* ORDER MENUE *******\n")
        second_input = int(input("0 Main Menue \n1 All Orders \n2 Create Order \n3 update Order status \n4 Update Existing order \n5 Delete order : "))
        
        # All orders list
        if second_input == 1:
            os.system("cls")
            print("******* All Orders *******\n")
            order_data.display_order()

        #create new order
        elif second_input == 2:
            os.system("cls")
            print("\n******* Create New Order *******\n")
            c_name = input("Customer name: ")
            c_address = input("Customer Address: ")
            c_phone = input("Customer Phone: ")
            o_status = "PREPARING"
            new_order = {"customer_name":c_name,"customer_address":c_address,"customer_phone":c_phone,"status":o_status}
            order_data.add_ordert(new_order)
            print("\nNew Order Added...")
        
        #update order status
        elif second_input == 3:
            temp = 'y'   
            while temp != 'n':
                os.system("cls")
                order_data.display_order()
                print("\n******* Update Order Status *******\n")
                order_no = int(input("Enter Order number: "))
                ord_lst = order_data.is_order_exist(order_no)
                if ord_lst != "none":
                    print("Current order status is:"+ ord_lst.get("status"))
                    temp = input("\nDo you want update status? y/n")
                    if temp == 'y':
                        get_status = int(input("\n0 'PPREPARING'\n1 'READY'\n2 'COMPLETED' "))
                        if get_status == 0:
                            ord_lst.update({"status":"PPREPARING"})
                            order_data.update_order(order_no,ord_lst)
                            break
                        elif get_status == 1:
                            ord_lst.update({"status":"READY"})
                            order_data.update_order(order_no,ord_lst)
                            break
                        elif get_status == 2:
                            ord_lst.update({"status":"COMPLETED"})
                            order_data.update_order(order_no,ord_lst)
                            break
                else:
                    temp = input("\nOrder not exist try again y/n: ")
        #update an existing order
        elif second_input == 4:
            temp = 'y'   
            while temp != 'n':
                os.system("cls")
                order_data.display_order()
                print("\n******* Update Order *******\n")
                order_no = int(input("Enter Order number: "))
                ord_lst = order_data.is_order_exist(order_no)
                if ord_lst != "none":
                    name = input("\nEnter new name: ")
                    add = input("\nEnter new address: ")
                    ph = input("\nEnter newphone : ")
                    ord_lst.update({"customer_name":name,"customer_address":add,"customer_phone":ph})
                    order_data.update_order(order_no,ord_lst)
                    print("Order Updated")
                    break
                else:
                    temp = input("\nOrder not exist try again y/n: ")

        #Delete an order
        elif second_input == 5:
            temp = 'y'   
            while temp != 'n':
                os.system("cls")
                order_data.display_order()
                print("\n******* Update Order *******\n")
                order_no = int(input("Enter Order number: "))
                ord_lst = order_data.is_order_exist(order_no)
                if ord_lst != "none":
                    ord_lst.update({"customer_name":name,"customer_address":add,"customer_phone":ph})
                    order_data.del_order(order_no)
                    print("Order Deleted")
                    break
                else:
                    temp = input("\nOrder not exist try again y/n: ")
    order_data.write_into_file()
            
main_menu()