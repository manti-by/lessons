from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import or_, and_

from models import Base, User, Purchase, Product
from utils import setup_db_engine, create_database_if_not_exists


if __name__ == "__main__":
    engine = setup_db_engine()
    create_database_if_not_exists(engine=engine)

    Base.metadata.create_all(engine)
    CurrentSession = sessionmaker(bind=engine)
    current_session = CurrentSession()

    users = current_session.query(User).join(Purchase).join(Product).filter(
        Purchase.count >= 2
    ).filter(
        Product.price >= 100,
    ).all()
    print([x.id for x in users])

    users = current_session.query(User).join(Purchase).join(Product).filter(
        Purchase.count >= 2, Product.price >= 100,
    ).all()
    print([x.id for x in users])

    users = current_session.query(User).join(Purchase).join(Product).filter(
        or_(Product.price >= 100, Product.price <= 10.0)
    ).all()
    print([x.id for x in users])

    users = current_session.query(User).join(Purchase).join(Product).filter(
        and_(or_(Product.price >= 100, Product.price <= 10.0), User.email == "test-1@test.com")
    ).all()
    print([x.id for x in users])

