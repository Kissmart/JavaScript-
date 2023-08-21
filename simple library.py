class Author:
    def __init__(self, name, birth_year):
        self.name = name
        self.birth_year = birth_year

    def __str__(self):
        return f"{self.name} ({self.birth_year})"


class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __str__(self):
        return f"{self.title} by {self.author}, {self.publication_year}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        if not self.books:
            print("No books in the library.")
            return
        print("Books in the library:")
        for book in self.books:
            print("-", book)


# Creating authors
author1 = Author("J.K. Rowling", 1965)
author2 = Author("George Orwell", 1903)

# Creating books
book1 = Book("Harry Potter and the Sorcerer's Stone", author1, 1997)
book2 = Book("1984", author2, 1949)

# Creating a library and adding books
library = Library()
library.add_book(book1)
library.add_book(book2)

# Displaying books in the library
library.display_books()
