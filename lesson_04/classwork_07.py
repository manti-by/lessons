"""
Пользователь вводит с клавиатуры числа до тех пор, пока не введет любой строчный символ, из этих чисел составляется
первый список. Далее таким же образом вводятся второй и третий списки. Вывести на экран список, элементы которого
есть в первых двух списках, но отсутствуют в третьем.
"""

my_list_01 = []
my_list_02 = []
my_list_03 = []

while True:
    x = input("Enter X1: ")
    try:
        my_number = int(x)
        my_list_01.append(my_number)
    except ValueError:
        break

while True:
    x = input("Enter X2: ")
    try:
        my_number = int(x)
        my_list_02.append(my_number)
    except ValueError:
        break

while True:
    x = input("Enter X3: ")
    try:
        my_number = int(x)
        my_list_03.append(my_number)
    except ValueError:
        break


for x in my_list_01:
    if x in my_list_02 and x not in my_list_03:
        print(x)
