from .library import Library


def display_books(books):
    """Display a list of books with their information."""
    if not books:
        print("No books available.")
        return
    for book in books:
        print(f"  - {book.get_info()}")


def main():
    """Main console application for the Library Management System."""
    library = Library()
    print("\n=== Welcome to Library Management System ===")

    while True:
        print("\n--- Library Menu ---")
        print("1. Add book")
        print("2. Register member")
        print("3. Show available books")
        print("4. Search books by title")
        print("5. Borrow book")
        print("6. Return book")
        print("7. List all members and their books")
        print("8. Exit")

        choice = input("\nChoose an option (1-8): ").strip()

        if choice == "1":
            print("\n--- Add Book ---")
            title = input("Book Title: ").strip()
            author = input("Author: ").strip()
            isbn = input("ISBN: ").strip()
            if title and author and isbn:
                print(f"✓ {library.add_book(title, author, isbn)}")
            else:
                print("✗ Please fill in all fields.")

        elif choice == "2":
            print("\n--- Register Member ---")
            name = input("Member Name: ").strip()
            member_id = input("Member ID: ").strip()
            if name and member_id:
                print(f"✓ {library.register_member(name, member_id)}")
            else:
                print("✗ Please fill in all fields.")

        elif choice == "3":
            print("\n--- Available Books ---")
            display_books(library.list_available_books())

        elif choice == "4":
            print("\n--- Search Books ---")
            term = input("Search title (partial match): ").strip()
            if term:
                results = library.search_by_title(term)
                print(f"Found {len(results)} book(s):")
                display_books(results)
            else:
                print("✗ Please enter a search term.")

        elif choice == "5":
            print("\n--- Borrow Book ---")
            member_id = input("Member ID: ").strip()
            isbn = input("Book ISBN: ").strip()
            if member_id and isbn:
                print(f"✓ {library.borrow_book(member_id, isbn)}")
            else:
                print("✗ Please fill in all fields.")

        elif choice == "6":
            print("\n--- Return Book ---")
            member_id = input("Member ID: ").strip()
            isbn = input("Book ISBN: ").strip()
            if member_id and isbn:
                print(f"✓ {library.return_book(member_id, isbn)}")
            else:
                print("✗ Please fill in all fields.")

        elif choice == "7":
            print("\n--- Members and Their Books ---")
            if library.members:
                for member in library.members:
                    member.display_info()
            else:
                print("No members registered yet.")

        elif choice == "8":
            print("\nThank you for using Library Management System. Goodbye!")
            break

        else:
            print("✗ Invalid choice. Please choose a number from 1 to 8.")


if __name__ == "__main__":
    main()
