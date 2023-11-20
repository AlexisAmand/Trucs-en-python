# Calendrier perpétuel

# Conversion d'un script initialement écrit en Basic Atmos
# paru dans "102 programmes pour l'Oric Atmos" en 1984

import calendar

# L'année est bissextile ?

def est_bissextile(annee):
    return (annee % 4 == 0 and annee % 100 != 0) or (annee % 400 == 0)

# Fonction qui fait les calculs et affiche le calendrier

def calendrier_perpetuel(annee, mois):
    jours_du_mois_31 = [1, 3, 5, 7, 8, 10, 12]
    jours_du_mois_30 = [4, 6, 9, 11]

    if mois == 2 and est_bissextile(annee):
        jours_du_mois = 29
    else:
        jours_du_mois = 31 if mois in jours_du_mois_31 else (30 if mois in jours_du_mois_30 else 28)

    premier_jour, _ = calendar.monthrange(annee, mois)

    print("\nLUN MAR MER JEU VEN SAM DIM\n")

    for jour in range(1, jours_du_mois + 1):
        if jour == 1:
            # Aligner le premier jour du mois avec le bon jour de la semaine
            print("    " * premier_jour, end="")

        print(f"{jour:3}", end=" ")
        premier_jour = (premier_jour + 1) % 7

        if premier_jour == 0:
            print()

# Programme principal

print("Calendrier perpétuel\n\n")
print("Conversion d'un script initialement écrit en Basic Atmos")
print("et paru dans \"102 programmes pour l'Oric Atmos\" en 1984")
print("Indiquez 0 comme réponse pour quitter le programme.\n\n")

while True:
    try:
        annee = int(input("Indiquez une année (après 1582): "))
    except ValueError as e:
        print("Vous devez choisir une année après 1582. - %s" % e)
    else:
        if annee >= 1582:          
            while True:
                try:
                    mois = int(input("Indiquez un mois (entre 1 et 12): "))
                except ValueError as e:
                    print("Vous devez choisir un mois entre 1 et 12. - %s" % e)
                else:
                    if 1 <= mois <= 12:                 
                        print(calendrier_perpetuel(int(annee), int(mois)), "\n\n")
                        break                         
                    elif mois == 0:
                        break    
                    else:
                        print("Le mois doit être un nombre entre 1 et 12\n")
        elif annee == 0:
            break      
        else:
            print("L'année doit être postérieure à 1582\n")

print("\n\n")