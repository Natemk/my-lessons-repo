from library_system.book import Book
from library_system.member import Member


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, title, author, isbn):
        if self.find_book_by_isbn(isbn):
            return "ISBN already exists."
        self.books.append(Book(title, author, isbn))
        return "Book added."

    def register_member(self, name, member_id):
        if self.find_member_by_id(member_id):
            return "Member ID already exists."
        self.members.append(Member(name, member_id))
        return "Member registered."

    def list_available_books(self):
        return [book for book in self.books if book.available]

    def search_by_title(self, search_term):
        term = search_term.strip().lower()
        return [book for book in self.books if term in book.title.lower()]

    def find_book_by_isbn(self, isbn):
        isbn = isbn.strip()
        return next((book for book in self.books if book.isbn == isbn), None)

    def find_member_by_id(self, member_id):
        member_id = member_id.strip()
        return next((member for member in self.members if member.member_id == member_id), None)

    def borrow_book(self, member_id, isbn):
        member = self.find_member_by_id(member_id)
        book = self.find_book_by_isbn(isbn)
        if member is None:
            return "Member not found."
        if book is None:
            return "Book not found."
        if member.borrow_book(book):
            return f"{member.name} borrowed '{book.title}'."
        return f"'{book.title}' is unavailable."

    def return_book(self, member_id, isbn):
        member = self.find_member_by_id(member_id)
        book = self.find_book_by_isbn(isbn)
        if member is None:
            return "Member not found."
        if book is None:
            return "Book not found."
        if member.return_book(book):
            return f"{member.name} returned '{book.title}'."
        return f"{member.name} did not borrow '{book.title}'."
