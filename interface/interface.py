WELCOME_MESSAGE = """
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

    Your Option:\t
    """


def start_app(bos):
    """The User Interface which users will use
    to perform actions on the Book Accounting System."""

    option = int(input(WELCOME_MESSAGE))

    print("\n\n")
    while option != 0:

        if option == 1:
            user_name = input("Enter user name: ")
            user = bos.add_user(user_name)
            print(f"\nUser has been created. \nUser name: {user.user_name}")

        elif option == 2:
            user_id = int(input("Enter user ID: "))
            user = bos.get_user(user_id)
            if user:
                print(f"\nUser name: {user.user_name}")
            else:
                print(f"\nUser with user ID {user_id} does not exist")

        elif option == 3:
            users = bos.get_all_users()
            for user in users:
                print(f"\nUser ID {user.user_id} \nUser name {user.user_name}")

        elif option == 4:
            book_name = input("Enter book name: ")
            book = bos.add_book(book_name)
            print(f"\nBook added into the DB. \nBook name: {book.book_name}")

        elif option == 5:
            books = bos.get_books()
            for book in books:
                print(f"\nBook ID {book.book_id} \nBook name {book.book_name}")

        elif option == 6:
            book_id = int(input("Enter book ID: "))
            update_book_name = input("Enter update book name: ")
            book = bos.update_book(book_id, update_book_name)
            print(f"\nBook name {book.book_name} has been updated")

        elif option == 7:
            book_id = int(input("Enter book ID to be delete: "))
            bos.delete_book(book_id)
            print(f"\nBook deleted")

        elif option == 8:
            user_id = int(input("Enter user ID: "))
            book_id = int(input("Enter book ID: "))
            order = bos.place_order(user_id, book_id)
            print(
                f"\nOrder placed! \nUser ID: {order.user_id} \nBook ID: {order.book_id}")

        elif option == 9:
            user_id = int(input("Enter user ID: "))
            orders_of_user = bos.get_orders_of_user(user_id)
            for order, user, book in orders_of_user:
                print(
                    f"User name: {user.user_name} \nBook name: {book.book_name} \nDate & Time of Order: {order.order_time}")

        elif option == 10:
            book_id = int(input("Enter book ID: "))
            orders_of_book = bos.get_orders_of_book(book_id)
            for order, user, book in orders_of_book:
                print(
                    f"User name: {user.user_name} \nBook Name: {book.book_name} \nDate & Time of Order: {order.order_time}")

        elif option == 11:
            display_orders = int(input("Display number of recent orders: "))
            recent_orders = bos.get_top_n_most_recent_orders(display_orders)
            for order in recent_orders:
                print(
                    f"\nMost recent orders: \nOrder ID: {order.order_id} \nOrder time: {order.order_time}")

        elif option == 12:
            display_orders = int(input("Display number of oldest orders: "))
            oldest_orders = bos.get_top_n_most_oldest_orders(display_orders)
            for order in oldest_orders:
                print(
                    f"\nMost oldest orders: \Order ID: {order.order_id} \nOrder time: {order.order_time}")

        elif option == 13:
            expired_orders = bos.get_orders_expired()
            if expired_orders:
                for expired_order in expired_orders:
                    print(
                        f"\nUser name: {expired_order.user_id} \nOrdered date & time: {expired_order.order_time} \n Book name: {expired_order.book_id} \nExpired date & time: {expired_order.expired_order}".format)
            else:
                print("No orders are expired yet")

        option = int(input("\nYour option: "))
