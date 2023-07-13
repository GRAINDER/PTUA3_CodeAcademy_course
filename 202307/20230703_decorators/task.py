# write a decorator that checks if the output of the function 
# in a positive integer if it is not print "RESULT IS NEGATIVE" otherwise print "RESULT IS POSITIVE"


# def check_positive_integer(func):
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         if isinstance(result, int) and result > 0:
#             print("RESULT IS POSITIVE")
#         else:
#             print("RESULT IS NEGATIVE")
#         return result
#     return wrapper


# @check_positive_integer
# def calculate_square(num):
#     return num ** 2


# calculate_square(5)  
# calculate_square(-3) 
# calculate_square(0)



# def add_numbers(*args):
#     result = 0
#     for num in args:
#         result += num
#     return result

# print(add_numbers(1,10,11))


# def multiply_numbers(*args):
#     result = 1
#     for num in args:
#         result *= num
#     return result

# print(multiply_numbers(1,10,11))



# def add_arguments(func):
#     def wrapper(*args, **kwargs):
#         result = sum(args)
#         return func(result, **kwargs)
#     return wrapper


# @add_arguments
# def calculate_total(num):
#     print("The total is:", num)

# calculate_total(1, 2, 3)  
# calculate_total(4, 5, 6, 7, 8) 
# calculate_total(9)  



# def multiply_arguments(func):
#     def wrapper(*args, **kwargs):
#         result = 1
#         for num in args:
#             result *= num
#         return func(result, **kwargs)
#     return wrapper



# @multiply_arguments
# def calculate_product(num):
#     print("The product is:", num)

# calculate_product(2, 3, 4)  
# calculate_product(5, 6, 7, 8)  
# calculate_product(9)  


def log_to_file(filename):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            with open(filename, 'a') as file:
                arguments = ', '.join(str(arg) for arg in args)
                file.write(f"Arguments: {arguments}\n")
                file.write(f"Result: {result}\n")
            return result
        return wrapper
    return decorator




@log_to_file('log.txt')
def multiply(a, b):
    return a * b

multiply(2, 3)
multiply(4, 5)