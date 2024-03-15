import pytest
from src.classes import Category, Product
'''Тест для класса Category'''
@pytest.fixture
def category_ball():
    return Category('Ball', 'Мяч для игры в футбол', ['Nike', 'adidas', 'Nike'])


def test_init_category(category_ball):
    assert category_ball.name == 'Ball'
    assert category_ball.description == 'Мяч для игры в футбол'
    assert category_ball.products == ['Nike', 'adidas', 'Nike']
    assert category_ball.count_uniq_category == 1


'''Тест для класса Product'''
@pytest.fixture
def product_f():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

def test_init_product(product_f):
    assert product_f.name == "Samsung Galaxy C23 Ultra"
    assert product_f.description == "256GB, Серый цвет, 200MP камера"
    assert product_f.price == 180000.0
    assert product_f.quantity_stock == 5
