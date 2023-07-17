import data
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional


class PCPart(ABC):
    def __init__(self, part_info: Dict[str, Any]):
        self.name = data.cpu_info["name"]
        self.price = data.cpu_info["price"]

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
        self.name = data.cpu_info["name"]
        self.price = data.cpu_info["price"]
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
        return f"{self.brand} {self.name}, Price: {self.price} Speed: {self.speed}, Power Usage: {self.power_usage}"


class CPUCooler(PCPart):
    def __init__(self, part_info: Dict[str, Any]):
        super().__init__(part_info)
        self.name = data.cpu_cooler_info["name"]
        self.price = data.cpu_cooler_info["price"]
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
        return f"{self.name}, Price, {self.price}, Noise Level: {self.noise_level}, Fan: {self.fan}, Color: {self.color}"


class CPUMotherBoard(PCPart):
    def __init__(self, part_info: Dict[str, Any]):
        super().__init__(part_info)
        self.name = data.motherboard_info["name"]
        self.price = data.motherboard_info["price"]
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
        return f"{self.name}, {self.price}, Memory: {self.memory}, Memory_slots: {self.memory_slots}, Color: {self.color}"


class CPUMemory(PCPart):
    def __init__(self, part_info: Dict[str, Any]):
        super().__init__(part_info)
        self.name = data.memory_info["name"]
        self.price = data.memory_info["price"]
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
        return f"{self.name}, {self.price}, speed: {self.speed}, modules: {self.modules}, Color: {self.color}"





class CPUStorage(PCPart):
    def __init__(self, part_info: Dict[str, Any]):
        super().__init__(part_info)
        self.name = data.storage_info["name"]
        self.price = data.storage_info["price"]
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
        return f"{self.name}, capacity: {self.capaciy}, cache: {self.cache}, cache: {self.type}"


class CPUVideoCard(PCPart):
    def __init__(self, part_info: Dict[str, Any]):
        super().__init__(part_info)
        self.name = data.video_card_info["name"]
        self.price = data.video_card_info["price"]
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
        return f"{self.name}, capacity: {self.chipset}, cache: {self.memory}, cache: {self.color}"


















if __name__ == "__main__":


    cpu = CPU(data.cpu_info)
    cpu_cooler = CPUCooler(data.cpu_cooler_info)
    cpu_mother_board = CPUMotherBoard(data.monitor_info)
    cpu_memory = CPUMemory(data.memory_info)
    cpu_storage = CPUStorage(data.storage_info)
    cpu_video_card = CPUVideoCard(data.video_card_info)


    print("CPU Information:")
    # print("name:", cpu.get_name())
    # print("price:", cpu.get_price())
    # print("brand:", cpu.get_brand())
    # print("Speed:", cpu.get_speed())
    # print("Power Usage:", cpu.get_power_usage())
    # print("Is higher price:", cpu.is_high_price())
    print("info:", cpu.get_info())

    print("\nCPU Cooler Information:")
    # print("name:", cpu_cooler.get_name())
    # print("price:", cpu_cooler.get_price())
    # print("color:", cpu_cooler.get_color())
    # print("noice level:", cpu_cooler.get_noise_level())
    # print("fan:", cpu_cooler.get_fan())
    print("info:", cpu_cooler.get_info())

    print("\nCPU Mother Board Information:")
    # print("name:", cpu_mother_board.get_name())
    # print("price:", cpu_mother_board.get_price())
    # print("color:", cpu_mother_board.get_color())
    # print("noice level:", cpu_mother_board.get_noise_level())
    # print("fan:", cpu_mother_board.get_fan())
    print("info:", cpu_mother_board.get_info())


    print("\nCPU Memory Information:")
    # print("name:", cpu_memory.get_name())
    # print("price:", cpu_memory.get_price())
    # print("color:", cpu_memory.get_color())
    # print("noice level:", cpu_memory.get_noise_level())
    # print("fan:", cpu_memory.get_fan())
    print("info:", cpu_memory.get_info())


    print("\nCPU Storage Information:")
    # print("name:", cpu_storage.get_name())
    # print("price:", cpu_storage.get_price())
    # print("capacity:", cpu_storage.get_capacity())
    # print("cashe:", cpu_storage.get_cache())
    # print("type:", cpu_storage.get_type())
    print("info:", cpu_storage.get_info())

    print("\nCPU Video Card Information:")
    # print("name:", cpu_storage.get_name())
    # print("price:", cpu_storage.get_price())
    # print("capacity:", cpu_storage.get_capacity())
    # print("cashe:", cpu_storage.get_cache())
    # print("type:", cpu_storage.get_type())
    print("info:", cpu_video_card.get_info())