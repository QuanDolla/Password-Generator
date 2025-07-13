import random
import string

def generate_password(length=12, use_upper=True, use_digits=True, use_special=True):
    # Base character set
    characters = list(string.ascii_lowercase)

    # Add optional character sets
    if use_upper:
        characters += list(string.ascii_uppercase)
    if use_digits:
        characters += list(string.digits)
    if use_special:
        characters += list("!@#$%^&*()-_=+[{]}|;:',<.>/?")

    # Ensure we have a valid set to choose from
    if not characters:
        raise ValueError("No character types selected for password generation.")

    # Randomly select characters
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage:
if __name__ == "__main__":
    # Customize these as needed
    length = int(input("Enter desired password length: "))
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include digits? (y/n): ").lower() == 'y'
    use_special = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, use_upper, use_digits, use_special)
    print(f"\nYour generated password: {password}")

