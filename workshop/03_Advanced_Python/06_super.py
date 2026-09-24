"""06 · Super()

super() ruft die Methode der Elternklasse auf.

Übung: Erweitere __init__ in einer Subklasse.
"""

class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
