from cafe_data import orders, products, courier_dict
import csv 
key_products = products[0].keys()

key_courier = courier_dict[0].keys()
key_order = orders[0].keys()


def products_menu_file():
    with open('products.csv', 'w+', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, key_products)
        dict_writer.writeheader()
        dict_writer.writerows(products)
    

def courier_file():
    with open('courier.csv', 'w+', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, key_courier)
        dict_writer.writeheader()
        dict_writer.writerows(courier_dict) #--> debug 
    

def orders_menu_file():

    with open('orders.csv', 'w+', newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, key_order)
        dict_writer.writeheader()
        dict_writer.writerows(orders)
    



    