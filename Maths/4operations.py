# Les 4 opérations

a = int()
b = int()
choix = 0

# fontion qui permet la saisie des 2 nombres

def saisie():
    global a, b
    a = int(input("Entrez un nombre :"))
    b = int(input("Entrez autre nombre :"))
    

   
# fonction qui fait une addition
def addition():
    saisie();
    print(f"la somme de {a} et {b} est : {a + b}")



# fonction qui fait un produit
def produit():
    saisie();
    print(f"le produit de {a} et {b} est : {a * b}")



# fonction qui fait un produit
def soustraction():
    saisie();
    print(f"la différence entre {a} et {b} est : {a - b}")
    


 # fonction qui fait un produit
def division():
    saisie();
    if b == 0:
        print("Oups ! On ne peut pas diviser par zéro !")
    else:
        print(f"la division de {a} par {b} est : {a / b}")
    

   
# programme principal

print("Opérations avec 2 nombres")

while choix != 5:
    print("\nMenu")
    print("----")
    print("1. Addition")
    print("2. Soustraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quitter")
    
    choix = int(input("Votre choix: "))
    while choix < 0 and choix > 6:
        choix = int(input("'Choix incorrect , réesayer: "))
        
    if choix == 1:
        addition()
    elif choix == 2:
        soustraction()
    elif choix == 3:
        produit()
    elif choix == 4:
       division()
       
print("Fin du programme.")