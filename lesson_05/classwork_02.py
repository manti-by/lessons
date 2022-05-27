"""
Создать функцию, которая принимает на вход неопределенное количество аргументов
и возвращает их сумму и максимальное из них.
"""


def sum_and_max(*args):
    result_sum = 0
    max_item = args[0]
    for item in args:
        result_sum += item
        if item > max_item:
            max_item = item
    return result_sum, max_item


my_list = [1, 5, 16, 3, 66, -20, 5]

print(sum_and_max(*my_list))
print(sum_and_max(1, 5, 16, 3, 66, -20, 5))
