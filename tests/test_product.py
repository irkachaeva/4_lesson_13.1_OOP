import pytest
from src.product import Product

'''Тест для класса Product'''
@pytest.fixture
def product_f():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

def test_init_product(product_f):
    assert product_f.name == "Samsung Galaxy C23 Ultra"
    assert product_f.description == "256GB, Серый цвет, 200MP камера"
    assert product_f.price == 180000.0
    assert product_f.quantity_stock == 5

@pytest.fixture
def product_3():
    return Product("iPhone", "smth", 1000, 32)

def test_get_price(product_3):
    product_3.price = 1000
    assert product_3.price == 1000

@pytest.fixture
def product_4():
    return Product("Iphone 15",{"description": "512GB, Gray space"},210000.0,8)

def test_str(product_4):
    assert str(product_4) == 'Iphone 15 210000.0руб. Остаток: 8 шт.'


def test_add_prise_quantity(product_4, product_f):
    assert product_4 + product_f == 2580000.0

