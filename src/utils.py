import json
import os
from src.category import Category
from src.product import Product

data = 'products.json'
categories = []


def get_info(data):
    filepath = os.path.join(os.path.dirname(__file__), data)
    with open(filepath, encoding='UTF-8') as file:
        content = json.loads(file.read()) #Строковое представление файла
    return content


def get_categories():
    categories = []
    for category_data in get_info(data):
        name = category_data['name']
        description = category_data['description']
        products = []
        for product_data in category_data['products']:
            name = product_data['name']
            description = product_data['description']
            price = product_data['price']
            quantity = product_data['quantity']
            product = Product(name, description, price, quantity)
            products.append(product)
        category = Category(name, description, products)
        categories.append(category)
    return categories
