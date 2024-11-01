import string

# Alfabetul extins pentru limba română (31 de litere)
alfabet_extins = "ABCDEFGHIJKLMNOPQRSTUVWXYZȘȚĂÎÂ"


def creare_matrice_playfair(cheie):
    # Convertim cheia la majuscule și eliminăm caracterele duplicate
    cheie = ''.join(sorted(set(cheie.upper()), key=cheie.index))
    matrice = []

    # Creăm lista cu literele rămase, eliminând literele din cheie
    litere_ramase = [litera for litera in alfabet_extins if litera not in cheie]
    toate_literele = cheie + ''.join(litere_ramase)

    # Formăm matricea de 6x6 pentru Playfair
    for i in range(0, 36, 6):
        matrice.append(list(toate_literele[i:i + 6]))
    return matrice


def gaseste_pozitie(matrice, litera):
    # Găsim poziția unei litere în matrice
    for i, rand in enumerate(matrice):
        if litera in rand:
            return i, rand.index(litera)
    return None, None


def cripteaza_digraf(digraf, matrice):
    # Aplicăm regulile Playfair pentru criptarea unui digraf
    i1, j1 = gaseste_pozitie(matrice, digraf[0])
    i2, j2 = gaseste_pozitie(matrice, digraf[1])

    if i1 == i2:  # Aceeași linie
        return matrice[i1][(j1 + 1) % 6] + matrice[i2][(j2 + 1) % 6]
    elif j1 == j2:  # Aceeași coloană
        return matrice[(i1 + 1) % 6][j1] + matrice[(i2 + 1) % 6][j2]
    else:  # Rectangular
        return matrice[i1][j2] + matrice[i2][j1]


def decripteaza_digraf(digraf, matrice):
    # Aplicăm regulile Playfair pentru decriptarea unui digraf
    i1, j1 = gaseste_pozitie(matrice, digraf[0])
    i2, j2 = gaseste_pozitie(matrice, digraf[1])

    if i1 == i2:  # Aceeași linie
        return matrice[i1][(j1 - 1) % 6] + matrice[i2][(j2 - 1) % 6]
    elif j1 == j2:  # Aceeași coloană
        return matrice[(i1 - 1) % 6][j1] + matrice[(i2 - 1) % 6][j2]
    else:  # Rectangular
        return matrice[i1][j2] + matrice[i2][j1]


def procesare_text(text):
    # Verificăm textul și returnăm doar caracterele permise
    text = ''.join([c.upper() for c in text if c.upper() in alfabet_extins])
    return text


def genereaza_digrafuri(text):
    # Generăm digrafuri pentru criptare
    digrafuri = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if (i + 1) < len(text) else 'X'
        if a == b:
            digrafuri.append(a + 'X')
            i += 1
        else:
            digrafuri.append(a + b)
            i += 2
    return digrafuri


def playfair(cheie, text, operatie):
    if len(cheie) < 7:
        raise ValueError("Cheia trebuie să aibă cel puțin 7 caractere.")

    text = procesare_text(text)
    matrice = creare_matrice_playfair(cheie)

    if operatie == 'criptare':
        digrafuri = genereaza_digrafuri(text)
        rezultat = ''.join([cripteaza_digraf(d, matrice) for d in digrafuri])
    elif operatie == 'decriptare':
        digrafuri = [text[i:i + 2] for i in range(0, len(text), 2)]
        rezultat = ''.join([decripteaza_digraf(d, matrice) for d in digrafuri])
    else:
        raise ValueError("Operație necunoscută. Alegeți 'criptare' sau 'decriptare'.")

    return rezultat


# Exemplu de utilizare
cheie = "EXEMPLUCHEIE"
mesaj = "MESAJ SECRET"
operatie = "criptare"
try:
    criptograma = playfair(cheie, mesaj, operatie)
    print("Rezultatul:", criptograma)

    mesaj_initial = playfair(cheie, criptograma, "decriptare")
    print("Mesaj initial: ", mesaj_initial)
except ValueError as e:
    print(e)
