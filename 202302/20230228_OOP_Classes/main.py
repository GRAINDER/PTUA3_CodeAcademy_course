# class Person: #Objektas =  daiktavardis, metodas b8na klasės viduje
class Person:
    description = "And i'm noob programmer"


    def __init__(self, name:str, surname:str):

        self.name = name
        self.surname = surname


    def greet(self):
        return f"Hello my name is {self.name}"
    

person = Person("Paulius", "Dailidonis")

print(person.greet())
print(person.description)


# def calculate_days_left_to_black_friday(self):
#     # init today date
#     # init black friday date
#     # return black friday - today date
#     today = date.today()

#     print(today)

def get_eye_color(self, my_eye_color:str="Brown") -> str:
print(Person.get_eye_color("Brown"))



__repr__ = Person.__repr__



#     def say_hello(self):
#             print("hello")

# from


class Calculator():
    # Klasės atributas
    def __init__(self, number_one: int, number_two: int):
        self.number_one = number_one
        self.number_two = number_two
    
    def sum(self):
        return self.number_one + self.number_two
    def multiply(self):
        return self.number_one * self.number_two
    def divide(self):
        return self.number_one / self.number_two
    def distraction(self):
        return self.number_one - self.number_two
    
number_one = int(input("Please enter the first number: "))
number_two = int(input("Please enter the second number: "))

obj=Calculator(number_one,number_two)
while True:
    def menu():
        x =("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
        print(x)
    menu()
    choice = int(input("Please select one of the following: "))
    if choice == 1:
        print("Result: ",obj.sum())
    elif choice == 2:
        print("Result: ",obj.distraction())
    elif choice == 3:
        print("Result: ",obj.multiply())
    elif choice == 4:
        print("Result: ",obj.divide())
    elif choice == 0:
        print("Try again")
        break
    

class Person: #Objektas =  daiktavardis, metodas b8na klasės viduje
class Person:
    description = "And i'm noob programmer"


    def __init__(self, name:str, surname:str):

        self.name = name
        self.surname = surname


    def greet(self):
        return f"Hello my name is {self.name}"
    

person = Person("Paulius", "Dailidonis")

print(person.greet().lower())
print(person.description)

    

class employee:
    def __init__(self, name: str, surname: str):
        self.name = name
        self.surname = surname

    def email(self) -> str:
        return f"{self.name}.{self.surname}@company.com"

employee_email = employee("PAULIUS", "DAILIDONIS")

print(employee_email.email().lower())



class book:
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author
    def get_title(self) -> str:
        return f"The Book name is {self.name}"


    def get_author(self) -> str:
        return f"The Book author is {self.author}"

book_one = book("Pride and Prejudice", "Jane Austen (PP)")
book_two = book("Hamletas ", "Viljamas Šekspyras (H)")
book_three = book("Karas ir taika", "Levas Tolstojus (WP)")

print(book_one.get_author())



 


