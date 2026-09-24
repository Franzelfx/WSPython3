"""15 · Best Practices

PEP 8, Docstrings, sprechende Namen, DRY, KISS.

Übung: Refactoriere alten Code nach PEP 8.
"""

# PEP 8 style
def calculate_total(items: list) -> float:
    """Sum item prices."""
    return sum(items)
