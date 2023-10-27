# tuto dvp.com - exercice 2

tva = 19.6
prix_ht = 1

# un prix est toujours > 0

while prix_ht > 0:
    prix_ht = float(input("Indiquez le prix HT: "))
    prix_ttc = prix_ht * (1 + tva / 100)
    print(f"Le prix TTC est de : {prix_ttc:.2f}")
   