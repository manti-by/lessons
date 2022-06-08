"""
Добавить в класс Dog метод change_name. Метод принимает на вход новое имя и
меняет атрибут имени у объекта. Создать один объект класса. Вывести имя.
Вызвать метод change_name. Вывести имя.
"""

from classwork_01 import Dog


class NewDog(Dog):

    def change_name(self, new_name):
        self.name = new_name


if __name__ == "__main__":
    dog1 = NewDog(height=10, weight=5, name="First name")
    print("Old name: ", dog1.name)
    dog1.change_name("New name")
    print("New name: ", dog1.name)

