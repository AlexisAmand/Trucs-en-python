# générateur de mot de passe aléatoire
# source : Coding Magazine n°23

# manipulation des chaines
import string

# manipulation des nombres aléatoires
import random

# manipulation des interfaces graphiques
from tkinter import *

# Fenêtre d'initialisation du projet
Screen = Tk()
Screen.geometry("500x300")
Screen.title("Générateur de mots de passe aléatoire")

# Titre du programme
Title = StringVar()
TitleLabel = Label(Screen, textvariable=Title).pack()
Title.set =("Générateur de mots de passe aléatoire")

# création des boutons radios
def SelectionOptions():
    SelectionOptions = Choice.get()
    

Choice = IntVar()

Radiobutton1 = Radiobutton(Screen, text="faible", variable=Choice, value=1, command=SelectionOptions).pack(anchor=CENTER)
Radiobutton2 = Radiobutton(Screen, text="moyen", variable=Choice, value=2, command=SelectionOptions).pack(anchor=CENTER)
Radiobutton3 = Radiobutton(Screen, text="fort", variable=Choice, value=3, command=SelectionOptions).pack(anchor=CENTER)

LabelChoice = Label(Screen)
LabelChoice.pack 

LengthLabel = StringVar()
LengthLabel.set("Longeur du mot de passe")
LengthTitle = Label(Screen, textvariable=LengthLabel).pack()

# Longueur du mot de passe

Value = IntVar()
SpinLength = Spinbox(Screen, from_=9, to_=25, textvariable=Value, width=14).pack()

# Logique du programme

Poor = string.ascii_uppercase+string.ascii_lowercase
Average = string.ascii_uppercase+string.ascii_lowercase+string.digits

Symbols="~'!@#$%^()_-+={[]}|_:;"

Advance = Poor+Average+Symbols

def PassGen():
    if Choice.get() == 1:
        return "".join(random.sample(Poor,Value.get()))
    if Choice.get() == 2:
        return "".join(random.sample(Average,Value.get()))
    if Choice.get() == 3:
        return "".join(random.sample(Advance,Value.get()))
    
# Bouton de génération du mot de passe

Lsum = Label(Screen, text="")
Lsum.pack(side=BOTTOM)

def CallBack():
    Lsum.config(text=PassGen())
    

Password=str(CallBack())
PassGenButton = Button(Screen, text="Générer mot de passe", bd=5, height=2, command=CallBack, pady=3)
PassGenButton.pack()

# La boucle d'événement dans tkinter

Screen.mainloop()