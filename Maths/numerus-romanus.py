# Les chiffres romains
# (c)1985 MICROTOM ET F.J. BAYARD
# Conversion d'un script initialement écrit en Basic

# Chiffres romains
romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

# Équivalents arabes
arabes = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

def convertir_romain(arabe):
    res_romain = ""
    c = 0
    while arabe > 0:
        if arabe >= arabes[c]:
            res_romain += romans[c]
            arabe -= arabes[c]
        else:
            c += 1
    return res_romain



# Programme principal

print("Numerus Romanus")
print("(c) 1985 MICROTHOM et F.J. Bayard")
print("conversion en python réalisée par A. Amand\n")


while True:
    try:
        nombre = int(input("Indiquez un nombre arabe (0 pour quitter): "))   
    except ValueError as e:
        print("Vous devez choisir un entier positif. - %s" % e)
    else:
        if nombre == 0:
            print("Au revoir !")
            break
        # Convertir le nombre en chiffres romains
        resultat_romain = convertir_romain(nombre)

        # Afficher le résultat
        print(f"Sa version romaine est : {resultat_romain}")