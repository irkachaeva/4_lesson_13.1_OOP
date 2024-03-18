
class Product:
    name: str #название
    description: str #описание
    price: float #цена
    quantity_stock: int #количество в наличии


    def __init__(self, name, description, price, quantity_stock):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity_stock = quantity_stock

    @classmethod
    def new_product(cls, name: str, description: str, price: float, quantity_stock: int):
        '''создание нового товара'''
        new_product = cls(name, description, price, quantity_stock)
        return new_product

    '''геттер для атрибута цены.'''
    @property
    def price(self):
        return self.__price

    '''cеттер для атрибута цены. В случае если цена равна или ниже нуля, выводится сообщение в консоль, при этом новая цена не устанавливается.'''
    @price.setter
    def price(self, new_price):
        if new_price <= 0:
            print("Введена некорректная цена")
        else:
            self.__price = new_price #устанавливаем цену, если она удовлетворяет условию выше
