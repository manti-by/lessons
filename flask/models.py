import json

from sqlalchemy import Integer, String, Column, ForeignKey, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    email = Column(String)
    password = Column(String)

    profile = relationship("Profile", back_populates="user", uselist=False)
    addresses = relationship("Address", back_populates="user")
    purchases = relationship("Purchase", back_populates="user")

    def __str__(self):
        return f"{self.id},{self.email}"

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email
        }

    def json(self):
        return json.dumps(self.serialize())


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    city = Column(String)
    address = Column(String)

    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="addresses")


class Profile(Base):
    __tablename__ = "profile"
    id = Column(Integer, primary_key=True)
    phone = Column(String)
    age = Column(Integer)

    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="profile")


class Purchase(Base):
    __tablename__ = "purchase"
    id = Column(Integer, primary_key=True)
    user_id = Column(ForeignKey("user.id"))
    product_id = Column(ForeignKey("product.id"))
    count = Column(Integer)

    user = relationship("User", back_populates="purchases")
    product = relationship("Product", back_populates="purchases")


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)

    purchases = relationship("Purchase", back_populates="product")
