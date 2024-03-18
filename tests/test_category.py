import pytest
from src.category import Category

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
    return Category('Ball', 'Мяч для игры в футбол', [{
        "name": "Iphone 15",
        "description": "512GB, Gray space",
        "price": 210000.0,
        "quantity": 8}])

def test_product_list(category_2):
    assert category_2.product_list == 'Iphone 15, 210000.0 руб. 8 шт.'