"""11 · Static Methods

@staticmethod: kein self/cls. Für Utility-Funktionen.

Übung: StringUtils mit reverse().
"""

class Math:
    @staticmethod
    def add(a, b):
        return a + b

Math.add(2, 3)
