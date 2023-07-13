import unittest
from main import convert_int_to_roman
from unittest.mock import Mock

class TestConvertIntToRoman(unittest.TestCase):
    def testconvert_to_five_correct(mock):
        mock.assertEqual(convert_int_to_roman(5),"V")

    def testconvert_to_nine_correct(self):
        self.assertEqual(convert_int_to_roman(9),"IX")

    def testconvert_to_forty_correct(self):
        self.assertEqual(convert_int_to_roman(40),"XL")
    
    def testconvert_to_one_ninty_zero_four_correct(self):
        self.assertEqual(convert_int_to_roman(1904),"MCMIV")


mock = Mock()
mock

# Pass mock as an argument to do_something()
TestConvertIntToRoman.testconvert_to_five_correct(mock)

# Patch the json library
json = mock




    


