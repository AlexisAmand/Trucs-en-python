# Calendrier du mois en cours

import calendar

yy = int(input("Indiquez une année : "))
mm = int(input("Indiquez un mois (entre 1 et 12): "))

# affiche le calendrier

print(calendar.month(yy,mm))
