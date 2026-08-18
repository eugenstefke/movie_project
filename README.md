German Version

Movie App

Eine Kommandozeilen-Anwendung zur Verwaltung persönlicher Filmsammlungen mit mehreren Benutzern, Anbindung an die OMDb-API und automatischer Generierung einer HTML-Filmwebsite.

Über das Projekt

Die Movie App ist eine Python-Anwendung, mit der mehrere Benutzer jeweils ihre eigene Filmsammlung verwalten können. Filmdaten (Titel, Erscheinungsjahr, Bewertung, Poster, IMDb-ID) werden automatisch über die OMDb-API abgerufen und in einer SQLite-Datenbank gespeichert. Aus der eigenen Sammlung lässt sich außerdem eine hübsch gestaltete, statische HTML-Website generieren, auf der jedes Filmposter zur zugehörigen IMDb-Seite verlinkt ist und beim Hovern die Bewertung als Tooltip anzeigt.

Hauptfunktionen

- 👥 **Mehrbenutzerverwaltung**: Benutzer anlegen, umbenennen und löschen – jeder mit eigener Filmliste
- 🎥 **Filme verwalten**: Filme über die OMDb-API hinzufügen, löschen und Bewertungen aktualisieren
- 📋 **Filme auflisten**: Alle Filme der eigenen Sammlung anzeigen
- 📊 **Statistiken**: Durchschnittsbewertung, Median, bestbewerteter und schlechtestbewerteter Film
- 🎲 **Zufälliger Filmvorschlag**: Für den Filmabend
- 🔍 **Filme suchen**: Nach Titel durchsuchen
- ⭐ **Sortierung nach Bewertung**: Filme absteigend nach Rating anzeigen
- 🌐 **Website-Generator**: Erstellt aus der eigenen Sammlung eine `movie.html` mit Filmpostern, Titel, Jahr, IMDb-Link und Bewertungs-Tooltip

Verwendete Technologien

- **Python** – Programmiersprache der Anwendung
- **SQLAlchemy** – ORM/SQL-Toolkit für den Zugriff auf die SQLite-Datenbank
- **SQLite** – lokale Datenbank (`app.db`) zur Speicherung von Benutzern und Filmen
- **OMDb API** – externe Schnittstelle zum Abrufen von Filminformationen
- **python-dotenv** – zum Laden des API-Keys aus einer `.env`-Datei
- **HTML/CSS** – für die generierte Filmwebsite

Einrichtung

### 1. Voraussetzungen

