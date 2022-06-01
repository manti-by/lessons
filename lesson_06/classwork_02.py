"""
Доработать первое задание так, чтобы словарь читался из текстового CSV файла,
где на каждой строке пары слов вида: apple,яблоко.
"""
import csv


with open("dictionary.csv", "r") as file:
    my_dict = {row[0]: row[1] for row in csv.reader(file)}


def eng_to_rus(word):
    return my_dict[word]


def rus_to_eng(word):
    new_dict = {
        value: key
        for key, value in my_dict.items()
    }
    return new_dict[word]


print(eng_to_rus("apple"))
print(eng_to_rus("fly"))

print(rus_to_eng("яблоко"))
print(rus_to_eng("зеленый"))
