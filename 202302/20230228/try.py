# Import necessary libraries
import pandas as pd

# Define the warehouse inventory
inventory = pd.DataFrame({'Item': ['A', 'B', 'C', 'D', 'E'],
                          'Location': ['W1', 'W2', 'W3', 'W4', 'W5'],
                          'Quantity': [10, 5, 20, 15, 8]})

# Define the order list
order = pd.DataFrame({'Item': ['A', 'B', 'C', 'D', 'E'],
                      'Quantity': [2, 1, 4, 3, 2]})

# Create a dictionary to store the locations of the items
locations = dict(zip(inventory['Item'], inventory['Location']))

# Loop through the order list and pick items from the inventory
for index, row in order.iterrows():
    item = row['Item']
    quantity = row['Quantity']
    location = locations[item]
    available_quantity = inventory.loc[inventory['Item'] == item, 'Quantity'].values[0]
    
    if available_quantity < quantity:
        print(f"Not enough {item} in stock.")
    else:
        inventory.loc[inventory['Item'] == item, 'Quantity'] -= quantity
        print(f"Picked {quantity} {item} from {location}.")
