# class Shape:
#     def __init__(self, shape_name: str, sides: int) -> None:
#         self.shape_name = shape_name
#         self.sides = sides

#     def get_area(self) -> None:
#         pass


# class Rectangle(Shape):
#     def __init__(self, shape_name: str, width: float, height: float) -> None:
#      self.width = width
#      self.height = height
#      super().__init__(shape_name=shape_name, sides=4)

#     def get_widtht(self) -> float:
#         return self.width

#     def get_height(self) -> float:
#         return self.height

#     def get_area(self) -> float:
#         return self.width*self.height


# class Square(Rectangle):
#     def __init__(self, side_lenght: float, width: float, height: float) -> None:
#         self.side_lenght = side_lenght
#         Rectangle.__init__(width=width, height=height)


# rectangle_parameters = Rectangle("Rectangular", 4, 5)
# print(rectangle_parameters.get_area())


# ---------------------------2 task --------------------------#


class Vehicle:
    FARE_CHARGE = 100

    def __init__(
        self, name: str, seating_capacity: int, speed: float, wheel_number: int
    ) -> None:
        self.name = name
        self.seating_capacity = seating_capacity
        self.speed = speed
        self.wheel_number = wheel_number

    def get_name(self):
        return self.name

    def get_seating_capacity(self):
        return self.seating_capacity

    def get_speed(self):
        return self.speed

    def get_wheel_number(self):
        return self.wheel_number

    def get_charge(self):
        FARE_CHARGE = 100
        seats = self.get_seating_capacity()
        return seats * FARE_CHARGE


class Bus(Vehicle):
    def __init__(
        self, name: str, seating_capacity: int, speed: float, wheel_number
    ) -> None:
        super().__init__(name, seating_capacity, speed, wheel_number)

    def get_charge(self):
        FARE_CHARGE = 110
        seats = self.get_seating_capacity()
        return seats * FARE_CHARGE


class Taxi(Bus):
    def __init__(
        self, name: str, seating_capacity: int, speed: float, wheel_number
    ) -> None:
        super().__init__(name, seating_capacity, speed, wheel_number)
        pass


vehicle = Vehicle("Man", 20, 60, 4)
bus = Bus("Mercedes", 80, 50, 8)
print(bus.get_charge())
print(bus.get_name())
