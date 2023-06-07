#Google is launching a network of autonomous pizza delivery drones and wants you to create a flexible rewards system (Pizza Points™) that can be tweaked in the future. The rules are simple: if a customer has made at least N orders of at least Y price, they get a FREE pizza!
#Create a function that takes a dictionary of customers, a minimum number of orders and a minimum order price. Return a list of customers that are eligible for a free pizza.

def eligible_customers(customers, min_orders, min_price):
    eligible = []
    for customer, orders in customers.items():
        num_orders = 0
        for order in orders:
            if order >= min_price:
                num_orders += 1
        if num_orders >= min_orders:
            eligible.append(customer)
    return eligible




customers = {
    "Alice": [2, 15],
    "Bob": [5, 10, 15],
    "Charlie": [2, 15, 20],
    "Dave": [5, 10, 15, 20],
    "Eve": [5, 10, 15]
}

min_orders = 3
min_price = 10

eligible = eligible_customers(customers, min_orders, min_price)

print(eligible)

