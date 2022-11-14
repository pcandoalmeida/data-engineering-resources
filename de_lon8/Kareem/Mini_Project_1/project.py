#Creating a new item
def createNew():
    new_addition = input('')
    new_addition = new_addition.lower()
    if new_addition == '':
        print('You cannot have an empty value.')
    else:
        return new_addition


#LOAD products list from products.txt
productsFile = open('products.txt', 'r')
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

    #The above can be replace with a functions to not be repeating 

# An empty list to append the orders
orders = []



selection = 0
    
#Printing the main menu
#Put the below on one line 
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
                print(products) #rename this pring products list

            
            #Creating new items in the list. 
            elif product_menu_choice == 2:

                #Code here verifys the correct spelling and puts everything into a lower case format.
                print('Please enter the name of the product that you would like to add.')
                newitem = createNew()
                products.append(newitem)
                    

            #This updates the product list 
            elif product_menu_choice == 3:

                item_number = 0
                for i in products:
                    print (item_number, ':', i) #change the name i to something else that is named better
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
                print('Please enter the name of the courier that you would like to add.')
                newcourier = createNew()
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


    if choice == 2:
        while True:
            print ('')
            print ('')
            print ('ORDERS MENU')
            print ('0. Return to the MAIN MENU.')
            print ('1. To PRINT all orders')
            print ('2. To CREATE a new order') 
            print ('3. To UPDATE STATUS')
            print ('4. To UPDATE an order')
            print ('5. To DELETE an order') 

            orders_menu_choice = int(input(''))

            #Return to previous menu
            if orders_menu_choice == 0:
                break
            
            #Prints all orders
            elif orders_menu_choice == 1:
                print(orders)

            #Adding a new order
            elif orders_menu_choice == 2:
                order_name = input('Please enter the customer name: ')
                order_address = (input('Enter the address number: '))
                order_phone_number = input('Please enter the phone number: ')
                order_status = 'PREPARING'
                
                single_order = {'Name': order_name, 'Address' : order_address, 'Phone Number' : order_phone_number, 'Status' : order_status}

                orders.append(single_order)

            #Updating existing orderstatus
            elif orders_menu_choice == 3:
                order_number = 0
                for i in orders:
                    print (order_number, ':', i)
                    order_number = order_number + 1

                to_amend = int(input('Which status would you like to change?: '))
                
                status_progression = ('PREPARING', 'READY')
                progression = 0
                for i in status_progression:
                    print (progression, ':', status_progression[progression])
                    progression = progression + 1

                amended_order = int(input ('What would you like to change the status to?'))

                orders[to_amend]['Status'] = status_progression[amended_order]
                
                print(orders)

            # #This is to update the existing orders
            # elif orders_menu_choice == 4:
            #     order_number = 0
            #     for i in orders:
            #         print (order_number, ':', i)
            #         order_number = order_number + 1
                
            #     orders_updates = ('Name', 'Address', 'Phone Number')
            #     updated_order = int(input('Which one of the inputs would you like to change? '))
                
            #     for key, value in orders[updated_order]:
            #         print (key, value)
                
            
            #This is deleting an entire order from the orders menu
            elif orders_menu_choice == 5:
                order_number = 0
                for i in orders:
                    print (order_number, ':', i)
                    order_number = order_number + 1

                deletingorder = int(input('Which order would you like to delete? '))
                del orders[deletingorder]