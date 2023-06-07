from dataclasses import dataclass
from typing import List

@dataclass
class Table:
    reservation_name: str
    reservation_surname: str
    reservation_time: str
    table_size: str
    table_status: str

@dataclass
class Restaurant:
    tables: List[Table] = []

    def reserve_table(self, table: Table) -> None:
        self.tables.append(table)

    # def remove_book(self, isbn: str) -> bool:
    #     for i, book in enumerate(self.books):
    #         if book.isbn == isbn:
    #             del self.books[i]
    #             return True
    #     return False

    def search_by_author(self, size: str, status: str) -> List[Table]:
        return [table for table in self.tables if table.table_size == size and table.table_status == status]

    def check_available_reservation(self, name: str, surname: str, time: str) -> List[Table]:
        return [table for table in self.tables if table.reservation_name == name and table.reservation_surname == surname and table.reservation_time == time]


    def all_reservations(self) -> None:
        for table in self.tables:
            print(f"{table.reservation_name}  {table.reservation_surname}, reserved {table.reservation_time}, on time: {table.table_size}")



first_reservation = Table(reservation_name="Paulius", reservation_surnname="Dailidonis", table_size="Single")
# seciond_reservation = Table(reservation_name="To Kill a Mockingbird", author="Harper Lee", publication_year=1960, isbn="9780446310789")

booking = Restaurant()
booking.reserve_table(first_reservation)





# # library.add_book(book2)

# booking.check_available_reservation()

# book3 = Table(title="Pride and Prejudice", author="Jane Austen", publication_year=1813, isbn="9780486284736")
# booking.reserve_table(book3)

# print(library.search_by_title("To Kill a Mockingbird"))
# print(library.search_by_author("F. Scott Fitzgerald"))

# library.remove_book("9780446310789")

# library.display_books()