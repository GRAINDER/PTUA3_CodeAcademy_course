import data
#from crud_op_for_db import add_info, delete_info, update_info
import logging
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional

logging.basicConfig(level=logging.DEBUG, filename='data.log', filemode='a', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')

"""Create a class that would represent pc parts. 
It should contain basic methods to retreive items name, price, colour (if applicable).
PC part list can be found here: https://pcpartpicker.com/list/
The every separate part should have at least 3-4 methods to gather this part specific data (example: CPU - brand , speed, power usuage etc.)
At this stage, dictionary data structures can work as Database. 
OOP abstraction, inheritance and encapsulation must be presented in a code base. 
Unit tests must be written for the methods."""


"""Phase 2: Add logging to all necessary functionality to see the data flow (with logger config.).
Add exception handling , describe your own exceptions if necessary. 
Create functions that would update current datasets (database). 
Add functions that would parse durrent datasets(database) by specific parameters (CPU name = 'AMD') 
Use  List, Dict comprehentions to get parsed data."""

class PCPart(ABC):
    def __init__(self, part_info: Dict[str, Any]):

        try:
            self.source = "PC part picker"
            self.name = part_info["name"]
            self.price = part_info["price"]

        except KeyError:
            logging.error(KeyError)
            logging.error("name or price is missing")


    def get_name(self) -> str:
        return self.name

    def get_price(self) -> float:
        return self.price

    @staticmethod
    def is_high_price() -> bool:
        return data.cpu_info["price"] > 200

    @abstractmethod
    def get_info(self):
        pass


class CPU(PCPart):
    def __init__(self, part_info: Dict[str, Any]):
        super().__init__(part_info)
        self.brand = data.cpu_info["brand"]
        self.speed = data.cpu_info["speed"]
        self.power_usage = data.cpu_info["power_usage"]

    def get_brand(self) -> str:
        return self.brand

    def get_speed(self) -> str:
        return self.speed

    def get_power_usage(self) -> str:
        return self.power_usage

    def get_info(self):
        return f"Brand: {self.brand} Name: {self.name}, Price: {self.price} Speed: {self.speed}, Power Usage: {self.power_usage}"


class CPUCooler(PCPart):
    def __init__(self, part_info: Dict[str, Any]):
        super().__init__(part_info)
        self.noise_level = data.cpu_cooler_info["noise_level"]
        self.fan = data.cpu_cooler_info["fan"]
        self.color = data.cpu_cooler_info["color"]

    def get_noise_level(self) -> str:
        return self.noise_level

    def get_fan(self) -> str:
        return self.fan

    def get_color(self) -> str:
        return self.color

    def get_info(self):
        return f"Name: {self.name}, Price, {self.price}, Noise Level: {self.noise_level}, Fan: {self.fan}, Color: {self.color}"


class CPUMotherBoard(PCPart):
    def __init__(self, part_info: Dict[str, Any]):
        super().__init__(part_info)
        self.memory = data.motherboard_info["memory"]
        self.memory_slots = data.motherboard_info["memory_slots"]
        self.color = data.motherboard_info["color"]

    def get_memory(self) -> str:
        return self.memory

    def get_memory_slots(self) -> str:
        return self.memory_slots

    def get_color(self) -> str:
        return self.color

    def get_info(self):
        return f"Name: {self.name}, Price: {self.price}, Memory: {self.memory}, Memory Slots: {self.memory_slots}, Color: {self.color}"


class CPUMemory(PCPart):
    def __init__(self, part_info: Dict[str, Any]):
        super().__init__(part_info)
        self.speed = data.memory_info["speed"]
        self.modules = data.memory_info["modules"]
        self.color = data.memory_info["color"]

    def get_speed(self) -> str:
        return self.speed

    def get_modules(self) -> str:
        return self.modules

    def get_color(self) -> str:
        return self.color

    def get_info(self):
        return f"Name: {self.name}, Price: {self.price}, Speed: {self.speed}, Modules: {self.modules}, Color: {self.color}"


class CPUStorage(PCPart):
    def __init__(self, part_info: Dict[str, Any]):
        super().__init__(part_info)
        self.capaciy = data.storage_info["capaciy"]
        self.cache = data.storage_info["cache"]
        self.type = data.storage_info["type"]

    def get_capacity(self) -> str:
        return self.capaciy

    def get_cache(self) -> str:
        return self.cache

    def get_type(self) -> str:
        return self.type

    def get_info(self):
        return f"Name: {self.name}, Capacity: {self.capaciy}, Cache: {self.cache}, Type: {self.type}"


class CPUVideoCard(PCPart):
    def __init__(self, part_info: Dict[str, Any]):
        super().__init__(part_info)
        self.chipset = data.video_card_info["chipset"]
        self.memory = data.video_card_info["memory"]
        self.color = data.video_card_info["color"]

    def get_chipset(self) -> str:
        return self.chipset

    def get_memory(self) -> str:
        return self.memory

    def get_color(self) -> str:
        return self.color

    def get_info(self):
        return f"Name: {self.name}, Capacity: {self.chipset}, Cache: {self.memory}, Color: {self.color}"


if __name__ == "__main__":

    try:
        cpu = CPU(data.cpu_info)
        print(cpu.source)
        print("CPU Information:")
        # print("name:", cpu.get_name())
        # print("price:", cpu.get_price())
        # print("brand:", cpu.get_brand())
        # print("Speed:", cpu.get_speed())
        # print("Power Usage:", cpu.get_power_usage())
        # print("Is higher price:", cpu.is_high_price())
        # logging.info(f"CPU Name: {cpu.get_name()}")
        # logging.info(f"CPU Price: {cpu.get_price()}")
        # logging.info(f"CPU Brand: {cpu.get_brand()}")
        # logging.info(f"CPU Speed: {cpu.get_speed()}")
        # logging.info(f"CPU Power Usage: {cpu.get_power_usage()}")
        logging.info(f"CPU full info: {cpu.get_info()}")
        print(cpu.get_info())

    except Exception as e:
        # Logging error if any exception occurs
        print(e)
        logging.error(f"Error: {str(e)}")
        print("An error occurred. Please check the log file for details.")

    try:
        cpu_cooler = CPUCooler(data.cpu_cooler_info)
        print(cpu_cooler.source)
        print("\nCPU Cooler Information:")
        # print("name:", cpu_cooler.get_name())
        # print("price:", cpu_cooler.get_price())
        # print("color:", cpu_cooler.get_color())
        # print("noice level:", cpu_cooler.get_noise_level())
        # print("fan:", cpu_cooler.get_fan())
        logging.info(f"CPU cooler full info: {cpu_cooler.get_info()}")
        print(cpu_cooler.get_info())

    except Exception as e:
        # Logging error if any exception occurs
        logging.error(f"Error: {str(e)}")
        print("An error occurred. Please check the log file for details.")

    try:
        cpu_mother_board = CPUMotherBoard(data.motherboard_info)
        print("\nCPU Mother Board Information:")
        # print("name:", cpu_mother_board.get_name())
        # print("price:", cpu_mother_board.get_price())
        # print("color:", cpu_mother_board.get_color())
        # print("noice level:", cpu_mother_board.get_noise_level())
        # print("fan:", cpu_mother_board.get_fan())
        logging.info(
            f"CPU Mother Board full info: {cpu_mother_board.get_info()}")
        print(cpu_mother_board.get_info())

    except Exception as e:
        # Logging error if any exception occurs
        logging.error(f"Error: {str(e)}")
        print("An error occurred. Please check the log file for details.")

    try:
        cpu_memory = CPUMemory(data.memory_info)
        print("\nCPU Memory Information:")
        # print("name:", cpu_memory.get_name())
        # print("price:", cpu_memory.get_price())
        # print("color:", cpu_memory.get_color())
        # print("noice level:", cpu_memory.get_noise_level())
        # print("fan:", cpu_memory.get_fan())
        logging.info(f"CPU Memory full info: {cpu_memory.get_info()}")
        print(cpu_memory.get_info())

    except Exception as e:
        # Logging error if any exception occurs
        logging.error(f"Error: {str(e)}")
        print("An error occurred. Please check the log file for details.")

    try:
        cpu_storage = CPUStorage(data.storage_info)
        print("\nCPU Storage Information:")
        # print("name:", cpu_storage.get_name())
        # print("price:", cpu_storage.get_price())
        # print("capacity:", cpu_storage.get_capacity())
        # print("cashe:", cpu_storage.get_cache())
        # print("type:", cpu_storage.get_type())
        logging.info(f"CPU Storage full info: {cpu_storage.get_info()}")
        print(cpu_storage.get_info())

    except Exception as e:
        # Logging error if any exception occurs
        logging.error(f"Error: {str(e)}")
        print("An error occurred. Please check the log file for details.")

    try:
        cpu_video_card = CPUVideoCard(data.video_card_info)
        print("\nCPU Video Card Information:")
        # print("name:", cpu_storage.get_name())
        # print("price:", cpu_storage.get_price())
        # print("capacity:", cpu_storage.get_capacity())
        # print("cashe:", cpu_storage.get_cache())
        # print("type:", cpu_storage.get_type())
        logging.info(f"CPU Video Card full info: {cpu_video_card.get_info()}")
        print(cpu_video_card.get_info())

    except Exception as e:
        # Logging error if any exception occurs
        logging.error(f"Error: {str(e)}")
        print("An error occurred. Please check the log file for details.")
