"""
Создать класс Car. Атрибуты: марка, модель, год выпуска, скорость (по умолчанию 0).
Методы: увеличить скорости (скорость +5), уменьшение скорости (скорость -5), стоп (сброс скорости на 0),
отображение скорости, задний ход (изменение знака скорости).
"""


class Car:

    def __init__(self, make: str, model: str, year: int, speed: int = 0):
        self.make = make
        self.model = model
        self.year = year
        self.speed = speed

    def increase_speed(self):
        self.speed += 5

    def decrease_speed(self):
        self.speed -= 5

    def stop(self):
        self.speed = 0

    def reverse(self):
        self.speed *= -1

    def print_speed(self):
        print(self.speed)


def main():
    car = Car("Mercedes", "E500", 2000)
    while car.speed < 100:
        car.increase_speed()
        car.print_speed()
    print("Done!")


if __name__ == "__main__":
    main()
