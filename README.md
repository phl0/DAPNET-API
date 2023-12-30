# DAPNET API Client

Dieses Repository enthält eine Python-Klasse zur Interaktion mit dem DAPNET (Digital Amateur Paging Network), speziell zum Senden von Nachrichten über das Netzwerk.

## Autor
Erik Schauer, DO1FFE (do1ffe@darc.de)

## Features
- Senden von Nachrichten über das DAPNET
- Einfache Authentifizierung mit Amateurfunkrufzeichen und Passwort
- Unterstützung für Notfallnachrichten
- Statische Methode zur vereinfachten Nutzung

## Voraussetzungen
- Python 3.x
- `requests` Bibliothek (Installierbar via `pip install requests`)

## Installation
Klonen Sie das Repository oder laden Sie die Dateien herunter. Stellen Sie sicher, dass Python 3.x installiert ist und fügen Sie die Datei `dapnet_api.py` in Ihr Projekt ein.

## Verwendung
Importieren Sie die `DAPNET`-Klasse aus `dapnet_api.py` in Ihr Python-Skript. Verwenden Sie dann die statische Methode `Send` oder erstellen Sie eine Instanz der Klasse, um Nachrichten zu senden.

### Beispiel
```python
from dapnet_api import DAPNET

# Senden einer Nachricht mit der statischen Methode
response = DAPNET.Send('Testnachricht', 'destinationcallsign', 'txgroup', 'yourcallsign', 'yourpassword')
print(response)
```

## Unterstützung und Mitwirkung
Für Unterstützung oder bei Interesse an einer Mitwirkung, kontaktieren Sie mich bitte unter do1ffe@darc.de.
