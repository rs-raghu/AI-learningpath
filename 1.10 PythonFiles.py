import csv
import json

# 1. Create and write to a text file
with open("example.txt", "w") as file:
    file.write("Line 1: Hello, World!\n")
    file.write("Line 2: Python file handling demo.\n")
    file.write("Line 3: End of sample.\n")

# 2. Append to the text file (non-destructive)
with open("example.txt", "a") as file:
    file.write("Line 4: This line is appended.\n")

# 3. Read the file’s full contents using .read()
with open("example.txt", "r") as file:
    content = file.read()
    print("--- Full File Contents ---")
    print(content)

# 4. Read line-by-line using .readline()
with open("example.txt", "r") as file:
    print("--- Read Line by Line ---")
    line = file.readline()
    while line:
        print(line.strip())
        line = file.readline()

# 5. Read all lines as a list using .readlines()
with open("example.txt", "r") as file:
    lines = file.readlines()
    print("--- Lines as List ---")
    print(lines)

# 6. Create and write to a CSV file
with open("example.csv", "w", newline='', encoding="utf-8") as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(["Name", "Role", "Salary"])
    csv_writer.writerow(["Alice", "Developer", "90000"])
    csv_writer.writerow(["Bob", "Designer", "80000"])
    csv_writer.writerow(["Charlie", "Manager", "95000"])

# 7. Read from the CSV file
with open("example.csv", "r", encoding="utf-8") as csvfile:
    csv_reader = csv.reader(csvfile)
    header = next(csv_reader)
    print("--- CSV Headers ---")
    print(header)
    print("--- CSV Data ---")
    for row in csv_reader:
        print(row)

# 8. Create and write to a JSON file
data = {
    "users": [
        {"name": "Alice", "active": True},
        {"name": "Bob", "active": False}
    ],
    "version": 1.0
}
with open("example.json", "w", encoding="utf-8") as jsonfile:
    json.dump(data, jsonfile, indent=2)

# 9. Read from a JSON file
with open("example.json", "r", encoding="utf-8") as jsonfile:
    loaded_data = json.load(jsonfile)
    print("--- JSON Loaded ---")
    print(loaded_data)
