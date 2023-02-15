a = 2
b = 5


def addition(number1, number2):
    sum = number1 + number2
    return sum


c = addition(a, b)
print(c)

b = addition(10, 15)
# print(b)


def print_smth():
    print('Hello world!')

print_smth()


import random

def get_random_number():
    print(random.randint(1, 10))

print(get_random_number()) # ismete None nes funkcija


import random

def get_random_number():
    print(random.randint(1, 10))

print(get_random_number()) # ismete None nes funkcija



def find_sum(num1, num2):
    '''Grąžina num1 ir num2 sumą.'''
    sum_nums = num1 + num2 # Suranda num1 ir num2 sumą
    return sum_nums # Grąžina skaičių sumą

a = find_sum(1, 2) # 3
print(a)



def even_odd(num):

    '''
    Grąžina "lyginis", jei num yra lyginis, ir "nelyginis", jei num yra nelyginis.    
    Parametrai:
        (int): Grąžinama:
        type (eilutė): "lyginis", jei num yra lyginis; "nelyginis", jei num yra nelyginis
    '''

    if num % 2 == 0: # Patikrina, ar num/2 turi likutį 0
        return "lyginis" # Jei likutis lygus 0, grąžinama "lyginis"
    else:
        return "nelyginis" # Jei likutis nelygus 0,
        # Jei neturi, grąžinama "nelyginis"

print(even_odd(2)) # "lyginis"



# def check_if_exist(a=None):
#   if a:
#     return a
#   return
    


def find_sum(num1, num2):
    '''Grąžina num1 ir num2 sumą.'''
    sum_nums = num1 + num2 # Suranda num1 ir num2 sumą
    return sum_nums # Grąžina skaičių sumą
print(find_sum(1)) # 3




def add_two_int_numbers(a: int, b: int) -> int:

    return a + b

def add_two_int_numbers(a: int, b: int) -> int:
    return a + b


from typing import List, Tuple, Dict, Union

Dicttype_annotation_tuple: Tuple[str] = ('1','2','3')
type_annotation_list: List[str] = ['a', 'b', 'c']
type_annotation_dict: Dict[str, int] = {'a': 1, 'b': 2}

from typing import Tuple, Optional

def the_func(x: Union[int, float], y: Tuple[str, str], z: Optional[float] = None) -> str:
   return 'You called the_func with ' +  str(x) +  str(y) +  str(z)

print(the_func(1, "Paulius", 3.14)) # You called the_func with 1, Paulius,


1 uzduotis Create at least 5 different functions by your own and test it.

def add_two_int_numbers(a: int, b: int, c: int) -> int:
    return (a + b)*c
print(add_two_int_numbers(1, 2, 3)) # 


def add_two_float_numbers(a: float, b: float, c:int) -> float:
    return (a*a + b**b)/c
print(round(add_two_float_numbers(1, 2, 3),2)) #


def add_two_string_numbers(a: str, b: str, c: int) -> str:
    return (a + b + c)
print(add_two_string_numbers('1', '2', '3')) #


def add_two_string_numbers(a: str, b: str, c: str) -> int:
    return int(a) + int(b) + int(c)

print(add_two_string_numbers(1, 2, 4))





# # # 2 Uzduotis Create a function that adds a string ending to each member in a list.
from typing import List



def add_string_to_list(a: List[str]) -> List[str]:
    new_items = []
    for items in a:
        new_items.append(items + "s")
        
    return new_items 


print(add_string_to_list(["Paulius", "Antanas", "Jonas"]))
    

# # print(add_string_to_list(["Paulius", "Antanas", "Jonas"]))

# # # Create a function that adds a string ending to each member in a list.


def add_string_to_list(a: List[str]) -> List[str]:
    for i in a:
        return  a[0] + "S" + " " + a[1] + "S" + " " + a[2] + "S"


print(add_string_to_list(["Paulius", "Antanas", "Jonas"]))


#3 Create a mini python program which would take two numbers as an input and would return their sum, subtraction, division, multiplication.

def add_two_numbers(a: int, b: int) -> str:
    return (f"sum: {int(a) + int(b)}, substraction: {int(a)-int(b)}, division: {int(a)/int(b)}, multiplication: {int(a)*int(b)}")
a = int(input("Add first integers: "))
b = int(input("Add second integers: "))

# print(add_two_numbers(a, b))

from typing import Tuple

def add_two_numbers(a: int, b: int) -> Tuple[int, int, float, int]:
    return a+b, a-b, a/b, a*b

a = int(input("Add first integers: "))
b = int(input("Add second integers: "))



sum, sub, div, mult = add_two_numbers(a, b)
print(sum)

