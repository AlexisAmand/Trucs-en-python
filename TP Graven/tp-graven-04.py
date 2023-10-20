# Tuto 04 de Graven : générateur de phrases

from random import shuffle

# Demander en console une chaine de la forme mot1/mot2/mot3/mot4
chaine = input("Entrez une chaine de la forme mot1/mot2/mot3/mot4.... : ")

# Transformer cette chaine en une liste
chaineListed = chaine.split("/")
print("Chaine avant de la mélanger : ")
print(chaineListed)

# la mélanger
shuffle(chaineListed)
print("Chaine mélangée : ")
print(chaineListed)

# si le nombre d'éléments de cette liste est inférieur à 10
# -> afficher les deux premiers mots
# si le nombre d'éléments est supérieur ou égal à 10
# -> afficher les 3 derniers mots 

nombreElements = len(chaineListed)

if nombreElements < 10:
    print(chaineListed[0])
    print(chaineListed[1])
else:
    for key in range(nombreElements-3, nombreElements):
        print(chaineListed[key])
        
