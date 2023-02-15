# squares = []
# for number in range(10):
#     squares.append(number * number)
# print(squares)


# my_names = ["Paulius", "Ignas", "Jonas", "Albertas", "Mindaugas"]
# for names in my_names:
#     if len(names)>=5:
#         print(names)
 
# my_names_two= ["Paulius", "Ign", "Jonas", "Albertas", "Mindaugas"]
# my_names2 = [names_two for names_two in my_names_two if len(names_two)>=5]
# print(my_names2)

# my_smth ={
#     'Alpha': 1,
#     'Beta': 2,
# }

# squares = {i: i * i for i in range(10)}
# print(squares)



# my_dict = {'Alpha': 15, 'Beta': 25, 'Gamma': 35, 'Delta': 45, 'Epsilon': 55}

# my_new_dict =  {key.upper(): int(str(value)[::-1]) for key, value in my_dict.items()}


# print(my_new_dict)


# my_new_dict = {key.upper(): int(str(value)[::-1]) for key, value


# my_names = ["Paulius", "Ignas", "Jonas", "Albertas", "Mindaugas"]
# my_dict ={}
# for count, value in enumerate(my_names):
#     my_dict[count] = value

# print(my_dict)




my_names = ["Paulius", "Ignas", "Jonas", "Albertas", "Mindaugas"]
my_dict = {key: name for key, name in enumerate(my_names, start=1)}

print(my_dict)
