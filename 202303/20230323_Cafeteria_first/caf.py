Tables = {
    "name": "Paulius",
    "surname": "Dailidonis",
    "time": "16:30",
    "table_type": "Single",
}

restaurants_greetings = input(
    "Hello and welcome to our restaurant. Do you have reservation? Please enter Yes or No: "
)

if restaurants_greetings == "Yes":
    name = input("Please say Your name: ")
    surname = input("Please say Your name: ")
    time = input("Please enter your reservation time: ")
    table_type = input("Please enter table type: ")

for table, reservation in Tables.items():
    if (
        reservation[name] == name
        and reservation[surname] == surname
        and reservation[time] == time
    ):
        print(
            f"Hello {name} {surname}, Your table is reserved for You at {time}. Please take your seats and choose from meniu"
        )
        break  # čia kažkaip reikės paduoti meniu kad rinktusi


# if restaurants_greetings == "No":
#     print("One moment i will check our tables available")
#     table_type = input("Please enter table type: ")
#     name = input("Please say Your name: ")
#     surname = input("Please say Your name: ")
#     time = input("Please enter your reservation time: (16:00 or 17:00) ")

#     Tables["name"] = name
#     Tables["surname"] = surname
#     Tables["time"] = time
#     Tables["table_type"] = table_type


# print(Tables)


# print(Tables)


# class Tables:
#     def __init__(self):
#         Tables = {
#         "Single":{
#         "name": "Paulius",
#         "surname": "Dailidonis",
#         "time": "18:30",
#         "table_status": "Reserved"}
# }


#     def check_availability(self, name, surname, time):
#         for table, reservation in self.Tables.values():
#             if reservation["Name"] == name:
#                 print(f"Hello {name}, Your table is reserved for You at . Please take your seats and choose from meniu")
#             break # čia kažkaip reikės paduoti meniu kad rinktusi
