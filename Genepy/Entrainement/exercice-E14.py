# Nombre d'Adam

def check_adam_number(num):
    # Calcul du carré de num et de son inverse
    square_num = num ** 2
    reverse_square_num = int(str(square_num)[::-1])
    
    # Calcul de l'inverse de num, puis de son carré
    inverse_num = int(str(num)[::-1])  
    square_inverse_num = inverse_num ** 2
    
    # Comparaison des carrés inversés
    if square_inverse_num == reverse_square_num:
        return True
    else:
        return False


