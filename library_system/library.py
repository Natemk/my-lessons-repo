from library_system.book import Book
from library_system.member import Member
from library_system.file_ops import read_file, write_file, append_file, pop_line, remove_by_value


class Library:
    def __init__(self, books_file="library_data/books.txt", members_file="library_data/members.txt"):
        self.books = []
        self.members = []
        self.books_file = books_file
        self.members_file = members_file
        self.load_from_files()

    def add_book(self, title, author, isbn):
        if self.find_book_by_isbn(isbn):
            return "ISBN already exists."
        self.books.append(Book(title, author, isbn))
        self.save_books()  # Write to txt file
        return "Book added."

    def register_member(self, name, member_id):
        if self.find_member_by_id(member_id):
            return "Member ID already exists."
        self.members.append(Member(name, member_id))
        self.save_members()  # Write to txt file
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
            self.save_books()   # Write to txt file
            self.save_members() # Write to txt file
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
            self.save_books()   # Write to txt file
            self.save_members() # Write to txt file
            return f"{member.name} returned '{book.title}'."
        return f"{member.name} did not borrow '{book.title}'."

    # ========== File Operations (Simple read/write/append/pop) ==========

    def save_books(self):
        """Write all books to txt file."""
        lines = []
        for book in self.books:
            status = "available" if book.available else "borrowed"
            line = f"{book.title}|{book.author}|{book.isbn}|{status}\n"
            lines.append(line)
        return write_file(self.books_file, lines)

    def save_members(self):
        """Write all members to txt file."""
        lines = []
        for member in self.members:
            borrowed = ",".join([book.isbn for book in member.borrowed_books])
            line = f"{member.name}|{member.member_id}|{borrowed}\n"
            lines.append(line)
        return write_file(self.members_file, lines)

    def load_from_files(self):
        """Read books and members from txt files."""
        try:
            # Load books from txt file
            book_lines = read_file(self.books_file)
            for line in book_lines:
                if line.strip():  # Skip empty lines
                    parts = line.strip().split('|')
                    if len(parts) >= 4:
                        title, author, isbn, status = parts[0], parts[1], parts[2], parts[3]
                        book = Book(title, author, isbn)
                        book.available = (status == "available")
                        self.books.append(book)
            
            # Load members from txt file
            member_lines = read_file(self.members_file)
            for line in member_lines:
                if line.strip():  # Skip empty lines
                    parts = line.strip().split('|')
                    if len(parts) >= 2:
                        name, member_id = parts[0], parts[1]
                        member = Member(name, member_id)
                        
                        # Restore borrowed books
                        if len(parts) >= 3 and parts[2]:
                            borrowed_isbns = parts[2].split(',')
                            for isbn in borrowed_isbns:
                                book = self.find_book_by_isbn(isbn)
                                if book:
                                    member.borrowed_books.append(book)
                        
                        self.members.append(member)
            
            return True
        except Exception as e:
            print(f"Error loading from files: {e}")
            return False

    def add_book_to_file(self, title, author, isbn):
        """Append a single book line to txt file."""
        line = f"{title}|{author}|{isbn}|available"
        return append_file(self.books_file, line)

    def add_member_to_file(self, name, member_id):
        """Append a single member line to txt file."""
        line = f"{name}|{member_id}|"
        return append_file(self.members_file, line)

    def remove_book_from_file(self, isbn):
        """Remove a book from txt file and memory."""
        self.books = [book for book in self.books if book.isbn != isbn]
        return remove_by_value(self.books_file, isbn)

    def remove_member_from_file(self, member_id):
        """Remove a member from txt file and memory."""
        self.members = [member for member in self.members if member.member_id != member_id]
        return remove_by_value(self.members_file, member_id)

    def clear_all_data(self):
        """Clear all data from both txt files."""
        self.books.clear()
        self.members.clear()
        write_file(self.books_file, [])
        return write_file(self.members_file, [])
