"""02 · Print & Input

print() gibt aus, input() liest ein. f-strings für Formatierung.

Übung: Frage nach Namen und Alter, gib eine Begrüßung aus.
"""

# Übung: Frage nach Name und Alter, gib Begrüßung aus
# Frage nach dem Namen
print("Wie ist dein Name?")
name = input('Dein Name: ')

# Frage nach dem Alter
print("Wie alt bist du?")
alter = input('Dein Alter: ')

# Begrüßung ausgeben
print(f'Hallo {name}, du bist {alter} Jahre alt.')
