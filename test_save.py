"""
Simple test to demonstrate saving to txt files
"""

from library_system.library import Library

# Create library instance (auto-loads from txt files)
library = Library()

print("Adding books...")
library.add_book("Python Guide", "John Doe", "ISBN001")
library.add_book("Clean Code", "Robert Martin", "ISBN002")
library.add_book("The Pragmatic Programmer", "Hunt & Thomas", "ISBN003")

print("Registering members...")
library.register_member("Alice Johnson", "M001")
library.register_member("Bob Smith", "M002")

print("Borrowing books...")
library.borrow_book("M001", "ISBN001")
library.borrow_book("M002", "ISBN002")

print("\nAvailable books:")
for book in library.list_available_books():
    print(f"  - {book.get_info()}")

print("\nMembers and their borrowed books:")
for member in library.members:
    member.display_info()

print("\n✓ All data saved to:")
print("  - library_data/books.txt")
print("  - library_data/members.txt")
