class MyString:
    def __init__(self, value: str):
        self.value = value

    def add_exclamation(self) -> 'MyString':
        self.value += "!"
        return self

    def make_upper(self) -> 'MyString':
        self.value = self.value.upper()
        return self

my_string = MyString("hello")
my_string.add_exclamation().make_upper()

print(my_string.value) # output: "HELLO!"


# Create a class Person that has two methods: set_name and set_age, 
# which set the name and age attributes of the class, respectively. 
# Modify these methods to return self, so that the calls can be chained together.


class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def set_name(self, name: str) -> 'Person':
        return self
    
    def set_age(self, age: int) -> 'Person':
        return self
    

my_person = Person("Paulius", 35)
my_person.set_name().set_age()
print(my_person("Paulius", 35))