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

def get_categories_products():
    for items in get_info(data):
        products = []
        category = Category(items["name"], items["description"], items["products"])
        categories.append(category)
        for element in items['products']:
            product = Product(element["name"], element["description"],
                              element["price"], element["quantity"])
            products.append(product)

    return [category, product]
