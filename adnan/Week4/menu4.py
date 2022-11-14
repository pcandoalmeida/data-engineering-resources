import Week4.Functions2 as func
func.load_products()
func.load_orders()
func.load_courier()
print(" |Cafe Generation| " )
main_menu = int(input(" '0' To Exit App \n '1' For Product Menu \n '2' For Order Menu \n '3' For Courier Menu \n >>>"))
while main_menu != 0:
    if main_menu == 1:

        Product_menu = int(input(" '0' To Exit App \n '1' To View Menu \n '2' To Create New Product \n '3' To Update Product \n '4' To Delete Product \n >>> "))
        
        while Product_menu != 0:
            if Product_menu == 1:
                print(func.product_list)
                Product_menu = int(input(" '0' To Exit App \n '1' To View Menu \n '2' To Create New Product \n '3' To Update Product \n '4' To Delete Product \n >>> "))
            elif Product_menu == 2:
                func.create_product()
                Product_menu = int(input(" '0' To Exit App \n '1' To View Menu \n '2' To Create New Product \n '3' To Update Product \n '4' To Delete Product \n >>> "))               
            elif Product_menu == 3:
               func.update_product()
               Product_menu = int(input(" '0' To Exit App \n '1' To View Menu \n '2' To Create New Product \n '3' To Update Product \n '4' To Delete Product \n >>> "))
            elif Product_menu == 4:
                func.delete_product()
                Product_menu = int(input(" '0' To Exit App \n '1' To View Menu \n '2' To Create New Product \n '3' To Update Product \n '4' To Delete Product \n >>> "))
        main_menu = int(input(" '0' To Exit App \n '1' For Product Menu \n '2' For Order Menu \n '3' For Courier Menu \n >>>"))


    elif main_menu == 2: #TODO: make a while loop to keep asking to add things to basket

        shopping_basket = {}
        order_status = 'preparing'
        orders_list = []
        order_menu = int(input(" '0' To Return to Main Menu \n 1 To View Orders \n 2 Add customer information \n 3 to update existing order status \n 4 to update order \n 5 to delete order \n>>>"))
        while order_menu != 0:
            if order_menu == 1:
                print(orders_list)
                order_menu = int(input(" '0' To Return to Main Menu \n 1 To View Orders \n 2 Add customer information \n 3 to update existing order status \n 4 to update order \n 5 to delete order \n>>>"))
            elif order_menu == 2:
                func.create_order()
                order_menu = int(input(" '0' To Return to Main Menu \n 1 To View Orders \n 2 Add customer information \n 3 to update existing order status \n 4 to update order \n 5 to delete order \n>>>"))
            elif order_menu == 3:
                func.change_order_status()
                order_menu = int(input(" '0' To Return to Main Menu \n 1 To View Orders \n 2 Add customer information \n 3 to update existing order status \n 4 to update order \n 5 to delete order \n>>>"))
            elif order_menu == 4:
                func.change_order()
                order_menu = int(input(" '0' To Return to Main Menu \n 1 To View Orders \n 2 Add customer information \n 3 to update existing order status \n 4 to update order \n 5 to delete order \n>>>"))
            elif order_menu == 5:
                func.delete_order()
                order_menu = int(input(" '0' To Return to Main Menu \n 1 To View Orders \n 2 Add customer information \n 3 to update existing order status \n 4 to update order \n 5 to delete order \n>>>"))
        
        
        main_menu = int(input(" '0' To Exit App \n '1' For Product Menu \n '2' For Order Menu \n '3' For Courier Menu \n >>>"))
        
    if main_menu == 3:


        Courier_menu = int(input(" '0' To Exit To MainMenu \n '1' To View Courier \n '2' To Create New Courier \n '3' To Change Courier \n '4' To Delete Courier\n >>>"))
        # couriers menu ELSE IF user input is 2:
        while Courier_menu != 0:
            if Courier_menu == 1:
                print(func.Courier_list)
                Courier_menu = int(input(" '0' To Exit To MainMenu \n '1' To View Courier \n '2' To Create New Courier \n '3' To Change Courier \n '4' To Delete Courier\n >>>"))
                 #view courier
            elif Courier_menu == 2:
                func.create_courier()
                Courier_menu = int(input(" '0' To Exit To MainMenu \n '1' To View Courier \n '2' To Create New Courier \n '3' To Change Courier \n '4' To Delete Courier\n >>>"))
                 # create new courier
            elif Courier_menu == 3:
                func.update_courier()
                Courier_menu = int(input(" '0' To Exit To MainMenu \n '1' To View Courier \n '2' To Create New Courier \n '3' To Change Courier \n '4' To Delete Courier\n >>>"))
                #change courier
            elif Courier_menu == 4:
                func.delete_courier
                Courier_menu = int(input(" '0' To Exit To MainMenu \n '1' To View Courier \n '2' To Create New Courier \n '3' To Change Courier \n '4' To Delete Courier\n >>>"))
                #delete #courier
        
        
        main_menu = int(input(" '0' To Exit App \n '1' For Product Menu \n '2' For Order Menu \n '3' For Courier Menu \n >>>"))


else:
    ans = input("would you like to continue or exit: ")
    if ans == "exit":
        #save and quit
        func.save_courier()
        func.save_products()
        func.save_orders()
        exit()

            
                


    #     #courier Menu
    #     pass     
    # ans = input("would you like to continue or exit: ")
    # if ans == "exit":
    #     # SAVE products list to products.txt 
    #     # SAVE couriers list to couriers.txt
    # #save everything
    #     exit()
    
            

