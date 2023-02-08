#1 uzduotis susumuoti saraso elementus

# # list = [1, 10, 15, 20]
# # print(sum(list))



Suma = 0
list = [1, 10, 15, 20]
for list_element in range(0, len(list)):
    Suma = Suma + list[list_element]

print("Suma:", Suma)


# 2 uzduotis sudauginti saraso elementus



# def multiplyList(myList):
 
#     # Multiply elements one by one
#     result = 2
#     for x in myList:
#         result = result * x
#     return result
 
 
# # Driver code
# list1 = [1, 2, 3]
# list2 = [3, 2, 4]
# print(multiplyList(list1))
# print(multiplyList(list2))

# 3 uzduotis

# my_third_list=[1, 200, 3, 500, 535]
# # print(max(my_third_list))

# 4 uzduotis nesuprantu salygos


# #python program which join all strings in list
# list = ['hello', 'geek', 'have','a', '1', 'day']
# # this will join all the# elements of the list with ' '
# list = ' '.join(list)
# print(list)






# #5 uzduotis


# # python program to demonstrate merging 
# # of lists using python
# def append_lists():
#     #list 1
#     ls1 = [1,2,3,4]
#     #list 2
#     ls2 = [5,6,7,8]
    
#     #iterating over list2
#     for i in ls2:
#         #appending in list1
#         ls1.append(i)
#     print(ls1)

# #function call    
# append_lists()


# #6 uzduotis Parašykite python programą, kuri paprašytų naudotojo įvesti 3 sveikuosius skaičius ir rastų didžiausią įvestą reikšmę.

# numbers=[]

# for i in range(3):
#     number = int(input("Iveskite tris random skaicius: "))
#     numbers.append(number)
# print(max(numbers))



# 7 uzduotis: viskas tas pats tik su tuples: 


# list = (1, 10, 15, 20)
# print(sum(list))


# #python program which join all strings in list
# list = ('hello', 'geek', 'have','a', '1', 'day')
# # this will join all the# elements of the list with ' '
# list = ' '.join(list)
# print(list)

# def get_pin():
#     while True:
#         try:
#             return int(input("Enter your pin: "))
#         except ValueError:
#             print("you must enter a number")

# #Then when you are currently doing

# enter_pin = int(input("Enter your pin: ")); # Ask user for pin code

# #change it to call the function:

# enter_pin = get_pin()


# # importing pandas as pd
# import pandas as pd
# import random,string
# num = string.digits
# result = True
# l = []
# while(True):
#    size = int(input("enter the series size"))
#    if(size%2==1):
#       result = False
#    else:
#       result = True
#       for i in range(size):
#          rand_pin = random.sample(num,4)
#          l.append("".join(rand_pin))
#       series = pd.Series(l)
#       print("Random four digit pin number series\n",series)
#    if(result==True):
#       break
