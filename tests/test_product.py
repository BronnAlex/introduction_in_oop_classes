def test_product_init(class_products):
    assert class_products.name == "Samsung Galaxy S23 Ultra"
    assert class_products.description == "256GB, Серый цвет, 200MP камера"
    assert class_products.price == 180000.0
    assert class_products.quantity == 5


def test_category_init(category, category_not_empty_product):
    assert category.name == "Смартфоны"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category.product_count == 2
    assert category.category_count == 2
    assert len(category.products) == 2


def test_category_not_empty_product_init(category_not_empty_product):
    assert category_not_empty_product.name == "Супер смартфоны"
    assert (
        category_not_empty_product.description
        == "Супер смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category_not_empty_product.product_count == 2
    assert category_not_empty_product.category_count == 3
    assert len(category_not_empty_product.products) == 0


def test_type_data_category(category):
    assert type(category.name) == str
    assert type(category.description) == str
    assert type(category.products) == list
    assert type(category.category_count) == int
    assert type(category.product_count) == int


def test_type_data_product(class_products):
    assert type(class_products.name) == str
    assert type(class_products.description) == str
    assert type(class_products.price) == float
    assert type(class_products.quantity) == int
