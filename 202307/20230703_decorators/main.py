from typing import Callable
# https://realpython.com/primer-on-python-decorators/


# def say_hello(name: str) -> str:
#     return f"Hello {name}"

# def be_awesome(name: str) -> str:
#     return f"Yo {name}, together we are the awesomest!"

# def greet_bob(greeter_func: Callable) -> str:
#     return greeter_func("Bob")

# print(greet_bob(say_hello))
# print(greet_bob(be_awesome))

# def parent():
#     print("Printing from the parent() function")

#     def first_child():
#         print("Printing from the first_child() function")

#     def second_child():
#         print("Printing from the second_child() function")

#     second_child()
#     first_child()



# def parent(num):
#     def first_child():
#         return "Hi, I am Emma"

#     def second_child():
#         return "Call me Liam"

#     if num == 1:
#         return first_child
#     else:
#         return second_child




# def my_decorator(func: Callable) -> Callable:
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# def say_whee():
#     print("Whee!")


# say_whee()
# print("--------------------")
# say_whee = my_decorator(say_whee)
# say_whee()



# from datetime import datetime

# def not_during_the_night(func: Callable) -> Callable:
#     def wrapper():
#         if 7 <= datetime.now().hour < 22:
#             func()
#         else:
#             pass  # Hush, the neighbors are asleep
#     return wrapper

# def say_whee():
#     print("Whee!")

# say_whee = not_during_the_night(say_whee)

# say_whee()


# def my_decorator(func):
#     def wrapper():
#         print("Something is happening before the function is called.")
#         func()
#         print("Something is happening after the function is called.")
#     return wrapper

# @my_decorator
# def say_whee():
#     print("Whee!")


# say_whee()



# def do_twice(func):
#     def wrapper_do_twice():
#         func()
#         func()
#     return wrapper_do_twice


# from main import do_twice

# @do_twice
# def say_whee():
#     print("Whee!")

# say_whee()



# def do_twice(func):
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#         return func(*args, **kwargs)
#     return wrapper_do_twice



# @do_twice
# def return_greetings(name: str) -> str:
#     print(f"Greeting greeting")
#     return f" Hi {name}"





# # greetings = return_greetings("Paulius")
# # print(greetings)

# print(return_greetings.__name__)
# print(help(print))




# import functools

# def do_twice(func):
#     @functools.wraps(func)
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#         return func(*args, **kwargs)
#     return wrapper_do_twice




# import functools

# def decorator(func):
#     @functools.wraps(func)
#     def wrapper_decorator(*args, **kwargs):
#         # Do something before
#         value = func(*args, **kwargs)
#         # Do something after
#         return value
#     return wrapper_decorator




# import functools
# import time

# def timer(func):
#     """Print the runtime of the decorated function"""
#     @functools.wraps(func)
#     def wrapper_timer(*args, **kwargs):
#         start_time = time.perf_counter()    # 1
#         value = func(*args, **kwargs)
#         end_time = time.perf_counter()      # 2
#         run_time = end_time - start_time    # 3
#         print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
#         return value
#     return wrapper_timer

# @timer
# def waste_some_time(num_times):
#     for _ in range(num_times):
#         return [i**2 for i in range(10000000)]


# print(waste_some_time(1000))


import functools

# def debug(func):
#     """Print the function signature and return value"""
#     @functools.wraps(func)
#     def wrapper_debug(*args, **kwargs):
#         args_repr = [repr(a) for a in args]                      # 1
#         kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]  # 2
#         signature = ", ".join(args_repr + kwargs_repr)           # 3
#         print(f"Calling {func.__name__}({signature})")
#         value = func(*args, **kwargs)
#         print(f"{func.__name__!r} returned {value!r}")           # 4
#         return value
#     return wrapper_debug



# @debug
# def make_greeting(name, age=None):
#     if age is None:
#         return f"Howdy {name}!"
#     else:
#         return f"Whoa {name}! {age} already, you are growing up!"


# # greeting = make_greeting("Paulius", 150)
# # print(greeting)

# import math
# from main import debug

# # Apply a decorator to a standard library function
# math.factorial = debug(math.factorial)

# def approximate_e(terms=18):
#     return sum(1 / math.factorial(n) for n in range(terms))

# print(approximate_e)


# import functools
# import time

# def slow_down(func):
#     """Sleep 1 second before calling the function"""
#     @functools.wraps(func)
#     def wrapper_slow_down(*args, **kwargs):
#         time.sleep(1)
#         return func(*args, **kwargs)
#     return wrapper_slow_down

# @slow_down
# def countdown(from_number):
#     if from_number < 1:
#         print("Liftoff!")
#     else:
#         print(from_number)
#         countdown(from_number - 1)


# countdown(10)



# import random
# PLUGINS = dict()

# def register(func):
#     """Register a function as a plug-in"""
#     PLUGINS[func.__name__] = func
#     return func

# @register
# def say_hello(name):
#     return f"Hello {name}"

# @register
# def be_awesome(name):
#     return f"Yo {name}, together we are the awesomest!"

# def randomly_greet(name):
#     greeter, greeter_func = random.choice(list(PLUGINS.items()))
#     print(f"Using {greeter!r}")
#     return greeter_func(name)

# print(PLUGINS)
# print(randomly_greet("Paulius"))



# from flask import Flask, g, request, redirect, url_for
# import functools
# app = Flask(__name__)

# def login_required(func):
#     """Make sure user is logged in before proceeding"""
#     @functools.wraps(func)
#     def wrapper_login_required(*args, **kwargs):
#         if g.user is None:
#             return redirect(url_for("login", next=request.url))
#         return func(*args, **kwargs)
#     return wrapper_login_required

# @app.route("/secret")
# @login_required
# def secret():
#     ...
