from controller.core import BookOrderingSystem
from interface.interface import start_app


def main():
    print("Starting the program...")

    connection_string = "sqlite:///book_ordering_system.db"

    print(f"Connecting to DB: {connection_string}")

    bos = BookOrderingSystem(connection_string)
    bos.bootstrap()

    print("Connected.")

    start_app(bos)


if __name__ == '__main__':
    main()
