# Fréquence de lettres dans un fichier

from string import ascii_lowercase

f = open("words.txt", "r")

alphabet = []
texte = f.read()
taille = len(texte)

for i in ascii_lowercase:
    alphabet.append((i,texte.count(i)))

for i in range(len(alphabet)):
    frequence = alphabet[i][1] / taille
    if frequence > 0:
        print(f"{alphabet[i][0]}: {frequence:.2f}")