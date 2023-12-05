# Le chiffre de César

import string

no_coded = input("Le texte à coder: ")
code = int(input("Le décalage (3 pour César): "))
coded = ""

# Alphabet avec le décalage
alphabet_strange = string.ascii_letters[code:] + string.ascii_letters[:code]

for c in no_coded:
    # c est un espace
    if c == " ":
        coded = coded + " "
    # c est de la ponctuation ou des chiffres, je ne fais pas de traitement pour le moment
    elif c in string.punctuation or c in string.digits:
        coded = coded + c
    elif c in string.ascii_letters:
        # on cherche c dans l'alphabet normal, et on récupére son index
        index = string.ascii_letters.find(c)
        # on affiche le caractère de rang index dans l'alphabet décallé
        coded = coded + alphabet_strange[index]

print(f"\nLa chaine codée est: {coded}")