from cafe_data import courier_dict

def open_courier():
    for couriers in courier_dict:
        print(couriers)

def add_name():
    new_name= input("""
    Please Add Name
    >>>>
    """)
    new_phone = input("""
    Please Add Phone Number
    >>>>
    """)
    new_courier = {}
    new_courier["name"] = new_name
    new_courier["phone"] = new_phone

    
    courier_dict.append(new_courier)
    
    print(f"The item you added is {new_name}, {new_phone}")
    for i in courier_dict:
        print(i)
    
def update_name():
    for product_index , value in enumerate(courier_dict):
        print(product_index, value)
    update_courier = input("""
    Please use the index to pick a product to update
    >>>>
    """)
    if update_courier:
        new_name = input("New Name? ")
        new_price = input("New Phone Number?")
        courier_dict[int(update_courier)]["name"] = new_name
        courier_dict[int(update_courier)]["phone"] = new_price
    for couriers in courier_dict:
        print(couriers)

def delete_name():
    for courier_index , value in enumerate(courier_dict):
        print(courier_index, value)
    product_delete = input("""
    Please use the index to pick a courier to delete
    >>>>
    """)
    if product_delete:
        del courier_dict[int(product_delete)]
    for couriers in courier_dict:
        print(couriers)
  


