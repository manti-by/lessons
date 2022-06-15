"""
Создать список фигур и в цикле подсчитать и вывести площади всех фигур на экран.
"""

from figures import Point, Circle, Triangle, Square


def main():
    a = Point(3, 7)
    circle = Circle(a, 3)

    a = Point(3, 7)
    b = Point(5, 2)
    square = Square(a, b)

    a = Point(1, 1)
    b = Point(7, 2)
    c = Point(5, 5)
    triangle = Triangle(a, b, c)

    for figure in [circle, square, triangle]:
        print(figure.__class__.__name__, figure.perimeter(), figure.area())


if __name__ == "__main__":
    main()
