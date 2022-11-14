import csv

def open_file():
    with open(filename) as file:
        lines = csv.reader(file)
        print(lines)

filename = []

def write_file():
    with open(filename) as file:
        fieldnames = ["Product", "Price"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    prod_name = input("Whats the name of the new product? ")
    prod_price = input("Whats the price of the product?: ")
    writer.writerow({"Product": prod_name, "Price": prod_price})