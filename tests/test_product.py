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
