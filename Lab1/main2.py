def get_user_input(prompt):
    return input(prompt).strip()


def validate_key1(key):
    try:
        key = int(key)
        if 1 <= key <= 25:
            return key
        else:
            print("Key 1 must be an integer between 1 and 25. Please try again.")
            return None
    except ValueError:
        print("Invalid input. Key 1 must be an integer between 1 and 25. Please try again.")
        return None


def validate_key2(key2):
    if key2.isalpha() and len(key2) >= 7:
        return key2.upper()
    else:
        print("Key 2 must be at least 7 letters long and contain only Latin alphabet letters. Please try again.")
        return None


def sanitize_text(text):
    # Convert to uppercase and remove non-alphabetic characters
    sanitized = ''.join([char.upper() for char in text if char.isalpha()])
    return sanitized


def shift_letter_with_key2(letter, key1, key2, index, operation):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    idx = alphabet.index(letter)

    # Get the letter from key2 to use for additional shifting
    key2_letter = key2[index % len(key2)]
    key2_shift = alphabet.index(key2_letter)

    # Adjust shift based on the operation
    if operation == "encrypt":
        new_idx = (idx + key1 + key2_shift) % 26
    elif operation == "decrypt":
        new_idx = (idx - key1 - key2_shift) % 26

    return alphabet[new_idx]


def process_message(message, key1, key2, operation):
    # Sanitize the message
    message = sanitize_text(message)

    result = []
    for i, letter in enumerate(message):
        shifted_letter = shift_letter_with_key2(letter, key1, key2, i, operation)
        result.append(shifted_letter)

    return ''.join(result)


def main():
    while True:
        operation = get_user_input("Would you like to encrypt or decrypt? (Enter 'encrypt' or 'decrypt'): ").lower()
        if operation not in ["encrypt", "decrypt"]:
            print("Invalid operation. Please enter 'encrypt' or 'decrypt'.")
            continue

        # Get and validate Key 1
        key1 = None
        while key1 is None:
            key1_input = get_user_input("Enter Key 1 (integer between 1-25): ")
            key1 = validate_key1(key1_input)

        # Get and validate Key 2
        key2 = None
        while key2 is None:
            key2_input = get_user_input("Enter Key 2 (at least 7 letters long): ")
            key2 = validate_key2(key2_input)

        # Get the message/cryptogram
        message = get_user_input("Enter the message or cryptogram: ")

        # Process the message with the two keys
        result = process_message(message, key1, key2, operation)

        if operation == "encrypt":
            print(f"Encrypted message (cryptogram): {result}")
        else:
            print(f"Decrypted message: {result}")

        # Ask if the user wants to perform another operation
        again = get_user_input("Would you like to perform another operation? (yes/no): ").lower()
        if again != 'yes':
            break


if __name__ == "__main__":
    main()
