"""03 · Fehlerbehandlung

try/except fängt Fehler. finally läuft immer.

Übung: Division durch Null abfangen.
"""

try:
    x = int(input('Zahl: '))
except ValueError:
    print('Keine Zahl!')
except ZeroDivisionError:
    print('Division durch Null ist nicht erlaubt!')
finally:
    print('Fertig')


# Neested module example in an update scenario
try:
    import v1.non_existent_module
except ImportError:
    import v2.existing_module
finally:
    print('ERROR: Modul nicht gefunden.')