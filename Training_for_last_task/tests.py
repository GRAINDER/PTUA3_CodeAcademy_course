import unittest
import data
import logging
from crudv5 import add_info, delete_info, read_info, update_info
from main import CPU, CPUCooler, CPUMotherBoard, CPUMemory, CPUStorage, CPUVideoCard


class TestCPU(unittest.TestCase):
    def setUp(self):
        self.cpu = CPU(data.cpu_info)

    def test_get_name(self):
        self.assertEqual(self.cpu.get_name(), data.cpu_info["name"])

    def test_get_price(self):
        self.assertEqual(self.cpu.get_price(), data.cpu_info["price"])

    def test_get_brand(self):
        self.assertEqual(self.cpu.get_brand(), data.cpu_info["brand"])

    def test_get_speed(self):
        self.assertEqual(self.cpu.get_speed(), data.cpu_info["speed"])

    def test_get_power_usage(self):
        self.assertEqual(self.cpu.get_power_usage(),data.cpu_info["power_usage"])

    def test_get_info(self):
        expected_info = f"{data.cpu_info['brand']} {data.cpu_info['name']}, Price: {data.cpu_info['price']} Speed: {data.cpu_info['speed']}, Power Usage: {data.cpu_info['power_usage']}"
        # self.assertEqual(self.cpu.get_info(), expected_info)


class TestCPUCooler(unittest.TestCase):
    def setUp(self):
        self.cpu_cooler = CPUCooler(data.cpu_cooler_info)





class TestDictionaryFunctions(unittest.TestCase):
    def setUp(self):
        # Sample dictionary for testing
        self.test_dict = {"name": "John", "age": 30, "city": "New York"}

    def test_delete_info(self):
        # Delete an existing key
        delete_info(self.test_dict, "name")
        self.assertNotIn("name", self.test_dict)

        # Try to delete a non-existent key
        with self.assertLogs(level=logging.ERROR):
            delete_info(self.test_dict, "gender")

    def test_update_info(self):
        # Update an existing key
        update_info(self.test_dict, "age", 35)
        self.assertEqual(self.test_dict["age"], 35)

        # Try to update a non-existent key
        with self.assertLogs(level=logging.ERROR):
            update_info(self.test_dict, "gender", "male")

    def test_read_info(self):
        # Read an existing key
        result = read_info(self.test_dict, "city")
        self.assertEqual(result, "New York")

        # Try to read a non-existent key
        with self.assertLogs(level=logging.ERROR):
            read_info(self.test_dict, "gender")

        # Try to read a non-existent key and check the returned value
        result = read_info(self.test_dict, "gender")
        self.assertIsNone(result)


if __name__ == "__main__":
    unittest.main()