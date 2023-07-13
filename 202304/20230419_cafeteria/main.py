from ast import List
from dataclasses import dataclass

# class Position:
#     def __init__(self, name: str, lan: float, long: float) -> None:
#         self.name = name
#         self.lan = lan
#         self.long = long

@dataclass
class Position:
    name: str
    lan: float
    long: float


pos = Position(name="Vilnius", lan=0.0, long=0.0)

print(pos.name, pos.lan, pos.long)


@dataclass
class Guest:
    name: str
    bill: float
    position: List[Position]

    def get_bill(self) -> float:
        return self.bill
    
first_guest = Guest(name="Paulius", bill=5.15)
print(first_guest.name, first_guest.bill)




