# library_system/book.py

from datetime import datetime, timedelta


class Book:
    """Represents a book in the library"""

    def __init__(self, title, author, isbn, year=None):
        self.title = title.strip()
        self.author = author.strip()
        self.isbn = isbn.strip()
        self.year = year
        self.available = True
        self.borrowed_by = None
        self.due_date = None
        self.date_added = datetime.now().strftime("%Y-%m-%d")

    def check_out(self, member_id, loan_days=14):
        """Check out the book to a member"""
        if not self.available:
            return False, "Book is already checked out."

        self.available = False
        self.borrowed_by = member_id
        due = datetime.now() + timedelta(days=loan_days)
        self.due_date = due.strftime("%Y-%m-%d")

        return True, f"Book checked out. Due date: {self.due_date}"

    def return_book(self):
        """Return the book"""
        if self.available:
            return False, "Book is already available."

        was_overdue = self.is_overdue()

        self.available = True
        self.borrowed_by = None
        self.due_date = None

        if was_overdue:
            return True, "Book returned (was overdue)."

        return True, "Book returned successfully."

    def is_overdue(self):
        """Check if book is overdue"""
        if not self.available and self.due_date:
            due = datetime.strptime(self.due_date, "%Y-%m-%d")
            return datetime.now() > due
        return False

    def days_overdue(self):
        """Calculate number of overdue days"""
        if self.is_overdue():
            due = datetime.strptime(self.due_date, "%Y-%m-%d")
            return (datetime.now() - due).days
        return 0

    def to_dict(self):
        """Convert object to dictionary for JSON saving"""
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "year": self.year,
            "available": self.available,
            "borrowed_by": self.borrowed_by,
            "due_date": self.due_date,
            "date_added": self.date_added
        }

    @classmethod
    def from_dict(cls, data):
        """Recreate object from dictionary"""
        book = cls(
            data["title"],
            data["author"],
            data["isbn"],
            data.get("year")
        )
        book.available = data["available"]
        book.borrowed_by = data.get("borrowed_by")
        book.due_date = data.get("due_date")
        book.date_added = data.get("date_added")
        return book

    def __str__(self):
        status = "Available" if self.available else f"Borrowed by {self.borrowed_by} (Due: {self.due_date})"
        return f"{self.title} by {self.author} | ISBN: {self.isbn} | {status}"
