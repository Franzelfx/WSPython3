"""09 · Property Decorator

@property macht eine Methode wie ein Attribut nutzbar.

Übung: Temperature C/F mit @property.
"""

class Circle:
    def __init__(self, r):
        self.r = r

    @property
    def area(self):
        return 3.14 * self.r**2
