class Restaurant:
    def __init__(self, name, tables):
        self.name = name
        self.tables = {i: None for i in range(1, tables+1)}  # initialize tables as empty dict

    def __str__(self):
        return f"{self.name} ({len(self.tables)} tables)"

    def check_availability(self, party_size):
        if party_size == 1:
            table_size = 1
            table_range = range(1, 4)
        elif party_size == 2:
            table_size = 2
            table_range = range(4, 7)
        elif party_size == 3:
            table_size = 3
            table_range = range(7, 10)
        else:
            return None  # party size too large
        for table in table_range:
            if self.tables[table] is None:
                return table
        return None

    def reserve_table(self, table_number, party_size):
        table_size = 1 if party_size == 1 else 2 if party_size == 2 else 3
        if self.tables[table_number] is None and table_number in range(table_size*3-2, table_size*3+1):
            self.tables[table_number] = party_size
            return True
        else:
            return False

    def print_menu(self):
        print("MENU:")
        for item, price in menu.items():
            print(f"{item}: ${price:.2f}")

    def take_order(self, table_number):
        order = {}
        while True:
            item = input("Enter item name (or 'done' to finish order): ")
            if item == "done":
                break
            elif item not in menu:
                print("Item not found.")
            else:
                quantity = int(input("Enter quantity: "))
                order[item] = quantity
        total = sum([menu[item] * quantity for item, quantity in order.items()])
        print(f"Total: ${total:.2f}")
        self.print_receipt(table_number, order, total)

    def print_receipt(self, table_number, order, total):
        print(f"TABLE {table_number} RECEIPT:")
        for item, quantity in order.items():
            print(f"{item} x{quantity}: ${menu[item] * quantity:.2f}")
        print(f"TOTAL: ${total:.2f}")


menu = {
    "Hamburger": 5.99,
    "Cheeseburger": 6.49,
    "Fries": 2.99,
    "Soda": 1.49,
}

restaurant = Restaurant("My Restaurant", 9)

print(restaurant)

while True:
    party_size = int(input("Enter party size (1, 2, or 3): "))
    table = restaurant.check_availability(party_size)
    if table is None:
        print("Sorry, no tables are available for your party size. Please try again later.")
    else:
        print(f"Table {table} is available for your party of {party_size}. Would you like to reserve it? (y/n)")
        choice = input().lower()
        if choice == "y":
            if restaurant.reserve_table(table, party_size):
                print(f"Table {table} is reserved for your party of {party_size}.")
                restaurant.take_order(table)
                restaurant.tables[table] = None  # free up table after customer leaves
            else:
                print("Sorry, something went wrong. Please try again later.")
        else:
            print("Okay, please come again soon!")
