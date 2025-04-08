# Calculette

import sys

if len(sys.argv) <= 3:
    print("usage: ./solution.py a_number (an_operator +-*/%^) a_number")    
else:
    if sys.argv[2] == "+":
        print(int(sys.argv[1]) + int(sys.argv[3]))
    elif sys.argv[2] == "-":
        print(int(sys.argv[1]) - int(sys.argv[3]))
    elif sys.argv[2] == "/":
        if int(sys.argv[3]) == 0:
            print("input error") 
        else:
            print(int(sys.argv[1]) / int(sys.argv[3]))
    elif sys.argv[2] == "^":
        print(int(sys.argv[1]) ** int(sys.argv[3]))
    elif sys.argv[2] == "%":
        print(int(sys.argv[1]) % int(sys.argv[3]))
    elif sys.argv[2] == "*":
        print(int(sys.argv[1]) * int(sys.argv[3]))
    else:
        print("input error")