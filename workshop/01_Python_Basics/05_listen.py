"""05 · Listen

Listen sind veränderbar. Zugriff via Index [0], [1]...

Übung: Erstelle eine Liste mit 5 Hobbys.
"""

fruits = ['Apfel', 'Birne']
fruits.append('Kirsche')
print(fruits[0])
print(len(fruits))

# Übung: Erstelle eine Liste mit 5 Hobbys
hobbies = ['Lesen', 'Schwimmen', 'Radfahren', 'Kochen', 'Reisen']
print(len(hobbies))

# Zugriff über Index
print(hobbies[0])
# Zugriff auf das letzte Element der Liste
print(hobbies[-1])
# Zugriff auf einen Teil der Liste (Slicing)
print(hobbies[1:4])
# Zugriff auf die ersten drei Elemente der Liste
print(hobbies[:3])
# Zugriff auf die Elemente ab dem dritten Element
print(hobbies[2:])
# Zugriff auf alle Elemente der Liste
print(hobbies[:])