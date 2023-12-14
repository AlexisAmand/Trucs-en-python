# Des emojis en forme de coeur

import unicodedata

for c in range(1, 230000):
    try:
        nom = unicodedata.name(chr(c))
        if "HEART" in nom:
            print(chr(c))
    except ValueError:
        continue