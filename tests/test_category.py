import pytest
from src.category import Category
from src.category import Product

'''Тест для класса Category'''
@pytest.fixture
def category_ball():
    return Category('Ball', 'Мяч для игры в футбол', ['Nike', 'adidas', 'Polo', "ololo"])


def test_init_category(category_ball):
    assert category_ball.name == 'Ball'
    assert category_ball.description == 'Мяч для игры в футбол'
    assert category_ball.get_products() == ['Nike', 'adidas', 'Polo', "ololo"]
    assert category_ball.count_uniq_category == 4


def test_add_category():
    assert Category.add_category('test') == ['test']


@pytest.fixture
def category_2():
    iphone = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    return Category('Ball', 'Мяч для игры в футбол', [iphone])


def test_product_list(category_2):
    assert category_2.product_list == ['Iphone 15, 210000.0 руб. Остаток: 8 шт.']


@pytest.fixture()
def category_4():
    iphone = Product("Iphone 15","512GB, Gray space", 210000.0, 8)
    samsung = Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    return Category('Ball', 'Мяч для игры в футбол', [iphone, samsung])


def test_product_str_len(category_4):
    assert str(category_4) =='Ball, количество продуктов:13 шт.'