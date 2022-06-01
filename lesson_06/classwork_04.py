"""
Использую функцию из предыдущей задачи, написать программу игру Блэкджек,
т.е. реализовать цикл в котором на каждом ходу у игрока спрашивается,
достать ли следующую карту, в случае положительного ответа  - вытягивать случайную карту.
Игра заканчивается если игрок отказывается брать карту, либо сумма его карт больше 21-го.
"""

from classwork_03 import get_random_card

my_dict = {
    "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 2, "D": 3, "K": 4, "A": 1
}


def nominal_to_value(nominal):
    return my_dict[nominal]


n, _ = get_random_card()
value = nominal_to_value(n)

current_sum = value
while True:
    choice = input("Достать следующую карту [Y/n]: ")
    if choice == "n":
        break

    n, _ = get_random_card()
    value = nominal_to_value(n)
    current_sum += value

    if current_sum > 21:
        print("Game over, ты проиграл, твоя текущая сумма: ", current_sum)
        break

    if current_sum == 21:
        print("Ты выйграл")
        break

    if current_sum < 21:
        print("Твоя текущая сумма: ", current_sum)
