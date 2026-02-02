from library_system.book import Book

b = Book("Python Crash Course", "Eric Matthes", "12345")
print(b)

success, msg = b.check_out("MEM001")
print(msg)
print(b)

success, msg = b.return_book()
print(msg)
print(b)
