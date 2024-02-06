# Afficher toutes les paires de lettres différentes

from string import ascii_lowercase

for i in ascii_lowercase:
    for j in ascii_lowercase:
        if i != j:
            print(i+j)