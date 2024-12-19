import pandas as pd
import string
import random
from tabulate import tabulate
import datetime

# Maximum weight capacity for each truck
MAX_WEIGHT_ONE_DOOR = 10  # Example: 10 kg for one-door truck
MAX_WEIGHT_TWO_DOOR = 15  # Optional, for future use

# Distance information
destinations = {
    "HCMC": 1700,
    "Da Nang": 800,
    "Dalat": 1500,
    "Nha Trang": 1300,
    "Hai Phong": 100
}

# Rates for billing
WEIGHT_RATE = 5000  # VND per kg
DISTANCE_RATE = 2000  # VND per km

# Item details
Item_detail = [
    {
        "name": "Clothes",
        "price": 100,
        "weight": 1.5,
        "height": 10,
        "length": 5,
        "width": 3,
        "city": "HCMC"
    },
    {
        "name": "Shoes",
        "price": 200,
        "weight": 2.5,
        "height": 15,
        "length": 7,
        "width": 4,
        "city": "Da Nang"
    },
    {
        "name": "Wallet",
        "price": 300,
        "weight": 1.8,
        "height": 20,
        "length": 10,
        "width": 6,
        "city": "Dalat"
    },
    {
        "name": "Iphone 16 Pro Max",
        "price": 400,
        "weight": 4.5,
        "height": 25,
        "length": 12,
        "width": 8,
        "city": "Nha Trang"
    },
    {
        "name": "Macbook Pro",
        "price": 500,
        "weight": 4.0,
        "height": 30,
        "length": 15,
        "width": 10,
        "city": "Hai Phong"
    }
]

def generate_parcel_id(pacellength=10):
    return "VN" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=max(pacellength - 2, 0)))

# Function to calculate volume
def calculate_volume(height, length, width):
    """Calculate the volume in cubic centimeters."""
    return height * length * width

# Function to calculate the bill
def calculate_bill(weight, distance):
    """Calculate the bill based on weight and distance rates."""
    return int(weight * WEIGHT_RATE + distance * DISTANCE_RATE)

# Process the item details
for item in Item_detail:
    # Calculate volume
    item['volume'] = calculate_volume(item['height'], item['length'], item['width'])
    # Assign a unique parcel ID
    item['parcel_id'] = generate_parcel_id()
    # Add distance
    item['distance'] = destinations.get(item['city'], 0)
    # Calculate the bill
    item['bill'] = calculate_bill(item['weight'], item['distance'])

# Knapsack recursive function
def knapsack_recursive(weights, bills, capacity, n):
    if n == 0 or capacity == 0:
        return 0
    if weights[n-1] > capacity:
        return knapsack_recursive(weights, bills, capacity, n-1)
    else:
        return max(
            bills[n-1] + knapsack_recursive(weights, bills, capacity - weights[n-1], n-1),
            knapsack_recursive(weights, bills, capacity, n-1)
        )

# Function to find the items selected in the knapsack
def find_knapsack_items(weights, bills, capacity, n):
    if n == 0 or capacity == 0:
        return []
    if weights[n-1] > capacity:
        return find_knapsack_items(weights, bills, capacity, n-1)
    else:
        if bills[n-1] + knapsack_recursive(weights, bills, capacity - weights[n-1], n-1) >= knapsack_recursive(weights, bills, capacity, n-1):
            return find_knapsack_items(weights, bills, capacity - weights[n-1], n-1) + [n-1]
        else:
            return find_knapsack_items(weights, bills, capacity, n-1)

# Extract weights and bills from item details
weights = [item['weight'] for item in Item_detail]
bills = [item['bill'] for item in Item_detail]

# Find the maximum value and the items selected for the one-door truck
selected_items_indices_one_door = find_knapsack_items(weights, bills, MAX_WEIGHT_ONE_DOOR, len(Item_detail))

# Get the selected items for the one-door truck
selected_items_one_door = [Item_detail[i] for i in selected_items_indices_one_door]

# Get the remaining items for the two-door truck
remaining_items_indices = [i for i in range(len(Item_detail)) if i not in selected_items_indices_one_door]
selected_items_two_door = [Item_detail[i] for i in remaining_items_indices]

# Convert to DataFrames for display
df_one_door = pd.DataFrame(selected_items_one_door)
df_two_door = pd.DataFrame(selected_items_two_door)

# Format the DataFrames for display
for df in [df_one_door, df_two_door]:
    df['weight'] = df['weight'].astype(str) + " kg"
    df['height'] = df['height'].astype(str) + " cm"
    df['length'] = df['length'].astype(str) + " cm"
    df['width'] = df['width'].astype(str) + " cm"
    df['volume'] = df['volume'].astype(str) + " cm³"
    df['bill'] = df['bill'].apply(lambda x: f"{x:,.0f} VND")

# Display the results
print("\n=== Items for One-Door Truck ===")
print(tabulate(df_one_door, headers='keys', tablefmt='grid', showindex=True, maxcolwidths=20))

print("\n=== Items for Two-Door Truck ===")
print(tabulate(df_two_door, headers='keys', tablefmt='grid', showindex=True, maxcolwidths=20))

# Export to CSV files
output_file_one_door = f"one_door_truck_items_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
output_file_two_door = f"two_door_truck_items_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
df_one_door.to_csv(output_file_one_door, index=False)
df_two_door.to_csv(output_file_two_door, index=False)

print(f"\nOne-door truck items exported successfully to {output_file_one_door}")
print(f"Two-door truck items exported successfully to {output_file_two_door}")