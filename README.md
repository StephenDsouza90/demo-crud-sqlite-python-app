# Book Ordering System

A simple command line app called **book ordering system** written in Python using SQLAlchemy.

## Code Structure

TBD


## Database

To use a Postgres database, the following connection string can be used. It needs to be replaced with the SQLite connection string.

postgres_connection_string = "postgres+psycopg2://<user_name>:<user_password>@localhost:5432/<database_name>"


## How to run locally
```bash
>> python main.py

Starting the program...
Connecting to DB: sqlite:///book_ordering_system.db
Connected.

    Welcome to the Book Accounting System!

    To interact with the app please press any of the following options:

    0. Quit

    1. Add user
    2. Get user
    3. Get all users

    4. Add book
    5. Get all books
    6. Update book
    7. Delete book

    8. Place an Order
    9. Get orders of a user
    10. Get orders of a book

    11. Get top 3 recent orders
    12. Get top 3 oldest orders
    13. Get orders expired

    Your Option:

```


## Install Dependencies

The dependencies are saved in the requirements.txt file.

It can be installed via the following command:

```bash
>> pip install -r requirements.txt
```