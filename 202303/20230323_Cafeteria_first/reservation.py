table_reservation = {
    "table_one": {
        "name": "",
        "surname": "",
        "time": "",
        "table_size": "single",
        "table_status": "free"}
    ,
        "table_two": {
        "name": "",
        "surname": "",
        "time": "",
        "table_size": "double",
        "table_status": "free"
    }
}

# rezervacijos informacija
name = input("Enter your name: ")
surname = input("Enter your surname: ")
time = input("Enter reservation time. Please enter time like 18:00 or 17:30): ")
table_size = input("Enter table size (Single, Double or Family): ")


# tikrinam ar stalas užrezervuotas
for table, reservation in table_reservation.items():
    if reservation["name"] == name and reservation["surname"] == surname and reservation["time"] == time and reservation["table_size"] == table_size:
        reservation["table_status"] = "reserved"
        print("Reservation successfully created")
        break
    elif reservation["table_status"] == "free":
        print("We can accept Your reservation. Please choose from available tables and time. \n Available tables are: ")
        print(reservation["table_size"])
        

#     print("Available Time Slots:")
# for time, status in time_slots.items():
#     if status == "Free":
#         print(time)



#         print(f"Hello {name} {surname}, Your table is reserved for You at {time}. Please take your seats and choose from meniu")
#         break # čia kažkaip reikės paduoti meniu kad rinktusi
# else:
#     # jei stalas nerezervuotas siūlo pasirinkti stalą
#     available_table = ""
#     for table, reservation in table_reservation.items():
#         if reservation["Size"] == table_size and reservation["Name"] == "":
#             available_table = table
#             break