class Member:
    def __init__(self, name, member_id):
        self.name = name.strip()
        self.member_id = member_id.strip()
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.borrow()
            self.borrowed_books.append(book)
            return True
        return False

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return True
        return False

    def display_info(self):
        if self.borrowed_books:
            titles = [book.title for book in self.borrowed_books]
            print(f"{self.name} ({self.member_id}) - Borrowed: {', '.join(titles)}")
        else:
            print(f"{self.name} ({self.member_id}) - Borrowed: None")
