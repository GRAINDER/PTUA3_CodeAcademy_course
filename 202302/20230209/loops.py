# import time

# i = 0
# while i < 10:
#   print(i)
#   i += 1

# time.sleep(1)

# apples = 0
# while apples <= 10:
#     print(f"gathered apples so far: {apples}")
#     apples += 1
#     # apples = apples +1


# names = ["Antanas", "Mindaugas"]


# for name in names:
#     print(name)
#     print(type(name))
#     print(len(name))


# for letter in "Antanas":
#     print(letter)


# my_items = {
#     "first_time": 1,
#      "last_itme": 2,
#  }

# for key in my_items.items():
#     print(key, my_items)


# my_number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# #range nurodo kiek iteraciju galima daryti. range(start, stop, step)


# for number in my_number_list:
#     print(number)


# for _ in range(0, 10, 2):
#     print("x")



# import time

# seconds = 1

# while True:
#     print("Žalgiris")
#     time.sleep(1)
#     seconds += 1
#     if seconds == 3:
#         break



# my_number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# #range nurodo kiek iteraciju galima daryti. range(start, stop, step)


# for number in my_number_list:
#     print(number)
#     if number >=9:
#         break




# my_number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#range nurodo kiek iteraciju galima daryti. range(start, stop, step)


# for _ in range(0,5):
#     for number in my_number_list:
#         print(number)
#         if number >=9:
#             break



# # for number in my_number_list:
# #     if number >=9:
# #         break


# my_number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# for number in my_number_list:
#     if number == 7:
#         continue   
#     print(number)





# 1 uzduotis 
# Create a variables containing strings for username and password. 
# Start Endless loop allowing to enter username and password. 
# If credentials are correct stop endless loop and print greeting message.

# login_name = {"Username": "Paulius", "Password": "Slaptazodis"}

# username = input("Username: ")
# password = input("Password: ")


# for username, password in login_name.items():
#     if username == "Paulius" and password == "Slaptazodis":
#         print(f"Welcome {username}")
#         break



# USERNAME = "Paulius"
# PASSWORD = "Slaptazodis"


# while True:
#     username = input("Username: ")
#     password = input("Password: ")
#     if username  == USERNAME and password == PASSWORD:
#         print(f"Welcome {username}")
#         break
#     print("Incorrect username or password")





#2 Allow user to enter 10 integers, and then print the sum and average of those entered numbers.

# numbers = []

# while len(numbers) <= 10:
#     score = int(input("Please enter 10 integers: "))
#     if (1 <= numbers <= 10):
#         sum(numbers)
#     else: 
#         break
        
# print(numbers)


# # Create a list of letters and generate 5 diferent words for 5 different lists. (A word must the size between 5 and letters)
# # Then count how many each letters are in those words.
# # Return answer as a dictionary. {'letter': count}
# # And all words sorted in one list.


letters = ["a", "s", "l", "k", "j", "m", "e", "d", "f", "g", "h", "i", "o", "k", "p", "q", "r", "s", "t", "u"]

return_list1 = []
return_list2 = []
return_list3 = []
return_list4 = []
return_list5 = []


for letter in letters: 

    return_list1.append(letter[0])


print(return_list1)




