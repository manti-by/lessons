"""
Написать функцию month_to_season(), которая принимает 1 аргумент - номер месяца
- и возвращает название сезона, к которому относится этот месяц.
Например, передаем 2, на выходе получаем "Winter".
"""


def month_to_season_1(month):
    mapping = {
        "winter": [1, 2, 12],
        "spring": [3, 4, 5],
        "summer": [6, 7, 8],
        "autumn": [9, 10, 11],
    }
    for season, month_list in mapping.items():
        if month in month_list:
            return season


def month_to_season_2(month):
    return {
        1: "winter",
        2:  "winter",
        12: "winter",
        3: "spring",
        4: "spring",
        5: "spring",
        6: "summer",
        7: "summer",
        8: "summer",
        9: "autumn",
        10: "autumn",
        11: "autumn",
    }[month]


print(month_to_season_1(4))
print(month_to_season_2(4))
