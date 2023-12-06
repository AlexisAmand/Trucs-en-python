# Mélange à queue d'aronde

def perfect_shuffle(deck):
    new_deck = []
    
    for i in range(len(deck) // 2):
        
        new_deck.append(deck[i])
        new_deck.append(deck[len(deck) // 2 + i])
            
    return new_deck
    


# pour les tests

test_deck = [1, 2, 3, 4, 5, 6]
print(perfect_shuffle(test_deck))