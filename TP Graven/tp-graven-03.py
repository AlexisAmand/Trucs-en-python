# Tuto 03 de Graven : Place de cinéma

# Récolter l'âge de la personne
AgeClient = int(input("Quel est votre âge ? "))

# Si la personne est mineure : 7 euros
# Si la personne est majeure : 12 euros

if AgeClient < 18:
    PrixPlace = 7
else:
    PrixPlace = 12

# Souhaitez-vous du pop-corn ?
PopCorn = input("Voulez-vous du pop-corn (o/n) ?")

# Si oui : 5 euros
if PopCorn == "o":
    PrixPlace += 5

# Afficher le prix total à payer
print(f"Vous devez payer {PrixPlace} euros.")