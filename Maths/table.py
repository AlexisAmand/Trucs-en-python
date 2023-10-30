# Afficher une table de multiplication

# Affichage de la table
def table(m):
    for t in range (1, 11):
        print(f"{t} x {m} = {t * m}")
        

# programme principal
while True:
        m = int(input("Quelle table voulez vous afficher (0 pour quitter)? ")) 
        try:
            if m == 0:
                print("Au revoir.")
            break
            table(m)
        except ValueError:
            print("\nVous devez indiquer un !\n")
        




