
from cafe_data import products

def open_menu():
    for view_products in products:
        print(view_products)
    

def add_item():
    new_item = input("""
    Please Add Item
    >>>>
    """)
    add_price = float(input("""
    Please Add Item Price
    >>>>
    """))
    new_product = {}
    new_product["name"] = new_item
    new_product["price"] = add_price
    
    
    products.append(new_product)
    
    print(f"The item you added is {new_item}, £{add_price} ")
    for i in products:
        print(i)
   
    #sort this out make it flow better , user friendly 
  
def update_item():
    for product_index , value in enumerate(products):
        print(product_index, value)
    update_product = input("""
    Please use the index to pick a product to update
    >>>>
    """)
    if update_product:
        new_name = input("New product name? ")
        new_price = float(input("New Price?"))
        products[int(update_product)]["name"] = new_name
        products[int(update_product)]["price"] = new_price
    for product in products:
        print(product)
    
def delete_product():
    for product_index , value in enumerate(products):
        print(product_index, value)
    product_delete = input("""
    Please use the index to pick a product to delete
    >>>>
    """)
    if product_delete:
        del products[int(product_delete)]
    for product in products:
        print(product)
        
