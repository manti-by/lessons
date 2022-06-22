"""
Создать таблицу продуктов. Атрибуты продукта: id, название, цена, количество, комментарий.
Реализовать следующие функции для продуктов: создание, чтение, обновление по id, удаление по id.
"""

import sqlite3


def create_product_table(database_name: str):
    with sqlite3.connect(database_name) as session:
        cursor = session.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS product (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name VARCHAR,
                price FLOAT,
                quantity INTEGER,
                comment TEXT
            );
            """
        )
        session.commit()


def get_products(database_name: str):
    with sqlite3.connect(database_name) as session:
        cursor = session.cursor()
        cursor.execute(
            """
            SELECT * FROM product;
            """
        )
        session.commit()
        return cursor.fetchall()


def create_product(database_name: str, name: str, price: float, quantity: int, comment: str):
    with sqlite3.connect(database_name) as session:
        cursor = session.cursor()
        cursor.execute(
            """
            INSERT INTO product (name, price, quantity, comment)
            VALUES (?, ?, ?, ?);
            """,
            (name, price, quantity, comment)
        )
        session.commit()


def update_product(database_name: str, product_id: int, name: str, price: float, quantity: int, comment: str):
    with sqlite3.connect(database_name) as session:
        cursor = session.cursor()
        cursor.execute(
            """
            UPDATE product SET name = ?, price = ?, quantity = ?, comment = ? where id = ?;
            """,
            (name, price, quantity, comment, product_id)
        )
        session.commit()


def delete_product(database_name: str, product_id: int):
    with sqlite3.connect(database_name) as session:
        cursor = session.cursor()
        cursor.execute(
            """
            DELETE FROM product WHERE id = ?;
            """,
            (product_id,)
        )
        session.commit()
