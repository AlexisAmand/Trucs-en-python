# Vendredi 13

# ce code fonctionne mais il peut surement être optimisé !

import datetime

def friday_the_13th():
    # date actuelle
    aujourdhui = datetime.datetime.now()    

    jour = int(aujourdhui.strftime('%d'))
    mois = int(aujourdhui.strftime('%m'))
    annee = int(aujourdhui.strftime('%Y'))
    
    # on teste si aujourd'hui nous sommes un vendredi 13

    if jour == 13 and aujourdhui.weekday() == 4:
        vendredi13 = str(annee) + "-" + str(mois).rjust(2, "0") + "-13"     
        
    # si on est avant le 13, on regarde si le 13 du mois courant est un vendredi

    elif jour < 13 and datetime.date(annee, mois, 13).weekday() == 4:
        vendredi13 = str(annee) + "-" + str(mois).rjust(2, "0") + "-13"
    elif jour > 13 and datetime.date(annee, mois, 13).weekday() == 4:
        if mois < 12:
            mois += 1
        elif mois == 12:
            mois = 1
            annee += 1
    
    # sinon, on boucle sur les 13 des mois successifs
    # pour voir si ça tombe un vendredi 
        
    while datetime.date(annee, mois, 13).weekday() != 4:
        if mois < 12:
            mois += 1
        elif mois == 12:
            mois = 1
            annee += 1
            
    # le prochain vendredi 13
    # avec un ajustement sur le mois pour l'avoir avec 2 chiffres      
     
    vendredi13 = str(annee) + "-" + str(mois).rjust(2, "0") + "-13"
        
    return vendredi13
    

# pour mes tests persos
print(friday_the_13th())
