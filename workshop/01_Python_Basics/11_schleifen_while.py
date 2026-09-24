"""11 · Schleifen (while)

while läuft solange die Bedingung wahr ist. Achtung Endlosschleife!

Übung: Zahlenraten-Spiel.
"""

count = 0
while count < 5:
    print(count)
    count += 1
    
# Übung: Zahlenraten-Spiel
import random
number_to_guess = random.randint(1, 100)
attempts = 0
while True:
    guess = int(input("Rate eine Zahl zwischen 1 und 100: "))
    attempts += 1
    if guess == number_to_guess:
        print(f"Richtig! Du hast gewonnen in {attempts} Versuchen.")
        break
    elif guess < number_to_guess:
        print("Zu niedrig!")
    else:
        print("Zu hoch!")
print("Spiel beendet.")