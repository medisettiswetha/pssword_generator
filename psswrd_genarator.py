import random
import string

def generate_password(length=12):
    # Define character pool: letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly choose characters from the pool
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Ask user for desired password length
try:
    length = int(input("Enter desired password length: "))
    if length < 4:
        print("Password should be at least 4 characters long.")
    else:
        print("Generated Password:", generate_password(length))
except ValueError:
    print("Please enter a valid number.")
