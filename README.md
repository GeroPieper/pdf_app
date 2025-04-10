# PDF App

Die Anwendung ist aktuell in einem sehr frühen Stadium und bei weitem noch nicht fertig. Ziel ist es ein Tool zu erstellen, über welches Dokumente gespeichert und verwaltet werden können.

Folgender KI-generierter Text beschreibt das Ziel recht gut:

## ReadMe PDF App (KI-generiert)

Die PDF App bietet eine Lösung, um PDF-Dokumente zentral zu verwalten, zu organisieren, zu durchsuchen und zu bearbeiten – und das in einem Netzwerk, das über ein modernes Web-Interface zugänglich ist. Das Backend basiert auf FastAPI, während das Frontend mit React realisiert wurde.

## Features

- PDF Upload & Verwaltung:
- Übersichtliche Anzeige:
- Leistungsstarke Suche:
- Einfache Kategorisierung der PDFs
- Responsive Web-Oberfläche:
- Sichere und skalierbare Architektur:

## Technologien

- **Backend:**  
  - FastAPI, SQLAlchemy, Uvicorn  
  - SQLite  
  - Python 3.9+

- **Frontend:**  
  - React mit modernem JavaScript (ES6+)  
  - Axios zur Kommunikation mit dem FastAPI-Backend  
  - Styling über CSS/SCSS und Responsive Design Prinzipien

- **Deployment & DevOps:**  
  - Docker-Container für ein konsistentes Deployment in internen Netzwerken  
  - GitHub Actions zur kontinuierlichen Integration und Bereitstellung  
  - NGINX als Reverse Proxy für das Backend und statische Dateien des Frontends
