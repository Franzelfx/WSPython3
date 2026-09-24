"""08 · Magic Methods

Dunder methods: __str__, __eq__, __len__, __add__...

Übung: Vector-Klasse mit __add__.
"""

class Book:
    def __init__(self, t):
        self.t = t

    def __str__(self):
        return f'Book: {self.t}'

print(Book('Py'))
