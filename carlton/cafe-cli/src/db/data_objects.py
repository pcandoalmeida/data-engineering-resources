from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass(kw_only=True, slots=True)
class Order:
    name: str
    address: str
    phone: int
    status: str = field(init=False, default="Preparing")


@dataclass(kw_only=True, slots=True)
class Product:
    name: str


@dataclass(kw_only=True, slots=True)
class Courier:
    name: str


# TODO: Move data update responsibilites
#       to the data object to support abstraction
#       for DataList inheritance.
class DataList(ABC):
    @abstractmethod
    def add_data(self):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def update_data(self):
        pass

    @abstractmethod
    def delete_data(self):
        pass


class OrderList(DataList):
    def __init__(self) -> None:
        self.list = []

    def add_data(self, *, order: Order) -> None:
        self.list.append(order)

    def get_data(self, *, target: int) -> Order:
        return self.list[target]

    @staticmethod
    def update_data(*, order: Order, **kwargs) -> None:
        for key in kwargs:
            if not getattr(order, kwargs[key]):
                continue

            setattr(order, key, kwargs[key])

    def delete_data(self, *, target: int) -> None:
        self.list.pop(target)

    def __repr__(self) -> str:
        if not self.list:
            return "No Data Available!\n"

        data_str = ""
        for num, data in enumerate(self.list, 1):
            data_str += f"""{num}) Name: {data.name}
                              \r   Address: {data.address}
                              \r   Phone: {data.phone}
                              \r   Status: {data.status}\n"""
        return data_str.title()


class ProductList(DataList):
    def __init__(self) -> None:
        self.list = []

    def add_data(self, *, product: Product) -> None:
        self.list.append(product)

    def get_data(self, *, target: int) -> Product:
        return self.list[target]

    @staticmethod
    def update_data(*, product: Product, **kwargs) -> None:
        for key in kwargs:
            if not getattr(product, kwargs[key]):
                continue

            setattr(product, key, kwargs[key])

    def delete_data(self, *, target: int) -> None:
        self.list.pop(target)

    def __repr__(self) -> str:
        if not self.list:
            return "No Data Available!\n"

        data_str = ""
        for num, data in enumerate(self.list, 1):
            data_str += f"{num}) {data.name}\n"
        return data_str.title()


class CourierList(DataList):
    def __init__(self) -> None:
        self.list = []

    def add_data(self, *, courier: Courier) -> None:
        self.list.append(courier)

    def get_data(self, *, target: int) -> Courier:
        return self.list[target]

    @staticmethod
    def update_data(*, courier: Courier, **kwargs) -> None:
        for key in kwargs:
            if not getattr(courier, kwargs[key]):
                continue

            setattr(courier, key, kwargs[key])

    def delete_data(self, *, target: int) -> None:
        self.list.pop(target)

    def __repr__(self) -> str:
        if not self.list:
            return "No Data Available!\n"

        data_str = ""
        for num, data in enumerate(self.list, 1):
            data_str += f"{num}) {data.name}\n"
        return data_str.title()
