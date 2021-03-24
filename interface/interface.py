WELCOME_MESSAGE = """
    Welcome to the Book Accounting System!

    To interact with the app please press any of the following options:

    0. Quit

    1. Add user
    2. Get user

    3. Add book
    4. Get all books
    5. Update book
    6. Delete book

    7. Place an Order
    8. Get orders of a user
    9. Get orders of a book

    10. Get top 3 recent orders
    11. Get top 3 oldest orders
    12. Get orders expired

    Your Option:\t
    """


def start_app(bas):
    """The User Interface which users will use
    to perform actions on the Book Accounting System."""

    option = int(input(WELCOME_MESSAGE))

    print("\n\n")
    while option != 0:

        if option == 1:
            user_name = input("Enter user name: ")
            user = bas.add_user(user_name)
            print(f"\nUser has been created. \nUser name: {user.user_name}")

        elif option == 2:
            user_id = int(input("Enter user ID: "))
            user = bas.get_user(user_id)
            if user:
                print(f"\nUser name: {user.user_name}")
            else:
                print(f"\nUser with user ID {user_id} does not exist")

        elif option == 3:
            book_name = input("Enter book name: ")
            book = bas.add_book(book_name)
            print(f"\nBook added into the DB. \nBook name: {book.book_name}")

        elif option == 4:
            books = bas.get_books()
            for book in books:
                print(f"\nBook ID {book.book_id} \nBook name {book.book_name}")

        elif option == 5:
            book_id = int(input("Enter book ID: "))
            update_book_name = input("Enter update book name: ")
            book = bas.update_book(book_id, update_book_name)
            print(f"\nBook name {book.book_name} has been updated")

        elif option == 6:
            book_id = int(input("Enter book ID to be delete: "))
            bas.delete_book(book_id)
            print(f"\nBook deleted")

        elif option == 7:
            user_id = int(input("Enter user ID: "))
            book_id = int(input("Enter book ID: "))
            order = bas.place_order(user_id, book_id)
            print(
                f"\nOrder placed! \nUser ID: {order.user_id} \nBook ID: {order.book_id}")

        elif option == 8:
            user_id = int(input("Enter user ID: "))
            orders_of_user = bas.get_orders_of_user(user_id)
            for order, user, book in orders_of_user:
                print(
                    f"User name: {user.user_name} \nBook name: {book.book_name} \nDate & Time of Order: {order.order_time}")

        elif option == 9:
            book_id = int(input("Enter book ID: "))
            orders_of_book = bas.get_orders_of_book(book_id)
            for order, user, book in orders_of_book:
                print(
                    f"User name: {user.user_name} \nBook Name: {book.book_name} \nDate & Time of Order: {order.order_time}")

        elif option == 10:
            display_orders = int(input("Display number of recent orders: "))
            recent_orders = bas.get_top_n_most_recent_orders(display_orders)
            for order in recent_orders:
                print(
                    f"\nMost recent orders: \nOrder ID: {order.order_id} \nOrder time: {order.order_time}")

        elif option == 11:
            display_orders = int(input("Display number of oldest orders: "))
            oldest_orders = bas.get_top_n_most_oldest_orders(display_orders)
            for order in oldest_orders:
                print(
                    f"\nMost recenet orders: \nBook ID: {order.book_id} \nOrder time: {order.order_time}")

        elif option == 12:
            expired_orders = bas.get_orders_expired()
            if expired_orders:
                for expired_order in expired_orders:
                    print(
                        f"\nUser name: {expired_order.user_id} \nOrdered date & time: {expired_order.order_time} \n Book name: {expired_order.book_id} \nExpired date & time: {expired_order.expired_order}".format)
            else:
                print("No orders are expired yet")

        option = int(input("\nYour option: "))
