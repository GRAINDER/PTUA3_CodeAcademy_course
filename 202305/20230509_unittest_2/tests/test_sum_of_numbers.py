import unittest
from main import sum_of_numbers, sum_of_list, max_number_f_one, back_str, max_number
import main


class TestSumOfNumbers(unittest.TestCase):
    def test_sum_of_numbers(self):
        self.assertEqual(6, main.sum_of_numbers(1, 2, 3)) #Callable


    def test_sum_of_numbers_two(self):
        result = sum_of_numbers(1, 2, 3)
        self.assertNotEqual(result, 8)

    def test_sum_of_numbers_three(self):
        result = sum_of_numbers(1, 2, 3)
        self.assertLess(result, 8)



class TestSumOfList(unittest.TestCase):
    def test_sum_of_list(self):
        result = sum_of_list([1, 2, 3])
        self.assertEqual(result, 6)


class TestMaxNumberFuncOne(unittest.TestCase):
    def test_max_number_f_one(self):
        result = max_number_f_one(1, 2, 3)
        self.assertEqual(result, 3)


class TestMaxStrBack(unittest.TestCase):
    def test_back_str(self):
        result = back_str("alibaba")
        self.assertEqual(result, "ababila")


class TestMaxNumber(unittest.TestCase):
    def test_max_number(self):
        result = max_number(2, 100, 5, 3)
        self.assertEqual(result, 100)