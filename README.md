# 🐍 WSPython3 – Python-Workshop-Reihe

Sammel-Repository für eine mehrteilige **Hands-on-Workshop-Reihe zu Python 3**.

Jeder Workshop ist ein eigenständiges Projekt mit vorgegebenem Grundgerüst
(Skeleton), das du Schritt für Schritt selbst ausfüllst. Die komplette Lösung
liegt jeweils in `LOESUNG.md` bzw. im Branch `loesung`.

---

## 📚 Die Workshops

| # | Workshop | Thema | Kernkonzepte |
|---|----------|-------|--------------|
| 1 | [🌤️ CLI Weather Dashboard](cli-weather-dashboard) | Wetterdaten von einer öffentlichen API im Terminal anzeigen | Projektstruktur, API-Client, `.env`-Konfiguration, `argparse`, `pytest` + Mocking |
| 2 | [✅ CLI Task Manager](cli-task-manager) | To-dos verwalten und dauerhaft speichern | SQLite, `@dataclass`, CRUD-Persistenzschicht, Subcommands, In-Memory-DB-Fixture |

Die Workshops bauen aufeinander auf – Workshop 2 setzt die Projektstruktur aus
Workshop 1 als bekannt voraus. Für sich genommen ist aber jeder Teil einzeln
lauffähig.

---

## 🎯 Was du lernst

Über die Reihe hinweg:

- Saubere Projektstruktur (`src/`, `config/`, `tests/`)
- Externe APIs anbinden und Netzwerkaufrufe kapseln
- Konfiguration & Secrets sauber über `.env` trennen
- Daten dauerhaft speichern mit **SQLite**
- Kommandozeilen-Interfaces mit `argparse` (inkl. Subcommands)
- Tests schreiben mit **pytest** – inkl. Mocking und Fixtures
- Virtuelle Umgebungen und `requirements.txt` / `pyproject.toml`

---

## 🚀 Loslegen

Dieses Repo bindet die Workshops als **Git-Submodule** ein. Zum Klonen inklusive
aller Workshops:

```bash
git clone --recurse-submodules git@github.com:Franzelfx/WSPython3.git
cd WSPython3
```

Bereits geklont? Submodule nachziehen:

```bash
git submodule update --init --recursive
```

Danach in den gewünschten Workshop wechseln und dessen `README.md` folgen:

```bash
cd cli-weather-dashboard
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🔧 Voraussetzungen

- **Python 3.10+**
- `git`
- Ein Editor deiner Wahl (z. B. VS Code)

---

## 💡 Lösung anschauen

Jeder Workshop enthält die vollständige Lösung an zwei Stellen:

- **`LOESUNG.md`** – die Lösung als kommentierte Schritt-für-Schritt-Erklärung
- **Branch `loesung`** – der fertige, lauffähige Code

```bash
cd cli-weather-dashboard
git checkout loesung
```

Zurück zum Skeleton:

```bash
git checkout main
```

---

## 📂 Struktur

```text
WSPython3/
├── README.md                 # diese Übersicht
├── cli-weather-dashboard/    # Workshop 1 (Submodul)
└── cli-task-manager/         # Workshop 2 (Submodul)
```
