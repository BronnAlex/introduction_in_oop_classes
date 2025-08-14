import pytest


def test_smartphone_init(smartphone_product):
    """Тест инициализации атрибутов экземпляра класса наследника смартфонов"""
    assert smartphone_product.name == "Samsung Galaxy S23 Ultra"
    assert smartphone_product.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone_product.private_price == 180000.0
    assert smartphone_product.quantity == 5
    assert smartphone_product.efficiency == 95.5
    assert smartphone_product.model == "S23 Ultra"
    assert smartphone_product.memory == 256
    assert smartphone_product.color == "Серый"


def test_lawngrass_init(lawngrass_product):
    """Тест инициализации атрибутов экземпляра класса наследника газонной травы"""
    assert lawngrass_product.name == "Газонная трава"
    assert lawngrass_product.description == "Элитная трава для газона"
    assert lawngrass_product.private_price == 500.0
    assert lawngrass_product.quantity == 20
    assert lawngrass_product.country == "Россия"
    assert lawngrass_product.germination_period == "7 дней"
    assert lawngrass_product.color == "Зеленый"


def test_classes_smartphone_add(smartphone_product):
    """Тестирование магического метода сложения суммы общего количесва и цены смартфонов"""
    assert smartphone_product + smartphone_product == 1_800_000.0


def test_classes_smartphone_add_error(smartphone_product):
    """Тестирование магического метода сложения суммы на ошибку в наследнике смартфонов"""
    with pytest.raises(TypeError):
        smartphone_product + 1


def test_classes_lawngrass_add(lawngrass_product):
    """Тестирование магического метода сложения суммы общего количесва и цены газонной травы"""
    assert lawngrass_product + lawngrass_product == 20_000.0


def test_classes_lawngrass_add_error(lawngrass_product):
    """Тестирование магического метода сложения суммы на ошибку в наследнике смартфонов"""
    with pytest.raises(TypeError):
        lawngrass_product + 1
