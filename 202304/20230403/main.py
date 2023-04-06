# #Sukurkite klasę Employee su statiniu metodu calculate_payroll, 
# #kuris priima Employee egzempliorių sąrašą ir grąžina bendrą sumą. kuri turi būti išmokėta visiems darbuotojams. 
# #Kiekvienas Employee egzempliorius turi du atributus: Vardas ir Apmokestis
# from typing import List


# class Employee():
#     def __init__(self, name: str, salary: float) -> None:
#         self.name: str = name
#         self.salary: float = salary
        

#     @staticmethod
#     def calculate_payroll(Employee_List: List["Employee"]) -> float:
#         return sum(Employee.salary for Employee in Employee_List) 
    
# employees = [Employee("Alice", 5000.0), Employee("Bob", 6000.0), Employee("Charlie", 7000.0)]
# print(Employee.calculate_payroll(employees))


# class Rectangle:
#     def __init__(self, width: float, height: float) -> None:
#         self.width = width
#         self.height = height
    
#     def area(self) -> float:
#         return self.width * self.height
    
#     @classmethod
#     def from_square(cls, side_length: float) -> 'Rectangle':
#         return cls(side_length, side_length * 2)

# rectangle1: Rectangle = Rectangle(3.0, 4.0)
# rectangle2: Rectangle = Rectangle.from_square(2.0)

#Create a class method to return the factorial of a given number.
import math

class Factorial:
    def __init__(self, number: int) -> None:
        self.number = number
        
    def factorial(self) -> int:
        return math.factorial(self.number)


    @classmethod
    def get_factorial(cls, number: int) -> "Factorial":
        return cls(number)


facto_one: Factorial = Factorial(3)
print(facto_one.factorial())