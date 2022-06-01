"""
Реализуйте алгоритм игры “Тайный Санта (Secret Santa)” - в шляпу кладутся небольшие записки с именами участников.
Затем каждый играющий по очереди вытягивает бумажку с именем того, кому предстоит вручить презент. Ваша программа
должна используя список имен участников выдать на выходе пары, кто и кому будет дарить, причем сам себе человек не
 может подарить, дубликаты тоже не допустимы.
"""

import random

people = ["Alex", "Olga", "Roma", "Dima", "Kiril"]
random.shuffle(people)

for index in range(len(people)):
    # Special case when we match the last person in list to the first
    if index == len(people) - 1:
        print(f"{people[index]} - {people[0]}")
    else:
        print(f"{people[index]} - {people[index + 1]}")
