# Le chiffre de Polybe (décrypter)
# j'ai utilisé la variante avec des chiffres pour éviter la confusion I/J

# cette fonction fait le décryptage

def Unpolybe(phrase):
    grille = [
            ["A", "B", "C", "D", "E", "F"], 
            ["G", "H", "I", "J", "K", "L"],
            ["M", "N", "O", "P", "Q", "R"],
            ["S", "T", "U", "V", "W", "X"],
            ["Y", "Z", "0", "1", "2", "3"],
            ["4", "5", "6", "7", "8", "9"]
            ]
    
    i = 0
    unpolybe = ""
    while i != len(phrase):
        if phrase[i].isdigit():
            if phrase[i + 1].isdigit():
                unpolybe = unpolybe + grille[int(phrase[i]) - 1][int(phrase[i + 1]) - 1]
                i = i + 2
        else:
            unpolybe = unpolybe + phrase[i]
            i = i + 1 
    return unpolybe



# programme principal

phrase = input("Texte a décrypter: ")
print(f"Texte décrypté: {phrase}")