import pytest

from src.product import Product


def test_product_init(class_products):
    """Тестируем инициализацию класса Product из фикстур с готовым экземпляром,
    через вызов атрибутов"""
    assert class_products.name == "Samsung Galaxy S23 Ultra"
    assert class_products.description == "256GB, Серый цвет, 200MP камера"
    # assert class_products.__price == 180000.0
    assert class_products.quantity == 5


def test_category_init(category, category_not_empty_product):
    """Тестируем инициализацию класса Category из фикстур с готовым экземпляром,
    через вызов атрибутов объекта и самого класса"""
    assert category.name == "Смартфоны"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert category.product_count == 2
    assert category.category_count == 2
    # Заменил атрибут category.product  на category.add_product_in_list
    # т.к создал геттер в котором образовалась строка
    assert len(category.add_product_in_list) == 2


def test_category_not_empty_product_init(category_not_empty_product):
    assert category_not_empty_product.name == "Супер смартфоны"
    assert (
        category_not_empty_product.description == "Супер смартфоны, как средство не только коммуникации, "
        "но и получения дополнительных функций для удобства жизни"
    )
    assert category_not_empty_product.product_count == 2
    assert category_not_empty_product.category_count == 3
    # assert len(category_not_empty_product.products) == 0


def test_type_data_category(category):
    """Тестируем на проверку типы данных экземпляра класса Category"""
    assert type(category.name) is str
    assert type(category.description) is str
    # assert type(category.products) == list
    assert type(category.category_count) is int
    assert type(category.product_count) is int


def test_type_data_product(class_products):
    """Тестируем на проверку типы данных экземпляра класса Product"""
    assert type(class_products.name) is str
    assert type(class_products.description) is str
    # assert type(class_products.price) == float
    assert type(class_products.quantity) is int


def test_category_property(category):
    """Тустируем геттер в классе Category"""
    assert category.add_product == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n" "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    )


def test_category_setter(category, class_products):
    """Тестируем сеттер в классе Category"""
    assert len(category.add_product_in_list) == 2
    category.add_product = class_products
    assert len(category.add_product_in_list) == 3


def test_create_new_product():
    """Тестируем новый созданный нами экземпляр класса, для этого импортируем Product
    так как если передавать из фикстур, то там уже ининциализированный готовый экземпляр"""
    creat_product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    assert creat_product.name == "Samsung Galaxy S23 Ultra"
    assert creat_product.description == "256GB, Серый цвет, 200MP камера"


def test_product_update_sette(capsys, class_products):
    """Тестируем сеттер из класса Product(обновленные данные)"""
    class_products.private_price = -10
    message = capsys.readouterr()
    # При добавлении abs класса и миксин класса
    # В данный тест добавил следующее .split("\n")[-1] и все заработало
    assert message.out.strip().split("\n")[-1] == "Цена не должна быть нулевая или отрицательная"


def test_product_str(class_products):
    """Тест на строковое представление экземпл Product"""
    # print(class_products) >>> ввод pytest -s
    assert str(class_products) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_category_str(category):
    """Тест на строковое представление экземпл Category"""

    assert str(category) == "Смартфоны, количество продуктов: 13"


def test_product_add(class_products, class_products_2):
    assert class_products + class_products_2 == 2580000.0


def test_product_add_error(class_products):
    with pytest.raises(TypeError):
        class_products + 1


def test_category_new_property(category):
    """Тустируем новый геттер product в классе Category"""
    assert category.add_product == (
        "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n" "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
    )


def test_avg_price(category, category_without_product):
    """Тестируем метод получения средней цены всех товаров
    а также при условии что товаров вообще нет"""
    assert category.avg_price_all_goods() == 195000
    assert category_without_product.avg_price_all_goods() == 0


def test_custom_exception(capsys, category):
    """"Тест, проверки вывода сообщений при количестве равном нулю
    Проверка своего рода исключений"""
    assert len(category.add_product_in_list) == 2  # Количество категорий товаров (product1, product2)

    quantity_full = Product("Iphone", "13 Pro max", 110000.0, 4)
    category.add_product = quantity_full  # метод add_product из сеттера в классе Category
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Товар успешно добавлен"
    assert message.out.strip().split("\n")[-1] == "Обработка добавления товара завершена."

    quantity_zero = Product("Iphone", "13 Pro max", 110000.0, 0)
    category.add_product = quantity_zero  # метод add_product из сеттера в классе Category
    message = capsys.readouterr()
    assert message.out.strip().split("\n")[-2] == "Нельзя добавлять товар с нулевым количеством"
    assert message.out.strip().split("\n")[-1] == "Обработка добавления товара завершена."


def test_init_product_zero_error():
    """Тест, на выброс исключения при отрицательном количестве"""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Iphone", "13 Pro max", 110000.0, -1)
