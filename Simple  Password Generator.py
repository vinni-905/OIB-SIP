import random
import string

def generate_password(length=12, exclude_chars='', include_uppercase=True, include_digits=True, include_special=True):
    # Define the character sets based on user preferences
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase if include_uppercase else ''
    digits = string.digits if include_digits else ''
    special_characters = string.punctuation if include_special else ''

    # Combine all character sets
    all_characters = lowercase + uppercase + digits + special_characters

    # Exclude specified characters
    all_characters = ''.join(c for c in all_characters if c not in exclude_chars)

    # Ensure the password contains at least one character from each selected set
    password = []
    if include_uppercase:
        password.append(random.choice(uppercase))
    if include_digits:
        password.append(random.choice(digits))
    if include_special:
        password.append(random.choice(special_characters))

    password += random.choices(all_characters, k=length - len(password))

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Convert the list to a string
    return ''.join(password)

def save_password(password, filename='password.txt'):
    with open(filename, 'w') as file:
        file.write(password)
    print(f"Password saved to {filename}")

def password_strength(password):
    strength = "Weak"
    if len(password) >= 12 and (any(c.isupper() for c in password) and
                                any(c.isdigit() for c in password) and
                                any(c in string.punctuation for c in password)):
        strength = "Strong"
    elif len(password) >= 8:
        strength = "Medium"
    return strength
