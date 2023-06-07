# a = range(5)
# list(a)


# def infinite_sequence():
#     num = 0
#     while True:
#         yield num
#         num += 1


# gen = infinite_sequence()

# next(gen)

#Create a generator function that takes a positive integer n as input and generates all the even numbers up to and including n.

# def even_generator():
#     n = 0
#     while (n % 2) == 0:
#         yield n
#         n += 1
        


# Python program to print Even Numbers in given range
 
# number = int(input("Enter the start of range: "))

# def even_generator():
# # iterating each number in list
#     for num in range(number):
#     # checking condition
#         if num % 2 == 0:
#             print(num, number)

# # generator = even_generator()
# # print(next(generator))

# gen = even_generator()

# print(next(gen))

# nums_squared_gc = (num**2 for num in range(5))


# from collections.abc import Iterator

# def generate_even_numbers(n: int) -> Iterator[int]:
#     for i in range(n+1):
#         if i % 2 == 0:
#             yield i



# my_generator = generate_even_numbers(20)
# print(next(my_generator))

# for value in my_generator:
#     print(value)

# number = int(input("Inser number: "))

# def even_numbers_up_to_n(n):
#     """
#     Generator function that yields all even numbers up to and including n.
#     """
#     i = number
#     while i <= n:
#         yield i  # Yield the current even number
#         i += 2  # Move to the next even number (increment by 2)

# # Example usage:
# n = 20
# for even_num in even_numbers_up_to_n(n):
#     print(even_num)



#Create a generator function that would pick word from a generator and list of generated random words and would stop itterating until the word longer than 7 lettters is found.
#Compare sizes of list and generator. Calculate performance per both executions (time to complete in ms)

# from typing import List
# from collections.abc import Iterator


# my_list = ["Arnas", "Jonas", "Vaidotasss"]
# def generate_even_numbers(words: List) -> Iterator[List]:
#     for i in words:
#         if len(i) == 7:
#             yield i



# my_generator = generate_even_numbers(my_list)
# print(next(my_generator))
import time
from faker import Faker
import random
from collections.abc import Iterator


def generate_random_word(words_generator):
    while True:
        word = next(words_generator)
        if len(word) > 7:
            yield word
            break

start_time_list = time.time()
fake = Faker()
words = [fake.word() for w in range(10000)]
word_generator = (word for word in words)


for word in generate_random_word(word_generator):
    print(word)
end_time_list = time.time()

time_taken_list = (end_time_list - start_time_list) * 1000 # Convert to ms
print(time_taken_list)

start_time_generator = time.time()
long_word_generator = next(word_generator)
print(long_word_generator)
end_time_generator = time.time()
time_taken_generator = (end_time_generator - start_time_generator) * 1000 
print(time_taken_generator)



# from turtle import Turtle 
# t = Turtle() 
# for step in range(36): 
#     t.forward(400) 
#     t.right(170) 



