def get_user_input(prompt):
    return input(prompt).strip()


def validate_key(key):
    try:
        key = int(key)
        if 1 <= key <= 25:
            return key
        else:
            print("Key must be an integer between 1 and 25. Please try again.")
            return None
    except ValueError:
        print("Invalid input. Key must be an integer between 1 and 25. Please try again.")
        return None


def sanitize_text(text):
    # Convert to uppercase and remove non-alphabetic characters
    sanitized = ''.join([char.upper() for char in text if char.isalpha()])
    return sanitized


def shift_letter(letter, key, operation):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    idx = alphabet.index(letter)

    if operation == "encrypt":
        new_idx = (idx + key) % 26
    elif operation == "decrypt":
        new_idx = (idx - key) % 26

    return alphabet[new_idx]


def process_message(message, key, operation):
    # Sanitize the message
    message = sanitize_text(message)

    result = []
    for letter in message:
        shifted_letter = shift_letter(letter, key, operation)
        result.append(shifted_letter)

    return ''.join(result)


def main():
    while True:
        operation = get_user_input("Would you like to encrypt or decrypt? (Enter 'encrypt' or 'decrypt'): ").lower()
        if operation not in ["encrypt", "decrypt"]:
            print("Invalid operation. Please enter 'encrypt' or 'decrypt'.")
            continue

        key = None
        while key is None:
            key_input = get_user_input("Enter the key (1-25): ")
            key = validate_key(key_input)

        message = get_user_input("Enter the message or cryptogram: ")

        result = process_message(message, key, operation)

        if operation == "encrypt":
            print(f"Encrypted message (cryptogram): {result}")
        else:
            print(f"Decrypted message: {result}")

        again = get_user_input("Would you like to perform another operation? (yes/no): ").lower()
        if again != 'yes':
            break


if __name__ == "__main__":
    main()
