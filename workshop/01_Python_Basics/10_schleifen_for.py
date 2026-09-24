"""10 · Schleifen (for)

for iteriert über Sequenzen. range() für Zahlen.

Übung: Summe der Zahlen 1 bis 100.
"""
for i in range(5):
    print(i)

for fruit in ['A', 'B', 'C']:
    print(fruit)
    
# Übung: Summe der Zahlen 1 bis 100
summe = 0
for zahl in range(1, 101):
    summe += zahl
print(summe)