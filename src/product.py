
class Product:
    name: str #название
    description: str #описание
    price: float #цена
    quantity_stock: int #количество в наличии


    def __init__(self, name, description, price, quantity_stock):
        self.name = name
        self.description = description
        self.price = price
        self.quantity_stock = quantity_stock