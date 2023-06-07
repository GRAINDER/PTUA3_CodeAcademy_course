import unittest

class TestIntegerToRoman(unittest.TestCase):

    def test_1_to_roman(self):
        self.assertEqual(integer_to_roman(5), 'V')

    def test_4_to_roman(self):
        self.assertEqual(integer_to_roman(9), 'IX')

    def test_9_to_roman(self):
        self.assertEqual(integer_to_roman(40), 'XL')

    def test_58_to_roman(self):
        self.assertEqual(integer_to_roman(1904), 'MCMIV')

    def test_1994_to_roman(self):
        self.assertEqual(integer_to_roman(1994), 'MCMXCIV')

def integer_to_roman(num: int) -> str:
    roman = ''
    values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    symbols = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    i = 0
    while num > 0:
        if num - values[i] >= 0:
            roman += symbols[i]
            num -= values[i]
        else:
            i += 1
    return roman

if __name__ == '__main__':
    unittest.main()
