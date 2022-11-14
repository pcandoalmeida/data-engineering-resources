
from functions_menu import main_menu, product_menu, orders_menu,courier_menu

"""

importing all my other files, then create classes & methods to make the app 



"""
class MyCafe:
    def __init__(self, mainmenu, productmenu,courier,ordersmenu):
        self.mainmenu = mainmenu
        self.productmenu = productmenu
        self.courier = courier
        self.ordersmenu = ordersmenu
    
    def get_mainmenu(self):
        main_menu()

    def get_productmenu(self):
        product_menu()

    def get_courier(self):
        courier_menu()

    def get_ordersmenu(self):
        orders_menu()

   

        

MyCafe()


