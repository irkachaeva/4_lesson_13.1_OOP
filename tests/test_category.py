import pytest
from src.category import Category

'''Тест для класса Category'''
@pytest.fixture
def category_ball():
    return Category('Ball', 'Мяч для игры в футбол', ['Nike', 'adidas', 'Polo'])


def test_init_category(category_ball):
    assert category_ball.name == 'Ball'
    assert category_ball.description == 'Мяч для игры в футбол'
    assert category_ball.products == ['Nike', 'adidas', 'Polo']
    assert category_ball.count_uniq_category == 3