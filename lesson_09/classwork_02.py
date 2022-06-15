"""
Переопределить магические методы сложения, вычитания, умножения на число.
"""
from __future__ import annotations

from classwork_01 import MyTime


class NewTime(MyTime):

    @staticmethod
    def seconds_to_time(seconds: int) -> NewTime:
        hours = seconds // (60 * 60)
        minutes = (seconds % (60 * 60)) // 60
        seconds = seconds % 60
        return NewTime(hours=hours, minutes=minutes, seconds=seconds)

    def __add__(self, other: NewTime) -> NewTime:
        seconds = self.to_seconds() + other.to_seconds()
        return NewTime.seconds_to_time(seconds)

    def __str__(self) -> str:
        return f"{self.hours}:{self.minutes}:{self.seconds}"


if __name__ == "__main__":
    print(NewTime.seconds_to_time(177))
