# Praktikums-Bewerbungsmanager

Ein modernes Web-Interface zur Verwaltung von Praktikumsbewerbungen für Fachinformatiker Systemintegration. Das System ermöglicht es, Unternehmen zu verwalten, Bewerbungsstatus zu tracken und alle relevanten Informationen zentral zu organisieren.

## Features

- **Unternehmensverwaltung**: Vollständige CRUD-Funktionen für Unternehmen
- **Bewerbungsstatus-Tracking**: Übersicht über Entwürfe, Versendete, Vorstellungsgespräche und Annahmen
- **CSV-Export**: Export der Daten im Format der Betriebsliste
- **Konfigurierbare Dashboard-Informationen**: Anpassbare Termine, Schwerpunkte und wichtige Informationen
- **Modernes Dark Mode Design**: Professionelles UI mit Tailwind CSS
- **Projekt-Ideen**: Übersicht möglicher Projekte für die Abschlussprüfung

## Voraussetzungen

- Python 3.7 oder höher
- pip (Python Package Manager)
- Moderner Webbrowser (Chrome, Firefox, Edge, Safari)

## Installation

### Option 1: Docker (Empfohlen)

#### Voraussetzungen
- Docker installiert ([Docker Desktop](https://www.docker.com/products/docker-desktop))
- Docker Compose (meist in Docker Desktop enthalten)

#### Installation mit Docker

1. **Docker Image bauen und starten:**
   ```bash
   docker-compose up -d
   ```

2. **Anwendung öffnen:**
   Öffnen Sie in Ihrem Webbrowser:
   ```
   http://localhost:5000
   ```

3. **Container stoppen:**
   ```bash
   docker-compose down
   ```

4. **Logs anzeigen:**
   ```bash
   docker-compose logs -f
   ```

#### Docker-Befehle

**Image bauen:**
```bash
docker build -t praktikum-manager .
```

**Container starten:**
```bash
docker run -d -p 5000:5000 \
  -v $(pwd)/companies.json:/app/companies.json \
  -v $(pwd)/config.json:/app/config.json \
  --name praktikum-manager \
  praktikum-manager
```

**Container stoppen:**
```bash
docker stop praktikum-manager
docker rm praktikum-manager
```

### Option 2: Lokale Installation

#### 1. Python-Abhängigkeiten installieren

Öffnen Sie ein Terminal im Projektverzeichnis und installieren Sie Flask:

```bash
pip install flask
```

Oder mit requirements.txt:
```bash
pip install -r requirements.txt
```

#### 2. Server starten

Starten Sie den Backend-Server:

```bash
python server.py
```

Der Server läuft standardmäßig auf `http://127.0.0.1:5000`

#### 3. Anwendung öffnen

Öffnen Sie in Ihrem Webbrowser:
```
http://127.0.0.1:5000
```

## Konfiguration

### config.json

Die Datei `config.json` ermöglicht es, wichtige Informationen individuell anzupassen:

#### Praktikumszeitraum

```json
{
  "internship": {
    "period": {
      "start": "27.04.2026",
      "end": "01.12.2026"
    },
    "examPreparation": [
      {
        "name": "Prüfungsvorbereitung 1",
        "start": "17.08.2026",
        "end": "28.08.2026"
      },
      {
        "name": "Prüfungsvorbereitung 2",
        "start": "12.10.2026",
        "end": "23.10.2026"
      }
    ]
  }
}
```

#### Dashboard-Informationen

```json
{
  "dashboard": {
    "importantDates": {
      "title": "Wichtige Termine",
      "items": [
        {
          "label": "Praktikum",
          "value": "27.04.2026 - 01.12.2026"
        },
        {
          "label": "Prüfungsvorbereitung 1",
          "value": "17.08. - 28.08.2026"
        }
      ]
    },
    "focusAreas": {
      "title": "Schwerpunkte",
      "items": [
        "Netzwerktechnik",
        "Cybersecurity",
        "IT-Infrastruktur",
        "Cloud Computing"
      ]
    },
    "importantInfo": {
      "title": "Wichtige Info",
      "content": "Das Praktikum ist für den Betrieb kostenfrei, da es im Rahmen einer Umschulung bei CBW Hamburg durch die Arbeitsagentur finanziert wird."
    }
  }
}
```

### Vollständige config.json Struktur

```json
{
  "internship": {
    "period": {
      "start": "DD.MM.YYYY",
      "end": "DD.MM.YYYY"
    },
    "examPreparation": [
      {
        "name": "Name der Prüfungsvorbereitung",
        "start": "DD.MM.YYYY",
        "end": "DD.MM.YYYY"
      }
    ]
  },
  "dashboard": {
    "importantDates": {
      "title": "Titel der Karte",
      "items": [
        {
          "label": "Bezeichnung",
          "value": "Wert/Zeitraum"
        }
      ]
    },
    "focusAreas": {
      "title": "Titel der Karte",
      "items": [
        "Schwerpunkt 1",
        "Schwerpunkt 2"
      ]
    },
    "importantInfo": {
      "title": "Titel der Karte",
      "content": "Ihr Text hier..."
    }
  }
}
```

## Verwendung

### Unternehmen hinzufügen

1. Klicken Sie in der Sidebar auf "Unternehmen hinzufügen"
2. Füllen Sie das Formular aus:
   - **Pflichtfelder**: Unternehmensname, Schwerpunkt, Status
   - **Optional**: Stadt, Branche, Kontaktdaten, Termine, Notizen
3. Klicken Sie auf "Speichern"

### Unternehmen bearbeiten

1. In der Ansicht "Alle Unternehmen" auf das Bearbeiten-Icon klicken
2. Oder in der Detailansicht auf "Bearbeiten" klicken
3. Änderungen vornehmen und speichern

### Unternehmen löschen

1. In der Tabelle auf das Löschen-Icon klicken
2. Oder in der Detailansicht auf "Löschen" klicken
3. Bestätigung bestätigen

### CSV-Export

1. In der Ansicht "Alle Unternehmen"
2. Klicken Sie auf "CSV Export"
3. Die Datei wird im Format `Betriebsliste_Praktikum_2026.csv` heruntergeladen

### Filter und Suche

- **Suche**: Geben Sie im Suchfeld einen Begriff ein (Unternehmensname oder Ansprechpartner)
- **Status-Filter**: Wählen Sie einen Bewerbungsstatus aus
- **Bereich-Filter**: Filtern Sie nach Schwerpunkt (Fokusbereich)

### Sortierung

Klicken Sie auf die Spaltenüberschriften in der Tabelle, um nach diesem Feld zu sortieren. Ein erneuter Klick kehrt die Sortierrichtung um.

## Datenstruktur

### Unternehmen (companies.json)

Jedes Unternehmen enthält folgende Felder:

- `id`: Eindeutige ID (automatisch generiert)
- `name`: Unternehmensname
- `focus`: Schwerpunkt/Fokusbereich
- `city`: Stadt
- `industry`: Branche
- `contact`: Ansprechpartner
- `contactTitle`: Titel/Position des Ansprechpartners
- `email`: E-Mail-Adresse
- `phone`: Telefonnummer
- `website`: Website-URL
- `status`: Bewerbungsstatus
- `applicationDate`: Bewerbungsdatum (YYYY-MM-DD)
- `followupDate`: Follow-up Datum (YYYY-MM-DD)
- `specialFeatures`: Besonderheiten
- `notes`: Notizen

### Bewerbungsstatus

Mögliche Status-Werte:
- `Noch nicht gestartet`
- `Entwurf`
- `Versendet`
- `Vorstellungsgespräch geplant`
- `Angenommen`
- `Abgelehnt`

## API-Endpunkte

### GET /api/companies
Lädt alle Unternehmen.

**Response**: Array von Unternehmen-Objekten

### POST /api/companies
Erstellt ein neues Unternehmen.

**Request Body**: Unternehmen-Objekt (ohne `id`, wird automatisch generiert)

**Response**: Erstelltes Unternehmen mit ID

### PUT /api/companies/{id}
Aktualisiert ein bestehendes Unternehmen.

**Request Body**: Zu aktualisierende Felder

**Response**: Aktualisiertes Unternehmen

### DELETE /api/companies/{id}
Löscht ein Unternehmen.

**Response**: 204 No Content

### GET /api/config
Lädt die Konfiguration.

**Response**: Config-Objekt mit `internship` und `dashboard` Bereichen

## Dateistruktur

```
Praktikum/
├── index.html              # Frontend-Anwendung
├── server.py               # Backend-Server (Flask)
├── config.json             # Konfigurationsdatei
├── companies.json          # Datenbank (Unternehmen)
├── requirements.txt        # Python-Abhängigkeiten
├── Dockerfile              # Docker Image Definition
├── docker-compose.yml      # Docker Compose Konfiguration
├── .dockerignore          # Docker Ignore-Datei
├── README.md              # Diese Anleitung
└── ...
```

## Fehlerbehebung

### Server startet nicht

- Überprüfen Sie, ob Python installiert ist: `python --version`
- Überprüfen Sie, ob Flask installiert ist: `pip list | grep flask`
- Installieren Sie Flask: `pip install flask`
- Überprüfen Sie, ob Port 5000 bereits belegt ist

### Daten werden nicht gespeichert

- Überprüfen Sie, ob der Server läuft
- Überprüfen Sie die Browser-Konsole auf Fehler (F12)
- Überprüfen Sie, ob `companies.json` schreibbar ist

### Config wird nicht geladen

- Überprüfen Sie, ob `config.json` existiert
- Überprüfen Sie die JSON-Syntax (z.B. mit einem JSON-Validator)
- Überprüfen Sie die Browser-Konsole auf Fehler

### CSV-Export funktioniert nicht

- Überprüfen Sie, ob Unternehmen vorhanden sind
- Überprüfen Sie die Browser-Konsole auf Fehler
- Testen Sie in einem anderen Browser

### Docker-Probleme

**ERR_EMPTY_RESPONSE im Browser:**
- Der Container muss neu gebaut werden: `docker-compose down && docker-compose build --no-cache && docker-compose up -d`
- Überprüfen Sie, ob der Container läuft: `docker ps`
- Überprüfen Sie die Logs: `docker-compose logs -f`
- Überprüfen Sie, ob der Server auf 0.0.0.0 bindet (siehe server.py)

**Container startet nicht:**
- Überprüfen Sie, ob Docker läuft: `docker ps`
- Überprüfen Sie die Logs: `docker-compose logs`
- Überprüfen Sie, ob Port 5000 frei ist: `netstat -an | grep 5000` (Linux/Mac) oder `netstat -an | findstr 5000` (Windows)

**Daten werden nicht gespeichert:**
- Überprüfen Sie, ob die Volumes korrekt gemountet sind
- Überprüfen Sie die Dateiberechtigungen: `ls -la companies.json config.json` (Linux/Mac) oder `dir companies.json config.json` (Windows)
- Überprüfen Sie die Container-Logs: `docker-compose logs praktikum-manager`

**Container kann nicht gebaut werden:**
- Überprüfen Sie die Docker-Version: `docker --version`
- Überprüfen Sie die Dockerfile-Syntax
- Versuchen Sie einen Clean Build: `docker-compose build --no-cache`

## Technische Details

### Backend
- **Framework**: Flask (Python)
- **Datenformat**: JSON
- **Port**: 5000 (Standard)

### Frontend
- **Framework**: Vanilla JavaScript
- **Styling**: Tailwind CSS (CDN)
- **Icons**: Heroicons (SVG)

### Browser-Kompatibilität
- Chrome/Edge (empfohlen)
- Firefox
- Safari
- Opera

## Entwicklung

### Lokale Entwicklung

1. Starten Sie den Server: `python server.py`
2. Öffnen Sie `http://127.0.0.1:5000` im Browser
3. Änderungen an `index.html` werden nach Neuladen sichtbar
4. Änderungen an `server.py` erfordern einen Server-Neustart

### Docker-Entwicklung

1. **Container im Entwicklungsmodus starten:**
   ```bash
   docker-compose up
   ```

2. **Container neu bauen nach Änderungen:**
   ```bash
   docker-compose build
   docker-compose up -d
   ```

3. **In den Container einsteigen:**
   ```bash
   docker exec -it praktikum-manager bash
   ```

### Produktions-Deployment

#### Mit Docker (Empfohlen)

1. **Docker Image bauen:**
   ```bash
   docker build -t praktikum-manager:latest .
   ```

2. **Container mit Volumes starten (für Datenpersistenz):**
   ```bash
   docker run -d \
     -p 5000:5000 \
     -v /pfad/zu/companies.json:/app/companies.json \
     -v /pfad/zu/config.json:/app/config.json \
     --restart unless-stopped \
     --name praktikum-manager \
     praktikum-manager:latest
   ```

#### Ohne Docker

Für den Produktionseinsatz sollten Sie:
- Einen Production WSGI-Server verwenden (z.B. Gunicorn)
- Environment-Variablen für Konfiguration nutzen
- HTTPS aktivieren
- CORS-Einstellungen anpassen, falls nötig
- Reverse Proxy (Nginx) verwenden

## Support

Bei Fragen oder Problemen:
1. Überprüfen Sie diese Anleitung
2. Überprüfen Sie die Browser-Konsole (F12) auf Fehler
3. Überprüfen Sie die Server-Logs im Terminal

## Lizenz

Dieses Projekt ist für den persönlichen Gebrauch erstellt worden.

