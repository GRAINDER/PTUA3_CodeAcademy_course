class Vehicle:
    def __init__(self, seating_capacity: int) -> int:
        self.seating_capacity = seating_capacity
        return self.seating_capacity

    def start_drive(self):
        print("The vehicle is now driving.")

    def stop(self):
        print("The vehicle has stopped.")

    def get_signal(self):
        print("Beep beep!")

    def get_default_fare(self):
        return self.seating_capacity * 100


class Bus(Vehicle):
    def get_fare(self):
        fare = super().get_default_fare()
        return fare * 1.1


class Taxi(Vehicle):
    def get_fare(self, distance):
        fare = super().get_default_fare()
        return fare + distance * 10


class Train(Vehicle):
    def __init__(self, seating_capacity, num_cars):
        super().__init__(seating_capacity)
        self.num_cars = num_cars

    def get_default_fare(self):
        return super().get_default_fare() * self.num_cars



bus = Bus(50)
print(bus.get_default_fare())  
print(bus.get_fare())         

taxi = Taxi(4)
print(taxi.get_default_fare())
print(taxi.get_fare(10))        

train = Train(50, 3)
print(train.get_default_fare())  
