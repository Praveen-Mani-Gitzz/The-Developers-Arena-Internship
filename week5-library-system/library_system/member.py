# library_system/member.py

class Member:
    """Represents a library member"""

    def __init__(self, name, member_id):
        self.name = name.strip()
        self.member_id = member_id.strip()
        self.borrowed_books = []   # store ISBNs
        self.max_books = 5

    def can_borrow(self):
        """Check if member can borrow more books"""
        return len(self.borrowed_books) < self.max_books

    def borrow_book(self, isbn):
        """Add book ISBN to borrowed list"""
        if not self.can_borrow():
            return False, "Borrow limit reached."

        if isbn in self.borrowed_books:
            return False, "Book already borrowed."

        self.borrowed_books.append(isbn)
        return True, "Book added to member record."

    def return_book(self, isbn):
        """Remove book ISBN from borrowed list"""
        if isbn not in self.borrowed_books:
            return False, "Book not found in member record."

        self.borrowed_books.remove(isbn)
        return True, "Book removed from member record."

    def to_dict(self):
        """Convert member to dictionary for JSON saving"""
        return {
            "name": self.name,
            "member_id": self.member_id,
            "borrowed_books": self.borrowed_books,
            "max_books": self.max_books
        }

    @classmethod
    def from_dict(cls, data):
        """Recreate member from dictionary"""
        member = cls(data["name"], data["member_id"])
        member.borrowed_books = data.get("borrowed_books", [])
        member.max_books = data.get("max_books", 5)
        return member

    def __str__(self):
        return f"{self.name} (ID: {self.member_id}) | Borrowed: {len(self.borrowed_books)} books"
