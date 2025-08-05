# so we will add an entirely different code for another task to this code.
# the reason i am adding the next segment of codes is that the file name assisgned in ALX training happen to be the same
# and python is not accepting duplicate file names in the same folder. 
# The code begins next line. i just hope it works and not affect the functionality of the other codes.

# Import the Book class from the book_class module
from book_class import Book

def main():
    # Creating an instance of Book
    my_book = Book("1984", "George Orwell", 1949)

    # Demonstrating the __str__ method (human-friendly description)
    print(my_book)  # Output: 1984 by George Orwell, published in 1949

    # Demonstrating the __repr__ method (official object representation)
    print(repr(my_book))  # Output: Book('1984', 'George Orwell', 1949)

    # Deleting the book instance to trigger the __del__ method
    del my_book  # Output: Deleting 1984

# This ensures the main() function runs only when the file is executed directly
if __name__ == "__main__":
    main()


# Mastering Inheritance and Composition in Python
#Objective: Deepen your understanding of inheritance and composition in Python by 
# creating a system that models a library with different types of books.
#main.py (Provided for Testing): library_system.py

# main.py

from library_system import Book, EBook, PrintBook, Library

def main():
    # Create a Library instance
    my_library = Library()

    # Create instances of each type of book
    classic_book = Book("Pride and Prejudice", "Jane Austen")
    digital_novel = EBook("Snow Crash", "Neal Stephenson", 500)
    paper_novel = PrintBook("The Catcher in the Rye", "J.D. Salinger", 234)

    # Add books to the library
    my_library.add_book(classic_book)
    my_library.add_book(digital_novel)
    my_library.add_book(paper_novel)

    # List all books in the library
    my_library.list_books()

if __name__ == "__main__":
    main()  


