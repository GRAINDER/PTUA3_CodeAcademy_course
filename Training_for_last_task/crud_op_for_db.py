import data
import logging

logging.basicConfig(level=logging.DEBUG, filename='crud_operations.log', filemode='a',
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %H:%M:%S')


def add_info(info_dict, name, **info):
    if name not in info_dict:
        info_dict[name] = info
        return True
    else:
        return False


def delete_info(info_dict, name: str):
    if name in info_dict:
        del info_dict
        return True
    else:
        return False


def update_info(info_dict, name, **updated_info):
    if name in info_dict:
        info_dict[name].update(updated_info)
        return True
    else:
        return False


if __name__ == "__main__":

    # Add a new CPU info to the cpu_info dictionary
    # add_info(data.cpu_info, "AMD Ryzen 9 5900XXXX", price=349.99,
    #          brand="AMD", speed="4.7GHz", power_usage="105W")

    # Delete the CPU cooler info from the cpu_cooler_info dictionary
    delete_info(data.cpu_cooler_info, "be quiet! Dark Rock Pro 4")
    print(data.cpu_cooler_info)
    # # Update the price of CPU Ryzen 5 5600X in the cpu_info dictionary
    # update_info(data.cpu_info, "AMD Ryzen 5 5600X", price=179.99)

    # Print the updated dictionaries
    # print("Updated CPU Info Dictionary:")
    # print(data.cpu_info)

    # print("\nUpdated CPU Cooler Info Dictionary:")
    # print(data.cpu_cooler_info)
