"""
Дана база данных (в виде текстового файла) о продажах некоторого интернет-магазина. Каждая строка входного файла
представляет собой запись вида Покупатель, Товар, Количество, Стоимость где Покупатель - имя покупателя (строка
без пробелов), товар - название товара (строка без пробелов), количество - количество приобретенных единиц товара.
1. Создайте список и выведите на экран всех покупателей, а для каждого покупателя подсчитайте общее количество
приобретенных им товаров и их стоимость.
2. Создайте список и выведите на экран все товары, а для каждого товара подсчитайте общее количество приобретенных
и их стоимость.
"""
import csv
from typing import Optional


def load_data_from_file(filename: Optional[str] = "dictionary.csv") -> list:
    """Загружаем данные из файла."""
    result = []
    with open(filename, "r") as file:
        for row in csv.reader(file):
            row[2], row[3] = int(row[2]), int(row[3])
            result.append(row)
    return result


def get_stats(data: list, index: int = 0) -> dict:
    """Агрегация списка пользователей и данных."""
    result = {}
    for row in data:
        # Если пользователь есть в списке, обновляем данные
        if row[index] in result:
            result[row[index]]["products_bought"] += row[2]
            result[row[index]]["total_price"] += row[3]
        else:
            # Если нет - задаем исходные значения
            result[row[index]] = {
                "products_bought": row[2],
                "total_price": row[3],
            }
    return result


def main():
    """Основная программа."""
    data = load_data_from_file()

    user_stats = get_stats(data)
    print("Статистика по пользователям: ", user_stats)

    product_stats = get_stats(data, index=1)
    print("Статистика по продуктам: ", product_stats)


if __name__ == "__main__":
    main()
