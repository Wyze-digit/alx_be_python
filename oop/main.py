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

