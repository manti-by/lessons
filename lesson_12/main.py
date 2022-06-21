from sqlalchemy.orm import sessionmaker

from models import Base, User
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
