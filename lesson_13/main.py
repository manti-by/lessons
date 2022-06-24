from faker import Faker
from sqlalchemy.orm import sessionmaker

from models import Base, User, Profile, Address, Product, Purchase
from utils import setup_db_engine, create_database_if_not_exists

fake = Faker()


def generate_user(session) -> User:
    user = User(
        email=fake.email(), password=fake.word()
    )
    profile = Profile(
        user=user, phone=fake.phone_number(), age=fake.pyint(min_value=18, max_value=60)
    )
    address = Address(
        user=user, city=fake.city(), address=fake.address()
    )
    session.add_all([user, profile, address])
    session.commit()
    return user


def generate_purchase(session):
    user = generate_user(session)
    product = Product(name=fake.company(), price=fake.pyfloat(min_value=20, max_value=100))
    purchase = Purchase(
        user=user, product=product, count=fake.pyint(min_value=1, max_value=5)
    )
    session.add_all([product, purchase])
    session.commit()


if __name__ == "__main__":
    engine = setup_db_engine()
    create_database_if_not_exists(engine=engine)

    Base.metadata.create_all(engine)
    CurrentSession = sessionmaker(bind=engine)
    current_session = CurrentSession()

    for _ in range(10):
        generate_purchase(current_session)
