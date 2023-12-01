# A quel jour de la semaine correspond une date ?

# Ce programme utilise l'algorithme de Mike Keith
# Il y a date.weekday() qui fait très bien le boulot

# On demande une date...
date = input("Entrez une date (JJ/MM/AAAA): ")

# ...et on en récupére les éléments
date_listed = date.split("/")
jour = int(date_listed[0])
mois = int(date_listed[1])
annee = int(date_listed[2])

# simplement une liste qui contient les jours de la semaine
semaine = ["dimanche", "lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi"]

# c = 1 pour janvier et février, c = 0 pour les autres mois.
c = (14 - mois) // 12
a = annee - c
m = mois + 12 * c - 2
j = (jour + a + a // 4 - a // 100 + a // 400 + (31 * m) // 12 ) 
j = j % 7

# La réponse obtenue pour j correspond alors à un jour de la semaine suivant :
# 0 = dimanche, 1 = lundi, 2 = mardi, etc.
# donc, à un élément de la liste

print(f"Le {jour}/{mois}/{annee} est un {semaine[j]}.\n")

