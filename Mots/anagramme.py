# Un mot est-il l'anagramme d'un autre ?

# cette fonction fait tout le boulot !
# on met un lower() pour éviter des pbs de majuscules.
def anagramme(a, b):
    if sorted(a.lower()) == sorted(b.lower()):
        print("Les mots sont des anagrammes.")
    else:
        print("Les mots ne sont pas des anagrammes.")



# Programme principal
print("Vérifions si deux mots sont des anagrammes !\n")

mot1 = input("Indiquez le premier mot: ")
mot2 = input("Indiquez le second mot: ")

anagramme(mot1, mot2)