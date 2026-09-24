"""03 · Methoden

Funktionen innerhalb einer Klasse. Erstes Arg immer self.

Übung: Car mit start() und stop().
"""

class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(f'{self.name}: Wuff!')
