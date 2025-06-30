import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password

print("Random Password Generator 🔏")
try:
    length = int(input("Enter desired password length: "))
    if length < 4:
        print("Password should be at least 4 characters long.")
    else:
        print("Generated password:", generate_password(length))
except ValueError:
    print("Please enter a valid number.")
