# 1. Customer names list
first_names = ["Ainsley", "Ben", "Chani", "Depak"]

# 2. Preferred sizes list for first three customers
preferred_size = ["Small", "Large", "Medium"]

# 3. Append Depak's size and print
preferred_size.append("Medium")
print(preferred_size)

# 4. Two-dimensional customer data list (name, size, expedited shipping)
customer_data = [
    ["Ainsley", "Small", True],
    ["Ben", "Large", False],
    ["Chani", "Medium", True],
    ["Depak", "Medium", False],
]
print(customer_data)

# 5. Update Chani's shipping to False
customer_data[2][2] = False

# 6. Remove Ben's (index 1) shipping option
customer_data[1].remove(False)

# 7. Add new customers and merge the lists
new_customers = [["Amit", "Large", True], ["Karim", "X-Large", False]]
customer_data_final = customer_data + new_customers
print(customer_data_final)
