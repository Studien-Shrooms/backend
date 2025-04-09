# Verwende ein schlankes Python-Image
FROM python:3.10-slim

# Setze das Arbeitsverzeichnis im Container
WORKDIR /app

# Kopiere requirements und installiere Abhängigkeiten
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kopiere den gesamten Rest der App ins Image
COPY . .

# Erstelle den Upload-Ordner (wird vom Code benötigt)
RUN mkdir -p uploads

# Exponiere den Port (optional, für Dokumentation)
EXPOSE 8080

# Starte FastAPI mit uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
