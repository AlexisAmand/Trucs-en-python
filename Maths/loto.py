# tirage du loto

# Depuis 2008, il faut désormais obtenir cinq numéros parmi 49
# plus un « numéro chance » parmi dix.

import random

numeros = list()

# cette fonction permet le tirage des 5 numéros
def tirage_numeros():
    for i in range(5):
        numeros.append(random.randint(1, 49))    


# cette fonction permet le tirage du numéro chance
def tirage_chance():
    return random.randint(1, 10)



# programme principal

print("Tirage du Loto")
print("--------------\n")

tirage_numeros()
    
print("liste des numéros: ", end="")
for value in numeros:
    print(f"{value} ", end="")
   
print()
print(f"Le numéro chance: {tirage_chance()}")
print("\nBonne chance !\n")

