from datetime import datetime

from sqlalchemy import Column, DateTime, String, Integer, ForeignKey

from utils.base import Base


class User(Base):
    """ Represents the User table """

    __tablename__ = 'users'

    user_id = Column(Integer(), primary_key=True)
    user_name = Column(String(32), nullable=False)


class Book(Base):
    """ Represents the Books table """

    __tablename__ = 'books'

    book_id = Column(Integer(), primary_key=True)
    book_name = Column(String(32), nullable=False)


class Order(Base):
    """ Represents the Orders table """

    __tablename__ = 'orders'

    order_id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), ForeignKey("users.user_id"), nullable=False)
    book_id = Column(Integer(), ForeignKey("books.book_id"), nullable=False)
    order_time = Column(DateTime, default=datetime.utcnow)
    expiry_period_in_days = Column(Integer, default=30)
