### **Repository 5: Password Generator**
```python
# Repository: python-password-generator
# Description: Generate secure random passwords.

import random
import string

def is_strong_password(password):
    return len(password) >= 8 and any(c.isupper() for c in password) and any(c.isdigit() for c in password)

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    if is_strong_password(password):
        return password
    return generate_password(length)

import argparse
import csv

def save_passwords_to_csv(passwords, filename="passwords.csv"):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Password"])
        for password in passwords:
            writer.writerow([password])
    print(f"Passwords saved to {filename}")

parser = argparse.ArgumentParser(description="Generate secure passwords.")
parser.add_argument("--length", type=int, default=12, help="Length of the password")
args = parser.parse_args()

print("Generated password:", generate_password(args.length))

# Example usage
print("Generated password:", generate_password())
