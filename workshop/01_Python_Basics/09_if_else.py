"""09 · If-Else

Bedingungen steuern den Programmfluss.

Übung: Note in Text: 1='sehr gut', 2='gut'...
"""

age = 18
if age >= 18:
    print('Erwachsen')
elif age >= 13:
    print('Teen')
else:
    print('Kind')

# Übung: Note in Text umwandeln

note = int(input("Note: "))
if note == 1:
    print('sehr gut')
elif note == 2:
    print('gut')
elif note == 3:
    print('befriedigend')
elif note == 4:
    print('ausreichend')
elif note == 5:
    print('mangelhaft')
else:
    print('ungenügend')