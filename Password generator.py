#Password Generator
import random
import string

def generate_password():
    try:
        length = int(input("Enter password length: "))
        if length <= 0:
            print("Password length must be greater than 0.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid number.")

generate_password()