# 📚 Library Management System

## 📝 Project Overview

The Library Management System is a console-based Python application developed using Object-Oriented Programming (OOP) principles. 

This system enables librarians to efficiently manage books and members, handle borrowing and returning operations, track overdue books, and maintain persistent data storage using JSON files.

The project demonstrates real-world software design using modular architecture and structured class relationships.

---

## 🎯 Project Objectives

The main objectives of this project are:

- Apply fundamental OOP principles (Classes, Objects, Encapsulation)
- Design interacting classes to model real-world systems
- Implement borrowing and returning workflows with due-date tracking
- Maintain persistent storage using JSON files
- Create a scalable and maintainable modular architecture
- Implement proper error handling and validation

---

## 🚀 Key Features

- Add new books to the library
- Remove books (if not currently borrowed)
- Register new members
- Borrow books with automatic due-date assignment
- Return books with overdue detection
- Search books by title, author, or ISBN
- View all books and registered members
- View library statistics (total books, available, borrowed, overdue)
- Save and load data using JSON files
- User-friendly console menu interface
- Structured modular code organization
- Comprehensive error handling

---

## 🏗️ System Architecture

The system is built using three primary classes:

### 📘 Book Class
Responsible for:
- Storing book details (title, author, ISBN, year)
- Tracking availability status
- Managing due dates
- Detecting overdue books
- Serializing and deserializing book data

### 👤 Member Class
Responsible for:
- Storing member information
- Tracking borrowed books
- Enforcing maximum borrow limits
- Serializing and deserializing member data

### 🏛️ Library Class
Acts as the central controller:
- Manages collections of books and members
- Coordinates borrowing and returning logic
- Implements search functionality
- Generates statistical summaries
- Handles file persistence (JSON)

This separation of responsibilities ensures clean object interaction and proper encapsulation.

---

## 📂 Project Structure



week5-library-system/
│
├── library_system/
│   ├── **init**.py
│   ├── book.py
│   ├── member.py
│   ├── library.py
│   └── main.py
│
├── data/
│   ├── books.json
│   ├── members.json
│   └── backup/
│
├── tests/
│   ├── test_book.py
│   ├── test_member.py
│   └── test_library.py
│
├── requirements.txt
├── README.md
└── .gitignore



No external dependencies are required. The project uses only Python’s built-in libraries.

---

## 💾 Data Persistence

- Books and members are stored in JSON format.
- Data is automatically loaded when the application starts.
- Users can save data before exiting.
- File operations include error handling for safe execution.

---

## 📊 Library Statistics

The system provides real-time statistics including:

- Total number of books
- Available books
- Borrowed books
- Total registered members
- Overdue books

These statistics help simulate real-world administrative insights.

---

## 🧪 Testing

Basic test files are included to validate:

- Book object behavior
- Member borrow-limit logic
- Library operational workflows

Testing ensures reliability and correctness of core features.

---

## ⚠️ Error Handling & Validation

The system handles:

- Duplicate ISBN entries
- Duplicate member IDs
- Borrowing unavailable books
- Exceeding borrow limits
- Returning books not borrowed
- File read/write exceptions
- Invalid user inputs

All critical operations include validation checks to maintain system integrity.

---

## 🧠 What I Learned

- Designing real-world systems using OOP principles
- Managing object relationships effectively
- Coordinating multi-class interactions
- Implementing serialization and deserialization using JSON
- Structuring modular and maintainable codebases
- Applying clean separation of concerns

---

## ✅ Conclusion

The Library Management System demonstrates the practical implementation of Object-Oriented Programming concepts in building a structured, scalable, and maintainable application. 


