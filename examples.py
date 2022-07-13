from Shop.purchase.print_result_to_console import print_result_to_console

session.query(Product).filter_by(id=id).update({"name": name})
session.query(Product).filter_by(id=id).update({"price": price})
session.query(Product).filter_by(id=id).update({"number": number})
session.query(Product).filter_by(id=id).update({"comment": comment})


def get_prod_list(session: Session) -> Product:
    return session.query(Product.id, Product.name, Product.price, Product.ammount, Product.comment).all()


def update_prod(session: Session, id: int, name: str, price: int) -> Product:
    session.query(Product).filter_by(id=id).update({"name": name, "price": price})
    session.commit()


def del_prod(session: Session, id: int) -> Product:
    session.query(Product).filter_by(id=id).delete()
    session.commit()


def read_users(session: Session):  # вывод всех пользователей
    for user in session.query(User).all():
        print(user.id, user.email, sep=" | ")


def read_users(session: Session):
    """Вывод всех пользователей."""
    for user in session.query(User).all():
        print(user.id, user.email, sep=" | ")


https://github.com/manti-by/mgallery-py/blob/master/mgallery.py