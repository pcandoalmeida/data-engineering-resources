#!/usr/bin/env python3
import db
from menu import Menu, MenuController
from menu import default_console as console


class MainMenu(Menu):
    def __init__(self) -> None:
        self._options = (
            "Manage Orders",
            "Manage Products",
            "Manage Couriers",
            "Exit Application",
        )

    def run(self, cmd: str = "") -> str | None:
        while True:
            cmd = console.input("[prompt]>>> ")
            if cmd == "0":
                break
            elif cmd == "1":
                return "order_menu"
            elif cmd == "2":
                return "product_menu"
            elif cmd == "3":
                return "courier_menu"
            else:
                console.clear()
                console.print("[warn]Invalid Input!\n")

            console.print(self)


class ProductMenu(Menu):
    def __init__(self, *, parent_menu: Menu, data: db.ProductList) -> None:
        self._options = (
            "Display Products",
            "Add New Product",
            "Update Product",
            "Delete Product",
            "Main Menu",
        )
        self.parent_menu = parent_menu
        self.data = data

    def run(self, cmd: str = "") -> None:
        while True:
            cmd = console.input("[prompt]>>> ")
            if cmd == "0":
                break
            elif cmd == "1":
                console.clear()
                console.print(self.data)
            elif cmd == "2":
                console.print("[notify]Enter Product Name:\n")
                new_product = db.Product(name=console.input("[prompt]>>> "))
                self.data.add_data(product=new_product)
                console.clear()
                console.print("[notify]Product Added!\n")
            elif cmd == "3":
                console.clear()
                console.print("[warn]Not Yet Implemented!\n")
            elif cmd == "4":
                console.clear()
                console.print("[warn]Not Yet Implemented!\n")
            else:
                console.clear()
                console.print("[warn]Invalid Input!\n")

            console.print(self)


class CourierMenu(Menu):
    def __init__(self, *, parent_menu: Menu, data: db.CourierList) -> None:
        self._options = (
            "Display Couriers",
            "Add New Courier",
            "Update Courier",
            "Delete Courier",
            "Main Menu",
        )
        self.parent_menu = parent_menu
        self.data = data

    def run(self, cmd: str = "") -> None:
        while True:
            cmd = console.input("[prompt]>>> ")
            if cmd == "0":
                break
            elif cmd == "1":
                console.clear()
                console.print(self.data)
            elif cmd == "2":
                console.print("Enter Courier Name:\n")
                new_courier = db.Courier(name=input(">>> ").lower())
                self.data.add_data(courier=new_courier)
                console.clear()
                console.print("Courier Added!\n")
            elif cmd == "3":
                console.clear()
                console.print("[warn]Not Yet Implemented!\n")
            elif cmd == "4":
                console.clear()
                console.print("[warn]Not Yet Implemented!\n")
            else:
                console.clear()
                console.print("[warn]Invalid Input!\n")

            console.print(self)


class OrderMenu(Menu):
    def __init__(self, *, parent_menu: Menu, data: db.OrderList) -> None:
        self._options = (
            "Display Orders",
            "Add New Order",
            "Update Order",
            "Update Status",
            "Delete Order",
            "Main Menu",
        )
        self.parent_menu = parent_menu
        self.data = data

    def run(self, cmd: str = "") -> None:
        while True:
            cmd = console.input("[prompt]>>> ")
            if cmd == "0":
                break
            elif cmd == "1":
                console.clear()
                console.print(self.data)
            elif cmd == "2":
                console.print("Enter Client Name:\n")
                name = input(">>> ")
                console.print("Enter Client Address:\n")
                address = input(">>> ")
                while True:
                    try:
                        console.print("Enter Client Phone Number:\n")
                        phone = int(input(">>> "))
                    except ValueError:
                        console.print("Invalid Input!\n")
                    else:
                        break
                new_order = db.Order(name=name, address=address, phone=phone)
                self.data.add_data(order=new_order)
                console.clear()
                console.print("Order Added!\n")
            elif cmd == "3":
                console.clear()
                console.print("[warn]Not Yet Implemented!\n")
            elif cmd == "4":
                console.clear()
                console.print("[warn]Not Yet Implemented!\n")
            elif cmd == "5":
                console.clear()
                console.print("[warn]Not Yet Implemented!\n")
            else:
                console.clear()
                console.print("[warn]Invalid Input!\n")

            console.print(self)


def cafe_factory() -> MenuController:
    product_data = db.ProductList()
    courier_data = db.CourierList()
    order_data = db.OrderList()
    main_menu = MainMenu()

    return MenuController(
        main_menu=main_menu,
        product_menu=ProductMenu(parent_menu=main_menu, data=product_data),
        courier_menu=CourierMenu(parent_menu=main_menu, data=courier_data),
        order_menu=OrderMenu(parent_menu=main_menu, data=order_data),
    )


def main() -> None:
    with console.status("[warn]Loading Data..."):
        controller = cafe_factory()

    while True:
        console.clear()
        controller.print()
        menu = controller.current_menu.run()
        if not menu:
            controller.prev_menu()
        else:
            controller.next_menu(menu)


if __name__ == "__main__":
    main()
