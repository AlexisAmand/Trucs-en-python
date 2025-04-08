# Du romain au décimal

def from_roman_numeral(roman_numeral):
    chiffres_romains = ["I", "V", "X", "L", "C", "D", "M"]
    chiffres_arabes = [1, 5, 10, 50, 100, 500, 1000]
    resultat = 0

    for i in range(len(roman_numeral) - 1):
        current_value = chiffres_arabes[chiffres_romains.index(roman_numeral[i])]
        next_value = chiffres_arabes[chiffres_romains.index(roman_numeral[i + 1])]

        if current_value < next_value:
            resultat -= current_value
        else:
            resultat += current_value

    resultat += chiffres_arabes[chiffres_romains.index(roman_numeral[-1])]

    return resultat

