# tuto dvp.com - exercice 10

# Distance entre la gare du Nord et Arras
distance = 170

# Fonction qui calcule l'heure du drame
def drame(vitesse):
    # on récupére le nombre d'heures
    heures = int(distance/vitesse)
    # calcul du temps total mis, et division par 60 pour récupérer le reste qui correspond aux minutes
    minutes = int((60 * distance / vitesse) % 60)
    print(f"Si le train roule à {vitesse} le déchiquetage aura lieu à {9 + heures:>2} h {minutes:>2} min.")
    


# programme principal
for i in range (100, 301, 10):
    drame(i)

