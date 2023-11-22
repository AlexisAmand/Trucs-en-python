# Afficher la date et l'heure

import datetime

aujourdhui = datetime.datetime.now()

jour = aujourdhui.strftime("%d")
mois = aujourdhui.strftime("%m")
annee =aujourdhui.strftime("%Y")

heure = aujourdhui.strftime("%H")
minute = aujourdhui.strftime("%M")
seconde =aujourdhui.strftime("%S")

print(f"Today is {annee}-{mois}-{jour} and it is {heure}-{minute}-{seconde}")
