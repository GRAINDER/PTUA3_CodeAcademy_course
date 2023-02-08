# # if 11 != 10: #< ! neigiama ekspresija. nelygi kaip <>
# #     print("Yes")

# # print("Finishing program")


# number = int(input("Enter Your Number: "))

# if number >= 18:
#     print("You are allowed to enter")
# elif number == 50:
#     print("You entered 5!")
# elif number < 5:
#     print("It's les then 5")
# else:
#     print(f"You have entered {number}")


# print(not False or False)


# name = "Tom"

# if name == "Tom":
#     print("Nice to see you Tom")
# else:
#     print("welcome, user")


# my_dict = {"name": "Steven", "born": "1955-02-24", "interests": "Apples"}
# if my_dict["name"] == "Steven":
#     print("This guy does not like Windows")
# else:
#     print("No clue who this is")



# my_list = ["Paulius"]
# if not my_list:
#   print("oh no, list is empty")
# else:
#     print(f"List is not empty. It's contains {my_list}")







#     #1 Let user enter name, surname and age. Print if user is allowed to enter an online casino or not. 21 is the age cap.

# name = input("Enter Your name: ")
# surname = input("Enter Your surname: ")
# age = int(input("Enter Your age: "))

# if age < 21:
#     print(f"{name} {surname} your are not elegible to enter online casino !")
# else:
#     print(f"Welcome {name} {surname} to our online casino")






#     #2 Create a database (List of privileged users) print a specific message with a personal greeting if the user is a privileged and just "Welcome otherwise"

# privilege_users = ["Paulius", "Vygantas", "Brigita"]

# user_name = input("Enter You User name: ")

# if  user_name in privilege_users:
#     print("Welcome to our Python community")
# else:
#     print("Hello, User, if You want to be privilege user, you must register")



#     #3 allow user to enter two numbers, print out which one is higher than the other, or are they equal?

# number_one = int(input("Insert first number: "))
# number_two = int(input("Insert second number: "))

# if number_one > number_two:
#     diff = number_one - number_two
#     print(f"Number one is bigger of number two by {diff}")
# elif number_one == number_two:
#     print(f"Number one is equal to number two {number_one} = {number_two}")



    #4 Write a small calculator application, that allows user to enter two numbers and a symbol, given and then do the operation and print an answer.

# number_one = int(input("Enter first number: "))
# function = input("Enter function (+, -, /, *): ")
# number_two = int(input("Enter second number: "))

# if function == "+":
#     sum = number_one + number_two
#     print(f"sum of two numbers = {sum}")
# elif function == "-":
#     diff = number_one - number_two
#     print(f"different of two numbers = {diff}")
# elif function == "*":
#     mult = number_one * number_two
#     print(f"multiplication of two numbers = {mult}")
# elif function == "-":
#     divide = number_one / number_two
#     print(f"division of two numbers = {divide}")


# number_one, operator, number_two = input("Enter number: ").split()
# number_one = int(number_one)
# number_two = int(number_two)

# operator_list = ["+", "-", "/", "*"]

# if operator in operator_list:
#     answer = number_one + number_two
# elif operator in operator_list:
#     answer = number_one - number_two
# elif operator in operator_list:
#     answer = number_one / number_two
# elif operator in operator_list:
#     answer = number_one * number_two
#     print(answer)










# create a number guessing game from 1-10, with random library. (IDEA FOR LATER MAYBE)
import random
print("Welcome to guessing game! You have to guess the correct number in 3 tries!")
random_int = random.randint(1,10)
tries = 3

while tries != 0:
    try:
        number = int(input("Guess the number!: "))
        tries = tries - 1        
        if number == random_int:
            tries += 1            
            print("Correct! The number was:",random_int)
            break       
        else:
            print("Wrong! Try again!")
            if number > random_int:
                print("The correct answer is lower than your current answer")
            else:
                print("The correct answer is higher than your current answer")
            print("Tries left:", tries)
    except ValueError:
        print("Must input a number")
        pass
    if tries == 0:
        print("Answer was:", random_int)