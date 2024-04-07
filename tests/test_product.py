import pytest
from src.product import Product
from src.product import Smartphone
from src.product import LawnGrass

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

@pytest.fixture
def product_smartphone():
    return Smartphone("Iphone 15",{"description": "512GB, Gray space"},210000.0,8, 'Turbo', '15 classic', 256, 'pink')
@pytest.fixture
def product_smartphone2():
    return Smartphone("Mi",{"description": "512GB, Gray space"},210000.0,10, 'Turbo', '15 classic', 256, 'pink')

def test_add_prise_quantity(product_f, product_smartphone, product_smartphone2):
    assert product_smartphone+product_smartphone2 == 3780000.0
    with pytest.raises(TypeError):
        product_f + product_smartphone


def test_zero_quantity(product_4):
    with pytest.raises(ValueError, match='Tовар с нулевым количеством не может быть добавлен.'):
        product_4.new_product("Iphone 10",{"description": "512GB, Gray space"},210000.0,0)