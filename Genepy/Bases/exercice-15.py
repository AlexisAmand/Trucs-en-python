# Somme des nombres pairs <= 100

somme = 0

for i in range(0,101):
    if i % 2 == 0:
        somme += i
    
print(somme)