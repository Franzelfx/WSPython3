"""13 · Enumerate & Zip

enumerate für Index+Wert. zip kombiniert Listen.

Übung: Namen und Alter parallel iterieren.
"""

for i, v in enumerate(['a', 'b', 'c']):
    print(i, v)

for a, b in zip([1, 2], ['x', 'y']):
    print(a, b)
