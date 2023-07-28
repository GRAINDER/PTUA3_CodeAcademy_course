import data
from typing import Dict, Union
import logging

# Define a logger to handle error messages
logging.basicConfig(level=logging.DEBUG, filename='data.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')


# Define types for the dictionaries
CPUInfo = Dict[str, Union[str, float]]
CPUCoolerInfo = Dict[str, Union[str, float]]
MotherboardInfo = Dict[str, Union[str, float]]
MemoryInfo = Dict[str, Union[str, float]]
StorageInfo = Dict[str, Union[str, float]]
VideoCardInfo = Dict[str, Union[str, float]]

# Function to add additional info to any chosen dictionary


def add_info(dictionary: Dict, key: str, value: Union[str, float]) -> None:
    dictionary[key] = value

# Function to delete information from any chosen dictionary


def delete_info(dictionary: Dict, key: str) -> None:
    try:
        del dictionary[key]
    except KeyError:
        logging.error(f"The key '{key}' does not exist in the dictionary.")

# Function to update information in any chosen dictionary


def update_info(dictionary: Dict, key: str, value: Union[str, float]) -> None:
    if key in dictionary:
        dictionary[key] = value
    else:
        logging.error(f"The key '{key}' does not exist in the dictionary.")

# Function to read information from any chosen dictionary


def read_info(dictionary: Dict, key: str) -> Union[str, float]:
    try:
        return dictionary[key]
    except KeyError:
        logging.error(f"The key '{key}' does not exist in the dictionary.")
        return None

# Sample dictionaries (same as before)
# ...


if __name__ == "__main__":
    # Dictionary selection
    dictionaries = {
        "cpu_info": data.cpu_info,
        "cpu_cooler_info": data.cpu_cooler_info,
        "motherboard_info": data.motherboard_info,
        "memory_info": data.memory_info,
        "storage_info": data.storage_info,
        "video_card_info": data.video_card_info,
    }

    print("Available dictionaries:")
    for idx, key in enumerate(dictionaries.keys(), start=1):
        print(f"{idx}. {key}")

    chosen_dict_name = input(
        "Enter the name of the dictionary you want to work with: ")

    # Check if the chosen_dict_name exists
    if chosen_dict_name in dictionaries:
        chosen_dict = dictionaries[chosen_dict_name]
    else:
        logging.error(f"The dictionary '{chosen_dict_name}' does not exist.")
        exit(1)

    # Interactively perform CRUD operations
    while True:
        print("\nOperations:")
        print("1. Add information")
        print("2. Delete information")
        print("3. Update information")
        print("4. Read information")
        print("5. Exit")
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            key = input("Enter the key for the new information: ")
            value = input("Enter the value for the new information: ")
            add_info(chosen_dict, key, value)
        elif choice == "2":
            key = input("Enter the key to delete information: ")
            delete_info(chosen_dict, key)
        elif choice == "3":
            key = input("Enter the key to update information: ")
            value = input("Enter the new value: ")
            update_info(chosen_dict, key, value)
        elif choice == "4":
            key = input("Enter the key to read information: ")
            info = read_info(chosen_dict, key)
            if info is not None:
                print(f"{key}: {info}")
        elif choice == "5":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
