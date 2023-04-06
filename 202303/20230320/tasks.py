# from abc import ABC, abstractmethod


class Animal:
    def __init__(self, name: str) -> str:
        self.name = name

    def speak(self) -> None:
        raise NotImplementedError

    def get_name(self, name: str) -> str:
        self.name = name
        return self.name


class Dog(Animal):
    def __init__(self, name: str) -> str:
        self.name = name
        super().__init__(name=name)

    def speak(self) -> str:
        return print("Dog says Woof!")


class Cat(Animal):
    def speak(self) -> str:
        return print("Cat says Meow!")


my_dog = Dog("Meshka")
my_cat = Cat("Kafka")
print(my_dog.speak())
print(my_cat.speak())
