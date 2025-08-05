# Mastering Inheritance and Composition in Python
# Objective: Deepen your understanding of inheritance and 
# composition in Python by creating a system that models a library with different types of books.

# library_system.py

# Base class representing a general Book
class Book:
    def __init__(self, title, author):
        self.title = title      # Title of the book
        self.author = author    # Author of the book

    def __str__(self):
        return f"Book: {self.title} by {self.author}"


# Derived class representing an EBook
class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)  # Call base class constructor
        self.file_size = file_size       # File size in MB

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}MB"


# Derived class representing a PrintBook
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)  # Call base class constructor
        self.page_count = page_count     # Number of pages

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Pages: {self.page_count}"


# Library class that manages a collection of books (composition)
class Library:
    def __init__(self):
        self.books = []  # List to store books

    def add_book(self, book):
        # Accepts any instance of Book, EBook, or PrintBook
        self.books.append(book)

    def list_books(self):
        # Print the details of each book in the library
        if not self.books:
            print("The library has no books.")
        else:
            for book in self.books:
                print(book)  # Will call each book's __str__ method

