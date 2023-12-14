# Le carré de Polybe (crypter)
# j'ai utilisé la variante avec des chiffres pour éviter la confusion I/J

# cette fonction fait le cryptage

def Polybe(phrase):
    grille = [
            ["A", "B", "C", "D", "E", "F"], 
            ["G", "H", "I", "J", "K", "L"],
            ["M", "N", "O", "P", "Q", "R"],
            ["S", "T", "U", "V", "W", "X"],
            ["Y", "Z", "0", "1", "2", "3"],
            ["4", "5", "6", "7", "8", "9"]
            ]
    
    polybe = ""
    for c in phrase:
        if c.isalnum():
            for ligne in range(len(grille)):
                for colonne in range(len(grille[ligne])):
                    if grille[ligne][colonne] == c :
                        polybe = polybe + str(ligne + 1) + str(colonne + 1)
        else:
            polybe = polybe + c
    return polybe



# programme principal

phrase = input("Texte à crypter: ").upper()
print(f"Texte crypté : {Polybe(phrase)}")               