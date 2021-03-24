from controller.core import BookAccountingSystem
from interface.interface import start_app


def main():
    print("Starting the prograg...")

    connection_string = "sqlite:///book_accounting_system.db"

    print(f"Connecting to DB: {connection_string}")

    # set up of the engine, session and connection
    bas = BookAccountingSystem(connection_string)
    bas.bootstrap()

    print("Connected.")

    start_app(bas)


if __name__ == '__main__':
    main()
