# You have been asked to create a simple inventory management system for a small retail store. You need to define a 
# Product class using the dataclass module that represents a product in the store. Each Product should have a unique ID, a name, a description, a price, and a quantity in  stock. 
# You also need to implement a method calculate_total_cost that calculates 
# the total cost of a given number of items of the product, taking into account any discounts that may apply


# from dataclasses import dataclass
# from typing import Optional


# @dataclass
# class Product:
#     ID: int
#     name: str
#     description: str
#     price: float
#     quantity: int

#     def calculate_total_cost(self, number_of_items: int = None) -> float:
#         if number_of_items is None:
#             return self.price * self.quantity
#         else: 
#             return self.price * number_of_items


# product_one = Product(1,"Morka", "Plauta",1.25,10)
# print(product_one.calculate_total_cost())
# print(product_one.calculate_total_cost(2))


# You need to create a program to manage a list of books in a library. 
# Each book has a title, an author, a publication year, and an ISBN. 
# You need to define a Book class using the dataclass module that contains attributes for these properties. 
# You also need to implement a Library class that manages a list of books. 
# The Library class should allow you to add and remove books from the library, search for books by title or author, and display the list of books currently in the library.

from dataclasses import dataclass
from typing import List

@dataclass
class Book:
    title: str
    author: str
    publication_year: int
    ISBN: str


@dataclass
class Library:
    list_of_books: List[Book] = []

    def add_book(self) -> Book:
        return self.list_of_books.append()
    
    def remove_book(self) -> Book:
        return self.list_of_books.remove()
    

    def search_by_author(self, author: str) -> Book:
        return [book for book in self.list_of_books if book.author == author]


    def search_by_title(self, title: str) -> Book:
        return [book for book in self.list_of_books if book.author == title]


new_book = Book("Mauglis", "Maironis", 1995, "SFSFNSOFS")
print(new_book.title, new_book.author, new_book.publication_year, new_book.ISBN)

