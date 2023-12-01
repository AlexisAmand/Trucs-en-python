# La boîte à musique
# ce programme fait l'objet d'une discussion sur le net :
# https://tinyurl.com/596tmkyc

import random
import mido
from mido import MidiFile, MidiTrack, Message

# cette fonction joue une mélodie
def playnotes(notes, instrument_number):
    # Création d'un fichier MIDI
    mid = MidiFile()
    # Création d'une piste MIDI
    track = MidiTrack()
    mid.tracks.append(track)
    velocity = 64  # Vitesse (doit être un entier)
    for note in notes:
        # l'instrument
        track.append(Message('program_change', program=instrument_number))
        # la note
        track.append(Message('note_on', note=note, velocity=velocity, time=100))
        track.append(Message('note_off', note=note, velocity=velocity, time=100))
    # Sauvegarde du fichier MIDI
    mid.save('melodie.mid')
    print("Le fichier a bien été créé !")
    



# programme principal

print("La boite à musique\n")
print("Indiquez juste un nombre de notes, et l'ordinateur va générer une petite mélodie aléatoire dans un fichier MIDI.\n")

# un n° de note MIDI est un nombre entre 0 et 127
# chaque note sera donc un nombre aléatoire entre 0 et 127 mis dans une liste

notes_to_play = []

# programme principal
while True:         
        try:
            n = int(input("Combien de notes dans votre mélodie (0 pour quitter) ? "))
        except ValueError as e:
	        print("Vous devez choisir un entier positif. - %s" % e)
        else:
            if n == 0:
                print("Au revoir !")
                break
            
            for i in range(n):
                x = random.randint(0, 127)
                notes_to_play.append(x)

            # n° de l'instrument avec les codes MIDI
            instrument = 10
            playnotes(notes_to_play, instrument)
       