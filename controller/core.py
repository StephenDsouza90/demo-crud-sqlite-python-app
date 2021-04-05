from sqlalchemy.sql import text

from .database_setup import SQLBackend
from models.models import User, Book, Order
from utils.decorator import handle_session


class BookOrderingSystem(SQLBackend):
    """ BookAccountingSystem is responsible for transactions to the Database.
        It has commands such as ADD, GET, UPDATE and DELETE. """

    def __init__(self, connection_string):
        super(BookOrderingSystem, self).__init__(connection_string)

    @handle_session
    def add_user(self, session, user_name):
        user = User(user_name=user_name)
        session.add(user)
        session.commit()
        return user

    @handle_session
    def get_all_users(self, session):
        users = session.query(User).all()
        return users

    @handle_session
    def get_user(self, session, user_id):
        user = session.query(User).filter_by(user_id=user_id).first()
        return user

    @handle_session
    def add_book(self, session, book_name):
        book = Book(book_name=book_name)
        session.add(book)
        session.commit()
        return book

    @handle_session
    def get_books(self, session):
        books = session.query(Book).all()
        return books

    @handle_session
    def update_book(self, session, book_id, updated_book_name):
        book = session.query(Book).filter_by(book_id=book_id).first()
        book.book_name = updated_book_name
        session.commit()
        return book

    @handle_session
    def delete_book(self, session, book_id):
        session.query(Book).filter_by(book_id=book_id).delete()
        session.commit()

    @handle_session
    def place_order(self, session, user_id, book_id):
        order = Order(user_id=user_id, book_id=book_id)
        session.add(order)
        session.commit()
        return order

    @handle_session
    def get_orders_of_user(self, session, user_id):
        orders = session.query(Order, User, Book).\
            filter(Order.user_id == User.user_id).\
            filter(Order.book_id == Book.book_id).\
            filter(User.user_id == user_id)
        return orders

    @handle_session
    def get_orders_of_book(self, session, book_id):
        orders = session.query(Order, User, Book).\
            filter(Order.user_id == User.user_id).\
            filter(Order.book_id == Book.book_id).\
            filter(Book.book_id == book_id)
        return orders

    @handle_session
    def get_top_n_most_recent_orders(self, session, number_of_books):
        recent_orders = session.query(Order).\
            order_by(Order.order_time.desc()).\
            limit(number_of_books).all()
        return recent_orders

    @handle_session
    def get_top_n_most_oldest_orders(self, session, number_of_books):
        oldest_orders = session.query(Order).\
            order_by(Order.order_time.asc()).\
            limit(number_of_books).all()
        return oldest_orders

    @handle_session
    def get_orders_expired(self, session):
        conn = session.connection()
        statement = text("""SELECT user_id, order_time, book_id,
                                datetime(order_time,'+'||expiry_period_in_days||' days') AS expiry_date
                            FROM orders
                            WHERE expiry_date < CURRENT_DATE;""")
        expired_orders = conn.execute(statement).fetchall()
        return expired_orders
