# Compter les « e » dans un fichier

f = open("words.txt", "r")
resultat = 0

for ligne in f:
  resultat += ligne.count("e")
  
print(resultat)
    
    