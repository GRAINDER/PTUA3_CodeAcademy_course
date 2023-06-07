import unittest
import calculator


class TestCalculator(unittest.TestCase):
    def test_sudetis(self):
        self.assertEqual(15, calculator.add(10, 5))
        self.assertEqual(0, calculator.add(-1, 1))
        self.assertEqual(-2, calculator.add(-1, -1))

    def test_atimtis(self):
        self.assertEqual(5, calculator.subtrack(10, 5))
        self.assertEqual(-2, calculator.subtrack(-1, 1))
        self.assertEqual(0, calculator.subtrack(-1, -1))

    def test_daugyba(self):
        self.assertEqual(50, calculator.multiply(10, 5))
        self.assertEqual(-1, calculator.multiply(-1, 1))
        self.assertEqual(1, calculator.multiply(-1, -1))

    def test_dalyba(self):
        self.assertEqual(2, calculator.divide(10, 5))
        self.assertEqual(-1, calculator.divide(-1, 1))
        self.assertEqual(1, calculator.divide(-1, -1))


# Ran 4 tests in 0.002s

# OK