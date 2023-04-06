# # let's play with separator:
# print("hello world", sep=",")

# # some more
# print("hello", "world", sep=" amazing ")

# #Print statemento negali likti PRINT statement'i. Svarbu ! Negali 

# # # 
# # 37064@DESKTOP-4DV8A0U MINGW64 ~/CodeAcademy Python 2023/20230202
# # $ mkdir gitbash

# # 37064@DESKTOP-4DV8A0U MINGW64 ~/CodeAcademy Python 2023/20230202
# # $ rm -rf gitbash/

# # 37064@DESKTOP-4DV8A0U MINGW64 ~/CodeAcademy Python 2023/20230202
# # $ touch lesson.py

# # 37064@DESKTOP-4DV8A0U MINGW64 ~/CodeAcademy Python 2023/20230202
# # $ rm lesson.py

# # 37064@DESKTOP-4DV8A0U MINGW64 ~/CodeAcademy Python 2023/20230202
# # $ cat lesson_four.py
# # # let's play with separator:
# # # print("hello world", sep=",")

# # # some more
# print("hello", "world", sep=" amazing ")

# # #Print statemento negali likti PRINT statement'i. Svarbu ! Negali

# #nano atidaro folderius ir ten galima sukurti failus issaugoti
# #touch sukuria naujus .py kodo failiukus

# print("Hello World!")
# a = "alibab"
# print(type(a))

# if type(a) == str:
#     print("Almost Friday")





# my_list = [45, 20, 14, 55]
# sorted_list = sorted(my_list)

# print(sorted_list)

# sorted_reverse_list = sorted(my_list, reverse=False)

# print(sorted_reverse_list)




# my_list = ["Albert", "Nicola", "Thomas"]
# sorted_list = sorted(my_list)

# print(sorted_list)

# sorted_reverse_list = sorted(my_list, reverse=True)

# print(sorted_reverse_list)

# A : int = 1 # Priskiriamas

# train_sentence = input("Insert sentence from 10 words: ")


# print(f" {len(train_sentence)}")
# print(f" {sorted({train_sentence})}")

# listas = [1, "Paulius", 1.2, True ]
# print(type(listas[0]))
# print(type(listas[1]))
# print(type(listas[2]))
# print(type(listas[3]))

# listas = [1, "Paulius", 1.2, True, sep=" | "]
# print(1, "Paulius", 1.2, True, sep=" | ")

# list1 = [1.235, 2.654, 3.655]
# #list2 = round(list1,2)
# for i in list1:
#     a = round(i[0])
# print(list1)



# def getroundvalue(i):
#     return round(float(i),2)
# uservalue = input("Enter a float number:")
# print(getroundvalue(uservalue))



# def getroundvalues(listfloatvalues):
#     for i in listfloatvalues:
#         value.append(round(i))
#     return value
# list = [2.7,4.2,8.9,1.5]
# value = []
# print("List of Float numbers:", list)
# print("Round number from the list:",getroundvalues(list))


# list = ["Paulius", "Antanas", "Jonas"]
# sorted_list = sorted(list, reverse=True)

# print(sorted_list)



# Create a program which would take 5 separate sentences containing 5 words.
# Make those sentences in separate lists and sort them out (reverse=False)
# Create 5 five new lists what would contain first, second  indexed elements from those lists. (first list containing
# all first elements of those five, second list second elements and so on).
# print the length of all list items and print the longest lenght list and shortest.

first_sentence = input("Iveskite pirma sakini is penkiu zodziu: ")
# second_sentence = input("Iveskite antra sakini is penkiu zodziu: ")
# third_sentence = input("Iveskite trecia sakini is penkiu zodziu: ")
# fourth_sentence = input("Iveskite ketvirta sakini is penkiu zodziu: ")
# fifth_sentence = input("Iveskite penkta sakini is penkiu zodziu: ")


list_one = [first_sentence]
# list_two = [second_sentence]
# list_three = [third_sentence]
# list_fourth = [fourth_sentence]
# list_fifth = [fifth_sentence]

list_one_reversed = sorted(list_one, reverse=False)
# list_two_reversed = sorted(list_two, reverse=False)
# list_three_reversed = sorted(list_three, reverse=False)
# list_fourt_reversed = sorted(list_fourth, reverse=False)
# list_fifth_reversed = sorted(list_fifth, reverse=False)

new_list_one = []
# new_list_two =[]
# new_list_three =[]
# new_list_four =[]
# new_list_five =[]

new_list_one.append(list_one_reversed[0])
# new_list_two.insert(list_one_reversed[1], list_two_reversed[1], list_three_reversed[1], list_fourt_reversed[1], list_fifth[1])
# new_list_three.insert(list_one_reversed[2], list_two_reversed[2], list_three_reversed[2], list_fourt_reversed[2], list_fifth[2])
# new_list_four.insert(list_one_reversed[3], list_two_reversed[3], list_three_reversed[3], list_fourt_reversed[3], list_fifth[3])
# new_list_five.insert(list_one_reversed[4], list_two_reversed[4], list_three_reversed[4], list_fourt_reversed[4], list_fifth[4])


print(new_list_one)
# print(new_list_two)
# print(new_list_three)
# print(new_list_four)
# print(new_list_five)