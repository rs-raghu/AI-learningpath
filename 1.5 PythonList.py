# Example inventory list
inventory = [
    "twin bed", "queen bed", "full bed", "twin bed", "king bed",
    "twin bed", "queen bed", "full bed", "full bed", "king bed"
]

# 1. Number of items in the warehouse
inventory_len = len(inventory)

# 2. First element
first = inventory[0]

# 3. Last element
last = inventory[-1]

# 4. Elements at index 2 to 5 (not including 6)
inventory_2_6 = inventory[2:6]

# 5. First 3 items
first_3 = inventory[:3]

# 6. Count 'twin bed's
twin_beds = inventory.count("twin bed")

# 7. Remove and store the 5th element (index 4)
removed_item = inventory.pop(4)

# 8. Insert "19th Century Bed Frame" as 11th item (index 10)
inventory.insert(10, "19th Century Bed Frame")

# 9. Sort inventory
inventory = sorted(inventory)
print(inventory)
