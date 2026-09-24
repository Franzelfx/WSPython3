"""02 · __init__ & self

__init__ ist der Konstruktor. self = die Instanz selbst.

Übung: Person mit name und age.
"""

class Dog:
    def __init__(self, name):
        self.name = name

rex = Dog('Rex')
print(rex.name)
