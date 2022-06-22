from sqlalchemy.orm import sessionmaker

from models import Base, User, Address, Profile
from utils import setup_db_engine, create_database_if_not_exists


if __name__ == "__main__":
    engine = setup_db_engine()
    create_database_if_not_exists(engine=engine)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    user = User(email="test@test.com", password="password")
    session.add(user)
    session.commit()

    session.query(User).filter_by(email="test@test.com")
    session.query(User).filter_by(email="test@test.com").first()

    session.query(User).filter_by(email="test@test.com").update({"email": "updated@test.com"})
    session.query(User).filter_by(email="test@test.com").first().update({"email": "updated@test.com"})

    session.query(User).filter(User.email == "test@test.com").first()
    session.query(Profile).filter(Profile.age >= 15)

    user = session.query(User).filter_by(email="test@test.com").first()
    user.email = "updated@test.com"
    session.add(user)
    session.commit()

    address = Address(user=user, city="Test", address="Test 123")
    session.add(address)
    session.commit()
