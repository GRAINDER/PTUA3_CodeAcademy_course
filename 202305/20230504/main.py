# from typing import List

# class Point:
#     def __init__(self, x: float, y: float):
#         self._x = x
#         self._y = y

#     def get_coordinates(self) -> List[float]:
#         return [self._x, self._y]




#     @property
#     def x(self):
#         return self._x

# my_point = Point(2.5, 6.3)
# print(my_point.get_coordinates())

# class Rectangle:
#     def __init__(self, width: float, height: float):
#         self.width = width
#         self.height = height

#     @property
#     def area(self) -> float:
#         return self.width * self.height

# r = Rectangle(3.0, 4.0)
# print(r.area)  #

#1 Task
#Write a Temperature class that has a celsius property and a fahrenheit property. 
#The celsius property stores the temperature in Celsius, and the fahrenheit property stores the temperature in Fahrenheit. 
#The fahrenheit property should be a computed property that converts the Celsius temperature to Fahrenheit.

# class Temperature:
#     def __init__(self, celsius: float):
#         self._celsius = celsius
    
#     @property
#     def celsijus(self):
#         return self._celsius
    
#     @celsijus.setter
#     def celsijus(self, value: float):
#         self._celsius = value
    
#     @property
#     def fahrenheit(self):
#         return self._celsius * 9 / 5 + 32


# temp = Temperature(3.5)

# print(temp.celsijus)
# print(temp.fahrenheit)

#Task Nr.2 : Write a User class that has a password property. 
#The password property should be a computed property that checks whether the password is strong enough. 
#A password is considered strong if it has at least 8 characters, contains at least one uppercase letter, one lowercase letter, and one number.
# from typing import Union

# class User:
#     def __init__(self, password: int) -> None:
#         self._password = password

#     @property
#     def password(self):
#         return self._password
    
#     @password.setter
#     def password(self, value):
#         if value.isalnum() == False:
#             print("Password should contain atleast one special character or number")
#         if value.isalnum() == False:
#             print("Password should contain atleast one numeric number")
#         elif len(value)<8:
#             print ('Too short')
#         elif value.isupper() == False:
#             print ('Password should contain atleast one uppercase character')
#         elif value.islower() == False:
#             print ('Password should contain atleast one lowercase character')
#         else:
#             print ("Password is OK")


# Paulius = User(password=123)
# # print(Paulius.password("qwerty123"))
# print(Paulius.password(123))





class User:
    def __init__(self, username, password):
        self.username = username
        self._password = password
    
    @property
    def password(self):
        return self._password
    
    @password.setter
    def password(self, value):
        if self.is_strong_password(value):
            self._password = value
        else:
            raise ValueError("Password is not strong enough.")
    
    def is_strong_password(self, password):
        if len(password) < 8:
            return False
        if not any(char.isdigit() for char in password):
            return False
        if not any(char.isupper() for char in password):
            return False
        if not any(char.islower() for char in password):
            return False
        return True



user = User("john_doe", "password123")
print(user.password)  # prints "password123"

user.password = "strongPassword123"
print(user.password)  # prints "strongPassword123"

user.password = "weakpw"
# raises ValueError: Password is not strong enough.

