# tuto dvp.com - exercice 4

n = int(input("Entrez un nombre: "))

while n < 1:
    print("Il doit être positif et non nul !")
    n = int(input("Entrez un nombre: "))

if n%2 == 0:
    print("PAIR")
else:
    print("IMPAIR")