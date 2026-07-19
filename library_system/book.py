class Book:
    def __init__(self, title, author, isbn):
        self.title = title.strip()
        self.author = author.strip()
        self.isbn = isbn.strip()
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        if not self.available:
            self.available = True
            return True
        return False

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - {status}"
