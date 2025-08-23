

import random
import string

def generate_password(length=12):
    """Generate a secure random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def save_password(password, filename="passwords.txt"):
    """Save generated password to a file."""
    with open(filename, 'a') as file:
        file.write(password + "\n")
    print(f"Password saved to {filename}")

# Example usage
password = generate_password()
print("Generated password:", password)
save_password(password)
