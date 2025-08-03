# Objective: Solidify understanding of basic OOP concepts in Python by implementing a system that tracks books in a library, 
# focusing on classes, object instantiation, and method invocation.

class Book:
#    """A class representing a book with title, author, and availability."""

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute

    def check_out(self):
        """Mark the book as checked out."""
        self._is_checked_out = True

    def return_book(self):
        """Mark the book as returned (available)."""
        self._is_checked_out = False

    def is_checked_out(self):
        """Check if the book is currently checked out."""
        return self._is_checked_out


class Library:
#    """A class representing a library that manages books."""

    def __init__(self):
        self._books = []  # Private list of Book instances

    def add_book(self, book):
        """Add a new book to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """Mark the book with the given title as checked out."""
        for book in self._books:
            if book.title == title:
                if not book.is_checked_out():
                    book.check_out()
                    print(f"Checked out: '{title}'")
                else:
                    print(f"Book '{title}' is already checked out.")
                return
        print(f"Book '{title}' not found in library.")

    def return_book(self, title):
        """Mark the book with the given title as returned."""
        for book in self._books:
            if book.title == title:
                if book.is_checked_out():
                    book.return_book()
                    print(f"Returned: '{title}'")
                else:
                    print(f"Book '{title}' was not checked out.")
                return
        print(f"Book '{title}' not found in library.")

    def list_available_books(self):
        """List all books that are currently available."""
        available_books = [book for book in self._books if not book.is_checked_out()]
        if not available_books:
            print("No books currently available.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")


