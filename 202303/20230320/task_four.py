from abc import ABC, abstractmethod


class Calculator(ABC):
    def __init__(self, number_one: float, number_two: float, function: str) -> None:
        self.number_one = number_one
        self.number_two = number_two
        self.function = function

    def get_sum(self):
        return self.number_one + self.number_two

    def get_diff(self):
        return self.number_one - self.number_two

    def get_multiple(self):
        return self.number_one * self.number_two

    def get_division(self):
        return self.number_one / self.number_two
    
    def get_exponentiation(self):
        return self.number_one ** self.number_two
    
    def get_floor_division(self):
        return self.number_one // self.number_two
    
    def get_modulus(self):
        return self.number_one % self.number_two
    
    @abstractmethod
    def get_something_one(self):
        pass

    @abstractmethod
    def get_something_two(self):
        pass

class Geometry(Calculator):
    def __init__(self, number_one: float, number_two: float, function: str) -> None:
        super().__init__(number_one, number_two, function)

    
    def get_something_one(self):
        return (self.number_one + self.number_two) ** 2

    
    def get_something_two(self):
        return (self.number_one - self.number_two) / 2
      
    

class Arithmetic(Calculator):
    def __init__(self, number_one: float, number_two: float, function: str) -> None:
        super().__init__(number_one, number_two, function)
    
    
    def get_something_one(self):
        if self.function == "+":
            return (self.number_one + self.number_two) ** 2

    
    def get_something_two(self):
        if self.function == "-":
            return (self.number_one - self.number_two) / 2
