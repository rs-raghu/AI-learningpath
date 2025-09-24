# 1. List from 0 to 9
single_digits = list(range(10))

# 2. Print each digit in the list
for digit in single_digits:
    print(digit)

# 3. Create an empty list called squares
squares = []

# 4. Append squared value to squares list inside the loop
for digit in single_digits:
    squares.append(digit ** 2)

# 5. Print squares after the loop
print(squares)

# 6. Create cubes using list comprehension
cubes = [digit ** 3 for digit in single_digits]

# 7. Print cubes
print(cubes)
