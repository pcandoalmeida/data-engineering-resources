class Couriers:
    list = []
    def __init__(self):
        self.read_file()

    def add_product(self, name):
        self.list.append(name)

    def update_product(self,indx,name):
        self.list[indx] = name

    def is_product_exist(self,name):
        for indx, l in enumerate(self.list):
            if name == l:
                return indx
            else:
                return "none"

    def del_product(self,name):
        if name in self.list:
            self.list.remove(name)
        

    def display_products(self):
        for l in self.list:
            print(l)

    def get_products(self):
        return self.list
    
    def read_file(self):
        f = open("data/couriers.txt", "r")
        f1 = f.readlines()
        for x in f1:
            self.list.append(x[:-1])
        f.close
    def write_into_file(self):
        f = open("data/couriers.txt", "w")
        for x in self.list:
            f.write(x+"\n")
        f.close() 