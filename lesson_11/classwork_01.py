"""
Создать функцию, которая позволяет добавлять данные в таблицу user. Добавить 5 различных записей.
"""

import sqlite3


def create_user(firstname: str, lastname: str, email: str, password: str, age: int):
    with sqlite3.connect("my_database.sqlite3") as session:
        cursor = session.cursor()
        cursor.execute(
            """
            INSERT INTO user (firstname, lastname, email, password, age)
            VALUES (?, ?, ?, ?, ?);
            """,
            (firstname, lastname, email, password, age),
        )
        session.commit()


if __name__ == "__main__":
    create_user("Alexander", "Chaika", "manti.by+1@gmail.com", "TestPass1", 36)
    create_user("Roman", "Test", "manti.by+2@gmail.com", "TestPass2", 22)
    create_user("Olga", "Next", "manti.by+3@gmail.com", "TestPass3", 26)
    create_user("Valery", "First", "manti.by+4@gmail.com", "TestPass4", 38)
    create_user("Max", "Last", "manti.by+5@gmail.com", "TestPass5", 20)
