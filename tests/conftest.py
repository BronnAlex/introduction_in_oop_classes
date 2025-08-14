import pytest
from src.product import Product, Category
from src.successor_classes_product import Smartphone, LawnGrass


@pytest.fixture
def class_products():
    return Product(
        name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5
    )


@pytest.fixture
def class_products_2():
    return Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)


@pytest.fixture
def category():
    return Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        products=[
            Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
            Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        ],
    )


@pytest.fixture
def category_not_empty_product():
    return Category(
        "Супер смартфоны",
        "Супер смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни",
    )


# Создал одну фикстуру на класс наследник по категории смартфонов и ее дважды исп в тесте сложения
@pytest.fixture
def smartphone_product():
    return Smartphone(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5, 95.5, "S23 Ultra", 256, "Серый"
    )


# Создал одну фикстуру на класс наследник по категории газонной травы и ее дважды исп в тесте сложения
@pytest.fixture
def lawngrass_product():
    return LawnGrass("Газонная трава", "Элитная трава для газона", 500.0, 20, "Россия", "7 дней", "Зеленый")
