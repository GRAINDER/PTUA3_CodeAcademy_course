# # list'ai arba dictionary daugiausiai naudojami
# # key visada immutiable, negali būti keičiamas, o value gali buti betkas
# # Dažniausiai dictionary buna multi level, hierarachy
# my_dictionary = {}
# my_dictionary["name"] = "Tom"
# print(my_dictionary["name"])


# my_dictionary = {"name": "Tom"}
# print(my_dictionary["name"])


# my_dictionary = {"name": "Tom", "surname": "Edison"}
# print(f"name: {my_dictionary['name']}")
# print(f"surname: {my_dictionary['surname']}")


# countries_and_capitals = {
#     "Lithuania": "Vilnius",
#     "Poland": "Warsaw",
#     "Latvia": {
#         "Capital":  "Riga",
#         "Populiation": 2000000,
#         "rich": "rich"
#     }

# }

# print(countries_and_capitals["Latvia"]["Populiation"])


# print(list(countries_and_capitals.items()))
# print(list(countries_and_capitals.values()))
# print(list(countries_and_capitals.keys()))

# # <- Funkcija POP išmeta iš žodyno tai ką nurodome
# countries_and_capitals.pop("Latvia")
# print(countries_and_capitals)

# new_country = {"Spain": "Madrid"}
# # <- Funkcija UPDATE prideda i dictionary tai koki pries tai sukureme sarasa
# countries_and_capitals.update(new_country)
# print(countries_and_capitals)


# test_keys = ["Albert", "Tom", "Stephen"]
# test_values = [1, 4, 5]
# # <- Funkcija ZIP apjungia KEY ir Values is skirtingu lists
# my_dictionary = dict(zip(test_keys, test_values))
# print(my_dictionary)


# my_set = {1, 2, 3, 4, "My test message"}


# user_info = {
#     "name": "Albert",
#     "surname": "Einstein",
#     "occupation": {
#         "role": "profesor",
#         "university": "ktu",
#         "faculty": {"Nature_and_science": "Mathematics",
#                     "Electronics_and_enginering": "Telecomunications",
#                     "Room":{"Size": "200", "Number": 216}

#                     }




#     }
# }
# print(user_info)


# d = {'a': 10, 'b': 20, 'c': 30}
# for key, value in d.items():
#     print(key, value)




# # We have 3 dictionaries :  dic_one={1:10, 2:20} dic_two={3:30, 4:40} dic_three={5:50,6:60}
# # Create one final dictionary from all those 3.

# dic_one={1:10, 2:20} 
# dic_two={3:30, 4:40} 
# dic_three={5:50, 6:60}

# my_dictonary = dic_one
# my_dictonary.update(dic_two)
# my_dictonary.update(dic_three)


# print(my_dictonary)



# # Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x):
# # You can use input to receive the number. Example:
# # n= 5 , output:  {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


# # n = int(input("iveskite skaiciu: "))

# # d = dict()

# # for x in range(1, 1+n):
# #     d[x]=x*x

# # print(d)












# # n=int(input("Input a number "))
# # d = dict()

# # for x in range(1,n+1):
# #     d[x]=x*x

# # print(d) 


# for n in range(2, 10):

#     for x in range(2, n):

#         if n % x == 0:

#             print(n, 'equals', x, '*', n//x)

#             break

#     else:

#         # loop fell through without finding a factor

#         print(n, 'is a prime number')


name = input("Enter name: ")
surname = input("Enter surname: ")
age = input("Enter age: ")



dictionary = {}

for i in range(3):
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    age = input("Enter age: ")

    dictionary[name] = surname

print(dictionary)
