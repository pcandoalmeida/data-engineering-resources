product_list = ['Snickers', 'Kit Kat', 'Mars', 'Bueno', 'Ritter']

cmd = input('Welcome to the product manager 2000!'
            ' Would you like to manage the products? 1 for Yes or 2 for No ').split(' ')
while cmd[0] != '2':
    choice = input("""
                  1: Show Products
                  2: Add products
                  3: Delete products
                  4: Change product
                  5: Exit to main menu

                  Please enter your choice: """)
    if choice == "1":
        print(product_list)
    elif choice == "2":
        print('What is the name of the new product? ')
        item = input()
        product_list.append(item)
        print(product_list)
    elif choice == "3":
        print(product_list)
        for product in range(len(product_list)):
            print(f'[{product}] {product_list[product]}')
        to_delete = int(input("Please choose the number of the product you'd like to delete: "))
        print(f"You have selected {product_list[to_delete]}")
        product_list.pop(to_delete)
        print(product_list)
        
    elif choice == "4":
        for i in range(len(product_list)):
            print(f'[{i}] {product_list[i]}')
        to_change = int(input('Please choose the product from the available options. '))
        print(f'You have selected {product_list[to_change]}: ')
        product_list[to_change] = input('Enter the new product name: ')
        print(product_list)
    elif choice == "5":
        cmd = input('Welcome to the product manager 2000!'
                    ' Would you like to manage the products? 1 for Yes or 2 for No ').split(' ')
    else:
        print("You must only select either 1, 2, 3, 4 or 5")
        print("Please try again")

print('Miss you already!')

# def signup():
#     email = input("Please enter your email address: ")
#     pwd = input("Please enter a password: ")
#     conf_pwd = input("Confirm password: ")

#     if conf_pwd == pwd:
#         enc = conf_pwd.encode()
#         hash1 = hashlib.md5(enc).hexdigest()

#     with open("credentials.txt", "w+") as f:
#         f.write(email + "\n")
#         f.write(hash1)
#     f.close()
#     print("You have registered successfully!")

#     # else:
#     #     print("Passwords don't match! Please try again.\n")

# def login():
#     email = input("Enter your email: ")
#     pwd = input("Enter password: ")
#     auth = pwd.encode()
#     auth_hash = hashlib.md5(auth).hexdigest()
#     with open("credentials.txt", "r") as f:
#         stored_email, stored_pwd = f.read().split("\n")
#     f.close()
#     if email == stored_email and auth_hash == stored_pwd:
#         print("Logged in Successfully!")
#     else:
#         print("Login failed! \n")
# while 1:
#     print("********** Login System **********")
#     print("1.Signup")
#     print("2.Login")
#     print("3.Exit")
#     ch = int(input("Enter your choice: "))
#     if ch == 1:
#         signup()
#     elif ch == 2:
#         login()
#     elif ch == 3:
#         break
#     else:
#         print("Wrong Choice!")

#print("Welcome to Sajid's delivery service! \n Please sign up before you begin your order.")

# print(signup())
# print(login())
# print(f"Hi {email}!")