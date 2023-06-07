# Create a dataclass named "Product" that has the following attributes:
#     product_id: int
#     name: str
#     price: float
#     quantity: int
# The class should also have a method named "total_cost" that calculates and returns the total cost of the product, which is the price multiplied by the quantity.
# Create a list from dataclass "Product" objects and write a function that takes this list as input and returns the product with the highest total cost.
# Write a program that creates a list of 5 Product objects, prints out their attributes, and then calls the function to find the product with the highest total cost.


# from dataclasses import dataclass
# @dataclass
# class Product:
#     product_id: int
#     name: str
#     price: float
#     quantity: int

#     def total_cost(self):
#         return self.price * self.quantity

# class Product_lists:
#     Apple = Product(product_id=1, name="Apple", price=1, quantity=10)
#     Banana = Product(product_id=2, name="Banana", price=2, quantity=5)
#     Peach = Product(product_id=3, name="Peach", price=1.5, quantity=15)
#     Pear = Product(product_id=4, name="Pear", price=2, quantity=20)
#     Orange = Product(product_id=5, name="Orange", price=0.5, quantity=25)

# @dataclass
# class Total:
#     product: Product_lists


# # my_product_two = Total(product=Product_lists.Apple)
# # # my_product_two_two = Total(price=1.1, quantity=2, product=Product_lists.Apple)
# # print(my_product_two.total_cost())

# my_products = Product(product_id=1, name="Apple", price=1, quantity=10)
# print(my_products.name, my_products.price, my_products.quantity)

# my_products = Product(1, "apple", 2.5, 2).total_cost()
# print(my_products)

# my_products = Product(product_id=2, name="Banana", price=2, quantity=5).total_cost()
# print(my_products)





from dataclasses import dataclass

@dataclass
class Product:
    product_id: int
    name: str
    price: float
    quantity: int
        
    def total_cost(self) -> float:
        return self.price * self.quantity

def find_highest_cost_product(products: list[Product]) -> Product:
    return max(products, key=lambda p: p.total_cost())

# creating a list of 5 Product objects
products_list = [
    Product(1, 'Product 1', 10.0, 3),
    Product(2, 'Product 2', 20.0, 2),
    Product(3, 'Product 3', 15.0, 4),
    Product(4, 'Product 4', 12.5, 5),
    Product(5, 'Product 5', 18.75, 2)
]

# printing out the attributes of the products
for product in products_list:
    print(f"ID: {product.product_id}, Name: {product.name}, Price: {product.price}, Quantity: {product.quantity}")

# finding the product with the highest total cost
highest_cost_product = find_highest_cost_product(products_list)

print(f"\nThe product with the highest total cost is: {highest_cost_product.name}, Total Cost: {highest_cost_product.total_cost()}") 
