"""
Дан список стран и городов каждой страны, где ключи это названия стран, а значения - списки городов в этих странах.
Написать функцию которая осуществляет поиск по городу и возвращает страну. Оформить в виде программы, которая считывает
название города и выводит на печать страну.
"""
from typing import Optional

CITY_TO_COUNTRY_MAP = {
    "Belarus": ["Minsk", "Vitebsk", "Grodno"],
    "Russia": ["Moskow", "Saint-Petersburg", "Smolensk"],
    "Ukraine": ["Kiev", "Chernigov", "Sumy"]
}


def find_country(city: str) -> Optional[str]:
    for country, cities in CITY_TO_COUNTRY_MAP.items():
        if city in cities:
            return country


def main():
    """Основная программа."""
    city = input("Enter city name: ")
    country = find_country(city)
    if country is not None:
        print(f"{city} is a part of {country}")
    else:
        print(f"Can't find a country for {city}")


if __name__ == "__main__":
    main()
