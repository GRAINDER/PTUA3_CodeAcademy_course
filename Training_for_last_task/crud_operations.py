import data


# 1. Add Part\n2. Delete Part\n3. Update Part\n4. Exit"
OPERATIONS_DICT = { "Add part": 1,
                    "Delete part": 2,
                    "Update part": 3,
                    "Exit": 4
                }


def add_info_to_dict(info_dict):
    name = input("Enter the name: ")
    if name not in info_dict:
        price = float(input("Enter the price: "))
        brand = input("Enter the brand: ")
        speed = input("Enter the speed: ")
        power_usage = input("Enter the power usage: ")

        info_dict[name] = {
            "name": name,
            "price": price,
            "brand": brand,
            "speed": speed,
            "power_usage": power_usage
        }
        return True
    else:
        print("A part with the same name already exists.")
        return False


def delete_info_from_dict(info_dict):
    name = input("Enter the name of the part to delete: ")
    # this_dict = info_dict

    # # info_dict.pop(name)
    # # print(info_dict)
    # for key in list(this_dict):
    #     if this_dict[key] == name:
    #         del this_dict[key]
    # print(f"{name} has been deleted.")
    # # else:
    # #     print("Part not found.")

    # info_dict.pop(name)
    # print(info_dict)
    # for key in list(info_dict):
    #     if info_dict[key] == name:
    #         del info_dict[key]
    # print(f"{name} has been deleted.")
    # # else:
    # #     print("Part not found.")

    for key in list(info_dict):
        if info_dict[key] == name:
            del info_dict[key]
    print(f"{name} has been deleted.")
    print(list(info_dict))
    # else:
    #     print("Part not found.")


def update_info_in_dict(info_dict):
    name = input("Enter the name of the part to update: ")
    if name in info_dict:
        updated_info = {}
        price = input(
            "Enter the updated price (leave blank to keep the current value): ")
        if price:
            updated_info["price"] = float(price)

        brand = input(
            "Enter the updated brand (leave blank to keep the current value): ")
        if brand:
            updated_info["brand"] = brand

        speed = input(
            "Enter the updated speed (leave blank to keep the current value): ")
        if speed:
            updated_info["speed"] = speed

        power_usage = input(
            "Enter the updated power usage (leave blank to keep the current value): ")
        if power_usage:
            updated_info["power_usage"] = power_usage

        info_dict[name].update(updated_info)
        return True
    else:
        print("Part not found.")
        return False


# Example usage:
def main():
    # cpu_info = {
    #     "name": "AMD",
    #     "price": 162.66,
    #     "brand": "AMD",
    #     "speed": "3.7GHz",
    #     "power_usage": "65W"
    # }

    # cpu_cooler_info = {
    #     "name": "be quiet! Dark Rock Pro 4",
    #     "price": 89.90,
    #     "noise_level": "12.8 - 24.3 dB",
    #     "fan": "1500 RPM",
    #     "color": "black"
    # }

    while True:
        print("Please choose which category you want to update: ")
        component_name, component_dict = _user_selection_from_dict(data.master_info)
        # print("\n1. cpu\n2. cpu cooler\n3. motherboard\n4. memory\n5.storage \n6. video card")
        # print("\n1. Add Part\n2. Delete Part\n3. Update Part\n4. Exit")
        # choice = input("Enter your choice (1/2/3/4): ")

        print(f"Please choose operation to perform on {component_name}:")
        operation_key, operation_name = _user_selection_from_dict(OPERATIONS_DICT)
        print(operation_key)
        if operation_key == "Add part":
            add_info_to_dict(component_dict)
        elif operation_key == "Delete part":
            delete_info_from_dict(component_dict)
        elif operation_key == "Update part":
            update_info_in_dict(component_dict)
        elif operation_key == "Exit":
            break
        else:
            print("Invalid choice. Please try again.")

    print("Final CPU Info Dictionary:")
    # print(cpu_info)


def _user_selection_from_dict(the_dict):
    """ Print the keys of the dictionary preceded by numbers 1..N, get selection from user, loop until successful. """
    selected_value = None
    while not selected_value:
        count = 0
        selection_dict = {}
        for key, value in the_dict.items():
            count += 1
            print(f'{count}. {key}')
            selection_dict[str(count)] = (str(key), value)
        choice = input(f"Enter your choice (1-{count}): ")
        selected_key, selected_value = selection_dict.get(choice)
    return selected_key, selected_value


if __name__ == "__main__":
    main()



