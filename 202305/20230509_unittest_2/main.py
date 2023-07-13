# Sukurkite ir išsibandykite funkcijas, kurios:

# 1. Gražinti trijų paduotų skaičių sumą.

def sum_of_numbers(no1: int, no2: int, no3: int) -> int:
    return no1 + no2 + no3


#print(skaiciu_suma(45, 5, 6))


# 2. Gražintų paduoto sąrašo iš skaičių, sumą.

def sum_of_list(list) -> int:
    sum = 0
    for num in list:
        sum += num
    return sum


#sarasas = [4, 5, 78, 8]
#print(saraso_suma(sarasas))


#3. Atspausdintų didžiausią iš kelių paduotų skaičių (panaudojant *args).

def max_number_f_one(*args):
    max = args[0]
    for no in args:
        if no > max:
            max = no
    return max


def max_number(*args):
    return max(args)


# print(didziausias_skaicius(5, 8, 789, 94, 78))


# 4. Gražintų paduotą stringą atbulai.

def back_str(str):
    return str[::-1]


##print(stringas_atbulai("Donatas Noreika"))


# 5. Atspausdintų, kiek paduotame stringe yra žodžių, didžiųjų ir mažųjų raidžių, skaičių.

def info_about_sentence(str):
    # print(f"Šiame sakinyje yra {len(stringas.split())} žodžių")
    upper = 0
    lower = 0
    numbers = 0
    for symbol in str:
        if symbol.isupper():
            upper += 1
        if symbol.islower():
            lower += 1
        if symbol.isnumeric():
            numbers += 1
    return upper, lower, numbers
#     #print(f"Didžiosios: {didziosios}, mažosios: {mazosios}, skaičiai: {skaiciai}")

#info_apie_sakini("Laba diena laba diena lab 522")


# 6. Gražintų sąrašą tik su unikaliais paduoto sąrašo elementais.

# def unikalus_sarasas(sarasas):
#     naujas_sarasas = []
#     for skaicius in sarasas:
#         if skaicius not in naujas_sarasas:
#             naujas_sarasas.append(skaicius)
#     return naujas_sarasas


#print(unikalus_sarasas([4, 5, "Labas", 6, "Labas", True, 5, True, 10]))

# alternatyva:
    
# def unique_only(*args):
#     return list(set(args))


# # 7. Gražintų, ar paduotas skaičius yra pirminis.

# n= int(input("Įveskite skaičių "))
# def ar_pirminis(skaicius):
#     if skaicius > 1:
#         for num in range(2, skaicius):
#             if skaicius % num == 0:
#                 return False
#         return True
#     return False

#print(ar_pirminis(n))


# 8. Išrikiuotų paduoto stringo žodžius nuo paskutinio iki pirmojo

# def isrikiuoti_nuo_galo(sakinys):
#     zodziai = sakinys.split()[::-1]
#     return " ".join(zodziai)


#print(isrikiuoti_nuo_galo("Vienas du trys keturi"))

# 9. Gražina, ar paduoti metai yra keliamieji, ar ne.

# import calendar


# def ar_keliamieji(metai):
#     return calendar.isleap(metai)


# print(ar_keliamieji(2020))
# print(ar_keliamieji(2100))
# print(ar_keliamieji(2000))

# 10. Gražina, kiek nuo paduotos sukakties praėjo metų, mėnesių, dienų, valandų, minučių, sekundžių.

# import datetime


# def patikrinti_data(sukaktis):
#     ivesta_data = datetime.datetime.strptime(sukaktis, "%Y-%m-%d %X")
#     now = datetime.datetime.now()
#     skirtumas = now - ivesta_data
#     return skirtumas

#     print("Praėjo metų: ", skirtumas.days // 365)
#     print("Praėjo mėnesių: ", skirtumas.days / 365 * 12)
#     print("Praėjo savaičių: ", skirtumas.days // 7)
#     print("Praėjo dienų: ", skirtumas.days)
#     print("Praėjo valandų: ", skirtumas.total_seconds() / 3600)
#     print("Praėjo minučių: ", skirtumas.total_seconds() / 60)
#     print("Praėjo sekundžių: ", skirtumas.total_seconds())


# patikrinti_data("2000-01-01 12:12:12")
# patikrinti_data("1991-03-11 12:12:12")