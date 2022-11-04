products = []
couriers = []
orders = [{
 "customer_name": "John",
 "customer_address": "Unit 2, 12 Main Street, LONDON, WH1 2ER",
 "customer_phone": "0789887334",
 "status": "preparing"
},{
 "customer_name": "Patrick",
 "customer_address": "10 Dowing St, LONDON, SW1A 2AA",
 "customer_phone": "0769696969",
 "status": "preparing"
},
]

# def print_list():
#   print()
#   for i in products:
#     print(i)

# print_list()

def new_product():
  new_product = input("New Prouduct? ")
  if new_product:
    confirm = int(input(f'Would you like to add {new_product}\n1: Yes\n2: No\n'))
    if confirm == 1:
      products.append(new_product.title())
  print(products)

def updating_product():
  print(products)
  update_product = input("Which product would you like to update? \nUse Index Number ")
  if update_product:
    change = input(f'What produt would you like to change {products[int(update_product)]} to? \n>>>')
    products[int(update_product)] = change.title()
  print(products)

def delete_product():
  print(products)
  delete_product = input("Which Product would you like to delete? \nUse Index Number ")
  if delete_product:
    confirm = int(input(f'Would you like to delete {products[int(delete_product)]}\n1: Yes\n2: No\n'))
    if confirm == 1:
      products.pop(int(delete_product))
  print(products)

def customer_inputs():
  customer_name = input("Customer Name? ")
  customer_address = input("Customers Address? ")
  customer_phone = input("Customers Phone Number? ")
  orders.append({
        "customer_name": customer_name,
        "customer_address": customer_address,
        "customer_phone": customer_phone,
        "status": "preparing"
        })
  for i in orders:
    print(i)

def update_status():
  for i,j in enumerate(orders):
    print(f'{i}: {j}')
  update_order_status = input("\nWhich order status would you like to update?\nUse Index Number ")
  if update_order_status:
    new_status = input("New Status? ")
    orders[int(update_order_status)]['status'] = new_status
  for i in orders:
    print(i)

def update_order():
  for i,j in enumerate(orders):
    print(f'{i}: {j}')
  update_order = input("What order would you like to update?\nUse Index Number ")
  if update_order:
    customer_name = input("New Customer Name? ")
    customer_address = input("New Customers Address? ")
    customer_phone = input("New Customers Phone Number? ")
    orders[int(update_order)] = {"customer_name": customer_name,
    "customer_address": customer_address,
    "customer_phone": customer_phone,
    "status": "preparing"}

def delete_order():
  for i,j in enumerate(orders):
    print(f'{i}: {j}')
  delete_order = input("What order would you like to delete?\nUse Index Number ")
  if delete_order:
    confirm = int(input(f'Would you like to delete {orders[int(delete_order)]}\n1: Yes\n2: No\n'))
    if confirm == 1:
      del orders[int(delete_order)]

def read_file():
    with open("couriers.txt", "r") as file:
        courier_list = file.readlines()
        for courier in courier_list:
            couriers.append((courier).strip('\n'))
        file.close()

    with open("products.txt", "r") as file:
        product_list = file.readlines()
        for product in product_list:
            products.append((product).strip('\n'))
        file.close()

def write_file():
    with open("couriers.txt", "w") as file:
        for courier in couriers:
            file.write(f'{courier}\n')
        file.close()

    with open("products.txt", "w") as file:
        for product in products:
            file.write(f'{product}\n')
        file.close()

def new_courier():
  new_courier = input("New Courier? ")
  if new_courier:
    confirm = int(input(f'Would you like to add {new_courier} as a Courier\n1: Yes\n2: No\n'))
    if confirm == 1:
      couriers.append(new_courier.title())
  print(couriers)

def updating_courier():
  print(couriers)
  update_courier = input("Which courier would you like to update? \nUse Index Number ")
  if update_courier:
    change = input(f'What produt would you like to change {couriers[int(update_courier)]} to? \n>>>')
    couriers[int(update_courier)] = change.title()
  print(couriers)

def delete_courier():
  print(couriers)
  delete_courier = input("Which courier would you like to delete? \nUse Index Number ")
  if delete_courier:
    confirm = int(input(f'Would you like to delete {couriers[int(delete_courier)]}\n1: Yes\n2: No\n'))
    if confirm == 1:
      couriers.pop(int(delete_courier))
  print(couriers)