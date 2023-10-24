# L'année est-elle bissextile ?

def julian(y):     
    if y%4 == 0:
        return True
    else:
        return False 
        

def gregorian(y):
    if (y %4 == 0 and y %100 != 0 or y %400 == 0):
       return True
    else:
        return False  
        

choix = 0

while choix != "3":
    print("------------------")
    print("Année bissextile ?")
    print("------------------")
    print("1. Calendrier julien")
    print("2. Calendrier grégorien")
    print("3. Fin")
    choix = input("choix :")  
    if choix == "1":
        y = int(input("Indiquez une année julienne (format AAAA): "))   
        if julian(y):
            print(f"L'année {y} est bissextile")
        else:
            print(f"L'année {y} n'est pas bissextile")  
    elif choix == "2":
        y = int(input("Indiquez une année grégorienne (format AAAA): "))   
        if gregorian(y):
            print(f"L'année {y} est bissextile")
        else:
            print(f"L'année {y} n'est pas bissextile")  
    elif choix == "3":
        print("Au revoir !")
    else:
        print("Choix incorrect !")

    

