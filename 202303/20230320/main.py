from abc import ABC, abstractmethod

class Vehicle(ABC):
    pass

    @abstractmethod
    def get_name(self) -> None:
        # Method to get the name
        pass
    
    @abstractmethod
    def get_cost(self) -> None:
        pass



class Car(Vehicle):
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def get_age(self) -> None:
        print(self.age)

 
    def get_name(self) -> None:
        # Method to get the name
        print(self.name)
    
    def get_cost(self) -> None:
        print("To much")


# my_car = Car(name="Audi", age=2018)
# my_car.get_age()
# print(my_car.get_cost())




class Vehicle:
    
    def get_something(self) -> None:
        pass

    def do_something(self) -> None:
        raise NotImplementedError