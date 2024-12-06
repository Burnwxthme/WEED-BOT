import os

# Name des Hauptprojekts
project_name = "Weed Grow Bot"

# Verzeichnisstruktur
folders = [
    "data",
    "shop",
    "grow",
    "handlers",
    "templates",
    "utils",
    "logs",  # Für Logs
    "tests"  # Für Unit-Tests
]

# Dateien im Hauptverzeichnis
main_files = [
    "bot.py", 
    "config.py", 
    "requirements.txt", 
    "uploader_google_drive.py",
    "credentials.json",
    "logger.py",
    "handlers.py"
]

# Dateien in den Unterverzeichnissen
data_files = ["database.json", "users.csv"]
shop_files = ["products.json", "transactions.log"]
grow_files = ["plants_data.json", "grow_log.txt"]
handlers_files = ["start_handler.py", "help_handler.py"]
templates_files = ["welcome_template.html", "error_template.html"]
utils_files = ["utils.py", "helpers.py"]

# Funktion zum Erstellen von Ordnern und Dateien
def create_folder_structure(base_path, folder_name, files):
    folder_path = os.path.join(base_path, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Ordner erstellt: {folder_path}")
    else:
        print(f"Ordner übersprungen (bereits vorhanden): {folder_path}")
    
    for file in files:
        file_path = os.path.join(folder_path, file)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                pass  # Leere Datei erstellen
            print(f"Datei erstellt: {file_path}")
        else:
            print(f"Datei übersprungen (bereits vorhanden): {file_path}")

# Hauptverzeichnis erstellen
if not os.path.exists(project_name):
    os.makedirs(project_name)
    print(f"Hauptverzeichnis erstellt: {project_name}")
else:
    print(f"Hauptverzeichnis übersprungen (bereits vorhanden): {project_name}")

# Hauptverzeichnisdateien erstellen
for file in main_files:
    file_path = os.path.join(project_name, file)
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            pass  # Leere Datei erstellen
        print(f"Datei erstellt: {file_path}")
    else:
        print(f"Datei übersprungen (bereits vorhanden): {file_path}")

# Unterverzeichnisse erstellen und Dateien hinzufügen
for folder, files in zip(
    folders, 
    [data_files, shop_files, grow_files, handlers_files, templates_files, utils_files, [], []]
):
    create_folder_structure(project_name, folder, files)
