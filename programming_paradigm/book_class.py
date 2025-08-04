# Objective: Master Python magic methods by implementing a Book class that incorporates constructors (__init__), destructors (__del__), and the 
# representation methods (__str__ and __repr__).

# book_class.py

class Book:
    # Constructor: initializes a new Book instance with title, author, and year
    def __init__(self, title, author, year):
        self.title = title        # Title of the book
        self.author = author      # Author of the book
        self.year = year          # Publication year
        print(f"Book created: {self.title}")

    # Destructor: called automatically when an object is deleted
    def __del__(self):
        print(f"Deleting {self.title}")

    # __str__: returns a readable string for users (e.g., print statements)
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"

    # __repr__: returns a string that can be used to recreate the object
    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})" 
    
