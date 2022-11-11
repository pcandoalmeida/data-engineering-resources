
# load product_list.txt
# load courier.txt
product = open("product_list.txt", 'w+')
courier = open("courier.txt",'w+')
product_list = ["sandwich","crisp","burger","soft drink","coffee"]
courier_list= ["Charlie", "John", "Yasmine", "Amy", "Roger"]
orders={
 "customer_name": "John",
 "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
 "customer_phone": "0789887334",
 "status": "preparing"
}
def read_file():
  for product_ in product_list:
    product.write(product_+"\n")
  product.close()

def read_courier_file():
  for courier_ in courier_list:
    courier.write(courier_+"\n")
  courier.close()


def main_menu():
    print("Welcome to my Cafe, Please pick the options below")

    print("***MAIN MENU***")
    command_ = int(input("0===>EXIT\n1===>PRODUCT MENU\n2===>COURIER MENU:"))
    while True:
      if command_ == 0:
        read_file()
        read_courier_file()
        exit()
      
      elif command_ == 1:
        main_menu_options()
     
      elif command_==2:
        courier_main_menu()
    
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
            
            



def courier_main_menu():
   print("***COURIER MAIN MENU***")
   command_courier = int(input("2===>COURIER EDIT\n0===>RETURN MAIN MENU\n:"))
   while True:
    if command_courier == 2:
      print(courier_list)
      courier_menu_option()
      break
    elif command_courier == 0:
      main_menu()
  
    


def courier_menu_option():
  print("***COURIER MENU***")
  user_courier = int(input("RETURN COURIER MAIN MENU:0\nSHOW COURIER:1\nADD COURIER:2\nUPDATE COURIER:3\nDELETE COURIER:4\n:")) 
  while True:

    if user_courier == 0:
            courier_main_menu()
          
                                 
        
    elif user_courier == 1:
      print(courier_list)
      break
               
        
    elif user_courier == 2:
            add_courier = input("ADD COURIER\n")
            courier_list.append(add_courier)
           
            added_courier= input("Continue Adding\ny/n\n")
            while added_courier == "y":
              courier_menu_option()
            print(courier_list)
            main_menu()
            

    elif user_courier == 3:
            print(courier_list)          
            for update in range(len(courier_list)):
               
                update_courier = int(input("Which position number you want to change\n:"))
                break
            courier_list[update_courier] = str(input("UPDATE COURIER\n"))
            print(f"COURIER UPDATED:  {courier_list[update_courier]}")
            updated_courier = input("Cotinue updating\ny/n\n")
            while updated_courier =="y":
              courier_menu_option()
            print(courier_list)
            main_menu()
            
            
            

    elif user_courier == 4:
            for delete in range(len(courier_list)):
                delete_courier = int(input("Input postion to delete: "))
                del courier_list[delete_courier]
                break
            del_courier = input("Continue deleting\ny/n\n")
            while del_courier=="y":
              courier_menu_option()
            print(courier_list)
            main_menu()
main_menu()