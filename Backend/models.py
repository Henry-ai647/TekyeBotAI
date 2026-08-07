from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class Restaurant(Base):
    __tablename__ = "restaurants"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    phone = Column(String)
    location = Column(String)

class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    customer = Column(String)
    meal = Column(String)
    quantity = Column(Integer)
    status = Column(String)
