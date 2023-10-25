# Palindrome

print("Un mot est-il un palindrome ? \n")

# Prompt pour entrer le mot
mot = input("Indiquez le mot: ")

# On met le mot en minuscules pour éviter les pbs de casse dans la chaine mot.
mot = mot.casefold()

# [::-1] permet d'inverser la chaine
inverse = mot[::-1]

# on compare le mot et son "inverse"
if inverse == mot:
    print(f"Le mot {mot} est un palindrome.")
else:
    print(f"Le mot {mot} n'est pas un palindrome.")



