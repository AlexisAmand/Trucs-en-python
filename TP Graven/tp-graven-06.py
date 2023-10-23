# Tuto 06 de Graven : compteur de voyelles

def get_vowels_numbers():
    global mot
    global vowels
    vowels_count = 0
    for x in mot:
        if x in vowels:
            vowels_count += 1
    return vowels_count
 

vowels = ["a", "e", "i", "o", "u", "y", "A", "E", "I", "O", "U", "Y"]
mot = input("Entrez un mot: ")
print(f"Il y a {get_vowels_numbers()} voyelle(s) dans le mot {mot}.")
