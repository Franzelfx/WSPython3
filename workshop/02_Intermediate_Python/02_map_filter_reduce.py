"""02 · Map/Filter/Reduce

Funktionale Werkzeuge: transformieren, filtern, akkumulieren.

Übung: Quadriere alle geraden Zahlen.
"""

nums = [1, 2, 3, 4]
doubled = list(map(lambda x: x*2, nums))
evens = list(filter(lambda x: x%2==0, nums))
