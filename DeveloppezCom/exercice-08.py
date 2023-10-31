# tuto dvp.com - exercice 8

# fonction qui fait le calcul
def hauteurParcourue(nombre, hauteur):
    distance = 7 * 5 * 2 * nombre * hauteur
    print(f"Pour {nombre} marches de {hauteur} cm, il parcourt {distance/100} m par semaine.")



# programme principal
nombreMarches = int(input("Combien de marches ?"))
hauteurMarche = float(input("Hauteur d'une marche (cm) ?"))

hauteurParcourue(nombreMarches, hauteurMarche)