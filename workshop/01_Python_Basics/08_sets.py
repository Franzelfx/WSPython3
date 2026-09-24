"""08 · Sets

Sets: einzigartige Werte, keine Reihenfolge.

Übung: Entferne Duplikate aus einer Liste.
"""

a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)  # Schnitt
print(a | b)  # Vereinigung

# Übung: Entferne Duplikate aus einer Liste
my_list = [1, 2, 2, 3, 4, 4, 5]
unique_set = set(my_list)
print(unique_set)