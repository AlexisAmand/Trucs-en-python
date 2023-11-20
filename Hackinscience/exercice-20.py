# Afficher des parfums de sorbets

FLAVORS = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]

boules = []

for i in FLAVORS:
    for j in FLAVORS:
        if i != j and (i,j) not in boules and (j,i) not in boules:
            boules.append((i,j))
           
for i, j in boules:
    print(i+", "+j)