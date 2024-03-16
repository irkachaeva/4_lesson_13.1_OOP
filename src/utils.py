import json
import os
from src.category import Category
from src.product import Product

data = 'products.json'
list_category = []

def get_info(data):
    filepath = os.path.join(os.path.dirname(__file__), data)
    with open(filepath, encoding='UTF-8') as file:
        content = json.loads(file.read()) #Строковое представление файла
    return content

def get_categories_products():
    for items in get_info(data):
        category = Category(items["name"], items["description"], items["products"])

        for element in items['products']:
            product = Product(element["name"], element["description"],
                              element["price"], element["quantity"])

    return [category, product]
