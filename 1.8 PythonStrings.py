# 1. username_generator function
def username_generator(first_name, last_name):
    user_name = first_name[:3] + last_name[:4]
    return user_name

# Example testing of username_generator:
print(username_generator("Abe", "Simpson"))  # Output: AbeSimp
print(username_generator("Jo", "Li"))        # Output: JoLi (uses entire names if shorter)

# 2 & 3. password_generator function
def password_generator(user_name):
    password = ""
    length = len(user_name)
    for i in range(length):
        previous_index = (i - 1) % length  # To wrap around circularly
        password += user_name[previous_index]
    return password

# Example testing of password_generator:
example_username = "AbeSimp"
print(password_generator(example_username))  # Output: pAbeSim
