from src.product import Product

class Category:
    name: str #название
    description: str #описание
    products: list #товары

    '''объекты на уровне класса'''
    count_of_category = 0
    count_uniq_category = 0
    products = [] #список товаров на уровне класса


    def __init__(self, name, description, products):
        """Инициализация"""
        self.name = name
        self.description = description
        self.__products = products

        """Атрибуты на уровне класса"""
        Category.count_of_category += 1
        Category.count_uniq_category += len(self.__products)

    def get_products(self):
        """Вывод приватного атрибута"""
        return self.__products

    @classmethod
    def add_category(cls, category):
        """добавление товаров в категорию: метод,
         который принимает на вход объект товара и добавляет его в список"""
        cls.products.append(category)
        return cls.products

    @property
    def product_list(self):
        """геттер, который выводит список товаров в формате: Продукт, 80 руб. Остаток: 15 шт."""
        products_info = []
        for product in self.__products:
            info = f'{product.name}, {product.price} руб. Остаток: {product.quantity_stock} шт.'
            products_info.append(info)
        return products_info

    def __len__(self):
        """строковое отображение в следующем виде:Название категории, количество продуктов: 200 шт."""
        total_stock = 0
        for i in self.__products:
            total_stock += i.quantity_stock
        return total_stock

    def __str__(self):
        return f'{self.name}, количество продуктов:{len(self)} шт.'

    def add_product(self, products):
        '''Функция добавляет в список продуктов новый продукт'''
        if not isinstance(products, Product):
            raise TypeError("Добавлять можно только объекты класса Product или его наследников")
        else:
            self.__products().append(products.__dict__)




