# Afficher une table de multiplication

# Affichage de la table
def table(m):
    for t in range (1, 11):
        print(f"{t} x {m} = {t * m}")
        
print("Tables de multiplication\n")
print("Ce programme affiche la table de N.\n")

# programme principal
while True:
        m = input("\nQuelle table voulez vous afficher (0 pour quitter)? ")
        try:
            m = int(m)
            if m == 0:
                print("Au revoir.")
                break
            print(f"\nVoici la table de {5}:\n")
            table(m)
        except ValueError:
            print("N doit être un entier positif.")
        




