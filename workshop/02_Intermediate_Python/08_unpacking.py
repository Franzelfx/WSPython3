"""08 · Unpacking

Sequenzen auf Variablen verteilen. * für den Rest.

Übung: Tausche zwei Variablen ohne Hilfsvariable.
"""

a, b, c = [1, 2, 3]
first, *rest = [1, 2, 3, 4]
print(rest)  # [2, 3, 4]
