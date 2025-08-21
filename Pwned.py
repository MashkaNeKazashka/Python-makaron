import hashlib
import requests

def is_password_safe(password):
    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1[:5], sha1[5:]
    response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
    hashes = (line.split(":") for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return False, count
    return True, 0

# Example usage
password = "password123"
safe, count = is_password_safe(password)
print(f"Password is {'safe' if safe else 'unsafe'} (found {count} times).")
