# Le chiffre de César (crypter)
# Il s'agit juste d'une version interactive de celle que j'ai proposé sur Hackinscience

import string

# Décryptage d'une chaîne de caractère s avec key pour décalage

def caesar_cypher_decrypt(s, key):

    key = key % 26
    alphabet_strange_min = string.ascii_lowercase[key:] + string.ascii_lowercase[:key]
    alphabet_strange_maj = string.ascii_uppercase[key:] + string.ascii_uppercase[:key]
    coded = ""
    
    for c in s:
        if c in string.ascii_lowercase:
            index = string.ascii_lowercase.find(c)
            coded = coded + alphabet_strange_min[index]
        elif c in string.ascii_uppercase:
            index = string.ascii_uppercase.find(c)
            coded = coded + alphabet_strange_maj[index]
        else:
            coded = coded + c
            
    return coded

no_coded = input("Le texte à décoder: ")
code = int(input("Le décalage (3 pour César): "))

print(f"\nLa chaine décodée est: {caesar_cypher_decrypt(no_coded, code)}")