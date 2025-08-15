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

# Example usage
print("Generated password:", generate_password())
