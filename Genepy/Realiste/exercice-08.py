# La carte manquante

def missing_card(cards):

    # liste avec les cartes proposées
    cards = cards.split(" ")
    
    # liste compléte des cartes
    couleur = ["S", "H", "D", "C"]
    valeur = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    cartes = []
    
    '''
    # la ligne qui suit correspond à ceci :
    for c in couleur:
        for v in valeur:
            cartes.append(c+v)
    '''
    
    [cartes.append(c+v) for c in couleur for v in valeur]

    # on cherche la carte manquante   

    '''
    # les 2 lignes qui suivent correspondent à ceci :
    for i in cartes:
        if i not in cards:
            return i
    '''
    
    resultat = next(i for i in cartes if i not in cards)
    return resultat

# pour les tests

print(missing_card("S2 S3 S4 S5 S6 S7 S8 S9 S10 SJ SQ SK SA "
        "H2 H3 H4 H5 H6 H7 H8 H9 H10 HJ HQ HK HA "
        "D2 D3 D4 D5 D6 D7 D8 D9 D10 DJ DQ DK DA "
        "C2 C3 C4 C5 C6 C7 C8 C9 C10 CJ CQ CK"))