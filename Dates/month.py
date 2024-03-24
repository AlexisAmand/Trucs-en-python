# Calendrier du mois en cours

import calendar

year = int(input("Indiquez une année : "))
month = int(input("Indiquez un mois (entre 1 et 12): "))

# affiche le calendrier

print(calendar.month(year,month))
