from typing import List

class Person:
    def __init__(self, name: str, food_like: List[str], food_hate: List[str]):
        self.name = name
        self.food_like = food_like
        self.food_hate = food_hate
    
    def taste(self, food_name: str):
        if food_name in self.food_like:
            return print(f"{self.name} eats the {food_name} and loves it!") 
        elif food_name in self.food_hate:
            return print(f"{self.name} hates the {food_name} and hates it!")  
        elif food_name not in self.food_like and food_name not in self.food_hate:
            return print(f"{self.name} does not like the {food_name}")

            

person_one = Person("Sam", ["ice cream"], ["carrots"])

person_one.taste("ice cream")  #"Sam eats the ice cream and loves it!"
person_one.taste("cheese")  #"Sam eats the cheese!"
person_one.taste("carrots")  #"Sam eats the carrots and hates it!"