import json
#LOAD products list from products.txt
productsFile = open('/Users/ciarrabalsomo/Desktop/Data Engineering/VVVS Code/Generation Project Work/Project Work/products.txt', 'r')
productsLine = productsFile.readlines()
products = []

for p_line in productsLine:
    p_line = p_line.strip()
    products.append(p_line)


#LOAD couriers list from couriers.txt
courierFile = open('couriers.txt', 'r')
courierLine = courierFile.readlines()
courier = []
for c_line in courierLine:
    c_line = c_line.strip()
    courier.append(c_line)


# #LOAD orders list from orders.txt
# ordersFile = open('/Users/ciarrabalsomo/Documents/Data Engineering/VVVS Code/Generation Project Work/Project Work/orders.json', 'r')
# orders = json.load(ordersFile)


selection = 0
    
#Printing the main menu
print('Welcome to the main menu')
while selection == 0 :
    print('')
    print('MENU')
    print('To EXIT the program select 0')
    print('To enter the PRODUCTS MENU select 1')
    print('To enter the ORDERS MENU select 2')
    print('To enter the COURIERS MENU select 3')
    
    #Get the choice from the main menu

    #Save everything for both files and then exit the APP
    print('')
    choice = (int(input('What is your choice: ')))
    if choice == 0:
        productsFile = open('products.txt', 'w')
        productsFile.write('\n'.join(products))
        productsFile.close()

        courierFile = open('couriers.txt', 'w')
        courierFile.write('\n'.join(courier))
        courierFile.close()

        ordersFile = open('orders.json', 'w')
        json.dump(orders, ordersFile)
        ordersFile.close()

        break

   
    elif choice == 1:
        while True:
            print ('')
            print ('')
            print ('PRODUCTS MENU')
            print ('0. Return to the MAIN MENU.')
            print ('1. To PRINT all products')
            print ('2. To CREATE a new product') 
            print ('3. To UPDATE a product')
            print ('4. To DELETE a product')
            print('')
            
            #Taking an input for the products menu
            product_menu_choice = int(input(''))

            #Exit out of the product menu
            if product_menu_choice == 0:
                break
            
            #Takes everyproduct and prints it to a new line.
            if product_menu_choice == 1:
                print(products)

            
            #Creating new items in the list. 
            elif product_menu_choice == 2:

                #Code here verifys the correct spelling and puts everything into a lower case format.
                print('') 
                new_item = input('Please enter the name of the item that you would like to add: ')
                newitem = new_item.lower()
                products.append(newitem)
                    

            #This updates the product list 
            elif product_menu_choice == 3:

                item_number = 0
                for i in products:
                    print (item_number, ':', i)
                    item_number = item_number + 1

                to_amend = int(input('Which item number would you like to change?: '))
                amended_item = input('What would you like to change this to?: ')

                products[to_amend] = amended_item
                
                print(products)


            #This will delete something from the list using the index number.
            elif product_menu_choice == 4:
                item_number = 0
                for i in products:
                    print (item_number, ':', i)
                    item_number = item_number + 1
                
                item_finder = int(input('Insert the item number that you would like to delete: '))
                del products[item_finder]
                print ('Your item has been deleted.')
                print (products)

    elif choice == 3:
        while True:
            print ('')
            print ('')
            print ('COURIERS MENU')
            print ('0. Return to the MAIN MENU.')
            print ('1. To PRINT all couriers')
            print ('2. To CREATE a new courier') 
            print ('3. To UPDATE a courier')
            print ('4. To DELETE a courier')
            print('') 

            #Taking an input for the products menu
            courier_menu_choice = int(input(''))

            #Exit out of the product menu
            if courier_menu_choice == 0:
                break
            
            #Takes everyproduct and prints it to a new line.
            if courier_menu_choice == 1:
                print(courier)

            
            #Creating new items in the list. 
            elif courier_menu_choice == 2:

                #Code here verifys the correct spelling and puts everything into a lower case format.
                print('') 
                new_courier = input('Please enter the name of the item that you would like to add: ')
                newcourier = new_courier.lower()
                courier.append(newcourier)
                    

            #This updates the product list 
            elif courier_menu_choice == 3:

                courier_number = 0
                for i in courier:
                    print (courier_number, ':', i)
                    courier_number = courier_number + 1

                to_amend = int(input('Which item number would you like to change?: '))
                amended_courier = input('What would you like to change this to?: ')

                courier[to_amend] = amended_courier
                
                print(courier)


            #This will delete something from the list using the index number.
            elif courier_menu_choice == 4:
                courier_number = 0
                for i in courier:
                    print (courier_number, ':', i)
                    courier_number =  courier_number + 1
                
                courier_finder = int(input('Insert the item number that you would like to delete: '))
                del courier[courier_finder]
                print ('Your item has been deleted.')
                print (courier)


    # if choice == 2:
    #     while True:
    #         print ('')
    #         print ('')
    #         print ('ORDERS MENU')
    #         print ('0. Return to the MAIN MENU.')
    #         print ('1. To PRINT all orders')
    #         print ('2. To CREATE a new order') 
    #         print ('3. To UPDATE an order')
    #         print ('4. To DELETE an order')
    #         print('') 

    #         orders_menu_choice = int(input(''))

    #         if orders_menu_choice == 0:
    #             break

    #         elif orders_menu_choice == 1:
    #             print(orders)

    #         elif orders_menu_choice == 2:
    #             order_name = input('Please enter the customer name: ')
    #             order_address = (input('Enter the address number: '))
    #             order_phone_number = input('Please enter the phone number: ')
    #             order_status = 'PREPARING'
                
    #             single_order = {'Name': order_name, 'Address' : order_address, 'Phone Number' : order_phone_number, 'Status' : order_status}

    #             orders.append(single_order)

    #         elif orders_menu_choice == 3:
    #             y = json.loads(orders)
    #             print(y)

    #         elif orders_menu_choice == 4:
    #             print('')
                
    #         elif orders_menu_choice == 5:
    #             print('')

