# Le chiffre de César

import string

# Cryptage d'une chaîne de caractère s avec key pour décalage

def caesar_cypher_encrypt(s, key):

    key = key % 26
    alphabet_strange_min = string.ascii_lowercase[key:] + string.ascii_lowercase[:key]
    alphabet_strange_maj = string.ascii_uppercase[key:] + string.ascii_uppercase[:key]
    coded = ""
    
    for c in s:
        if c == " ":
            coded = coded + " "
        elif c in string.punctuation or c in string.digits:
            coded = coded + c
        elif c in string.ascii_lowercase:
            index = string.ascii_lowercase.find(c)
            coded = coded + alphabet_strange_min[index]
        elif c in string.ascii_uppercase:
            index = string.ascii_uppercase.find(c)
            coded = coded + alphabet_strange_maj[index]

    return coded



# Décryptage d'une chaîne de caractère s avec key pour décalage

def caesar_cypher_decrypt(s, key):

    key = key % 26
    alphabet_strange_min = string.ascii_lowercase[key:] + string.ascii_lowercase[:key]
    alphabet_strange_maj = string.ascii_uppercase[key:] + string.ascii_uppercase[:key]
    coded = ""
    
    for c in s:
        if c == " ":
            coded = coded + " "
        elif c in string.punctuation or c in string.digits:
            coded = coded + c
        elif c in alphabet_strange_min:
            index = alphabet_strange_min.find(c)
            coded = coded + string.ascii_lowercase[index]
        elif c in alphabet_strange_maj:
            index = alphabet_strange_maj.find(c)
            coded = coded + string.ascii_uppercase[index]

    return coded     



# pour les tests

print(caesar_cypher_encrypt("Python is super disco !", 31))
print(caesar_cypher_decrypt("Udymts nx xzujw inxht !", 31))