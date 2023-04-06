class Person:
    def __init__(self, name: str, surname: str) -> str:
        self.name = name
        self.surname = surname

    def say_hello(self):
        print(f"Hello, {self.name} {self.surname}")

person = Person("Paulius", "Dailidonis")
person.say_hello()



def greeting(name: str, surname: str) -> str:

    """Function greets a person given full name as a string"""

    person = f"Hello, {name} {surname}"
    return person


person = Person("Paulius", "Dailidonis")
print(person)









