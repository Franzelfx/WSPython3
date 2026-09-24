"""12 · List Comprehensions

Kompakte Syntax um Listen zu erzeugen.

Übung: Liste aller Wörter länger als 5 Zeichen.
"""

squares = [x**2 for x in range(10)]
evens = [x for x in range(20) if x % 2 == 0]

# Übung: Liste aller Wörter länger als 5 Zeichen
words = ["Python", "ist", "eine", "tolle", "Sprache"]
long_words = [word for word in words if len(word) > 5]
print(long_words)