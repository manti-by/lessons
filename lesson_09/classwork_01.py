"""
Создать класс MyTime. Атрибуты: hours, minutes, seconds.
Методы: переопределить магические методы сравнения (==, !=, >=, <=, <, >).
"""
from __future__ import annotations


class MyTime:

    def __init__(self, hours: int, minutes: int, seconds: int):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def to_seconds(self) -> int:
        return self.seconds + self.minutes * 60 + self.hours * 60 * 60

    def __eq__(self, other: MyTime):
        return self.to_seconds() == other.to_seconds()

    def __ne__(self, other: MyTime):
        return not self.__eq__(other)

    def __lt__(self, other: MyTime):
        return self.to_seconds() < other.to_seconds()

    def __gt__(self, other: MyTime):
        return self.to_seconds() > other.to_seconds()

    def __le__(self, other: MyTime):
        return self.to_seconds() <= other.to_seconds()

    def __ge__(self, other: MyTime):
        return not self.__le__(other)


if __name__ == "__main__":
    a = MyTime(hours=3, minutes=30, seconds=30)
    b = MyTime(hours=3, minutes=30, seconds=30)
    print("a == b: ", a == b)
    print("a >= b: ", a >= b)

    b.seconds = 45
    print("a == b: ", a == b)
