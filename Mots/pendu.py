# Le Pendu (Les animaux)

import random
import string

words = ["chat", "chien", "oiseaux", "rat", "pigeon", "lapin", "lion", "souris","hibou", "chouette", "aigle", "vautour", "tortue", "hamster", "cochon", "vache","grenouille", "poule", "coq", "pie", "corbeau", "mouton","cheval", "ane", "mulet", "moustique", "abeille", "tique", "fourmi"]
life = 6
coup = 0

# Loading the lowercase alphabet to a list
alphabet = list(string.ascii_lowercase)

# on tire un mot au hasard parmi ceux de la liste
wordtofind = words[random.randint(0, len(words))]
letter = ""

# création du mot vide
emptyword = list()
for i in range(len(wordtofind)):
    emptyword.append("_")
    
# en tête
print("Le Pendu !\n")
print("L'ordinateur pense à un mot.")
print("Allez-vous réussir à le trouver ?\n")
print("C'est parti !\n")

# boucle de jeu
while emptyword != wordtofind:
    
    life -= 1
    coup += 1
        
    # affichage du mot vide
    for i in range(len(emptyword)):
        print(f"{emptyword[i]}", end="")
    print()
    
    # coup du joueur
    print(f"\nIl vous reste {life} coup(s) à jouer.")   
    while True:
        letter = input("Votre proposition (lettre ou mot): ")
        if len(letter) == 1:
            if letter in alphabet:
                alphabet.remove(letter)
                break
            else:
                print("Vous avez déjà fait cette proposition.") 
        else:
            break
        
    # on met la proposition en miniscule pour éviter les soucis de case
    letter = letter.casefold()
    
    # on cherche la lettre du joueur dans le mot   
    if len(letter) != 1: # le coup du joueur est un mot
        if letter == wordtofind:
            print(f"Bravo ! Vous avez trouvé le mot en {coup} coup(s) !\n")
            break
    else: # le coup du joueur est une lettre
        find = 0       
        for i in range(len(wordtofind)):
            if wordtofind[i] == letter:
                emptyword[i] = letter
                find = find + 1
            
    # on dit au joueur si sa lettre est dans le mot              
    if find > 0:
        print("La lettre est dans le mot !\n")
    elif find == 0:                          
        print("La lettre n'a pas été trouvée dans le mot\n")

    # le joueur a gagné
    if "".join(emptyword) == wordtofind:
       print(f"Bravo ! Vous avez trouvé le mot en {coup} coup(s) !\n")
       break
    
    # le joueur a perdu
    if life == 0:
       print("Vous avez perdu !")
       print(f"Le mot à trouvé était {wordtofind}\n")
       break
    
print("Fin de la partie.")