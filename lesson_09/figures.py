"""
Создать класс Point, описывающий точку (атрибуты: x, y). Создать класс Figure.
Создать три дочерних класса Circle (атрибуты: координаты центра, длина радиуса;
методы: нахождение периметра и площади окружности), Triangle (атрибуты: три точки,
методы: нахождение площади и периметра), Square (атрибуты: две точки, методы: нахождение площади и периметра).
При потребности создавать все необходимые методы не описанные в задании.
"""

import math


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


class Figure:

    @staticmethod
    def segment_length(a: Point, b: Point):
        return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)

    def perimeter(self):
        raise NotImplementedError

    def area(self):
        raise NotImplementedError


class Circle(Figure):
    def __init__(self, a: Point, radius: int):
        self.a = a
        self.radius = radius

    def perimeter(self):
        return round(2 * math.pi * self.radius, 2)

    def area(self):
        return round(math.pi * (self.radius ** 2), 2)


class Triangle(Figure):
    def __init__(self, a: Point, b: Point, c: Point):
        self.a = a
        self.b = b
        self.c = c

        # Calculate segments length using points
        self.segment_1 = self.segment_length(self.a, self.b)
        self.segment_2 = self.segment_length(self.b, self.c)
        self.segment_3 = self.segment_length(self.c, self.a)

    def perimeter(self):
        return round(self.segment_1 + self.segment_2 + self.segment_3, 2)

    def area(self):
        # Use Heron's Formula to calculate triangle area
        half_pr = self.perimeter() / 2
        return round(math.sqrt(
            half_pr * (half_pr - self.segment_1) * (half_pr - self.segment_2) * (half_pr - self.segment_3)
        ), 2)


class Square(Figure):
    def __init__(self, a: Point, b: Point):
        self.a = a
        self.b = b

        # Calculate segments length using points
        self.segment_1 = abs(self.a.x - self.b.x)
        self.segment_2 = abs(self.a.y - self.b.y)

    def perimeter(self):
        return round((self.segment_1 + self.segment_2) * 2, 2)

    def area(self):
        return round(self.segment_1 * self.segment_2, 2)
