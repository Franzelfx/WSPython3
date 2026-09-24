"""10 · Klassenmethoden

@classmethod: cls statt self. Für Factories.

Übung: from_string Factory-Methode.
"""

class Dog:
    count = 0

    @classmethod
    def total(cls):
        return cls.count
