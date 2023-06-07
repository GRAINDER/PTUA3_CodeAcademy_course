

class Banana:
    def __init__(self, color: str, taste: str) -> str:
        self.color = color
        self.taste = taste

    def get_color(self):
        return self.color
      
    def get_taste(self):
        return self.taste
      


fruits = Banana("Yellow", "Sweet")

print(fruits.get_color())
print(fruits.get_taste())