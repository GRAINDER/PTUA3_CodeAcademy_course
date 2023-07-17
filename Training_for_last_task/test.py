import unittest
import data
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
        self.assertEqual(self.cpu.get_info(), expected_info)


class TestCPUCooler(unittest.TestCase):
    def setUp(self):
        self.cpu_cooler = CPUCooler(data.cpu_cooler_info)



if __name__ == "__main__":
    unittest.main()
