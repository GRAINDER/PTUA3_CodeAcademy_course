import logging
#logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
logging.basicConfig(level=logging.DEBUG,filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')
# logging.debug('This is a debug message')
# logging.info('This is an info message')
# logging.warning('This is a warning message')
# logging.error('This is an error message')
# logging.critical('This is a critical message')


# def add_few_number(a: int, b: int) -> int:
#     logging.warning('Received numbers a {a} and b {b}')

    
#     return a + b

# add_few_number(a=6, b=7)


# # def money_collected(amount: float) -> None:
#     logging.info('Ammount of money received: {amount}')
#     if amount == 0:
#         logging.warning('No money collected')
#     #doing something else


# try:

# except Exception as e:
#     logging.error(f'Error: {e}')


# def emergency_stop(is_stop_event: bool) -> None:

#     if is_stop_event:
#         logging.critical()
#         #func stop()
        

#1 uzduotis

# first_debbuger = [int(x) for x in input("Enter multiple value: ").split()]
# logging.debug(f'This is first debug try and my input numbers are: {first_debbuger}')


# first_debbuger = [int(x) for x in input("Enter multiple value: ").split()]
# logging.info(f'This is first debuging info message and my input numbers are: {first_debbuger}')


# first_debbuger = [int(x) for x in input("Enter multiple value: ").split()]
# logging.warning(f'This is first debuging warning message and my input numbers are: {first_debbuger}')

# first_debbuger = [int(x) for x in input("Enter multiple value: ").split()]
# logging.error(f'This is first error warning message and my input numbers are: {first_debbuger}')


# first_debbuger = [int(x) for x in input("Enter multiple value: ").split()]
# logging.critical(f'This is first critical warning message and my input numbers are: {first_debbuger}')

# first_debbuger = [int(x) for x in input("Enter multiple value: ").split()]
# logging.info(f'Received numbers of my first input debbuger: {first_debbuger}')



# age = int(input("Enter your age: "))
# logging.info(f'Age of user is: {age}')
# if age < 18:
#     logging.info('User is under 18')

 

# age = int(input("Enter your age: "))
# def age_check (age: int) -> int:
#     try:
#         age >= 18
#     except: 
#         age < 18
#         logging.error(f'Error: {age}')
#     return age
    


# a = 5
# b = 0

# try:
#   c = a / b
# except ZeroDivisionError as e:
#     logging.error(f"Exception occurred: {e}") #, exc_info=True
# else:
#     c = a / b
#     logging.info("I'm skipping else clause")
# finally:
#     logging.info("I'm still in the finally block")


#2 
