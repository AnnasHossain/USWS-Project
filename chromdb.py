import chromadb
from chromadb.config import Settings

# Konfigurieren Sie die Einstellungen, um das Zurücksetzen zu erlauben
settings = Settings(allow_reset=True)

# Erstellen Sie eine Instanz des Chroma-Clients mit den angepassten Einstellungen
chroma_client = chromadb.PersistentClient(path="....here put path of this project...", settings=settings)

# Löschen Sie alle Daten in der Datenbank
chroma_client.reset()
