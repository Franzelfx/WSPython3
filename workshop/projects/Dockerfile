# Mini-ResNet (CIFAR-10) im Container trainieren.
#
# Hinweis: Docker-Container laufen unter Linux und haben auf dem Mac keinen
# Zugriff auf die Metal-GPU – das Training läuft hier also auf der CPU.
#
# Bauen:    docker build -t neural-net .
# Starten:  docker run --rm -v "$PWD/output:/app/output" -v keras-cache:/root/.keras neural-net

# TensorFlow 2.18 unterstützt höchstens Python 3.12 (siehe pyproject.toml).
FROM python:3.12-slim

# Graphviz wird von utils.plot_model zum Zeichnen des Modells benötigt.
RUN apt-get update \
    && apt-get install -y --no-install-recommends graphviz \
    && rm -rf /var/lib/apt/lists/*

# uv installiert die Abhängigkeiten direkt aus der pyproject.toml.
COPY --from=ghcr.io/astral-sh/uv:0.13.4 /uv /bin/uv

WORKDIR /app

# Erst nur die Abhängigkeiten installieren: Diese Schicht bleibt im Cache,
# solange sich pyproject.toml nicht ändert – auch wenn sich der Code ändert.
# (Nicht requirements.txt verwenden: Dort steht tensorflow-metal, das es
# für Linux nicht gibt.)
COPY pyproject.toml .
RUN uv pip install --system --no-cache -r pyproject.toml

COPY neural_net.py .

# Das Modell-Diagramm landet in /app/output (per -v nach außen gemountet).
RUN mkdir output
WORKDIR /app/output

CMD ["python", "/app/neural_net.py"]
