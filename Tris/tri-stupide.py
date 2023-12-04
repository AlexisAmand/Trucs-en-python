# Tri stupide
# (adapté de l'article dispo sur Wikipedia)

# il existe une fonction native sorted() qui construit une nouvelle liste triée
# mais c'est moins drôle !

from random import shuffle

# Une liste de 15 éléments pour tester

a_list = ["chat", "hibou", "coq", "hamster", "chien", "rat", "cheval", "pie", "moineau", "lapin", "abeille", "canard", "vache", "mouton", "poule"]
i = 0

# cette fonction vérifie si la liste est triée 

def est_triee(liste):
    return all(a_list[i] <= a_list[i + 1] for i in range(len(a_list) - 1))

# On affiche la liste d'origine

print("La liste de départ:")
print(a_list)

# On fait le tri stupide

while not est_triee(a_list):
    shuffle(a_list)
    # pour le fun, on affiche le nombre d'essais
    i+=1
    print(i)
            
# On affiche la liste triée

print("La liste triée avec un tri stupide:")
print(a_list)
