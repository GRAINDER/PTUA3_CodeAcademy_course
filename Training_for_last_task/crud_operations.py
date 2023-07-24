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
            "Enter the updated price (le3ave blank to keep the current value): ")
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
if __name__ == "__main__":
    cpu_info = {
        "name": "AMD",
        "price": 162.66,
        "brand": "AMD",
        "speed": "3.7GHz",
        "power_usage": "65W"
    }

    cpu_cooler_info = {
        "name": "be quiet! Dark Rock Pro 4",
        "price": 89.90,
        "noise_level": "12.8 - 24.3 dB",
        "fan": "1500 RPM",
        "color": "black"
    }

    while True:
        print("\n1. Add Part\n2. Delete Part\n3. Update Part\n4. Exit")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            add_info_to_dict(cpu_info)
        elif choice == "2":
            delete_info_from_dict(cpu_info)
        elif choice == "3":
            update_info_in_dict(cpu_info)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

    print("Final CPU Info Dictionary:")
    print(cpu_info)
