# --- Pypang : adaptation en python de San Pablo ---

import random

class VillageGame:
    def __init__(self):
        self.year = 1
        self.population = 100  # Population initiale du village
        self.rice_stock = 500  # Stock initial de riz en kg
        self.wood_stock = 100  # Stock initial de bois
        self.money = 200  # Argent initial
        self.rice_per_person = 2  # Quantité de riz nécessaire par personne par an
        self.rice_yield_per_person = 10  # Quantité de riz produite par travailleur
        self.wood_yield_per_person = 5  # Quantité de bois produite par travailleur
        self.planting_rate = 0.2  # Pourcentage du riz réservé pour la prochaine récolte
        self.max_years = 10  # Le jeu dure 10 ans
        self.events = [
            {"name": "Invasion de sauterelles", "effect": self.locust_attack},
            {"name": "Attaque de brigands", "effect": self.bandit_attack}
        ]
        self.market_prices = {
            "buy_rice": 5,   # Prix d'achat du riz (par kg)
            "sell_rice": 3,  # Prix de vente du riz (par kg)
            "buy_wood": 2,   # Prix d'achat du bois (par unité)
            "sell_wood": 1    # Prix de vente du bois (par unité)
        }
        self.warehouse_capacity = 500  # Capacité de l'entrepôt en kg de riz
        self.wood_capacity = 200  # Capacité de l'entrepôt en unités de bois
        self.house_capacity = 10  # Capacité d'une maison pour la population
        self.houses_built = 5  # Nombre de maisons construites
        self.warehouses_built = 1  # Nombre d'entrepots construits

    def plant_rice(self, workers):
        rice_yield = workers * self.rice_yield_per_person
        yield_modifier = random.uniform(0.8, 1.2)
        actual_yield = rice_yield * yield_modifier
        return actual_yield

    def harvest_wood(self, workers):
        wood_yield = workers * self.wood_yield_per_person
        return wood_yield

    def trade(self):
        print("\n--- Commerce avec d'autres villages ---")
        print(f"Argent disponible : {self.money} pièces")
        print(f"Prix d'achat du riz : {self.market_prices['buy_rice']} pièces/kg")
        print(f"Prix de vente du riz : {self.market_prices['sell_rice']} pièces/kg")
        print(f"Prix d'achat du bois : {self.market_prices['buy_wood']} pièces/unité")
        print(f"Prix de vente du bois : {self.market_prices['sell_wood']} pièces/unité")
        
        choice = input("veux-tu (A) acheter, (V) vendre ou (N) ne rien faire ? ").lower()
        if choice == 'a':
            resource = input("veux-tu acheter du (R) riz ou du (B) bois ? ").lower()
            if resource == 'r':
                amount = int(input(f"Combien de kg de riz veux-tu acheter ? (max {self.money // self.market_prices['buy_rice']} kg) "))
                cost = amount * self.market_prices['buy_rice']
                if self.money >= cost:
                    self.money -= cost
                    self.rice_stock += amount
                    print(f"Acheté {amount} kg de riz pour {cost} pièces.")
                else:
                    print("Pas assez d'argent.")
            elif resource == 'b':
                amount = int(input(f"Combien d'unités de bois veux-tu acheter ? (max {self.money // self.market_prices['buy_wood']} unités) "))
                cost = amount * self.market_prices['buy_wood']
                if self.money >= cost:
                    self.money -= cost
                    self.wood_stock += amount
                    print(f"Acheté {amount} unités de bois pour {cost} pièces.")
                else:
                    print("Pas assez d'argent.")
        elif choice == 'v':
            resource = input("veux-tu vendre du (R) riz ou du (B) bois ? ").lower()
            if resource == 'r':
                amount = int(input(f"Combien de kg de riz veux-tu vendre ? (max {self.rice_stock} kg) "))
                if amount <= self.rice_stock:
                    self.rice_stock -= amount
                    profit = amount * self.market_prices['sell_rice']
                    self.money += profit
                    print(f"Vendu {amount} kg de riz pour {profit} pièces.")
                else:
                    print("Pas assez de riz en stock.")
            elif resource == 'b':
                amount = int(input(f"Combien d'unités de bois veux-tu vendre ? (max {self.wood_stock} unités) "))
                if amount <= self.wood_stock:
                    self.wood_stock -= amount
                    profit = amount * self.market_prices['sell_wood']
                    self.money += profit
                    print(f"Vendu {amount} unités de bois pour {profit} pièces.")
                else:
                    print("Pas assez de bois en stock.")
    
    # La fonction qui permet de construire
    def build_bat(self):
        
        # On construit des maisons ?
        if self.money >= 20:  # Coût pour améliorer un bâtiment ou construire une maison
            build_choice = input("Veux-tu construire une maison pour un coût de 10 unités de bois (O/N) ? ").lower()
            if build_choice == 'o':
                if self.wood_stock >= 10:  # Coût en bois pour construire une maison
                    self.wood_stock -= 10  # Coût en bois pour construire une maison
                    self.houses_built += 1
                    print("Une maison a été construite !")
                else:
                    print("Pas assez de bois pour construire une maison.")

        # On construit des entrepôts ?
        if self.money >= 20:  # Coût pour améliorer un bâtiment ou construire une maison
            build_choice = input("Veux-tu construire un entrepot pour un coût de 10 unités de bois (O/N) ? ").lower()
            if build_choice == 'o':
                if self.wood_stock >= 10:  # Coût en bois pour construire un entrepot
                    self.wood_stock -= 10  # Coût en bois pour construire un entrepot
                    self.warehouses_built += 1
                    print("Un entrepot a été construit !")
                    self.warehouse_capacity =  self.warehouse_capacity + 100
                else:
                    print("Pas assez de bois pour construire un entrepot.")
        
    def simulate_year(self, rice_workers, wood_workers):
        # Calculer la récolte de riz et de bois
        rice_produced = self.plant_rice(rice_workers)
        wood_produced = self.harvest_wood(wood_workers)

        # Ajouter au stock, en respectant les capacités
        self.rice_stock += rice_produced
        self.wood_stock += wood_produced

        # Limiter le stock de riz et de bois
        if self.rice_stock > self.warehouse_capacity:
            self.rice_stock = self.warehouse_capacity
            print("Le stock de riz a atteint la capacité maximale de l'entrepôt.")
        if self.wood_stock > self.wood_capacity:
            self.wood_stock = self.wood_capacity
            print("Le stock de bois a atteint la capacité maximale de l'entrepôt.")

        # Déclencher un événement aléatoire avec 30% de chance **avant de nourrir la population**
        if random.random() < 0.3:
            event = random.choice(self.events)
            print(f"\nÉvénement : {event['name']} !")
            event['effect']()

        # Nourrir la population
        rice_needed_for_population = self.population * self.rice_per_person
        if self.rice_stock < rice_needed_for_population:
            deficit = rice_needed_for_population - self.rice_stock
            deaths = int(deficit / self.rice_per_person)
            self.population -= deaths
            self.rice_stock = 0
            if self.population < 0:
                self.population = 0
            print(f"Famine ! {deaths} personnes sont mortes. Population actuelle : {self.population}")
        else:
            self.rice_stock -= rice_needed_for_population
            surplus = self.rice_stock
            births = int(surplus / (self.rice_per_person * 2))
            self.population += births
            print(f"La récolte a été bonne. {births} naissances. Population actuelle : {self.population}")

        # Vérifier la capacité de population
        max_population = self.houses_built * self.house_capacity
        if self.population > max_population:
            self.population = max_population
            print("La population a atteint la capacité maximale des maisons.")

        print(f"Stock de riz : {self.rice_stock} kg (max : {self.warehouse_capacity} | Stock de bois : {self.wood_stock} unités | Argent : {self.money} pièces")

    def locust_attack(self):
        lost_rice = int(self.rice_stock * 0.3)
        self.rice_stock -= lost_rice
        print(f"Une invasion de sauterelles a détruit {lost_rice} kg de riz.")

    def bandit_attack(self):
        stolen_rice = int(self.rice_stock * 0.2)
        self.rice_stock -= stolen_rice
        print(f"Des brigands ont pillé {stolen_rice} kg de riz.")

    def play(self):

        print("Bienvenue dans Pypang !")
        print("Tu viens d'être élu chef du village pour 10 ans.")
        print("Tous les habitants vont-ils survivre ?")

        while self.year <= self.max_years and self.population > 0:
            print(f"\n--- Année {self.year} ---")
            print(f"Population actuelle : {self.population}")
            print(f"Stock de riz : {self.rice_stock} kg (max : {self.warehouse_capacity}) | Stock de bois : {self.wood_stock} unités | Argent : {self.money} pièces")

            while True:
                rice_workers = int(input(f"Combien de villageois affectés à l'agriculture (sur {self.population}) ? "))
                wood_workers = int(input(f"Combien de villageois affectés à la coupe de bois (sur {self.population - rice_workers}) ? "))
                
                if rice_workers + wood_workers > self.population:
                    print("Doucement petit dragon !")
                    print("Le nombre total de travailleurs dépasse la population.")
                else:
                    break

            self.simulate_year(rice_workers, wood_workers)

            # Commerce avec d'autres villages
            self.trade()

            # Construction
            self.build_bat()

            self.year += 1

        if self.population > 0:
            print(f"Félicitations jeune dragon !")
            print(f"Tu as terminé les 10 ans avec une population de {self.population}.")
        else:
            print("Tous les habitants sont morts... Tu asz perdu.")

game = VillageGame()
game.play()

