"""
Plottet die EV-Produktionszahlen aus ev_produktion.xlsx (Blatt "Übersicht").

Benötigt: pip install openpyxl matplotlib
Aufruf:   python plot_produktion.py
"""

from pathlib import Path

import matplotlib.pyplot as plt
from openpyxl import load_workbook

BASIS = Path(__file__).parent
EINGABE = BASIS / "ev_produktion.xlsx"
AUSGABE = BASIS / "ev_produktion.png"


def lade_uebersicht(pfad: Path) -> tuple[list[str], dict[str, list[int]]]:
    """Liest Jahre und Stückzahlen pro Region (ohne Gesamtzeile/-spalte)."""
    blatt = load_workbook(pfad, data_only=True)["Übersicht"]
    zeilen = list(blatt.values)
    jahre = [str(j) for j in zeilen[0][1:-1]]
    daten = {z[0]: list(z[1:-1]) for z in zeilen[1:] if z[0] != "Gesamt"}
    return jahre, daten


def main() -> None:
    jahre, daten = lade_uebersicht(EINGABE)
    # Größte Region unten, damit der Stapel gut lesbar ist
    regionen = sorted(daten, key=lambda r: sum(daten[r]), reverse=True)

    fig, ax = plt.subplots(figsize=(9, 5.5))
    unten = [0] * len(jahre)
    for region in regionen:
        werte = [w / 1e6 for w in daten[region]]
        ax.bar(jahre, werte, bottom=unten, label=region)
        unten = [u + w for u, w in zip(unten, werte)]

    for x, summe in enumerate(unten):
        ax.text(x, summe + 0.3, f"{summe:.1f} Mio.", ha="center", fontweight="bold")

    ax.set_title("EV-Komponenten: Produktion nach Region und Jahr")
    ax.set_xlabel("Jahr")
    ax.set_ylabel("Produzierte Stückzahl (Mio.)")
    ax.set_ylim(0, max(unten) * 1.1)
    ax.legend(title="Region", loc="upper left")
    ax.spines[["top", "right"]].set_visible(False)

    fig.tight_layout()
    fig.savefig(AUSGABE, dpi=150)
    print(f"Plot gespeichert unter: {AUSGABE}")
    plt.show()


if __name__ == "__main__":
    main()
