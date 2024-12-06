import os

# Name des Hauptprojekts
project_name = "Weed Grow Bot"

# Verzeichnisstruktur
folders = [
    

]

# Dateien im Hauptverzeichnis
main_files = [
    "bot.py",
    "config.py",
    "requirements.txt",
    "Uploader_GoogleDrive.py",
    "Credentials.json"
]

# Dateien in den Unterverzeichnissen
data_files = [
    
]

shop_files = [
    
]

grow_files = [
    
]

handlers_files = [
]

templates_files = [
]

utils_files = [
]

# Hauptverzeichnis erstellen
os.makedirs(project_name, exist_ok=True)

# Hauptverzeichnisdateien erstellen
for file in main_files:
    open(os.path.join(project_name, file), 'w').close()

# Unterverzeichnisse erstellen und Dateien hinzufügen
for folder, files in zip(
    folders, 
    [data_files, shop_files, grow_files, handlers_files, templates_files, utils_files]
):
    folder_path = os.path.join(project_name, folder)
    os.makedirs(folder_path, exist_ok=True)
    for file in files:
        open(os.path.join(folder_path, file), 'w').close()

print(f"Projekt '{project_name}' wurde erfolgreich mit der angegebenen Struktur erstellt!")
