import pytest
from src.product import Product, Category


@pytest.fixture
def class_products():
    return Product(
        name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5
    )


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
        "Супер смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
    )