- Python 3.10 oder neuer
- Ein kostenloser API-Key von [OMDb API](https://www.omdbapi.com/apikey.aspx)

### 2. Repository klonen

```bash
git clone git@github.com:eugenstefke/movie_project.git
cd <dein-repository>
```

### 3. Abhängigkeiten installieren

```bash
pip install sqlalchemy
pip install requests
pip install python-dotenv
```

### 4. API-Key hinterlegen

Lege im Projektordner eine Datei namens `.env` an und trage dort deinen OMDb-API-Key ein:

```
API_KEY=dein_api_key_hier
```

### 5. Datenbank

Beim ersten Start werden die Tabellen `users` und `movies` automatisch angelegt (in `app.db`). Ein manuelles Einrichten der Datenbank ist nicht nötig.

## ▶️ Verwendung

### Anwendung starten

```bash
python run.py
```

### Ablauf

1. Beim Start erscheint der **Begrüßungsbildschirm** mit einer Liste aller vorhandenen Benutzer.
2. Wähle einen bestehenden Benutzer aus oder lege über die entsprechende Option einen **neuen Benutzer** an.
3. Nach der Benutzerauswahl öffnet sich das **Hauptmenü** mit folgenden Optionen:

   | Option | Funktion |
   |--------|----------|
   | 0 | Programm beenden |
   | 1 | Filme auflisten |
   | 2 | Film hinzufügen |
   | 3 | Film löschen |
   | 4 | Film-Bewertung aktualisieren |
   | 5 | Statistiken anzeigen |
   | 6 | Zufälligen Film vorschlagen |
   | 7 | Film suchen |
   | 8 | Filme nach Bewertung sortiert anzeigen |
   | 9 | Filmwebsite generieren |
   | 10 | Benutzer wechseln |

4. Beim **Hinzufügen eines Films** (Option 2) genügt die Eingabe des Filmtitels – alle weiteren Daten (Jahr, Bewertung, Poster, IMDb-ID) werden automatisch über die OMDb-API abgerufen.
5. Mit **Option 9** wird aus der aktuellen Filmsammlung des Benutzers eine `movie.html` erzeugt. Diese Datei kann im Browser geöffnet werden und zeigt alle Filme als Poster-Grid – ein Klick auf ein Poster führt zur passenden IMDb-Seite, beim Hovern erscheint die Bewertung als kleiner Tooltip.

### Projektstruktur

```
├── user_log.py            # Einstiegspunkt: Benutzerverwaltung & Login
├── user_storage_sql.py    # Datenbankzugriff für Benutzer
├── movies.py               # Hauptmenü & Filmverwaltung
├── movie_storage_sql.py   # Datenbankzugriff für Filme
├── data_collector.py      # Anbindung an die OMDb-API
├── text_generator.py      # HTML-Generierung aus Template
├── index_template.html    # HTML-Vorlage für die Filmwebsite
├── style.css               # Styling der generierten Website
└── app.db                  # SQLite-Datenbank (wird automatisch erstellt)

### Hinweis

In movies.py sind 2 Funktionen (movies_sorted_by_year und filter_movies) auskommentiert, diese sind kein Projektstand mehr und dienen nur als Historie zur vorherigen Version des Projektes.

English Version 

Movie App

A command-line application for managing personal movie collections with multiple users, integration with the OMDb API, and automatic generation of an HTML movie website.

About the Project

The Movie App is a Python application that allows multiple users to each manage their own movie collection. Movie data (title, release year, rating, poster, IMDb ID) is automatically retrieved via the OMDb API and stored in a SQLite database. From your own collection, you can also generate a nicely styled, static HTML website where every movie poster links to the corresponding IMDb page and shows the rating as a tooltip on hover.

### Main Features

- 👥 **Multi-user management**: Create, rename, and delete users – each with their own movie list
- 🎥 **Manage movies**: Add, delete, and update ratings for movies via the OMDb API
- 📋 **List movies**: Display all movies in your own collection
- 📊 **Statistics**: Average rating, median, highest-rated and lowest-rated movie
- 🎲 **Random movie suggestion**: For movie night
- 🔍 **Search movies**: Search by title
- ⭐ **Sort by rating**: Display movies sorted by rating in descending order
- 🌐 **Website generator**: Creates a `movie.html` from your own collection, including posters, titles, years, IMDb links, and a rating tooltip

### Technologies Used

- **Python** – the application's programming language
- **SQLAlchemy** – ORM/SQL toolkit for accessing the SQLite database
- **SQLite** – local database (`app.db`) for storing users and movies
- **OMDb API** – external interface for retrieving movie information
- **python-dotenv** – for loading the API key from an `.env` file
- **HTML/CSS** – for the generated movie website

## ⚙️ Setup

### 1. Requirements

- Python 3.10 or newer
- A free API key from [OMDb API](https://www.omdbapi.com/apikey.aspx)

### 2. Clone the repository

```bash
git clone git@github.com:eugenstefke/movie_project.git
cd <your-repository>
```

### 3. Install dependencies

```bash
pip install sqlalchemy
pip install requests
pip install python-dotenv
```

### 4. Set up the API key

Create a file named `.env` in the project folder and enter your OMDb API key there:

```
API_KEY=your_api_key_here
```

### 5. Database

On first run, the `users` and `movies` tables are created automatically (in `app.db`). No manual database setup is required.

## ▶️ Usage

### Starting the application

```bash
python run.py
```

### Workflow

1. On startup, the **welcome screen** appears, listing all existing users.
2. Select an existing user, or use the corresponding option to create a **new user**.
3. After selecting a user, the **main menu** opens with the following options:

   | Option | Function |
   |--------|----------|
   | 0 | Exit the program |
   | 1 | List movies |
   | 2 | Add movie |
   | 3 | Delete movie |
   | 4 | Update movie rating |
   | 5 | Show statistics |
   | 6 | Suggest a random movie |
   | 7 | Search movie |
   | 8 | Show movies sorted by rating |
   | 9 | Generate movie website |
   | 10 | Switch user |

4. When **adding a movie** (option 2), simply enter the movie title – all other data (year, rating, poster, IMDb ID) is retrieved automatically via the OMDb API.
5. **Option 9** generates a `movie.html` file from the user's current movie collection. This file can be opened in a browser and displays all movies as a poster grid – clicking a poster leads to the corresponding IMDb page, and hovering over it shows the rating as a small tooltip.

### Project Structure

```
├── user_log.py            # Entry point: user management & login
├── user_storage_sql.py    # Database access for users
├── movies.py               # Main menu & movie management
├── movie_storage_sql.py   # Database access for movies
├── data_collector.py      # Integration with the OMDb API
├── text_generator.py      # HTML generation from template
├── index_template.html    # HTML template for the movie website
├── style.css               # Styling for the generated website
└── app.db                  # SQLite database (created automatically)
```
```

### Note
In movies.py, 2 functions (movies_sorted_by_year and filter_movies) are commented out; they are no longer part of the current project state and are kept only as a historical reference to a previous version of the project.
