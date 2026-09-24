"""14 · Parameter & Return

Parameter = Input, return = Output.

Übung: Funktion für die Kreisfläche.
"""

def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # 8

# Übung: Funktion für die Kreisfläche
import math
def kreisflaeche(radius):
    return math.pi * radius ** 2

print(kreisflaeche(3))
