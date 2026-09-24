"""04 · File I/O

with schließt die Datei automatisch. Modes: r, w, a.

Übung: Speichere eine Notiz in einer Datei.
"""

# Speichere eine EIngabe in einer Datei
user_input = input("Gib eine Notiz ein: ")

# Schreibe die Eingabe in die Datei 'data.txt'
with open('data.txt', 'w') as f:
    f.write(user_input)

# Lese die Datei und gib den Inhalt aus
with open('data.txt', 'r') as f:
    print(f.read())