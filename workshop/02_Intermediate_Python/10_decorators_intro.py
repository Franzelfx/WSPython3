"""10 · Decorators Intro

Wrappt Funktionen. @ Syntax für sauberen Code.

Übung: Timer-Decorator schreiben.
"""

def log(fn):
    def wrap(*a):
        print('call')
        return fn(*a)
    return wrap

@log
def hi():
    print('hi')
