# Le chiffre de César (décrypter)
# Il s'agit juste d'une version interactive et optimisée de celle que j'ai proposé sur Hackinscience

import string

# Décryptage d'une chaîne de caractère s avec key pour décalage

def caesar_cypher_decrypt(s, key):

    key = key % 26
    alphabet_strange_min = string.ascii_lowercase[key:] + string.ascii_lowercase[:key]
    alphabet_strange_maj = string.ascii_uppercase[key:] + string.ascii_uppercase[:key]
    decoded = ""

    for c in s:
        if c in alphabet_strange_min:
            index = alphabet_strange_min.find(c)
            decoded = decoded + string.ascii_lowercase[index]
        elif c in alphabet_strange_maj:
            index = alphabet_strange_maj.find(c)
            decoded = decoded + string.ascii_uppercase[index]
        else:
            decoded = decoded + c
    
    return decoded   

string_decoded = input("Le texte à décoder: ")
code = int(input("Le décalage (3 pour César): "))

print(f"\nLe texte est: {caesar_cypher_decrypt(string_decoded, code)}")