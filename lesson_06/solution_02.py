"""
В школе решили набрать три новых класса по программированию.
Так как занятия по у них проходят в одно и то же время, было решено выделить кабинет
для каждого класса и купить в них новые парты.
За каждой партой может сидеть не больше двух учеников. Известно количество учащихся в
каждом из трёх классов. Сколько всего нужно закупить парт чтобы их хватило на всех учеников?
Программа получает на вход три натуральных числа: количество учащихся в каждом из трех классов.
"""

import math
import random


def get_tables_count(students_in_a_class: list) -> list:
    # Using map function calculate parts count
    # we should buy for each class and round this value to the next
    return list(map(lambda x: math.ceil(x / 2), students_in_a_class))


# Generate test data
students_in_a_class = [
    random.randint(10, 50),
    random.randint(10, 50),
    random.randint(10, 50),
]

class_1, class_2, class_3 = get_tables_count(students_in_a_class)

print(f"Class #1 students = {students_in_a_class[0]}, tables = {class_1}")
print(f"Class #2 students = {students_in_a_class[1]}, tables = {class_2}")
print(f"Class #3 students = {students_in_a_class[2]}, tables = {class_3}")