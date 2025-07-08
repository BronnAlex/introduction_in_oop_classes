import json
from pathlib import Path

from src.product import Category, Product


def read_json(path):
    """Функция читающая файл json"""
    file_path = path / "../data/data.json"
    full_path = file_path.resolve()

    with open(full_path, "r", encoding="UTF-8") as file:
        data = json.load(file)
    return data


def created_object_from_json(data_json):
    """Функция осуществляющая подгрузку данных по категориями и товарам из файла JSON
    И создающая объекты классов"""
    categories_list = []
    for dict_from_json in data_json:
        product_list = []
        for product_dict in dict_from_json["products"]:
            product_list.append(Product(**product_dict))

        dict_from_json["products"] = product_list
        categories_list.append(Category(**dict_from_json))

    return categories_list


if __name__ == "__main__":  # pragma: no cover
    home_dir = Path.cwd()
    row_data = read_json(home_dir)
    user_data = created_object_from_json(row_data)
    print(user_data[1].name)
    print(user_data[1].products)
    print(user_data[1].products[0].name)
    print(user_data[1].products[0].description)
    print(user_data[1].products[0].price)
    print(user_data[1].products[0].quantity)

    print(user_data[0].name)
    print(user_data[0].products)
    print(user_data[0].products[0].name)
    print(user_data[0].products[0].description)
    print(user_data[0].products[0].price)
    print(user_data[0].products[0].quantity)
