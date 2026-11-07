# Downloads Sorter

Ein kleines Python-Skript, das meinen Downloads-Ordner automatisch sortiert.

Die Dateien werden anhand ihrer Dateiendung erkannt und in passende Unterordner verschoben. Bilder landen zum Beispiel in „Images“ und PDF-Dateien in „Documents“.

## Funktionen

- Bilder, Videos, Dokumente und Musik sortieren
- Archive und Installationsdateien sortieren
- Code-Dateien wie C, Java und Python in eigene Ordner verschieben
- Benötigte Ordner automatisch erstellen
- Dateien überspringen, wenn im Ziel bereits derselbe Dateiname existiert

Unbekannte Dateitypen bleiben im Downloads-Ordner liegen. Vorhandene Unterordner werden nicht durchsucht.

## Starten

Für das Skript wird Python 3 benötigt. Zusätzliche Pakete sind nicht nötig.

Im Projektordner folgenden Befehl ausführen:

```bash
python DownloadsSorter.py
```

Beim Ausführen werden die Dateien direkt in die passenden Unterordner verschoben.

## Anpassung

Die Dateiendungen und Zielordner stehen im Dictionary `extensions`. Dort können weitere Einträge hinzugefügt oder bestehende geändert werden.

Zum Beispiel:

```python
".pdf": "Documents",
".py": "Python",
```