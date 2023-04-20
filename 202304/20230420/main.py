#Create a dataclass named "Product" that has the following attributes:
    # product_id: int
    # name: str
    # price: float
    # quantity: int
# The class should also have a method named "total_cost" that calculates and returns the total cost of the product, which is the price multiplied by the quantity.
# Create a list of Product objects and write a function that takes this list as input and returns the product with the highest total cost.
# Write a program that creates a list of 5 Product objects, prints out their attributes, and then calls the function to find the product with the highest total cost.


from dataclasses import dataclass
@dataclass
class Product:
    product_id: int
    name: str
    price: float
    quantity: int

    def total_cost(self):
        return self.price * self.quantity

class Product_lists:
    Apple = Product(product_id=1, name="Apple", price=1, quantity=10)
    Banana = Product(product_id=2, name="Banana", price=2, quantity=5)
    Peach = Product(product_id=3, name="Peach", price=1.5, quantity=15)
    Pear = Product(product_id=4, name="Pear", price=2, quantity=20)
    Orange = Product(product_id=5, name="Orange", price=0.5, quantity=25)

@dataclass
class Total:
    product: Product_lists


# my_product_two = Total(product=Product_lists.Apple)
# # my_product_two_two = Total(price=1.1, quantity=2, product=Product_lists.Apple)
# print(my_product_two.total_cost())

my_products = Product(product_id=1, name="Apple", price=1, quantity=10)
print(my_products.name, my_products.price, my_products.quantity)

my_products = Product(1, "apple", 2.5, 2).total_cost()
print(my_products)



