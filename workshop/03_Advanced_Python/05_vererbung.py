"""05 · Vererbung

Die Kindklasse erbt alle Methoden der Elternklasse.

Übung: Vehicle -> Car, Bike.
"""

class Animal:
    def eat(self):
        print('eating')

class Dog(Animal):
    def bark(self):
        print('wuff')
