"""
Создать класс Dog. Класс имеет четыре атрибута: height, weight, name, age.
Класс имеет три метода: jump, run, bark. Каждый метод выводит сообщение на экран.
Создать объект класса Dog, вызвать все методы объекта и вывести на экран все его атрибуты.
"""


class Animal:
    height: int = None
    weight: int = None
    name: str = None
    age: int = 10

    def __init__(self, *args, **kwargs):
        self.height = kwargs.get("height")
        self.weight = kwargs.get("weight")
        self.name = kwargs.get("name")
        if kwargs.get("age") is not None:
            self.age = kwargs.get("age")

    def talk(self):
        raise NotImplementedError


class Dog(Animal):
    def talk(self):
        print(f"{self.name} is barking.")


if __name__ == "__main__":
    dog1 = Dog(height=10, weight=5, name="First")
    dog1.jump()

    dog2 = Dog(height=10, weight=5, name="Second", age=5)
    dog2.talk()
