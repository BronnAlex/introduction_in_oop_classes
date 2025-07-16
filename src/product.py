class Product:
    """Класс, для обозначения товара и его количества"""

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """Инициализация класса и свойств атрибутов"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @classmethod
    def new_product(cls, product_from_dict):
        return cls(**product_from_dict)

    @property
    def private_price(self):
        """Геттер для приватного атрибута __price"""
        return self.__price

    @private_price.setter
    def private_price(self, new_price):
        """Сеттер, обновление цены и её проверка через спец. метод """
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
            return
        self.__price = new_price


class Category:
    """Класс для выявления категории товара и его описания"""

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product] = None):
        """Инициализация класса, свойств атрибутов и атрибутов самого класса"""
        self.name = name
        self.description = description
        self.__products = products if products else []
        Category.category_count += 1
        Category.product_count += len(products) if products else 0

    @property
    def add_product(self):
        """Геттер для приватного атрибута __products,
        который возвращает тип данных строку, а не список"""
        product_str = ""
        for current_product in self.__products:
            product_str += (
                f"{current_product.name}, {current_product.private_price} руб. Остаток: {current_product.quantity} шт.\n"
            )

        return product_str

    @add_product.setter
    def add_product(self, new_product: Product):
        """Сетте, добавляет и обновляет приватный список продуктов
        через спец. метод add_product"""
        self.__products.append(new_product)
        Category.product_count += 1

    @property
    def add_product_in_list(self):
        """Геттер, который возвращет, ранее измененный приватный атрибут __products,
        списком, а не строкой"""
        return self.__products


if __name__ == "__main__":  # pragma: no cover
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    print(product1.name)
    print(product1.description)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.quantity)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    # category2 = Category(
    #     "Телевизоры",
    #     "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
    #     [product4],
    # )
    # print(category2.name)
    # print(category2.description)

    category1.add_product = product4
    print(category1.product_count)
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    print(new_product.name)
    print(new_product.description)
    print(new_product.quantity)
    new_product.private_price = -10

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)

    print(Category.category_count)
    print(Category.product_count)
