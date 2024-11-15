import random

# Permutare inițială (IP)
IP = [
    58, 50, 42, 34, 26, 18, 10, 2,
    60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6,
    64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9,  1,
    59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5,
    63, 55, 47, 39, 31, 23, 15, 7
]

def text_to_binary(text):
    return ''.join(f"{ord(c):08b}" for c in text)

def apply_permutation(data, table):
    return ''.join(data[i - 1] for i in table)

def generate_random_text(length):
    return ''.join(chr(random.randint(32, 126)) for _ in range(length))

# Pasul principal
def calculate_L1():
    # Introducere date
    choice = input("Doriți să introduceți un mesaj? (y/n): ").strip().lower()
    if choice == 'y':
        text = input("Introduceți mesajul (8 caractere): ").strip()
        if len(text) != 8:
            print("Mesajul trebuie să aibă exact 8 caractere!")
            return
    else:
        text = generate_random_text(8)
        print(f"Mesaj generat aleatoriu: {text}")

    # Conversie în binar
    binary_message = text_to_binary(text)
    print(f"Mesaj în binar: {binary_message}")

    # Aplicare permutare inițială
    permuted_message = apply_permutation(binary_message, IP)
    print(f"Mesaj după permutarea inițială: {permuted_message}")

    # Împărțire în L0 și R0
    L0 = permuted_message[:32]
    R0 = permuted_message[32:]
    print(f"L0: {L0}")
    print(f"R0: {R0}")

    # Calcul L1
    L1 = R0
    print(f"L1: {L1}")

# Rulare funcție
calculate_L1()
