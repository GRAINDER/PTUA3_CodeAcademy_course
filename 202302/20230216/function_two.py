# from typing import Any

# def check_arguments(mandatory: Any, *args, **kwargs) -> None: #key wards arguments, args - arguments 

#     print (mandatory)
#     if args:
#         print (args)
#     if kwargs:
#         print (kwargs)



# def multiply(x: int,y: int) -> int:
#     return x * y

# print(multiply(2,3))



# multiplication =  lambda  x,y :  x * y
# print(multiplication(2,3))



# multiplication2 =  lambda: "Hello World"

# print(multiplication2())


# from typing import Callabledef my_func(n: int) -> Callable:
#     return lambda a: a**nmy_doubler = my_func(2)
# print(my_doubler(11))

# #1 uzduotis
from typing import List

list_one = [1,2,3,4,5]
list_two = [2,3,4,5,6]

list_three = [1, 2, 3, 4, 5]
list_four = [5, 4, 3, 2, 1]


def list_index_sum(list_one: List, list_two: List) -> List:
    list_sum = [sum(items) for items in zip(list_one,list_two)]
    if len(set(list_sum)) == 1:
        print(True)
    else:
        print(False)    
    return list_sum
print(f"Sum of lists are: {list_index_sum(list_one,list_two)}")



# def list_index_sum(list_one: List, list_two: List) -> bool:
#     list_sum = [sum(items) for items in zip(list_one,list_two)]
#     if len(set(list_sum)) == 1:
#         return True
#     else:
#         return False

# print(f"Sum of lists are: {list_index_sum(list_three,list_four)}")


#2 uzduotis 

# def even_sum(NumList):
#     Even_Sum = 0
#     for j in range(Number):
#         if(NumList[j] % 2 == 0):
#             Even_Sum = Even_Sum + NumList[j]
#     return Even_Sum

# def odd_sum(NumList):
#     Odd_Sum = 0
#     for j in range(Number):
#         if(NumList[j] % 2 != 0):
#             Odd_Sum = Odd_Sum + NumList[j]
#     return Odd_Sum

# NumList = []
# Number = int(input("Please enter the Total Number of List Elements: "))
# for i in range(1, Number + 1):
#     value = int(input("Please enter the Value of %d Element : " %i))
#     NumList.append(value)

# Even_Sum = even_sum(NumList)
# Odd_Sum = odd_sum(NumList)
# print("\nThe Sum of Even Numbers in this List =  ", Even_Sum)
# print("The Sum of Odd Numbers in this List =  ", Odd_Sum)