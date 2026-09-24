"""07 · Polymorphismus

Gleicher Methodenname, verschiedenes Verhalten.

Übung: Shape mit area() für Circle/Square.
"""

class Cat:
    def speak(self):
        return 'Miau'

class Dog:
    def speak(self):
        return 'Wuff'

for a in [Cat(), Dog()]:
    print(a.speak())
