import unittest
from main import eligible_customers


class TestofEligibleCustomer(unittest.TestCase):
    def test_for_eligible_customer(self):
        
        customers = {
            "Alice": [2, 15],
            "Bob": [5, 10, 15],
            "Charlie": [2, 15, 20],
            "Dave": [5, 10, 15, 20],
            "Eve": [5, 10, 15]
        }

        min_orders = 3
        min_price = 10


        result = eligible_customers(customers, min_orders, min_price)
        self.assertEqual(result, ["Dave"])

    # def test_amount_of_receipt(self):
    #     result = eligible_customers(1, 2, 3)
    #     self.assertLess(result, 8)

    def test_amount_of_orders(self):
        
        customers = {
            "Alice": [2, 15],
            "Bob": [5, 10, 15],
            "Charlie": [2, 15, 20],
            "Dave": [5, 10, 15, 20],
            "Eve": [5, 10, 15]
        }

        min_orders = 3
        min_price = 10


        result = eligible_customers(min_orders)
        self.assertEqual(result, 2)
