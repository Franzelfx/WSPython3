"""15 · Scope

Lokale vs. globale Variablen. LEGB-Regel.

Übung: Experimentiere mit dem global keyword.
"""

x = 10  # global

def foo():
    x = 5  # local
    print(x)

foo()
print(x)

# Übung: Verwende das global keyword, um die globale Variable zu ändern
def bar():
    global x
    x = 20
    print(x)

bar()
print(x)