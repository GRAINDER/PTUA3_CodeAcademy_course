# import os

# # print(dir(os))

# # print(os.getcwd())

# # print(os.listdir())

# # print(os.stat("repos"))


# with open("failas.txt", 'r', encoding="utf-8") as failas:
#     print(failas.readline(), end="")
#     print(failas.readline(), end="")
#     print(failas.readline(), end="")



# import pickle

# a = 1024

# with open("a.pkl", "wb") as pickle_out:
#     pickle.dump(a, pickle_out)

# import pickle
# with open("a.pkl", "rb") as pickle_in:
#     naujas_a = pickle.load(pickle_in)

# # print(naujas_a)



# import pickle

# zodynas = {1:"Pirmas", 2:"Antras", 3:"Trečias"}

# with open("zodynas.pkl", "wb") as pickle_out:
#     pickle.dump(zodynas, pickle_out)



# import pickle

# with open("zodynas.pkl", "rb") as pickle_in:
#     naujas_zodynas = pickle.load(pickle_in)

# print(naujas_zodynas)

# a = 10
# b = 7
# c = 23
# with open("abc.pkl", "wb") as pickle_out:
#     pickle.dump(a, pickle_out)
#     pickle.dump(b, pickle_out)
#     pickle.dump(c, pickle_out)



import pickle

# with open("abc.pkl", "rb") as pickle_in:
#     while True:
#         try:
#             print(pickle.load(pickle_in))
#         except EOFError:
#             break

import pickle
from datetime import datetime


with open("text.txt", 'w') as file:
    file.write("Mokaus su Python!")


with open('text.txt', 'r') as file:
    print(file.read())

with open("text.txt", 'a') as file:
    file.write(str(datetime.today()))

with open('text.txt', 'r') as file:
    print(file.read())


naujas = ""
skaicius = 1
with open('text.txt', 'r') as file:
    for eilute in file:
        naujas += str(skaicius) + " " + eilute
        skaicius += 1

with open('text.txt', 'w') as file:
    file.write(naujas)

with open('text.txt', 'r') as file:
    print(file.read())

