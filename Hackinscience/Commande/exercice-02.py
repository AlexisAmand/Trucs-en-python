# Afficher le premier paramètre

import sys

if len(sys.argv) < 2:
    print("usage: python3 exercice-22.py PARAM")    
else:
    print(sys.argv[1])