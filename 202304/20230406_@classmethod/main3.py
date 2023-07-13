class Book:
    def __init__(self, title, author, copies):
        self.title = title
        self.author = author
        self.copies = copies

    def __str__(self):
        return f"{self.title} by {self.author} ({self.copies} copies available)"

class User:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def __str__(self):
        return self.name

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def register_user(self, user):
        self.users.append(user)

    def borrow_book(self, user, book_title):
        for book in self.books:
            if book.title == book_title and book.copies > 0:
                book.copies -= 1
                user.borrowed_books.append(book)
                print(f"{user.name} has borrowed '{book.title}' by {book.author}")
                return True
        print(f"Sorry, '{book_title}' is not available for borrowing.")
        return False

    def return_book(self, user, book_title):
        for book in user.borrowed_books:
            if book.title == book_title:
                book.copies += 1
                user.borrowed_books.remove(book)
                print(f"{user.name} has returned '{book.title}' by {book.author}")
                return True
        print(f"Sorry, '{book_title}' was not borrowed by {user.name}.")
        return False

    def list_books(self):
        print("Library Collection:")
        for book in self.books:
            print(book)

    def list_borrowed_books(self, user):
        print(f"Borrowed Books by {user.name}:")
        for book in user.borrowed_books:
            print(book)

# Example usage:
# Create some books
book1 = Book("The Catcher in the Rye", "J.D. Salinger", 3)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 5)
book3 = Book("1984", "George Orwell", 2)

# Create some users
user1 = User("Alice")
user2 = User("Bob")

# Create a library
library = Library()

# Add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Register users to the library
library.register_user(user1)
library.register_user(user2)

# List all books in the library
library.list_books()

# Alice borrows a book
library.borrow_book(user1, "The Catcher in the Rye")

# Bob borrows a book
library.borrow_book(user2, "1984")

# List borrowed books by Alice and Bob
library.list_borrowed_books(user1)
library.list_borrowed_books(user2)

# Alice returns a book
library.return_book(user1, "The Catcher in the Rye")

# Bob returns a book
library.return_book(user2, "1984")

# List borrowed books by Alice and Bob after returning
library.list_borrowed_books(user1)
library.list_borrowed_books(user2)

# List all books in the library after borrowing and returning
library.list_books()
