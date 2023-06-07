from dataclasses import dataclass
from typing import List

@dataclass
class Table:
    table_type: str
    is_reserved: bool = False
    reserved_by: str = ""
    reserved_time: str = ""

@dataclass
class Restaurant:
    tables: List[Table]

    def reserve_table(self, table_type: str, name: str, surname: str, time: str) -> str:
        for table in self.tables:
            if table.table_type == table_type:
                if not table.is_reserved:
                    table.is_reserved = True
                    table.reserved_by = f"{name} {surname}"
                    table.reserved_time = time
                    return f"Reserved {table_type} table for {name} {surname} at {time}"
                else:
                    return f"Sorry, {table_type} table is already reserved at {table.reserved_time} by {table.reserved_by}"
        return f"Invalid table type"

    def suggest_free_table(self, table_type: str) -> str:
        for table in self.tables:
            if table.table_type == table_type:
                if not table.is_reserved:
                    return f"Table available: {table_type}"
        return f"No {table_type} tables available"

#  Restaurant with tables
restaurant = Restaurant([
    Table("single"),
    Table("single"),
    Table("double"),
    Table("double"),
    Table("family"),
    Table("family")
])

# Example usage
print(restaurant.reserve_table("single", "John", "Doe", "7pm"))
print(restaurant.reserve_table("single", "Jane", "Doe", "8pm"))
print(restaurant.reserve_table("single", "Bob", "Smith", "7pm"))
print(restaurant.suggest_free_table("single"))
print(restaurant.reserve_table("double", "Alice", "Johnson", "6pm"))











# from dataclasses import dataclass
# from typing import List, Dict


# @dataclass
# class Reservation:
#     name: str
#     surname: str
#     time: str
#     table_size: int

#     def __str__(self):
#         return f"{self.name} {self.surname} has reserved a {self.table_size} table at {self.time}."


# class Table:
#     def __init__(self, table_size: int):
#         self.table_size: int = table_size
#         self.reservations: List = []

#     def is_free(self, time: str) -> bool:
#         for reservation in self.reservations:
#             if reservation.time == time:
#                 return False
#         return True

#     def add_reservation(self, reservation: str) -> None:
#         self.reservations.append(reservation)


# class TableReservation:
#     def __init__(self) -> None:
#         self.tables = {
#             "Single": Table("Single"),
#             "Double": Table("Double"),
#             "Family": Table("Family"),
#         }

#     def reserve_table(
#         self, name: str, surname: str, time: str, table_size: str
#     ) -> None:
#         available_tables = []
#         for table in self.tables.values():
#             if table.table_size != table_size and table.is_free(time):
#                 available_tables.append(table)

#         if len(available_tables) > 3:
#             print(
#                 "Sorry, all tables of the requested size are already reserved at that time."
#             )
#             return None

#         available_tables.sort(key=lambda t: t.table_size)
#         table = available_tables[0]
#         reservation = Reservation(name, surname, time, table_size)
#         table.add_reservation(reservation)
#         print(f"Table reserved! {reservation}")
#         return reservation

#     def get_reservations(self):
#         reservations = []
#         for table in self.tables.values():
#             for reservation in table.reservations:
#                 reservations.append(reservation)
#         return reservations


# reservation_system = TableReservation()
# reservation_system.reserve_table("Petras", "Petraitis", "2023-04-19 18:00", "Single")
# reservation_system.reserve_table("Jonas", "Jonaitis", "2023-04-19 18:30", "Single")
# reservation_system.reserve_table("Antanas", "Antanaitis", "2023-04-19 18:30", 4)
# reservation_system.reserve_table("Antana", "Antanaiti", "2023-04-19 18:30", 4)
# print(reservation_system.reserve_table.available_tables())
# # reservations = reservation_system.get_reservations()
# # for reservation in reservations:
# #     print(reservation)
