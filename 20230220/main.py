# from typing import Union

# def divider(number: Union[float, int]) -> None:
#     return number / 2 if isinstance(number, float) else number // 2
    
# # try:
# #     my_divided_number = divider(0)
# #     print(my_divided_number)
# # except TypeError:
# #     print("Something went wrong")

# # except ZeroDivisionError:
# #     print("Something went wrong")

# ############################################# Exception Handling #############################################
# try: 
#     my_magic_number = 10

#     my_divided_number = divider(number=10)
#     print(my_divided_number)
#     print(my_divided_number / my_magic_number)

    
# except ZeroDivisionError:
#     print("Something went wrong")
# except Exception as e:
#     print(f"Error: {e}")
############################################# Exception Handling #############################################

# else:
#     print("success")



# from typing import Union
# def divider(number: Union[float, int]) -> Union[float, int]:
#     try:
#         return number / 2 if isinstance(number, float) else number // 2
#     except TypeError:
#         print("Something went wrong")
#     except Exception as e:
#         print(f"Error: {e}")

#1

def my_function(a: int, b: int) -> int:

    try:
       sum = a // b
    
    except ValueError:
    
        print("Something went wrong")
    except Exception as e:
        print(f"Error: {e}")
    return sum


#print(my_function(2, 1))




# # #2

# def multiple_two_numbers(first_number: int, second_number: int) -> None:
#     try:
#         result = first_number * second_number

#     except TypeError:
#         print("Please enter a number")
#     except:
#         if result > 100:
#             print('Result is greater or equal to 100')
#     return result   

# print(multiple_two_numbers(3,80))


# # #3 
# try:
#     index_numbers = [2,4,6,8,0]
#     print(index_numbers[5])
    
# except IndexError:
#     print("Index Out of Bound.")

