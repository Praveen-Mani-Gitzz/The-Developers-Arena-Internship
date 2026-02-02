from .library import Library


def display_menu():
    print("\n" + "=" * 40)
    print("   LIBRARY MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Add New Book")
    print("2. Register New Member")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Search Books")
    print("6. View All Books")
    print("7. View All Members")
    print("8. View Statistics")
    print("9. Save & Exit")
    print("0. Exit Without Saving")


def main():
    library = Library()

    while True:
        display_menu()
        choice = input("Enter choice: ")

        if choice == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            year = input("Year (optional): ")
            success, msg = library.add_book(title, author, isbn, year)
            print(msg)

        elif choice == "2":
            name = input("Member Name: ")
            member_id = input("Member ID: ")
            success, msg = library.register_member(name, member_id)
            print(msg)

        elif choice == "3":
            member_id = input("Member ID: ")
            isbn = input("ISBN: ")
            success, msg = library.borrow_book(member_id, isbn)
            print(msg)

        elif choice == "4":
            member_id = input("Member ID: ")
            isbn = input("ISBN: ")
            success, msg = library.return_book(member_id, isbn)
            print(msg)

        elif choice == "5":
            keyword = input("Search keyword: ")
            results = library.find_book(keyword)
            for book in results:
                print(book)
            print(f"Found {len(results)} result(s).")

        elif choice == "6":
            for book in library.books.values():
                print(book)

        elif choice == "7":
            for member in library.members.values():
                print(member)

        elif choice == "8":
            stats = library.get_statistics()
            print(stats)

        elif choice == "9":
            success, msg = library.save_data()
            print(msg)
            break

        elif choice == "0":
            print("Exiting without saving.")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
