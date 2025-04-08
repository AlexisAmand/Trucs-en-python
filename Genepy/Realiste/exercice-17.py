﻿# Indicateur de charge

def battery_charge(charge):
    nb = round(charge / 10)
    print("[" + nb * "|" + (10 - nb) * " " + "]")    
    print(f"{charge}%")

# pour les tests
        
battery_charge(0)
battery_charge(5)
battery_charge(9)
battery_charge(26)
battery_charge(72)
battery_charge(11)
battery_charge(100)