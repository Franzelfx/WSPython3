"""04 · Attribute

Klassen- vs. Instanzattribute. Erstere sind geteilt.

Übung: Klasse mit Zählerattribut.
"""

class Dog:
    species = 'Canis'  # class attr

    def __init__(self, name):
        self.name = name  # instance attr
