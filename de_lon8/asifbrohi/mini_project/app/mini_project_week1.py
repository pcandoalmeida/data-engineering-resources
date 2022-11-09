product_list = ["sandwich","crisp","burger","soft drink","coffee"]


def main_menu():

    print("Welcome to my Cafe, Please pick the options below")

    print("***MAIN MENU***")
    command_ = int(input("0===>EXIT\n1===>PRODUCT MENU\n:"))
    while True:
      if command_ == 0:
        
        exit()
      elif command_ == 1:
        main_menu_options()
     
      
        
 
 




    #commands in here 
    # EXIT
    # PRODUCT MENU




""" The use of this function is to allow users to input values to add, update, delete or pick products inside the list"""
def main_menu_options():
    print("***PRODUCTS MENU***")
    user= int(input("RETURN MAIN MENU:0\nOPEN MENU:1\nADD ITEM:2\nUPDATE ITEM:3\nDELETE ITEM:4\n:")) 
    # code make easeir to read 
                                
    while True:
        if user == 0:
            main_menu()                     
        
        elif user == 1:
            input_1 = int(input("VIEW LIST:1\nMAIN MENU:0 \n:"))
            
            if input_1==1:
                print(product_list)
                continued = input("Continue \ny/n\n")
                while continued == "y":
                  main_menu_options()
                
                main_menu()
                  

            elif input_1==0:
                main_menu()
                
#add item   
        elif user == 2:
            new_item = input("ADD ITEM\n")
            product_list.append(new_item)
           
            added_item= input("Continue Adding\ny/n\n") 
            while added_item == "y":
              main_menu_options()
            
            print(product_list)
            main_menu()
            
            
            
            
#update item
        elif user == 3:
            print(product_list)          
            for update in range(len(product_list)):
               
                update_item = int(input("Input index change\n:"))
                break
            product_list[update_item] = str(input("UPDATE ITEM\n"))
            print(f"ITEM UPDATED:  {product_list[update_item]}")
            update_condition = input("Continue Updating\ny/n\n")
            while update_condition =="y":
              main_menu_options()
            
            print(product_list)
            main_menu()
          
            
     
            
            
            
# del item
        elif user == 4:
            for delete in range(len(product_list)):
                delete_item = int(input("Input index to delete: "))
                del product_list[delete_item]
                break
            del_condition = input("Continue Deleting\ny/n\n")
            while del_condition =="y":
              main_menu_options()
            print(product_list)
            main_menu()


main_menu()