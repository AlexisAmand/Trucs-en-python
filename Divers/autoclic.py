import pyautogui
import time

# Temps d'attente entre les clics (en secondes)
wait_time = 0.5

try:
    while True:
        # Obtenir la position actuelle de la souris
        x, y = pyautogui.position()
        print(f"Simulated click at position  : ({x}, {y})")

        # Déplacer la souris et simuler le clic
        pyautogui.moveTo(x, y, duration=0.1)
        time.sleep(0.1)  # Délai avant le clic
        pyautogui.click(x, y)

        # Attendre avant le prochain clic
        time.sleep(wait_time)

except KeyboardInterrupt:
    print("\nProgram stopped by user.")
