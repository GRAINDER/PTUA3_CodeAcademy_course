import unittest

from main import is_leap


class TestIsLeap(unittest.TestCase):
    def test_returns_true_when_is_leap(self):
        result = is_leap(2000)
        self.assertTrue(result)

    def test_returns_false_when_is_not_leap(self):
        result = is_leap(2100)
        self.assertFalse(result)

    def test_raises_error_when_str_is_passed(self):
        with self.assertRaises(TypeError):
            is_leap(2000)