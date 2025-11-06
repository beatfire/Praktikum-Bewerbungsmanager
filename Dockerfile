FROM python:3.11-slim

# Setze Arbeitsverzeichnis
WORKDIR /app

# Installiere System-Abhängigkeiten
RUN apt-get update && apt-get install -y \
    && rm -rf /var/lib/apt/lists/*

# Kopiere Requirements-Datei (falls vorhanden) oder installiere direkt
COPY requirements.txt* ./
RUN if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; \
    else pip install --no-cache-dir flask; fi

# Kopiere alle Projektdateien
COPY . .

# Erstelle Verzeichnisse für Daten, falls sie nicht existieren
RUN mkdir -p /app/data && \
    touch /app/data/companies.json /app/data/config.json || true

# Exponiere Port
EXPOSE 5000

# Setze Environment-Variablen
ENV FLASK_APP=server.py
ENV FLASK_ENV=production
ENV FLASK_HOST=0.0.0.0
ENV PYTHONUNBUFFERED=1

# Starte den Server
CMD ["python", "server.py"]

