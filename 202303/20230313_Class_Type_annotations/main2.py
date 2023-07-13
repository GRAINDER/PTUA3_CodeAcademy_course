# Create a class Smoothie and do the following:
# Create an instance attribute called ingredients.
# Create a get_cost method which calculates the total cost of the ingredients used to make the smoothie.
# Create a get_price method which returns the number from get_cost plus the number from get_cost multiplied by 1.5. Round to two decimal places.
# Create a get_name method which gets the ingredients and puts them in alphabetical order into a nice descriptive sentence. If there are multiple ingredients, add the word "Fusion" to the end but otherwise, add "Smoothie". Remember to change "-berries" to "-berry". See the examples below.
# Then create two specific smotthies with specific ingredients (new classes) which inherits base Smoothie class and call all methods you implemented.



class Smoothie:
    def __init__(self, ingredients):
       self.ingredients = ingredients

    def get_cost(self):
        cost = 0
        for ingredient in self.ingredients:
            if ingredient == "Strawberries":
                cost += 1.5
            elif ingredient == "Banana":
                cost += 0.5
            elif ingredient == "Mango":
                cost += 2.5
            elif ingredient == "Blueberries":
                cost += 1.0
            elif ingredient == "Raspberries":
                cost += 1.0
            elif ingredient == "Apple":
                cost += 1.0
            elif ingredient == "Pineapple":
                cost += 3.0
        return cost

    def get_price(self):
        cost = self.get_cost()
        price = cost + cost * 1.5
        return round(price, 2)
    
    def get_name(self):
        ingredients = sorted(self.ingredients)

        if len(ingredients) > 1:
            name = " ".join(ingredients) + " Fusion"
        else:
            name = ingredients[0] + " Smoothie"
        return name


class StrawberryBananaSmoothie(Smoothie):
    def __init__(self):
        super().__init__(["Banana", "Strawberries", "Pineapple"])

class MangoPineappleSmoothie(Smoothie):
    def __init__(self):
        super().__init__(["Mango", "Pineapple", "Pineapple"])

sb_smoothie = StrawberryBananaSmoothie()
mp_smoothie = MangoPineappleSmoothie()

print(sb_smoothie.get_cost())
print(sb_smoothie.get_price()) 
print(sb_smoothie.get_name())


print(mp_smoothie.get_cost())  
print(mp_smoothie.get_price())  
print(mp_smoothie.get_name())


