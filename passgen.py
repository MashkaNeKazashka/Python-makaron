### **Repository 5: Password Generator**
```python
# Repository: python-password-generator
# Description: Generate secure random passwords.

import random
import string

def generate_password(length=12):
    """Generate a secure random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage
print("Generated password:", generate_password())
