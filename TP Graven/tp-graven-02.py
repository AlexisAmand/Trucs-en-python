# Tuto 02 de Graven

# récolter une valeur porte monnaie
porte_monnaie = int(input("Quelle est la valeur du porte monnaie ?"))
print(f"Vous avez {str(porte_monnaie)} euros.")

# créer un produit qui aura pour valeur 50
prix_produit = 50
print(f"Le produit coûte {str(prix_produit)} euros.")

# afficher la nouvelle valeur du porte monnaie, après son achat
porte_monnaie -= prix_produit
print(f"Vous avez maintenant {str(porte_monnaie)} euros.")