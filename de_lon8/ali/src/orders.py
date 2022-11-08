import json
class Orders:
    list = []
    def __init__(self):
        self.read_file()

    def add_ordert(self, name):
        self.list.append(name)

    def update_order(self,indx,list):
        self.list[indx] = list

    def is_order_exist(self,index):
        for indx, l in enumerate(self.list):
            if index == indx:
                return l
            else:
                return "none"

    def del_order(self,indx):
        self.list.pop(indx)
        

    def display_order(self):
        print("No  Name  Address  Phone  Status")
        for index,name in enumerate(self.list):
            # name = dict(name)
            # print(f"{index})  "+name["customer_name"]+"  "+name["customer_address"]+"  "+name["customer_phone"]+"  "+name["status"])
            print(f"{index})  {name.value('customer_name')}  {name.value('customer_address')}  {name.value('customer_phone')}  {name.value('status')}")

    def get_order(self):
        return self.list
    
    def read_file(self):
        with open("data/orders.txt") as f:
            data = f.readlines()
            self.list = data
            # js = json.load(data)
            # for x in js:
            #     self.list.append(x)
                
        f.close
    def write_into_file(self):
        f = open("data/orders.txt", "w")
        f.writelines(self.list)
        # for x in self.list:
        #     f.write(f"{x}\n")
        f.close() 