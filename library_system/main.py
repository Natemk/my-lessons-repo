from library_system.library import Library


def display_books(books):
    if not books:
        print("No books available.")
        return
    for book in books:
        print(book)


def main():
    library = Library()

    while True:
        print("\nLibrary Menu")
        print("1. Add book")
        print("2. Register member")
        print("3. Show available books")
        print("4. Search books")
        print("5. Borrow book")
        print("6. Return book")
        print("7. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            title = input("Title: ").strip()
            author = input("Author: ").strip()
            isbn = input("ISBN: ").strip()
            print(library.add_book(title, author, isbn))

        elif choice == "2":
            name = input("Name: ").strip()
            member_id = input("Member ID: ").strip()
            print(library.register_member(name, member_id))

        elif choice == "3":
            display_books(library.list_available_books())

        elif choice == "4":
            term = input("Search title: ").strip()
            display_books(library.search_by_title(term))

        elif choice == "5":
            member_id = input("Member ID: ").strip()
            isbn = input("Book ISBN: ").strip()
            print(library.borrow_book(member_id, isbn))

        elif choice == "6":
            member_id = input("Member ID: ").strip()
            isbn = input("Book ISBN: ").strip()
            print(library.return_book(member_id, isbn))

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Please choose a number from 1 to 7.")


if __name__ == "__main__":
    main()
