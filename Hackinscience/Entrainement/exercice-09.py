# Afficher le contenu d'un fichier

# pour tester, il faut créer un fichier words.txt qui contient des mots

f = open("words.txt", "r")
print(f.read())