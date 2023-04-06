    # Kelvin to Celsius: C = K - 273 (C = K - 273.15 if you want to be more precise)
    # Kelvin to Fahrenheit: F = 9/5(K - 273) + 32 or F = 1.8(K - 273) + 32.

# class Circle:
#     PI = 3.14159
    
#     def __init__(self, radius: float) -> None:
#         self.radius = radius
    
#     def area(self) -> float:
#         return Circle.calculate_area(self.radius)
    
#     @staticmethod
#     def calculate_area(radius: float) -> float:
#         return Circle.PI * radius ** 2

from abc import ABC, abstractmethod

class Conversion(ABC):

    @abstractmethod
    def __init__(self, kelvin_temperature: int) -> None:
        self.kelvin_temperature = kelvin_temperature


    @abstractmethod
    def celcius_temperature(self) -> float:
        pass


    @abstractmethod
    def get_celcius_temperature(kelvin_temperature: float) -> float:
        pass
    
    @abstractmethod
    def get_Fahrenheittemperature(kelvin_temperature: float) -> float:
        pass




class Temperature(Conversion):

    def __init__(self, kelvin_temperature: int) -> None:
        self.kelvin_temperature = kelvin_temperature

    def celcius_temperature(self) -> float:
        return Temperature.get_celcius_temperature(self.kelvin_temperature)


    @staticmethod
    def get_celcius_temperature(kelvin_temperature: float) -> float:
        return kelvin_temperature-273.15
    
    @staticmethod
    def get_Fahrenheit_temperature(kelvin_temperature: float) -> float:
        return 1.8 * (kelvin_temperature - 273.15) + 32
    
from_kelvin_to_celsis = Temperature(10)
from_fahrenheit_to_celsis = Temperature(10)

print(Temperature.celcius_temperature(from_kelvin_to_celsis))
print(Temperature.celcius_temperature(from_fahrenheit_to_celsis))