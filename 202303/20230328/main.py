# my_number = 5


# def add(number1: int, number2: int) -> int:
#     return number1 + number7)

# from collections.abc import Callable

# def say_hello(name: str) -> str:
#   print(f"hello {name}")

# def another_function(f: Callable, *args) -> None:
#   f(*args)

# # another_function(say_hello, "Paulius")


# def outer():
#     def inner():
#         print("I am function inner()!")

#     # Function outer() returns function inner()
#     return inner


# function = outer()
# print(function)
# # <function outer.<locals>.inner at 0x7f18bc85faf0>
# function()
# # I am function inner()!

# outer()()
# # I am function inner()!


# reverse = lambda a, b: a + b
# print(reverse(1, 2))






#Write a Python program to find if a given string starts with a given character using Lambda. Sample Output: True False


# check_string = lambda x: x.startswith("S")
# print(check_string("Paulius"))
# print(check_string("Saulius"))


# #Write a Python program to create a lambda function that adds 15 to a given number passed in as an argument, 
# #also create a lambda function that multiplies argument x with argument y and print the result

# adding_number = lambda x: (x+15)
# print(adding_number(1))

# adding_number = lambda x, y: (x+15)*y
# print(adding_number(1,2))


#Write a Python program to add two given lists using map and lambda.
# #3.1
# a = [1, 2, 3, 4]
# b = [4, 3, 2, 1]

# adding_list = lambda a, b: a + b

# print(adding_list(a, b))


# #3.2
# list_one = [1, 2, 3, 4]
# list_two = [4, 3, 2, 1]

# sum_list = list(map(lambda x, y: x + y,list_one, list_two))

# print(sum_list)

# #Write a Python program to square and cube every number in a given list of integers using Lambda


# numbers = [1, 2, 3, 4, 5]

# square = lambda x: x ** 2
# cube = lambda x: x ** 3


# squared_numbers = list(map(square, numbers))
# cubed_numbers = list(map(cube, numbers))

# print(squared_numbers)
# print(cubed_numbers)

# list_nums = [1, 2, 3, 4, 5] 
# square_cube_list = map(lambda x: [x ** 2, x ** 3], (list_nums)) 
# print(list(square_cube_list))




# #Write a Python program to extract year, month, date and time using Lambda. Sample Output: 2020-01-15 09:03:32.744178 2020 1 15 09:03:32.744178

# import datetime

# now_time = datetime.datetime.now()
# print(now_time)

# year = lambda x: x.year
# month = lambda x: x.month
# day = lambda x: x.day
# t = lambda x: x.time()

# print(year(now_time), month(now_time), day(now_time), t(now_time))


#Write a Python program to sort a list of tuples using Lambda. 
#Original list of tuples: 

#Sorting the List of Tuples: [('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

my_tuple_list = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)] 

sorted_tuple_list = sorted(my_tuple_list, key = lambda a: a[1], reverse = True)
print(sorted_tuple_list)


# animals = ["ferret", "vole", "dog", "gecko"]
# sorted(animals, key=len)
# ['dog', 'vole', 'gecko', 'ferret']


# #  Write a Python program to sort a list of dictionaries using Lambda.
# # list_of_dict =  [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}] 

# # Sorting the List of dictionaries : [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, 
# # {'make': 'Samsung', 'model': 7, 'color': 'Blue'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}]

# sorted = sorted(list_of_dict, key=lambda x: x['color'])
# print(sorted)




# def f(a, b, c):
#     return a + b + c


# list(map(f, [1, 2, 3], [10, 20, 30], [100, 200, 300]))
# # [111, 222, 333]