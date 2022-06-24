from faker import Faker
from sqlalchemy.orm import sessionmaker

from models import Base, User, Profile, Address
from utils import setup_db_engine, create_database_if_not_exists

fake = Faker()


def generate_user(session):
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


if __name__ == "__main__":
    engine = setup_db_engine()
    create_database_if_not_exists(engine=engine)

    Base.metadata.create_all(engine)
    CurrentSession = sessionmaker(bind=engine)
    current_session = CurrentSession()

    for _ in range(10):
        generate_user(current_session)
