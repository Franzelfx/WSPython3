"""09 · Args & Kwargs

*args = beliebige Positionsargs, **kwargs = Keyword-Args.

Übung: Funktion, die beliebig viele Zahlen summiert.
"""

def fn(*args, **kwargs):
    print(args)
    print(kwargs)

fn(1, 2, name='Ben')
