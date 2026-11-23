
import random
import string

def generate_password(length):

    if length < 4:
        return "Password length must be at least 4."

    # Character collections
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits
    symbols = string.punctuation

    # Select at least one character from each category
    password = [
        random.SystemRandom().choice(uppercase),
        random.SystemRandom().choice(lowercase),
        random.SystemRandom().choice(numbers),
        random.SystemRandom().choice(symbols)
    ]

    # Combine all available characters
    all_characters = uppercase + lowercase + numbers + symbols

    # Fill remaining password length
    for i in range(length - 4):
        password.append(random.SystemRandom().choice(all_characters))

    # Shuffle characters
    random.SystemRandom().shuffle(password)

    return ''.join(password)


print("===== PASSWORD GENERATOR =====")

length = int(input("Enter password length: "))

result = generate_password(length)

print("Generated Password:", result)
