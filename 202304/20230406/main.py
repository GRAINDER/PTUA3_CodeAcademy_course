# squares = []
# for number in range(10):
#     squares.append(number * number)
# print(squares)


# my_names = ["Paulius", "Ignas", "Jonas", "Albertas", "Mindaugas"]
# for names in my_names:
#     if len(names)>=5:
#         print(names)

# my_names_two= ["Paulius", "Ign", "Jonas", "Albertas", "Mindaugas"]
# my_names2 = [names_two for names_two in my_names_two if len(names_two)>=5]
# print(my_names2)

# my_smth ={
#     'Alpha': 1,
#     'Beta': 2,
# }

# squares = {i: i * i for i in range(10)}
# print(squares)


# my_dict = {'Alpha': 15, 'Beta': 25, 'Gamma': 35, 'Delta': 45, 'Epsilon': 55}

# my_new_dict =  {key.upper(): int(str(value)[::-1]) for key, value in my_dict.items()}


# print(my_new_dict)


# my_new_dict = {key.upper(): int(str(value)[::-1]) for key, value


# my_names = ["Paulius", "Ignas", "Jonas", "Albertas", "Mindaugas"]
# my_dict ={}
# for count, value in enumerate(my_names):
#     my_dict[count] = value

# print(my_dict)


# my_names = ["Paulius", "Ignas", "Jonas", "Albertas", "Mindaugas"]
# my_dict = {key: name for key, name in enumerate(my_names, start=1)}

# print(my_dict)


# create a class to represent a library system.
# The library system should have a collection of books that can be borrowed by users.
# Users can register to the library system, borrow books and return books.
# The library system should keep track of the books borrowed by users and the number of available copies of each book.

book_library = {
    'Maironis': 'Jurate ir Kastytis',   
    'Neris': 'Egle Zalciu karaliene', 
    'Brazdionis': 'Simta metu as gyvensiu'}

borrowed_library = {}


class Library:
    def __init__(self) -> dict:
        self.books = book_library
        self.borrows = borrowed_library

    def add_book(self, book_name: str, author: str) -> str:
        self.book_name = book_name
        self.author = author

        if book_name in self.books:
            print(f"{book_name} already exists in the library.")
        else:
            self.books[book_name] = self.author
            print(f"{book_name} by {author} has been added to the library.")

    def borrow_book(self, borrow_book_name: str, borrow_author: str) -> str:
        self.borrow_book_name = borrow_book_name
        self.borrow_author = borrow_author

        if borrow_book_name in self.borrows:
            self.borrows = self.borrows.pop(borrow_book_name)
            print(f"Yes, book {borrow_book_name} is available")
        else:
            print(f"{borrow_book_name} by {borrow_author} is not available now")



new_book = Library()
new_book.add_book("Maironis", "Jurate ir Kastytis")
new_book.add_book("Neris", "Egle Zalciu karaliene")
new_book.add_book("Brazdionis", "Simta metu as gyvensiu")

new_book.borrow_book("Maironis", "Jurate ir Kastytis")

print(book_library)


# my_dict = {"name": "Paulius", "surname": "Dailidonis"}

# my_dict.pop("name")

# print(my_dict)