import json
import os
from datetime import datetime
from .book import Book
from .member import Member


class Library:

    def __init__(self):
        self.books = {}      # isbn -> Book
        self.members = {}    # member_id -> Member
        self.data_folder = "data"
        self.books_file = os.path.join(self.data_folder, "books.json")
        self.members_file = os.path.join(self.data_folder, "members.json")

        self.load_data()

    # -------------------------
    # BOOK MANAGEMENT
    # -------------------------

    def add_book(self, title, author, isbn, year=None):
        if isbn in self.books:
            return False, "Book with this ISBN already exists."

        book = Book(title, author, isbn, year)
        self.books[isbn] = book
        return True, "Book added successfully."

    def remove_book(self, isbn):
        if isbn not in self.books:
            return False, "Book not found."

        if not self.books[isbn].available:
            return False, "Cannot remove borrowed book."

        del self.books[isbn]
        return True, "Book removed successfully."

    def find_book(self, keyword):
        results = []
        keyword = keyword.lower()

        for book in self.books.values():
            if (keyword in book.title.lower() or
                keyword in book.author.lower() or
                keyword in book.isbn.lower()):
                results.append(book)

        return results

    # -------------------------
    # MEMBER MANAGEMENT
    # -------------------------

    def register_member(self, name, member_id):
        if member_id in self.members:
            return False, "Member ID already exists."

        member = Member(name, member_id)
        self.members[member_id] = member
        return True, "Member registered successfully."

    # -------------------------
    # BORROW / RETURN
    # -------------------------

    def borrow_book(self, member_id, isbn):
        if member_id not in self.members:
            return False, "Member not found."

        if isbn not in self.books:
            return False, "Book not found."

        member = self.members[member_id]
        book = self.books[isbn]

        if not member.can_borrow():
            return False, "Member reached borrow limit."

        success, message = book.check_out(member_id)
        if not success:
            return False, message

        member.borrow_book(isbn)
        return True, message

    def return_book(self, member_id, isbn):
        if member_id not in self.members:
            return False, "Member not found."

        if isbn not in self.books:
            return False, "Book not found."

        member = self.members[member_id]
        book = self.books[isbn]

        success, message = book.return_book()
        if not success:
            return False, message

        member.return_book(isbn)
        return True, message

    # -------------------------
    # STATISTICS
    # -------------------------

    def get_statistics(self):
        total_books = len(self.books)
        available_books = sum(1 for b in self.books.values() if b.available)
        borrowed_books = total_books - available_books
        total_members = len(self.members)
        overdue_books = sum(1 for b in self.books.values() if b.is_overdue())

        return {
            "total_books": total_books,
            "available_books": available_books,
            "borrowed_books": borrowed_books,
            "total_members": total_members,
            "overdue_books": overdue_books
        }

    # -------------------------
    # FILE OPERATIONS
    # -------------------------

    def save_data(self):
        os.makedirs(self.data_folder, exist_ok=True)

        try:
            with open(self.books_file, "w") as f:
                json.dump([b.to_dict() for b in self.books.values()], f, indent=4)

            with open(self.members_file, "w") as f:
                json.dump([m.to_dict() for m in self.members.values()], f, indent=4)

            return True, "Data saved successfully."

        except Exception as e:
            return False, f"Error saving data: {e}"

    def load_data(self):
        if not os.path.exists(self.data_folder):
            return

        try:
            if os.path.exists(self.books_file):
                with open(self.books_file, "r") as f:
                    books_data = json.load(f)
                    for b in books_data:
                        book = Book.from_dict(b)
                        self.books[book.isbn] = book

            if os.path.exists(self.members_file):
                with open(self.members_file, "r") as f:
                    members_data = json.load(f)
                    for m in members_data:
                        member = Member.from_dict(m)
                        self.members[member.member_id] = member

        except Exception:
            print("Error loading data. Starting fresh.")
