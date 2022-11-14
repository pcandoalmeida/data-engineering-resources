from cafe_data import product_list
from functions import main_menu

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