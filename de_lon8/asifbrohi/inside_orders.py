from cafe_data import orders

from cafe_data import products
from cafe_data import courier_dict

def open_order():
    for order in orders:
       print(order)

def add_order():

    new_name = input("""
     Add Name
     >>>>
     """)
    new_address = input("""
     Add Address
     >>>>
     """)
    new_phone = input("""
     Add Phone
     >>>>
     """)
    for products_index, value in enumerate(products):
        print(products_index, value)
    items = input('Enter comma-separated integers: ').split(',')

    
    
    item_string = ','.join(map(str,items))


    for courier_index, courier_value in enumerate(courier_dict):
        print(courier_index, courier_value)
    courer_input = int(input("""
        Add courier number
        >>>>
        """))
    

    new_order = {}
    new_order["customer_name"] = new_name
    new_order["customer_address"] = new_address
    new_order["customer_phone"] = new_phone
    new_order["courier"] = courer_input
    new_order["status"] ="preparing"
    new_order["items"] = item_string

    orders.append(new_order)
    for order_view in orders:
        print(order_view)



def update_order_status():
    for order_index, value in enumerate(orders):
        print(order_index, value)
    update_order_status = input("""
    Please use the index to pick an order to update the status
    >>>>
    """)
    if update_order_status:
        new_order_status = input("""
        New Status?
        >>>>
        """)
    orders[int(update_order_status)]["status"] = new_order_status
    for order in orders:
        print(order)

def update_order():
    for order_index, value in enumerate(orders):
        print(order_index, value)
    update_order = input("""
    Please use the index to pick an order to update
    >>>>
    """)
    if update_order:
        new_name = input(""""
        New Name?
        >>>>
        """)
        new_address = input(""""
        New Address?
        >>>>
        """)
        new_phone =  input(""""
        New Phone?
        >>>>
        """)
        new_courier =  int(input(""""
        New Courier?
        >>>>
        """))
        new_status =  input(""""
        New Status?
        >>>>
        """)
        new_items = input('Enter comma-separated integers: ').split(',')

        new_items= [int(item) for item in new_items]
        new_items = str(new_items)
        orders[int(update_order)]["customer_name"] = new_name
        orders[int(update_order)]["customer_address"] = new_address
        orders[int(update_order)]["customer_phone"] = new_phone
        orders[int(update_order)]["customer_courier"] = new_courier
        orders[int(update_order)]["customer_status"] = new_status
        orders[int(update_order)]["items"] = new_items
        for order in orders:
            print(order)

    



def delete_order():

    for order_index, value in enumerate(orders):
        print(order_index, value)
    order_delete = input("""
    Please use the index to pick a product to delete
    >>>>
    """)
    if order_delete:
        del orders[int(order_delete)]
    for order in orders:
        print(order)
  

    
