# Afficher toutes les paires de lettres

from string import ascii_lowercase

for i in ascii_lowercase:
    for j in ascii_lowercase:
        r = i + j
        print(r)