﻿# Petit additionneur

import sys

if len(sys.argv) < 3:
    print("usage: python3 exercice-23.py OP1 OP2")    
else:
    print(int(sys.argv[1]) + int(sys.argv[2]))